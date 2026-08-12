# Infrastructure, VPN & Cloudflare

**Code de service** : `INFRA` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Durcissement d'infrastructures, architectures VPN et exposition maîtrisée via Cloudflare. Le service à forte marge : largement scorable automatiquement.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **CIS Benchmarks** | Scorables automatiquement (CIS-CAT, Lynis, OpenSCAP) |
| **Guides ANSSI** | Crédibilité francophone, attendus des administrations |
| **CIS Controls v8** | Grille de maturité d'ensemble pour PME |
| **NIST SP 800-207** | Architecture zéro confiance |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Audit de durcissement serveurs (Linux, Windows, hyperviseurs)
- Architecture et déploiement VPN (WireGuard, IPsec)
- Exposition maîtrisée via Cloudflare (WAF, Zero Trust Access, Tunnel)
- Segmentation réseau et matrice de flux
- Durcissement Kubernetes et conteneurs

## 3. Portée

### Ce qui est dans le périmètre

- Écart aux référentiels CIS/ANSSI, scoré
- Correctifs applicables en IaC (Ansible)
- Architecture cible documentée
- Matrice de flux et politique de segmentation

### Ce qui n'y est pas

- Infogérance et exploitation courante
- Support de niveau 1 aux utilisateurs finaux

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission - jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- NDA
- Accès en lecture aux systèmes audités
- Fenêtre de maintenance pour toute application de correctif
- Sauvegarde vérifiée avant tout durcissement - **bloquant**

## 5. Livrables

- `RAPPORT` d'écart CIS scoré, avant / après
- Playbooks Ansible de durcissement
- Schéma d'architecture cible
- Matrice de flux


## Documents disponibles

| Document | Objet |
|---|---|
| [`methodologie/README.md`](methodologie/README.md) | Les phases, et ce qui est propre a ce service |
| [`procedures/PRO-INFRA-001-cadrage.md`](procedures/PRO-INFRA-001-cadrage.md) | Sauvegardes restaurables, exposition reelle, fenetres d intervention |
| [`procedures/PRO-INFRA-100-durcissement.md`](procedures/PRO-INFRA-100-durcissement.md) | Un changement, une fenetre, un retour arriere |
| [`checklists/checklist-durcissement.md`](checklists/checklist-durcissement.md) | Exposition, acces, segmentation, systemes, bordure |
| [`outillage/OUTILLAGE.md`](outillage/OUTILLAGE.md) | Outils qui mesurent et outils qui appliquent |

La collecte et la destruction des preuves suivent la procedure commune
[`PRO-PT-100`](../pentest-audit/procedures/PRO-PT-100-collecte-de-preuves.md).

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-INFRA-NNN-*.md` | Des notes personnelles |
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
