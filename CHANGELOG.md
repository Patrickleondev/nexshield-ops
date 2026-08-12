# Journal des changements

Format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versionnage [SemVer](https://semver.org/lang/fr/) appliqué à la **doctrine** (voir `CONTRIBUTING.md` §5).

Généré semi-automatiquement depuis les Conventional Commits (`make changelog`),
puis relu à la main avant chaque tag.

---

## [Non publié]

### Ajouté

- Squelette du dépôt d'exploitation : arborescence, gouvernance, conventions.
- `SECURITY.md` : politique de non-versionnement des secrets et des preuves de mission.
- `CONTRIBUTING.md` : modèle de branches, matrice de revue, cycle de vie d'une mission,
  versionnage sémantique de la doctrine.
- `CONVENTIONS.md` : nommage des documents, des SOP, des missions ; échelle de
  sévérité CVSS v4.0 unique ; référencement WSTG/ASVS/ATT&CK/ATLAS/CWE.
- `00-societe/smsi/REFERENTIELS.md` : choix des référentiels et justification.
- Squelette des huit services dans `10-services/`.
- `90-templates/` : chaîne de génération Markdown → DOCX/PDF à la charte (pandoc).
- `40-veille/` : classement de la veille technique par service.
- `NOMENCLATURE.md` : aide-mémoire d'une page de tous les codes employés.
- `NOTICE.md` : propriété et confidentialité du dépôt.
- `00-societe/rh/prompt-presentation-equipe.md` : prompt de génération du support
  de présentation du dépôt aux associés.
- `10-services/pentest-audit/` : méthodologie PTES adaptée, procédure de cadrage
  (`PRO-PT-001`), procédure de collecte et destruction des preuves (`PRO-PT-100`),
  checklist de relecture avant livraison. Ce service sert de référence aux autres.
- `10-services/*/methodologie/` : phases propres à chacun des sept autres services,
  avec ce qui leur est spécifique et le socle commun.
- `10-services/ai-redteaming/` : trois procédures (cadrage, tests adverses,
  notation et restitution) et la checklist de couverture OWASP Top 10 for LLM
  Applications 2025, avec référencement MITRE ATLAS. Notation adaptée au
  caractère non déterministe des modèles.
- `00-societe/juridique/CADRE-LEGAL.md` : cadre Togo (lois 2018-026 et 2019-014,
  ANCy, IPDCP), Afrique (Convention de Malabo) et Union européenne (RGPD, NIS2,
  AI Act), avec sources primaires.
- `00-societe/smsi/REFERENCES.md` : liens vers les sources officielles de tous
  les référentiels cités.
- `00-societe/PILOTAGE-PROJET.md` : tâches, répartition, estimation, délais, cadence.
- `00-societe/rh/GESTION-EQUIPE.md` : rôles, décisions, séniorité, accueil, départ.
- `00-societe/commercial/POSTURE.md` : posture commerciale par interlocuteur et par domaine.
- `30-outils/mcp/` : règles d'usage des serveurs MCP en mission.
- Chaîne de génération bureautique en Python natif (DOCX, XLSX, PPTX) à charte unique.

### À faire avant la v1.0.0

- [x] Pays de constitution : Togo → volet juridique local rédigé (`CADRE-LEGAL.md`)
- [ ] Faire relire les modèles NDA / MSA / RoE par un juriste
- [ ] Nommer les `CODEOWNERS` réels (comptes GitHub des 5 membres)
- [ ] Souscrire une assurance RC professionnelle → plafond à reporter dans le MSA
- [ ] Choisir et provisionner le coffre à preuves
- [ ] Passer chaque service de v0.1 à v1.0 (méthodologie complète + gabarit validé)

---

## Historique des versions de doctrine

| Version | Date | Portée |
|---|---|---|
| _(à venir)_ | | |
