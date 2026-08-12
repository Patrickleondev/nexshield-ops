# PRO-AIRT-001 - Cadrage d'une mission AI RedTeaming

**Version** : v0.1 · **Service** : `ai-redteaming` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : RoE signé + fiche système complétée

---

## Ce qui distingue ce cadrage d'un cadrage de pentest

Quatre différences, et chacune a déjà fait échouer des missions ailleurs.

| Point | Pourquoi c'est spécifique |
|---|---|
| **Coût des tests** | Chaque requête consomme des jetons facturés au client. Un test intensif peut coûter cher - il faut un budget cadré. |
| **Conditions du fournisseur** | Tester une application bâtie sur OpenAI, Anthropic ou Mistral engage le client vis-à-vis des conditions d'utilisation de ce fournisseur. |
| **Périmètre du modèle** | On teste **l'application du client**, pas le modèle de fondation. À dire explicitement, sinon le client attend l'impossible. |
| **Non-déterminisme** | Le résultat est un **taux de réussite**, pas un oui/non. À expliquer avant la mission, jamais dans le rapport. |

---

## Étapes

### 1. Fiche du système évalué

À remplir intégralement avant toute proposition. Un système IA mal décrit produit
une estimation fausse.

| Élément | À obtenir |
|---|---|
| Modèle et fournisseur | Nom exact, version, hébergement (API tierce, cloud privé, local) |
| Architecture | Simple appel, RAG, agent, multi-agents, chaîne d'outils |
| Sources d'ancrage | Base vectorielle, documents ingérés, qui peut y écrire |
| Outils accessibles au modèle | Liste exhaustive, avec leurs droits réels |
| Garde-fous | Filtres d'entrée et de sortie, modération, listes de refus |
| Entrées | Qui peut écrire au modèle : utilisateurs authentifiés, public, documents |
| Sorties | Où va la réponse : affichage, exécution, courriel, appel d'API |
| Données manipulées | Personnelles, bancaires, de santé, secrets industriels |
| Volumétrie | Requêtes par jour, coût unitaire moyen |

**La question la plus importante** : *que peut faire le modèle, concrètement, s'il
est détourné ?* Un modèle qui répond du texte est un risque de réputation. Un
modèle qui appelle des outils et écrit dans une base est un risque d'exploitation.

### 2. Vérifier les conditions du fournisseur de modèle

Bloquant. La plupart des fournisseurs encadrent les tests adverses.

- [ ] Conditions d'utilisation du fournisseur lues
- [ ] Test adverse autorisé, ou dérogation obtenue par le client
- [ ] Le client reste **responsable** de sa relation avec son fournisseur - écrit au RoE
- [ ] Politique du fournisseur sur l'entraînement à partir des entrées : vérifiée
      et désactivée si possible

> Nous ne signons pas les conditions du fournisseur à la place du client. Nous
> l'alertons par écrit et nous consignons sa réponse.

### 3. Cadrer les coûts d'inférence

- Estimer le nombre de requêtes par catégorie de test.
- Convertir en coût avec le tarif réel du client.
- Faire valider **par écrit** le budget de jetons, avec un plafond.
- Prévoir la conduite à tenir en cas de dépassement : arrêt, ou accord d'extension.

Ce point figure au RoE. Un client qui découvre une facture d'inférence après coup
ne revient pas.

### 4. Choisir l'environnement de test

| Environnement | Quand | Réserve |
|---|---|---|
| Production | Le système n'existe qu'en production | Aucune manipulation de données, aucun empoisonnement |
| Préproduction | Cas nominal | Vérifier qu'elle reflète la production, sinon les résultats ne valent rien |
| Copie isolée | Tests d'empoisonnement, tests destructifs | À provisionner par le client |

**Un test d'empoisonnement de base vectorielle ne se fait jamais en production.**
Sans environnement isolé, cette catégorie sort du périmètre - et c'est écrit.

### 5. Retenir les catégories testées

Périmètre exprimé en **OWASP Top 10 for LLM Applications 2025**. Cocher ce qui
est retenu, et écrire pourquoi le reste ne l'est pas.

| Réf. | Risque | Applicable si |
|---|---|---|
| `LLM01` | Injection de prompt | Toujours |
| `LLM02` | Divulgation d'informations sensibles | Le modèle a accès à des données internes |
| `LLM03` | Vulnérabilités de la chaîne d'approvisionnement | Modèles, adaptateurs ou jeux de données tiers |
| `LLM04` | Empoisonnement des données et du modèle | Affinage ou ingestion de contenu externe |
| `LLM05` | Traitement incorrect des sorties | La sortie est interprétée, exécutée ou affichée en HTML |
| `LLM06` | Autonomie excessive | Le modèle appelle des outils ou déclenche des actions |
| `LLM07` | Fuite du prompt système | Toujours |
| `LLM08` | Faiblesses des vecteurs et des plongements | Architecture RAG |
| `LLM09` | Désinformation | La sortie fonde une décision métier |
| `LLM10` | Consommation non bornée | Le service est exposé et facturé à l'usage |

Les techniques adverses correspondantes sont référencées en **MITRE ATLAS**
(`AML.T<NNNN>`). La version d'ATLAS appliquée est inscrite au rapport : le
référentiel évolue vite, et des techniques agentiques ont été ajoutées début 2026.

### 6. Définir les critères de réussite

C'est ici qu'on évite le malentendu du non-déterminisme.

- **Nombre de tentatives par cas de test** : 20 par défaut. En dessous de 10, le
  taux n'a aucune valeur statistique.
- **Seuil de signalement** : une attaque réussissant au moins une fois sur 20 est
  consignée. Le taux qualifie la sévérité, il ne décide pas de l'existence.
- **Marqueur de succès** : un jeton inoffensif convenu à l'avance, jamais du
  contenu réellement nuisible.

> Exemple de marqueur : faire produire au modèle la chaîne `NEXSHIELD-PREUVE-001`
> alors que sa consigne le lui interdit. Cela prouve le contournement sans
> produire quoi que ce soit de dangereux.

### 7. Rédiger le RoE

Gabarit : `Modele-ROE-regles-engagement.docx`. Clauses à ajouter pour ce service :

- Budget de jetons et plafond
- Conditions du fournisseur de modèle et responsabilité du client
- Environnement de test et interdiction d'empoisonnement en production
- Nombre de tentatives par cas de test
- Marqueur de preuve convenu
- Interdiction de produire du contenu réellement illégal ou nuisible, y compris
  à titre de démonstration

---

## Critères de sortie

- [ ] Fiche système complète, y compris la liste exhaustive des outils accessibles
- [ ] Conditions du fournisseur de modèle vérifiées, réponse du client consignée
- [ ] Budget de jetons validé par écrit, avec plafond
- [ ] Environnement de test arrêté et provisionné
- [ ] Catégories OWASP LLM retenues, et exclusions justifiées
- [ ] Nombre de tentatives et marqueur de preuve convenus
- [ ] RoE et autorisation de test signés
- [ ] Version d'OWASP LLM et d'ATLAS appliquée notée dans la fiche de mission

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Promettre de « tester le modèle » | Le client attend un audit du fournisseur : promesse intenable |
| Omettre le budget de jetons | Facture surprise, relation abîmée |
| Tester l'empoisonnement en production | Corruption durable de la base du client |
| Une seule tentative par cas | Résultat non reproductible, sans valeur |
| Démontrer par du contenu réellement nuisible | Faute professionnelle, et preuve inutilisable |
