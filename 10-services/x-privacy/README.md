# X-Privacy

**Code de service** : `PRIV` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Notre philosophie autant que notre offre : la vie privée comme propriété par défaut, pas comme option de conformité.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **RGPD** | Référence mondiale de fait |
| **ISO/IEC 27701** | Extension vie privée d'ISO 27001 - s'emboîte dans notre SMSI |
| **NIST Privacy Framework** | Pour les interlocuteurs non juristes |
| **Droit local + Convention de Malabo** |  à compléter - voir REFERENTIELS.md §3.6 |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Audit de conformité RGPD / droit local
- Cartographie des traitements et registre
- Analyse d'impact (AIPD / DPIA)
- Accompagnement DPO externalisé
- Audit de minimisation et de rétention des données
- Architecture de confidentialité par conception

## 3. Portée

### Ce qui est dans le périmètre

- Registre des traitements
- Bases légales et consentement
- Droits des personnes concernées
- Transferts hors territoire
- Sous-traitance et contrats
- Durées de conservation

### Ce qui n'y est pas

- Conseil juridique au sens strict - nous ne sommes pas avocats. Nous produisons des constats techniques et organisationnels ; le conseil juridique est renvoyé à un partenaire.

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission - jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- NDA
-  **Pays de constitution arrêté** et volet juridique local complété - ce service ne doit pas être vendu avant
- Partenariat avec un cabinet juridique local

## 5. Livrables

- `RAPPORT` d'écart de conformité
- Registre des traitements
- Plan de mise en conformité priorisé
- AIPD si applicable


## Documents disponibles

| Document | Objet |
|---|---|
| [`methodologie/README.md`](methodologie/README.md) | Les phases, et ce qui est propre a ce service |
| [`procedures/PRO-PRIV-001-cadrage.md`](procedures/PRO-PRIV-001-cadrage.md) | Regimes applicables, registre, formalites IPDCP |
| [`procedures/PRO-PRIV-100-evaluation-de-conformite.md`](procedures/PRO-PRIV-100-evaluation-de-conformite.md) | Verification sur piece, droits eprouves reellement, analyses d impact |
| [`checklists/checklist-conformite-donnees.md`](checklists/checklist-conformite-donnees.md) | Conformite des traitements, loi 2019-014 et RGPD |
| [`outillage/OUTILLAGE.md`](outillage/OUTILLAGE.md) | Le peu qui s outille, et tout ce qui ne s outille pas |

La collecte et la destruction des preuves suivent la procedure commune
[`PRO-GEN-100`](../../00-societe/procedures/PRO-GEN-100-collecte-de-preuves.md).

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-PRIV-NNN-*.md` | Des notes personnelles |
| `checklists/` | Checklists structurées par identifiant de référentiel | Des résultats de mission |
| `livrables/` | Gabarits de rapport propres à ce service | Des rapports clients (→ `20-missions/`) |
| `juridique/` | Clauses de RoE spécifiques à ce service | Les modèles génériques (→ `00-societe/juridique/`) |
| `outillage/` | Outils, configurations et scripts propres au service | Des secrets, des licences |

## 7. Reste à faire pour passer en v1.0

- [ ] Rédiger la méthodologie complète
- [ ] Rédiger les SOP de cadrage, d'exécution, de livraison
- [ ] Produire les checklists à partir du référentiel
- [ ] Valider le gabarit de livrable sur une mission blanche
- [ ] Faire relire les clauses juridiques spécifiques
- [ ] Fixer la grille tarifaire (`00-societe/commercial/`)
