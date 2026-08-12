# DevSecOps

**Code de service** : `DSO` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Intégration de la sécurité dans la chaîne de développement et de livraison. Le service qui crée du revenu récurrent : un score de maturité se re-mesure chaque année.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **NIST SSDF (SP 800-218)** | Les 42 pratiques : le quoi |
| **OWASP SAMM 2.0** | La maturité mesurable : le combien |
| **SLSA** | Chaîne d'approvisionnement logicielle : niveaux 1 à 3 |
| **CIS Benchmarks** | Durcissement des runners, registres, conteneurs |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Audit de maturité SAMM (état des lieux + feuille de route)
- Mise en place d'une chaîne CI/CD sécurisée (SAST, SCA, secrets, IaC, conteneurs)
- Sécurisation de la chaîne d'approvisionnement (SBOM, signature, SLSA)
- Accompagnement au shift-left et formation des équipes de développement

## 3. Portée

### Ce qui est dans le périmètre

- Analyse statique, composition logicielle, détection de secrets
- Sécurité des conteneurs et de l'IaC
- Gestion des secrets et des identités de pipeline
- SBOM et politique de dépendances
- Feuille de route de maturité chiffrée

### Ce qui n'y est pas

- Développement fonctionnel
- Exploitation quotidienne de la chaîne (offre d'infogérance distincte)

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission - jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- NDA
- Accès en lecture aux dépôts et à la plateforme CI/CD
- Entretiens avec les équipes de développement - prévoir la disponibilité

## 5. Livrables

- `RAPPORT` de maturité SAMM avec scores par domaine
- Feuille de route priorisée à 6/12/18 mois
- Configurations CI/CD de référence
- Réévaluation annuelle (base du récurrent)

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-DSO-NNN-*.md` | Des notes personnelles |
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
