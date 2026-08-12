# NexShield - Dépôt d'exploitation

> **Next Threat. Next Shield.**
> Dépôt **privé**. Mémoire opérationnelle, méthodologique et juridique de la société.

Ce dépôt n'est pas un dépôt de code. C'est la **doctrine** : comment nous vendons,
cadrons, exécutons et livrons chaque service - de manière identique, quel que soit
le membre de l'équipe qui tient le clavier.

> **Nom de la société**- Le nom peut encore changer. Il n'apparaît en dur que dans
> ce README et dans `90-templates/design/`. Un renommage = `make rename NOM="..."`.

---

## Je veux… → je vais là

| Je veux… | Dossier |
|---|---|
| Comprendre comment on travaille ensemble | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Nommer un fichier, une branche, un livrable | [`CONVENTIONS.md`](CONVENTIONS.md) |
| Retrouver un code, une sévérité, un statut | [`NOMENCLATURE.md`](NOMENCLATURE.md) - aide-mémoire d'une page |
| Savoir ce qui ne doit **jamais** entrer ici | [`SECURITY.md`](SECURITY.md) |
| Démarrer une mission client | [`20-missions/README.md`](20-missions/README.md) |
| Exécuter un service (méthodo, checklists, gabarits) | [`10-services/<service>/`](10-services/) |
| Un modèle de NDA, RoE, autorisation de test | [`00-societe/juridique/modeles/`](00-societe/juridique/modeles/) |
| Savoir qui fait quoi, pour quand | [`00-societe/PILOTAGE-PROJET.md`](00-societe/PILOTAGE-PROJET.md) |
| Comprendre les rôles et accueillir un nouveau | [`00-societe/rh/GESTION-EQUIPE.md`](00-societe/rh/GESTION-EQUIPE.md) |
| Préparer un rendez-vous client | [`00-societe/commercial/POSTURE.md`](00-societe/commercial/POSTURE.md) |
| Un classeur de suivi, un support de restitution | `make modeles` puis `90-templates/build/` |
| Générer un `.docx` / PDF à la charte | [`90-templates/README.md`](90-templates/README.md) |
| Un outil, une ressource de veille | [`40-veille/`](40-veille/) |
| Savoir ce qui a changé | [`CHANGELOG.md`](CHANGELOG.md) |

---

## Arborescence

```
00-societe/     L'entreprise elle-même : SMSI (ISO 27001), juridique, commercial, RH
10-services/    Une offre = un dossier, structure IDENTIQUE partout
20-missions/    Un client = un dossier. AUCUNE preuve brute ici (voir SECURITY.md)
30-outils/      Nos scripts, règles SIGMA, wordlists, configurations MCP
40-veille/      Veille technique classée par service
90-templates/   La charte documentaire et les gabarits (source unique)
```

**Règle de séparation**- `10-services/` ne contient que du **réutilisable**,
`20-missions/` que du **spécifique client**. Si vous écrivez deux fois la même
chose dans deux missions, c'est que ça appartient à `10-services/`.

---

## Les huit services

| Service | Référentiel d'exécution | Cadrage | Exécution | Checklist | Outillage |
|---|---|:-:|:-:|:-:|:-:|
| [`pentest-audit`](10-services/pentest-audit/) | PTES + OWASP WSTG + NIST SP 800-115 | oui | partiel | oui | non |
| [`ai-redteaming`](10-services/ai-redteaming/) | OWASP Top 10 LLM 2025 + MITRE ATLAS + NIST AI RMF | oui | oui | oui | oui |
| [`secu-applicative`](10-services/secu-applicative/) | OWASP ASVS 5.0 + WSTG + API Top 10 + MASTG | oui | oui | oui | oui |
| [`devsecops`](10-services/devsecops/) | OWASP SAMM + NIST SSDF (SP 800-218) + SLSA | oui | oui | oui | oui |
| [`soc-ai-tools`](10-services/soc-ai-tools/) | MITRE ATT&CK + D3FEND + SIGMA + NIST SP 800-61r3 | oui | oui | oui | oui |
| [`x-privacy`](10-services/x-privacy/) | Loi togolaise 2019-014 + RGPD + Convention de Malabo | oui | oui | oui | oui |
| [`sensibilisation`](10-services/sensibilisation/) | NIST SP 800-50r1 | oui | oui | oui | oui |
| [`infra-vpn-cloudflare`](10-services/infra-vpn-cloudflare/) | CIS Benchmarks + guides ANSSI + NIST SP 800-207 | oui | oui | oui | oui |

Tous les services sont en doctrine `v0.1` : la base est écrite et utilisable,
elle sera passée en `v1.0` après épreuve sur une première mission réelle.
`pentest-audit` reste à compléter sur ses procédures d'exécution
(`PRO-PT-101` à `PRO-PT-104`) et son outillage.

**Colonne vertébrale transverse : ISO/IEC 27001:2022** (notre SMSI) et
**MITRE ATT&CK** comme langage commun de tous nos livrables.

Voir [`00-societe/smsi/REFERENTIELS.md`](00-societe/smsi/REFERENTIELS.md) pour le
raisonnement complet.

---

## Onboarding d'un nouveau membre

1. Lire ce README, puis `SECURITY.md` - **avant** le premier commit.
2. Lire `CONTRIBUTING.md` et `CONVENTIONS.md`.
3. Installer les garde-fous : `make setup` (hooks pre-commit + gitleaks).
4. Lire [`00-societe/commercial/POSTURE.md`](00-societe/commercial/POSTURE.md) -
   comment nous parlons aux clients.
5. Lire le README du ou des services dont vous êtes responsable (`CODEOWNERS`).
6. Première contribution : corriger une coquille dans la doctrine, via PR. Ça
   valide que le circuit fonctionne pour vous.

Le parcours complet d'accueil est dans
[`00-societe/rh/GESTION-EQUIPE.md`](00-societe/rh/GESTION-EQUIPE.md) §4.
