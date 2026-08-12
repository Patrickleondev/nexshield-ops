# Checklist - maturité OWASP SAMM et chaîne de livraison

**Version** : v0.1 · Se recopie dans l'annexe du rapport de maturité.

**Référentiels** : [OWASP SAMM](https://owaspsamm.org/) ·
[NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) ·
[SLSA](https://slsa.dev/) · [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

**Règle d'évaluation** : une pratique déclarée sans preuve est notée au niveau
réellement constaté. On demande la preuve, systématiquement.

---

## 1. Évaluation SAMM

Cinq fonctions, quinze pratiques. Noter le niveau observé (0 à 3) et la preuve.

| Fonction | Pratique | Niveau | Preuve |
|---|---|---|---|
| Gouvernance | Stratégie et paramétrage | | |
| Gouvernance | Politique et conformité | | |
| Gouvernance | Éducation et sensibilisation | | |
| Conception | Évaluation des menaces | | |
| Conception | Exigences de sécurité | | |
| Conception | Architecture de sécurité | | |
| Implémentation | Construction sécurisée | | |
| Implémentation | Déploiement sécurisé | | |
| Implémentation | Gestion des défauts | | |
| Vérification | Évaluation de l'architecture | | |
| Vérification | Tests fondés sur les exigences | | |
| Vérification | Tests de sécurité | | |
| Opérations | Gestion des incidents | | |
| Opérations | Gestion de l'environnement | | |
| Opérations | Gestion opérationnelle | | |

---

## 2. Secrets

- [ ] Contrôle avant fusion refusant tout nouveau secret
- [ ] Historique complet balayé
- [ ] Chaque secret trouvé **révoqué** avant toute autre action
- [ ] Secrets remplacés par une référence à un coffre
- [ ] Aucun secret découvert n'a été testé pour vérifier sa validité
- [ ] Rotation des secrets documentée

## 3. Dépendances

- [ ] Inventaire complet, production et développement
- [ ] SBOM produit (CycloneDX ou SPDX)
- [ ] Priorisation croisée avec CISA KEV et EPSS
- [ ] Versions épinglées, intégrité vérifiée
- [ ] Distinction faite entre dépendance vulnérable et dépendance atteignable

## 4. Chaîne d'intégration

- [ ] Actions et images tierces épinglées par empreinte, pas par étiquette
- [ ] Droits des jetons réduits au strict nécessaire
- [ ] Chaînes déclenchées depuis l'extérieur sans accès aux secrets
- [ ] Branche principale protégée, revue obligatoire
- [ ] Journaux d'exécution conservés
- [ ] Chaîne de test sans accès à la production
- [ ] Tous les chemins vers la production identifiés et contrôlés

## 5. Analyse statique et dynamique

- [ ] Règles réglées avant activation du blocage
- [ ] Taux de faux positifs mesuré, sous 20 % avant blocage
- [ ] Résultats remis dans l'outil des développeurs
- [ ] Analyse dynamique branchée sur la préproduction seulement

## 6. Conteneurs et infrastructure

- [ ] Images de base minimales et à jour
- [ ] Aucun conteneur exécuté en `root` sans justification
- [ ] Analyse des images à la construction
- [ ] Configuration d'orchestration mesurée contre un CIS Benchmark
- [ ] Infrastructure en code analysée avant application

## 7. Seuils

- [ ] Sévérité bloquante définie pour la fusion et pour le déploiement
- [ ] Flux bloqué dès le premier jour
- [ ] Stock traité par un plan daté, non bloquant
- [ ] Procédure de dérogation écrite, tracée, avec un responsable nommé

---

## Avant de clore

- [ ] Score SAMM de départ et de sortie, tous deux datés
- [ ] Plan à 30, 90 et 365 jours, chaque action portant un nom et une date
- [ ] Recommandations rattachées à leur identifiant SSDF
- [ ] Aucun secret client conservé dans nos systèmes
- [ ] Double relecture effectuée
