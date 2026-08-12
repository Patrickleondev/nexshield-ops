# Sources officielles des référentiels

Toutes les sources primaires, à consulter **directement** - jamais via un blog ou
un résumé. Un référentiel cité dans un livrable client doit être vérifié à sa
source le jour où on l'écrit : ces documents évoluent.

**Règle** : un rapport ne cite jamais un identifiant (WSTG-ATHN-01, T1190,
V2.1.1) sans que son auteur ait ouvert la page correspondante. Un identifiant
inventé ou périmé détruit la crédibilité de tout le document.

---

## Colonne vertébrale

| Référentiel | Source officielle | Gratuit |
|---|---|---|
| ISO/IEC 27001:2022 | [iso.org/standard/27001](https://www.iso.org/standard/27001) | Non - norme payante |
| ISO/IEC 27002:2022 | [iso.org/standard/75652.html](https://www.iso.org/standard/75652.html) | Non |
| ISO/IEC 27701 (vie privée) | [iso.org/standard/85819.html](https://www.iso.org/standard/85819.html) | Non |
| ISO/IEC 42001 (management de l'IA) | [iso.org/standard/81230.html](https://www.iso.org/standard/81230.html) | Non |
| MITRE ATT&CK | [attack.mitre.org](https://attack.mitre.org/) | Oui |
| MITRE D3FEND | [d3fend.mitre.org](https://d3fend.mitre.org/) | Oui |

> Les normes ISO sont payantes et **ne doivent pas être versionnées dans le
> dépôt** (droits d'auteur). On achète les exemplaires nécessaires, on en cite
> les numéros de mesure, on n'en recopie pas le texte.

---

## Pentest et audit

| Référentiel | Source |
|---|---|
| PTES - Penetration Testing Execution Standard | [pentest-standard.org](http://www.pentest-standard.org/) |
| OWASP Web Security Testing Guide (WSTG) | [owasp.org/www-project-web-security-testing-guide](https://owasp.org/www-project-web-security-testing-guide/) |
| NIST SP 800-115 - Technical Guide to Information Security Testing | [csrc.nist.gov/pubs/sp/800/115/final](https://csrc.nist.gov/pubs/sp/800/115/final) |
| OSSTMM | [isecom.org/OSSTMM.3.pdf](https://www.isecom.org/OSSTMM.3.pdf) |
| TIBER-EU (red team piloté par le renseignement) | [ecb.europa.eu - TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html) |

## Sécurité applicative

| Référentiel | Source |
|---|---|
| OWASP ASVS | [owasp.org/www-project-application-security-verification-standard](https://owasp.org/www-project-application-security-verification-standard/) |
| OWASP MASVS / MASTG (mobile) | [mas.owasp.org](https://mas.owasp.org/) |
| OWASP API Security Top 10 | [owasp.org/API-Security](https://owasp.org/API-Security/) |
| OWASP Top 10 (web) | [owasp.org/Top10](https://owasp.org/Top10/) |
| OWASP Cheat Sheet Series | [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/) |
| CWE - Common Weakness Enumeration | [cwe.mitre.org](https://cwe.mitre.org/) |
| CVSS v4.0 | [first.org/cvss/v4-0](https://www.first.org/cvss/v4-0/specification-document) |
| Calculateur CVSS v4.0 | [first.org/cvss/calculator/4.0](https://www.first.org/cvss/calculator/4.0) |

## AI RedTeaming

| Référentiel | Source |
|---|---|
| OWASP Top 10 for LLM Applications (2025) | [genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) |
| OWASP GenAI Security Project | [genai.owasp.org](https://genai.owasp.org/) |
| MITRE ATLAS | [atlas.mitre.org](https://atlas.mitre.org/) |
| NIST AI Risk Management Framework | [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| NIST AI 600-1 - profil IA générative | [nvlpubs.nist.gov - NIST.AI.600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) |
| Règlement européen sur l'IA (AI Act) | [eur-lex.europa.eu - 2024/1689](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=OJ:L_202401689) |

> L'édition 2025 (v2.0) du Top 10 LLM a été publiée le 18 novembre 2024 et
> utilise les identifiants `LLM01:2025` à `LLM10:2025`. Vérifier l'édition en
> vigueur avant chaque mission - ce référentiel bouge vite.

## DevSecOps

| Référentiel | Source |
|---|---|
| NIST SSDF - SP 800-218 | [csrc.nist.gov/pubs/sp/800/218/final](https://csrc.nist.gov/pubs/sp/800/218/final) |
| OWASP SAMM | [owaspsamm.org](https://owaspsamm.org/) |
| SLSA - chaîne d'approvisionnement | [slsa.dev](https://slsa.dev/) |
| OWASP Dependency-Track | [dependencytrack.org](https://dependencytrack.org/) |
| CycloneDX (SBOM) | [cyclonedx.org](https://cyclonedx.org/) |

## SOC et défensif

| Référentiel | Source |
|---|---|
| SIGMA - règles de détection | [sigmahq.io](https://sigmahq.io/) |
| NIST SP 800-61 - réponse à incident | [csrc.nist.gov/pubs/sp/800/61/r3/final](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |
| STIX / TAXII | [oasis-open.github.io/cti-documentation](https://oasis-open.github.io/cti-documentation/) |
| MITRE ATT&CK Navigator | [mitre-attack.github.io/attack-navigator](https://mitre-attack.github.io/attack-navigator/) |
| MITRE Engenuity - évaluations | [attackevals.mitre-engenuity.org](https://attackevals.mitre-engenuity.org/) |

## Durcissement et infrastructure

| Référentiel | Source |
|---|---|
| CIS Benchmarks | [cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks) |
| CIS Controls v8 | [cisecurity.org/controls](https://www.cisecurity.org/controls) |
| Guides et recommandations ANSSI | [cyber.gouv.fr/publications](https://cyber.gouv.fr/publications) |
| DISA STIG | [public.cyber.mil/stigs](https://public.cyber.mil/stigs/) |
| NIST SP 800-207 - architecture zéro confiance | [csrc.nist.gov/pubs/sp/800/207/final](https://csrc.nist.gov/pubs/sp/800/207/final) |

## Vie privée

| Référentiel | Source |
|---|---|
| RGPD - Règlement (UE) 2016/679 | [eur-lex.europa.eu - 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) |
| CNIL - guides et référentiels | [cnil.fr](https://www.cnil.fr/) |
| NIST Privacy Framework | [nist.gov/privacy-framework](https://www.nist.gov/privacy-framework) |
| Directive NIS2 - (UE) 2022/2555 | [eur-lex.europa.eu - 2022/2555](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022L2555) |

## Sensibilisation

| Référentiel | Source |
|---|---|
| NIST SP 800-50r1 | [csrc.nist.gov/pubs/sp/800/50/r1/final](https://csrc.nist.gov/pubs/sp/800/50/r1/final) |
| ENISA - sensibilisation | [enisa.europa.eu](https://www.enisa.europa.eu/topics/cybersecurity-education) |

---

## Cadre légal

Voir [`../juridique/CADRE-LEGAL.md`](../juridique/CADRE-LEGAL.md) pour l'analyse.
Sources primaires :

| Texte | Source |
|---|---|
| Togo - Loi n° 2018-026 (cybersécurité, cybercriminalité) | [ancy.gouv.tg](https://ancy.gouv.tg/wp-content/uploads/2022/02/Loi_n2018-026_du_07_decembre_2018_cybersecurite_et_cybercriminalite.pdf) |
| Togo - règles de cybersécurité (arrêté 2022-040/PMRT) | [cert.tg](https://cert.tg/wp-content/uploads/2022/07/20220705-Arrete-n%C2%B0-2022-040-PMRT-portant-adoption-des-regles-de-cybersecurite-en-Republique-togolaise.pdf) |
| Togo - Loi n° 2019-014 (données personnelles) | [afapdp.org](https://www.afapdp.org/archives/download-view/togo-loi-n-2019-014-du-29-octobre-2019-relative-a-la-protection-des-donnees-a-caractere-personnel) |
| Togo - IPDCP, cadre juridique | [ipdcp.tg](https://ipdcp.tg/ipdcp/cadre-juridique/) |
| Togo - ANCy, réglementations | [ancy.gouv.tg/reglementations](https://ancy.gouv.tg/reglementations/) |
| Togo - Journal officiel | [jo.gouv.tg](https://jo.gouv.tg/) |
| Union africaine - Convention de Malabo | [au.int](https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection) |

---

## Veille sur les vulnérabilités

| Source | Usage |
|---|---|
| NVD - base nationale des vulnérabilités | [nvd.nist.gov](https://nvd.nist.gov/) |
| CVE Program | [cve.org](https://www.cve.org/) |
| CISA KEV - vulnérabilités activement exploitées | [cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) |
| CERT-FR - avis et alertes | [cert.ssi.gouv.fr](https://www.cert.ssi.gouv.fr/) |
| CERT.tg | [cert.tg](https://cert.tg/) |
| EPSS - probabilité d'exploitation | [first.org/epss](https://www.first.org/epss/) |
| Exploit-DB | [exploit-db.com](https://www.exploit-db.com/) |

**CISA KEV et EPSS servent à prioriser.** Une vulnérabilité au catalogue KEV est
activement exploitée : elle passe devant, quel que soit son score CVSS. C'est un
argument de priorisation que peu de concurrents utilisent, et qui parle
immédiatement à un RSSI.
