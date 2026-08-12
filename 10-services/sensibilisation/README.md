# Sensibilisation

**Code de service** : `SENS` · **Version de doctrine** : `v0.1` (brouillon) ·
**Statut commercial** : non vendable tant que la doctrine n'est pas en `v1.0`

> Programmes de sensibilisation mesurés. Une sensibilisation non mesurée ne se vend qu'une fois ; une sensibilisation mesurée se reconduit chaque année.

---

## 1. Référentiels

| Référentiel | Rôle |
|---|---|
| **NIST SP 800-50r1** | Impose la mesure d'efficacité |
| **ENISA** | Kits et supports réutilisables |
| **ISO 27001 A.6.3** | Nos livrables servent de preuve à l'audit du client |

Justification du choix : [`00-societe/smsi/REFERENTIELS.md`](../../00-societe/smsi/REFERENTIELS.md).

## 2. Offres

- Programme annuel de sensibilisation
- Campagnes de phishing simulé avec mesure
- Ateliers par métier (direction, développeurs, comptabilité, RH)
- Sensibilisation dirigeants (fraude au président, risques ciblés)
- Contenus sur mesure aux couleurs du client

## 3. Portée

### Ce qui est dans le périmètre

- État des lieux initial (mesure avant)
- Contenus et animations
- Simulations et exercices
- Mesure d'efficacité et rapport de progression

### Ce qui n'y est pas

- Sanction ou évaluation individuelle des employés — la mesure est **collective et anonymisée**. Point non négociable : une simulation de phishing utilisée pour sanctionner détruit la confiance et l'efficacité du programme.

> Cette section n'est pas décorative : elle est **reprise mot pour mot** dans la
> proposition commerciale et dans le RoE. Un désaccord de périmètre se règle ici,
> avant la mission — jamais pendant.

## 4. Préalables bloquants

Aucune action technique ne démarre tant que ces points ne sont pas satisfaits :

- NDA
- **Accord des représentants du personnel** pour les campagnes de phishing simulé
- Information préalable des employés sur l'existence du programme (pas sur ses dates)
- Cadrage des données collectées avec le service `x-privacy`

## 5. Livrables

- Programme annuel
- Supports et contenus
- Rapport de campagne (taux de clic, de signalement, de saisie)
- Rapport de progression d'une année sur l'autre

## 6. Contenu de ce dossier

| Dossier | Ce qu'on y met | Ce qu'on n'y met pas |
|---|---|---|
| `methodologie/` | Notre adaptation des référentiels, phase par phase | Le référentiel brut (mettre un lien) |
| `procedures/` | SOP numérotées `PRO-SENS-NNN-*.md` | Des notes personnelles |
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
