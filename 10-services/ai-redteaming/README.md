# AI RedTeaming

**Code de service** : `AIRT` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Test offensif des systèmes à base d'IA : LLM, agents, RAG, pipelines de données. Notre différenciateur — très peu d'acteurs sont structurés sur ce métier.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **OWASP Top 10 for LLM Applications** | Taxonomie reconnue par le marché |
| **MITRE ATLAS** | TTP adverses IA — pendant d'ATT&CK |
| **NIST AI RMF 1.0 + profil GenAI** | Gouvernance, préparation à l'EU AI Act |
| **ISO/IEC 42001** | En réserve : offre gouvernance IA |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Audit de robustesse d'un LLM applicatif
- Test d'agents autonomes et de leur outillage
- Sécurité de pipeline RAG (empoisonnement, fuite par le contexte)
- Revue de garde-fous (guardrails) et de filtrage
- Évaluation de conformité NIST AI RMF

## 3. Portée

### Ce qui est dans le périmètre

- Injection de prompt directe et indirecte
- Contournement de garde-fous et de filtres
- Extraction de prompt système et de données d'entraînement
- Abus d'outils et d'appels de fonction par un agent
- Empoisonnement de la base vectorielle
- Dépassement de coût / déni de portefeuille

### Ce qui n'y est pas

- Attaques sur le modèle de fondation du fournisseur (hors périmètre client)
- Génération de contenu illégal à titre de démonstration — la preuve se fait par un marqueur inoffensif
- Tests dépassant les conditions d'utilisation du fournisseur de modèle

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission — jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- Idem pentest, plus :
- Accord explicite sur les coûts d'inférence engendrés par les tests
- Vérification des CGU du fournisseur de modèle (le client reste responsable)
- Environnement de test isolé quand la manipulation de données est nécessaire

## 5. Livrables

- `RAPPORT` avec mapping OWASP LLM + ATLAS
- `SYNTH` orientée risque métier et réglementaire
- Jeu de cas de test rejouable (`30-outils/`) pour la non-régression

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-AIRT-NNN-*.md` | Des notes personnelles |
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
