# Méthodologie - Évaluation de sécurité applicative

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : OWASP ASVS + MASTG + API Security Top 10

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | Niveau ASVS visé (L1, L2 ou L3), accès au code, jeu de comptes couvrant tous les rôles |
| 2 | **Analyse de l'architecture** | Composants, flux de données, points de confiance, dépendances |
| 3 | **Revue des exigences ASVS** | Parcours chapitre par chapitre, statut par exigence |
| 4 | **Tests dynamiques** | Authentification, session, contrôle d'accès, injections, logique métier |
| 5 | **Revue de code** | En boîte blanche uniquement : cryptographie, gestion des secrets, validation d'entrées |
| 6 | **Restitution** | Score de conformité par chapitre, écart au niveau visé, matrice exigence par exigence |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- ASVS transforme un avis d'expert en **niveau d'assurance mesurable**. C'est ce qui rend la prestation re-mesurable l'année suivante - donc refacturable.
- Le **contrôle d'accès** et la **logique métier** sont les deux domaines où l'automatisation ne trouve rien et où se situe la valeur.
- L'interlocuteur est une équipe de développement : le rapport doit être exploitable par un développeur, avec la correction et non seulement le constat.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/secu-applicative/README.md` §4.
- **Preuves** : coffre chiffré, manifeste d'empreintes, destruction à J+90.
  Voir `10-services/pentest-audit/procedures/PRO-PT-100-collecte-de-preuves.md`,
  qui fait référence pour tous les services.
- **Journal des opérations** : horodaté, en temps réel, y compris pour les actions
  passant par un agent ou un serveur MCP.
- **Livraison** : double relecture avant remise, 3 jours ouvrés minimum entre la
  fin des travaux et la remise.
- **Clôture** : RETEX obligatoire, y compris quand la mission s'est bien passée.

---

## Reste à faire pour passer en v1.0

- [ ] Détailler chaque phase en procédure numérotée `PRO-APP-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
