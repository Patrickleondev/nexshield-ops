# Sécurité applicative

**Code de service** : `APP` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Revue de sécurité d'applications web, mobiles et API, mesurée sur un niveau d'assurance ASVS — pas sur un avis d'expert.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **OWASP ASVS 4.x** | Niveau d'assurance mesurable et re-mesurable |
| **OWASP MASTG/MASVS** | Applications mobiles |
| **OWASP API Security Top 10** | API REST et GraphQL |
| **CWE** | Classification des faiblesses |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Évaluation ASVS niveau 1 / 2 / 3
- Revue de code sécurité (boîte blanche)
- Audit d'API (REST, GraphQL)
- Audit d'application mobile Android / iOS
- Modélisation de menaces (threat modeling) en amont du développement

## 3. Portée

### Ce qui est dans le périmètre

- Authentification, session, contrôle d'accès
- Validation d'entrées, injections
- Cryptographie applicative, gestion des secrets
- Logique métier et enchaînements d'états
- Dépendances et chaîne d'approvisionnement

### Ce qui n'y est pas

- Infrastructure sous-jacente (relève de `infra-vpn-cloudflare`)
- Correction du code — nous recommandons, le client implémente (offre d'accompagnement distincte)

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission — jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- Idem pentest
- Accès au code source pour les prestations en boîte blanche, sous NDA renforcé
- Jeu de comptes de test couvrant tous les rôles applicatifs

## 5. Livrables

- `RAPPORT` avec score de conformité ASVS par chapitre
- Matrice ASVS exigence par exigence
- `SYNTH` avec le niveau atteint et l'écart au niveau visé

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-APP-NNN-*.md` | Des notes personnelles |
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
