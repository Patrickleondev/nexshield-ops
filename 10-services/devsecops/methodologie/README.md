# Méthodologie — Audit de maturité et sécurisation de la chaîne

**Version** : v0.1 — **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : OWASP SAMM 2.0 + NIST SSDF (SP 800-218) + SLSA

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | Périmètre des dépôts et de la chaîne, disponibilité des équipes pour les entretiens |
| 2 | **Entretiens** | Une heure par domaine SAMM, avec les personnes qui font, pas seulement celles qui pilotent |
| 3 | **Analyse de la chaîne** | Étapes, contrôles en place, temps de traversée, gestion des secrets et des identités de pipeline |
| 4 | **Revue des dépôts** | Analyse statique, composition logicielle, détection de secrets, IaC, conteneurs |
| 5 | **Notation** | Niveau par pratique SAMM, comparaison au niveau cible |
| 6 | **Restitution** | Scores par domaine, feuille de route priorisée à 6, 12 et 18 mois |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- SAMM produit un **score qui se re-mesure**. C'est le service qui crée du revenu récurrent et stabilise la trésorerie.
- Toute recommandation qui allonge la chaîne de plus de **10 %** sera contournée dans les six mois. Mesurer le temps de traversée avant de recommander.
- L'équipe de développement craint qu'on lui impose des outils. Poser d'abord « combien de temps prend votre chaîne aujourd'hui ? ».

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/devsecops/README.md` §4.
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

- [ ] Détailler chaque phase en procédure numérotée `PRO-DSO-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
