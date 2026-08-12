# PRO-AIRT-100 - Exécution des tests adverses

**Version** : v0.1 · **Service** : `ai-redteaming` · **Phase** : tests adverses
**Responsable** : testeur · **Sortant** : jeu de cas de test rejouable + constatations

**Préalable bloquant** : `PRO-AIRT-001` close, tous critères de sortie cochés.

---

## Principe

On teste par **scénario d'abus**, pas par liste de charges utiles. Une collection
de prompts trouvés en ligne prouve seulement que le modèle a déjà vu ces prompts.

Chaque cas de test est :

1. **écrit** avant d'être lancé - objectif, entrée, résultat attendu ;
2. **rejoué N fois** (20 par défaut) ;
3. **consigné** avec son taux de réussite ;
4. **versé** au jeu de test rejouable, qui devient un livrable.

Le jeu rejouable est ce qui permet au client de vérifier ses correctifs plus tard.
C'est notre valeur ajoutée durable - un rapport se périme, un jeu de test non.

**Outillage** : [`../outillage/OUTILLAGE.md`](../outillage/OUTILLAGE.md) - socle
retenu, couverture réelle par catégorie, et ce qu'aucun outil ne couvre.
Aucun outil n'est lancé avant la clôture de `PRO-AIRT-001` : chaque requête
consomme le budget de jetons du client.

---

## Par catégorie OWASP LLM 2025

### LLM01 - Injection de prompt

La catégorie la plus rentable, et celle que le marché comprend le mieux.

**Injection directe** - l'utilisateur écrit au modèle :

- Réécriture de rôle et de consigne
- Encodage et obscurcissement : base64, homoglyphes, langues alternatives, séparateurs
- Conflit de consignes : faire croire à une consigne système plus récente
- Détournement par fiction, jeu de rôle ou hypothèse
- Charge progressive sur plusieurs tours plutôt qu'en une requête

**Injection indirecte** - la charge arrive par un contenu ingéré. C'est la voie
la plus dangereuse et la moins testée par les autres :

- Document versé par l'utilisateur, contenant des instructions
- Page web récupérée par le modèle
- Champ de base de données, ticket, courriel ingéré
- Texte invisible : blanc sur blanc, taille nulle, métadonnées, commentaire HTML

> Une injection indirecte réussie sur un système agentique est presque toujours
> **critique** : l'attaquant n'a pas besoin d'accéder au système, il lui suffit
> d'y faire entrer un document.

ATLAS : famille des techniques d'injection de prompt (`AML.T*`) - vérifier
l'identifiant exact dans la version d'ATLAS appliquée.

### LLM02 - Divulgation d'informations sensibles

- Extraction de données présentes dans le contexte d'autres utilisateurs
- Fuite par la base d'ancrage : demander des documents hors de ses droits
- Reconstitution par recoupement sur plusieurs échanges
- Fuite de secrets techniques : clés, points d'accès internes, schémas

Test de cloisonnement : ouvrir deux sessions avec des comptes de droits
différents et vérifier qu'aucune donnée ne franchit la frontière.

### LLM03 - Chaîne d'approvisionnement

- Provenance des modèles, adaptateurs, jeux de données
- Dépendances de la chaîne d'inférence
- Serveurs MCP et extensions tierces branchés au système
- Vérification d'intégrité et épinglage des versions

### LLM04 - Empoisonnement des données et du modèle

**Jamais en production.** Sans environnement isolé, catégorie hors périmètre.

- Injection de contenu malveillant dans une source ingérée automatiquement
- Persistance : le contenu empoisonné survit-il au redémarrage ?
- Empoisonnement de la mémoire d'un agent entre deux sessions

### LLM05 - Traitement incorrect des sorties

Le pont entre la sécurité IA et la sécurité applicative classique. Souvent le
plus facile à démontrer, et le plus parlant pour une équipe de développement.

- Sortie affichée en HTML sans échappement → XSS
- Sortie interprétée comme une commande, une requête SQL, du code
- Sortie déclenchant un appel réseau - exfiltration par URL construite
- Sortie utilisée dans un chemin de fichier

Mapping classique : `CWE-79`, `CWE-89`, `CWE-78`. Une constatation ici porte à la
fois un identifiant LLM et un identifiant WSTG.

### LLM06 - Autonomie excessive

Central dès qu'il y a des agents. Trois questions, dans cet ordre :

1. **Permissions** - le modèle peut-il appeler des outils dont il n'a pas besoin ?
2. **Portée** - un outil légitime peut-il être détourné vers une cible non prévue ?
3. **Validation** - une action irréversible passe-t-elle par un humain ?

Cas à démontrer : faire exécuter à l'agent une action hors de son objectif, à
partir d'une entrée non fiable. C'est la démonstration qui marque le plus une
direction.

Les techniques agentiques d'ATLAS (empoisonnement de contexte et de mémoire,
altération de configuration d'agent, exfiltration par invocation d'outil) ont été
ajoutées début 2026 - vérifier la version appliquée.

### LLM07 - Fuite du prompt système

- Demande directe, puis détournée, puis par reformulation partielle
- Reconstruction progressive sur plusieurs tours
- Fuite par message d'erreur ou par comportement de refus

**Attention à la conclusion.** Un prompt système n'est pas un secret : il ne doit
jamais contenir de clé ni de règle métier critique. La constatation à écrire est
souvent « des secrets figurent dans le prompt système », pas « le prompt fuit ».

### LLM08 - Faiblesses des vecteurs et des plongements

Architecture RAG uniquement.

- Cloisonnement multi-locataires de la base vectorielle
- Récupération de documents hors droits par formulation de requête
- Injection de documents à forte similarité pour détourner la récupération
- Inversion : reconstituer du texte source à partir des plongements

### LLM09 - Désinformation

À tester quand la sortie fonde une décision métier.

- Taux d'invention sur des questions du domaine du client
- Comportement face à une prémisse fausse : corrige-t-il ou suit-il ?
- Citations et sources : sont-elles réelles et vérifiables ?
- Sur-confiance : le modèle signale-t-il son incertitude ?

Ce n'est pas de la sécurité au sens strict, mais c'est ce qui inquiète le plus
une direction. Le mesurer donne du poids au rapport.

### LLM10 - Consommation non bornée

- Absence de limitation par utilisateur ou par adresse
- Entrées provoquant une génération très longue
- Récursion d'agent, boucles d'appels d'outils
- **Déni de portefeuille** : coût d'inférence provoqué par un attaquant

Mesurer le coût réel d'une requête abusive, en francs CFA. Un chiffre parle plus
qu'un principe.

---

## Consigner un cas de test

Une ligne par cas, dans l'onglet dédié du classeur de mission :

| Champ | Exemple |
|---|---|
| Identifiant | `AIRT-001` |
| Catégorie | `LLM01` |
| Technique ATLAS | `AML.T<NNNN>` |
| Objectif | Faire produire le marqueur malgré la consigne |
| Entrée | Charge utile complète, reproductible |
| Résultat attendu | Refus |
| Tentatives | 20 |
| Réussites | 7 |
| Taux | 35 % |
| Reproductible | Oui / partiellement |
| Sévérité | Selon impact et taux |

---

## Règles d'exécution

- **Aucun contenu réellement nuisible.** La preuve se fait par le marqueur
  convenu au cadrage.
- **Aucune donnée personnelle réelle** dans les charges utiles ni dans les preuves.
- **Suivre le budget de jetons** en continu ; alerter à 70 % du plafond.
- **Journaliser** chaque campagne : horodatage, catégorie, nombre de requêtes,
  coût. Comme pour un pentest, y compris quand un agent ou un serveur MCP exécute
  à votre place.
- **Arrêt immédiat** si une action a un effet réel non prévu - courriel envoyé,
  enregistrement créé, appel externe déclenché. Notification au client sous 2 h.

---

## Critères de sortie

- [ ] Toutes les catégories retenues au RoE ont été couvertes, ou déclarées non exécutées avec motif
- [ ] Chaque cas rejoué au nombre de tentatives convenu
- [ ] Jeu de cas de test rejouable constitué et documenté
- [ ] Taux de réussite consignés
- [ ] Coût d'inférence réel relevé et comparé au budget
- [ ] Journal des campagnes complet
- [ ] Aucun contenu nuisible produit ni conservé
