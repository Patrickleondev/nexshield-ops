# Méthodologie - Évaluation et ingénierie de détection

**Version** : v0.1 - **Statut** : brouillon, à éprouver sur la première mission
**Référentiels** : MITRE ATT&CK + D3FEND + SIGMA + NIST SP 800-61

Sources officielles : `00-societe/smsi/REFERENCES.md`.

---

## Phases

| # | Phase | Contenu |
|---|---|---|
| 1 | **Cadrage** | SIEM en place, sources de journaux accessibles, périmètre de simulation |
| 2 | **Inventaire de la télémétrie** | Sources disponibles, sources manquantes, rétention, qualité |
| 3 | **Évaluation de la couverture** | Cartographie ATT&CK de l'existant, identification des angles morts |
| 4 | **Simulation d'adversaire** | Exécution contrôlée de techniques, mesure de ce qui est détecté |
| 5 | **Ingénierie de détection** | Rédaction de règles SIGMA, réduction du bruit, seuils |
| 6 | **Restitution** | Matrice de couverture avant / après, règles livrées, playbooks de réponse |

Une phase ne démarre pas tant que la précédente n'est pas consignée dans le
classeur de mission.

---

## Ce qui est propre à ce service

- Les règles sont écrites en **SIGMA**, format portable : écrites une fois, compilées vers Splunk, Elastic, Wazuh ou Sentinel. Elles deviennent un actif réutilisable dans `30-outils/sigma-rules/`.
- Une détection qui génère trop de faux positifs sera désactivée par l'équipe du client. Le **taux de faux positifs** fait partie du livrable, pas seulement la couverture.
- Ce service prolonge naturellement chaque mission offensive : le chemin d'attaque d'un pentest devient la liste des détections à écrire.

---

## Socle commun à toutes les missions

Ces règles ne se redéclinent pas par service, elles s'appliquent partout :

- **Préalables bloquants** : NDA, contrat, RoE et autorisation signés avant toute
  action technique. Voir `10-services/soc-ai-tools/README.md` §4.
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

- [ ] Détailler chaque phase en procédure numérotée `PRO-SOC-NNN`
- [ ] Produire les checklists d'exécution à partir du référentiel
- [ ] Valider le gabarit de rapport sur une mission blanche
- [ ] Documenter l'outillage dans `outillage/`
- [ ] Faire relire les clauses juridiques spécifiques
