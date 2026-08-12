# Méthodologie - Audit de conformité en protection des données

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : RGPD + loi togolaise n° 2019-014 + ISO/IEC 27701

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | Traitements concernés, interlocuteurs juridiques et techniques, partenaire avocat identifié |
| 2 | **Entretiens** | Métiers, informatique, juridique, ressources humaines |
| 3 | **Cartographie** | Inventaire des traitements, bases légales, durées, destinataires, transferts |
| 4 | **Analyse d'écart** | Confrontation aux exigences du RGPD et de la loi n° 2019-014 |
| 5 | **Analyse d'impact** | Si un traitement présente un risque élevé pour les personnes |
| 6 | **Restitution** | Registre des traitements, plan de mise en conformité priorisé |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- **Nous ne sommes pas avocats.** Nous produisons des constats techniques et organisationnels ; le conseil juridique est renvoyé à un partenaire. Le dire explicitement crédibilise le reste.
- Le volet local relève de la **loi n° 2019-014** et de l'**IPDCP** - voir `00-societe/juridique/CADRE-LEGAL.md` §1.3.
- ISO 27701 s'emboîte dans ISO 27001 : un client déjà engagé dans un SMSI n'a pas de second système à monter.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/x-privacy/README.md` §4.
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

- [ ] Détailler chaque phase en procédure numérotée `PRO-PRIV-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
