# Méthodologie - Audit de durcissement d'infrastructure

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : CIS Benchmarks + guides ANSSI + CIS Controls v8

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | Systèmes concernés, niveau CIS visé, fenêtre de maintenance, **sauvegardes vérifiées** |
| 2 | **Collecte des configurations** | Exports anonymisés, versions de firmware et de système |
| 3 | **Analyse d'écart** | Confrontation aux référentiels CIS et ANSSI, scoring automatisé |
| 4 | **Architecture et segmentation** | Schéma de l'existant, matrice des flux constatée |
| 5 | **Remédiation** | Si au contrat : playbooks Ansible, application en fenêtre de maintenance |
| 6 | **Contre-mesure** | Nouveau scoring, comparaison avant / après |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- **Sauvegarde vérifiée avant tout durcissement - bloquant.** Une mesure CIS mal appliquée peut couper un service de production.
- Le scoring est largement automatisable (CIS-CAT, Lynis, OpenSCAP) : l'audit se produit en heures, pas en jours. C'est le service à plus forte marge.
- Un score avant / après est immédiatement lisible par une direction. Bonne porte d'entrée chez un prospect qui hésite sur un engagement plus lourd.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/infra-vpn-cloudflare/README.md` §4.
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

- [ ] Détailler chaque phase en procédure numérotée `PRO-INFRA-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
