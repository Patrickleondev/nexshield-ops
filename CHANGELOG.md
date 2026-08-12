# Journal des changements

Format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versionnage [SemVer](https://semver.org/lang/fr/) appliqué à la **doctrine** (voir `CONTRIBUTING.md` §5).

Généré semi-automatiquement depuis les Conventional Commits (`make changelog`),
puis relu à la main avant chaque tag.

---

## [Non publié]

### Ajouté

- Socle opérationnel des six services restants : pour chacun, une procédure de
  cadrage, une procédure d'exécution, une checklist bâtie sur le référentiel et
  un document d'outillage.
  - `secu-applicative` : `PRO-APP-001`, `PRO-APP-100`, couverture des 17 chapitres
    d'OWASP ASVS 5.0.0.
  - `devsecops` : `PRO-DSO-001`, `PRO-DSO-100`, évaluation OWASP SAMM et
    durcissement de la chaîne de livraison.
  - `soc-ai-tools` : `PRO-SOC-001`, `PRO-SOC-100`, couverture ATT&CK notée en
    trois états, règles SIGMA éprouvées avant livraison.
  - `x-privacy` : `PRO-PRIV-001`, `PRO-PRIV-100`, régimes togolais et européen
    traités ensemble, droits des personnes réellement exercés.
  - `sensibilisation` : `PRO-SENS-001`, `PRO-SENS-100`, charte de campagne
    interdisant toute sanction individuelle et tout résultat nominatif.
  - `infra-vpn-cloudflare` : `PRO-INFRA-001`, `PRO-INFRA-100`, restauration
    vérifiée avant intervention, un changement par fenêtre.
- `10-services/*/outillage/OUTILLAGE.md` : pour chaque service, le socle d'outils
  retenu avec sa licence, et surtout le tableau de ce qu'aucun outil ne couvre.
- Liens vers les sources officielles dans les checklists et les README de service.
- `pentest-audit` complété : `PRO-PT-100` (renseignement), `PRO-PT-101`
  (modélisation de menaces), `PRO-PT-102` (analyse de vulnérabilités),
  `PRO-PT-103` (exploitation), `PRO-PT-104` (post-exploitation et nettoyage),
  `PRO-PT-200` (restitution), et son document d'outillage.

### Modifié

- La procédure de collecte et de destruction des preuves, commune à tous les
  services, est renommée `PRO-PT-100` en **`PRO-GEN-100`** et déplacée dans
  `00-societe/procedures/`. Le code `GEN` est celui prévu par `NOMENCLATURE.md`
  pour les documents transverses ; le numéro `PRO-PT-100` revient au
  renseignement, comme l'annonçait la méthodologie PTES. Renommage par `git mv`,
  toutes les références mises à jour.
- Suppression des tirets cadratins et demi-cadratins dans l'ensemble du dépôt.

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
  (`PRO-PT-001`), procédure de collecte et destruction des preuves (`PRO-GEN-100`),
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
