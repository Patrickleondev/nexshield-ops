# Méthodologie - Programme de sensibilisation mesuré

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : NIST SP 800-50r1 + kits ENISA + ISO 27001 A.6.3

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | Populations, objectifs, **accord des représentants du personnel**, données collectées cadrées avec x-privacy |
| 2 | **Mesure initiale** | État des lieux avant toute action, pour pouvoir démontrer la progression |
| 3 | **Conception** | Contenus adaptés par métier, scénarios de simulation |
| 4 | **Exercice** | Campagne de hameçonnage simulé ou atelier |
| 5 | **Mesure** | Taux de clic, de saisie, de signalement, délai moyen de signalement |
| 6 | **Restitution** | Rapport agrégé et anonymisé, programme de l'année suivante |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- **La mesure est collective et anonymisée.** Une campagne utilisée pour sanctionner un employé détruit la confiance et l'efficacité du programme. Refuser cette formulation dès le premier rendez-vous.
- Le **taux de signalement** compte plus que le taux de clic : il mesure la capacité de l'organisation à réagir, pas la faillibilité des personnes.
- NIST SP 800-50 impose de mesurer l'efficacité - c'est ce qui justifie la reconduction annuelle. Une sensibilisation non mesurée ne se vend qu'une fois.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/sensibilisation/README.md` §4.
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

- [x] Procédures de cadrage et d'exécution écrites
- [x] Checklist d'exécution produite à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [x] Outillage documenté dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
