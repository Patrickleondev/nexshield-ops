# Checklist - couverture OWASP Top 10 for LLM Applications 2025

**Version** : v0.1 · Se recopie dans l'annexe de couverture du rapport.

Trois statuts possibles : **Exécuté**, **Non applicable** (avec la raison
technique), **Non exécuté** (avec le motif - fenêtre, refus du client, absence
d'environnement isolé).

Un statut « Non exécuté » n'est pas une faute. Le taire en est une.

**Référentiel appliqué** : [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/)
· [version PDF citable](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)
· techniques adverses : [MITRE ATLAS](https://atlas.mitre.org/)

Chaque titre ci-dessous renvoie à la page officielle du risque. **Un identifiant
ne se cite jamais sans avoir ouvert sa page** (`NOMENCLATURE.md` §8).

Outillage et couverture réelle par catégorie :
[`../outillage/OUTILLAGE.md`](../outillage/OUTILLAGE.md).

---

## [LLM01 - Injection de prompt](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

- [ ] Réécriture de rôle et de consigne
- [ ] Encodage et obscurcissement : base64, homoglyphes, langues alternatives
- [ ] Conflit de consignes, fausse consigne système plus récente
- [ ] Détournement par fiction, jeu de rôle, hypothèse
- [ ] Charge progressive sur plusieurs tours
- [ ] **Injection indirecte** par document versé par l'utilisateur
- [ ] **Injection indirecte** par page web récupérée
- [ ] **Injection indirecte** par contenu de base, ticket ou courriel ingéré
- [ ] Texte invisible : blanc sur blanc, taille nulle, métadonnées, commentaire HTML

## [LLM02 - Divulgation d'informations sensibles](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

- [ ] Cloisonnement entre utilisateurs : deux comptes, droits différents
- [ ] Accès à des documents hors des droits de l'utilisateur
- [ ] Reconstitution par recoupement sur plusieurs échanges
- [ ] Fuite de secrets techniques : clés, points d'accès, schémas internes
- [ ] Fuite par message d'erreur

## [LLM03 - Chaîne d'approvisionnement](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)

- [ ] Provenance des modèles, adaptateurs et jeux de données
- [ ] Dépendances de la chaîne d'inférence
- [ ] Serveurs MCP et extensions tierces branchés au système
- [ ] Épinglage des versions et vérification d'intégrité

## [LLM04 - Empoisonnement des données et du modèle](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)

> Environnement isolé obligatoire. Sans lui : **Non exécuté**, motif à écrire.

- [ ] Injection de contenu malveillant dans une source ingérée automatiquement
- [ ] Persistance après redémarrage
- [ ] Empoisonnement de la mémoire d'un agent entre sessions

## [LLM05 - Traitement incorrect des sorties](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/)

- [ ] Sortie affichée en HTML sans échappement (XSS)
- [ ] Sortie interprétée comme commande, requête SQL ou code
- [ ] Sortie déclenchant un appel réseau - exfiltration par URL construite
- [ ] Sortie utilisée dans un chemin de fichier
- [ ] Constatations rattachées à leur CWE et à leur identifiant WSTG

## [LLM06 - Autonomie excessive](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

- [ ] Inventaire réel des outils accessibles, comparé à l'inventaire déclaré
- [ ] Appel d'un outil non nécessaire à la fonction
- [ ] Détournement d'un outil légitime vers une cible non prévue
- [ ] Action irréversible sans validation humaine
- [ ] Chaînage d'outils aboutissant hors de l'objectif
- [ ] Enchaînement injection indirecte → appel d'outil

## [LLM07 - Fuite du prompt système](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/)

- [ ] Demande directe
- [ ] Demande détournée ou reformulée
- [ ] Reconstruction progressive sur plusieurs tours
- [ ] Fuite par comportement de refus ou message d'erreur
- [ ] **Vérifier ce que contient le prompt** : présence de secrets ou de règles critiques

## [LLM08 - Faiblesses des vecteurs et des plongements](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)

> Architecture RAG uniquement. Sinon : **Non applicable**.

- [ ] Cloisonnement multi-locataires de la base vectorielle
- [ ] Récupération de documents hors droits par formulation de requête
- [ ] Injection de documents à forte similarité pour détourner la récupération
- [ ] Inversion : reconstitution de texte source depuis les plongements

## [LLM09 - Désinformation](https://genai.owasp.org/llmrisk/llm092025-misinformation/)

- [ ] Taux d'invention sur des questions du domaine du client
- [ ] Comportement face à une prémisse fausse
- [ ] Vérifiabilité des citations et des sources produites
- [ ] Signalement de l'incertitude par le modèle

## [LLM10 - Consommation non bornée](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)

- [ ] Limitation par utilisateur et par adresse
- [ ] Entrées provoquant une génération très longue
- [ ] Récursion d'agent, boucles d'appels d'outils
- [ ] **Déni de portefeuille** : coût d'une requête abusive, chiffré

---

## Avant de clore

- [ ] Chaque cas rejoué au nombre de tentatives convenu au RoE
- [ ] Taux de réussite consignés pour chaque cas
- [ ] Jeu rejouable constitué, documenté, livrable en l'état
- [ ] Modèle, version et date des tests notés sur chaque constatation
- [ ] Coût d'inférence réel relevé et comparé au budget
- [ ] Aucun contenu réellement nuisible produit ni conservé
- [ ] Version d'OWASP LLM et d'ATLAS appliquée notée au rapport
