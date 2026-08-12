# SOC & outillage IA défensif

**Code de service** : `SOC` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Détection, réponse et outillage augmenté par l'IA. Le service qui prolonge naturellement chaque mission offensive.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **MITRE ATT&CK** | Couverture de détection |
| **MITRE D3FEND** | Contre-mesures |
| **SIGMA** | Règles portables, indépendantes du SIEM |
| **NIST SP 800-61** | Cycle de réponse à incident |
| **STIX/TAXII** | Renseignement sur les menaces |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Évaluation de couverture de détection (ATT&CK Navigator)
- Rédaction et déploiement de règles SIGMA
- Mise en place SIEM (Wazuh, Elastic, OpenSearch)
- Enrichissement CTI (OpenCTI, MISP)
- Automatisation SOAR et triage assisté par IA
- Exercices de simulation d'adversaire (purple team)

## 3. Portée

### Ce qui est dans le périmètre

- Cartographie de couverture ATT&CK et identification des angles morts
- Ingénierie de détection et réduction du bruit
- Playbooks de réponse à incident
- Automatisation du triage de niveau 1

### Ce qui n'y est pas

- Surveillance 24/7 (offre SOC managé - à construire, ne pas vendre avant d'être capables de la tenir)
- Réponse à incident en urgence (offre distincte, contrat de disponibilité)

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission - jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- NDA
- Accès en lecture au SIEM et aux sources de journaux
- Inventaire des sources de télémétrie disponibles

## 5. Livrables

- Matrice de couverture ATT&CK avant / après
- Règles SIGMA versionnées et documentées
- Playbooks de réponse
- `RAPPORT` d'écart de détection

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-SOC-NNN-*.md` | Des notes personnelles |
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
