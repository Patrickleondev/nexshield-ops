# Méthodologie - Test offensif de systèmes à base d'IA

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : OWASP Top 10 for LLM Applications (2025) + MITRE ATLAS + NIST AI RMF

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | RoE incluant les coûts d'inférence, les conditions d'utilisation du fournisseur de modèle et l'environnement de test |
| 2 | **Analyse du système** | Modèle et fournisseur, architecture (RAG, agents, outils), garde-fous, sources d'ancrage, périmètre d'action des agents |
| 3 | **Modélisation des menaces IA** | Surfaces d'entrée directe et indirecte, capacités accessibles au modèle, impact d'un détournement d'outil |
| 4 | **Tests adverses** | Injection directe et indirecte, contournement de garde-fous, extraction de prompt système et de données, abus d'appels de fonction, empoisonnement de la base vectorielle |
| 5 | **Évaluation des garde-fous** | Taux de réussite par catégorie, reproductibilité, comportement en sortie de distribution |
| 6 | **Restitution** | Rapport avec mapping OWASP LLM et ATLAS, jeu de cas de test rejouable pour la non-régression |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- Le caractère **stochastique** des modèles impose de mesurer un **taux de réussite** sur N tentatives, pas un résultat binaire. Une attaque qui réussit 3 fois sur 20 reste une vulnérabilité.
- On teste **l'application du client**, jamais le modèle de fondation du fournisseur. Le dire explicitement au cadrage évite une attente impossible à satisfaire.
- Les tests consomment des **jetons facturés au client**. Le budget est cadré au RoE et suivi dans le classeur.
- La preuve d'un contournement se fait par un **marqueur inoffensif**, jamais en générant du contenu réellement illégal ou nuisible.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/ai-redteaming/README.md` §4.
- **Preuves** : coffre chiffré, manifeste d'empreintes, destruction à J+90.
  Voir `10-services/pentest-audit/procedures/PRO-GEN-100-collecte-de-preuves.md`,
  qui fait référence pour tous les services.
- **Journal des opérations** : horodaté, en temps réel, y compris pour les actions
  passant par un agent ou un serveur MCP.
- **Livraison** : double relecture avant remise, 3 jours ouvrés minimum entre la
  fin des travaux et la remise.
- **Clôture** : RETEX obligatoire, y compris quand la mission s'est bien passée.

---

## Reste à faire pour passer en v1.0

- [ ] Détailler chaque phase en procédure numérotée `PRO-AIRT-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
