# Contribuer

La règle d'or : **tout changement passe par une branche et une revue**, et
**tout est écrit**. Un membre absent ne doit jamais être un blocage.

---

## 1. Modèle de branches

`main` est toujours livrable et documentée. **Aucun commit direct**, pour personne,
y compris le fondateur.

| Préfixe | Usage | Exemple |
|---|---|---|
| `feat/` | Nouvelle procédure, nouveau gabarit, nouvelle offre | `feat/methodo-ai-redteam` |
| `fix/` | Correction d'une procédure existante | `fix/roe-clause-arret-urgence` |
| `docs/` | Documentation, README, veille | `docs/veille-outils-defcon` |
| `legal/` | **Tout document juridique**- relecture par 2 personnes | `legal/modele-nda-bilateral` |
| `mission/` | Une mission client | `mission/acme-pentest-webapp` |
| `chore/` | Outillage, CI, maintenance | `chore/gitleaks-ci` |

Cycle : brancher → committer petit et souvent → PR → revue → merge (squash) →
supprimer la branche.

---

## 2. Messages de commit (Conventional Commits)

```
<type>(<portée>): <résumé à l'impératif, sans point final>

<corps : le POURQUOI, pas seulement le quoi>
```

Types : `feat`, `fix`, `docs`, `chore`, `refactor`, `sec`, `legal`, `mission`.

```
feat(pentest): ajoute la phase de cadrage PTES à la méthodologie
legal(roe): précise la clause d'arrêt d'urgence sur découverte critique
sec(depot): active gitleaks en pre-commit
mission(acme): verse le rapport de pentest v1.0
```

Ces messages alimentent le `CHANGELOG.md` automatiquement (`git-cliff`). Un commit
mal typé = une ligne manquante dans le changelog.

---

## 3. Revue

| Type de changement | Approbations | Qui |
|---|---|---|
| Documentation, veille | 1 | n'importe quel pair |
| Procédure, méthodologie, checklist | 1 | le `CODEOWNERS` du service |
| **Document juridique** (`legal/`) | **2** | dont le responsable GRC |
| **Rapport client** | **2** | 1 pair technique + 1 relecture qualité/langue |
| Sécurité du dépôt, CI | 1 | responsable sécurité interne |

Toute PR doit :

1. décrire le **quoi** et le **pourquoi** ;
2. référencer l'issue ou la décision (ADR) concernée ;
3. passer la CI (gitleaks, lint Markdown, liens morts) ;
4. ne contenir **aucun secret ni preuve brute** (voir `SECURITY.md`) ;
5. mettre à jour la version de doctrine si la procédure change (§5).

**Un rapport client ne part jamais au client avant la fusion de sa PR.** La PR
*est* la relecture qualité.

---

## 4. Cycle de vie d'une mission

```
1. Issue "mission"          → périmètre pressenti, client, échéance
2. NDA signé                → avant toute discussion technique
3. Branche mission/<client>-<type>
4. PR "RoE"                 → 2 approbations, puis signature client
5. Autorisation de test     → signée, versée au dossier, AVANT la 1re commande
6. Exécution                → preuves dans le coffre, jamais dans Git
7. PR "rapport v1.0"        → 2 approbations
8. Merge + tag mission-<client>-<date>
9. Restitution client
10. J+90 : destruction des preuves + certificat signé
```

Les étapes 2 et 5 sont **bloquantes**. Aucune commande n'est lancée avant.

---

## 5. Versionnage de la doctrine (SemVer)

Chaque service porte un numéro de version affiché dans son README.

| Incrément | Quand | Conséquence |
|---|---|---|
| **MAJEUR** (2.0.0) | Changement qui invalide une mission en cours | Prévenir les missions actives ; ne s'applique qu'aux nouvelles |
| **MINEUR** (1.1.0) | Nouvelle étape, nouveau test, nouvelle checklist | S'applique aux prochaines missions |
| **CORRECTIF** (1.0.1) | Clarification, coquille, reformulation | S'applique immédiatement |

Chaque rapport client mentionne **sous quelle version de méthodologie** la mission
a été menée. C'est ce qui nous protège en cas de contestation : nous pouvons
prouver ce qui était notre standard à la date des tests.

---

## 6. Bonnes pratiques

- Un commit = une intention.
- Un `README.md` par dossier, qui explique ce qu'on y met **et ce qu'on n'y met pas**.
- On écrit en **Markdown**. Les `.docx` et PDF sont **générés** (`90-templates/`),
  jamais édités à la main puis committés - sinon les revues deviennent illisibles.
- Pas de binaire lourd hors Git LFS.
- Français pour la doctrine interne et les livrables clients francophones ;
  anglais pour les termes techniques consacrés (on n'écrit pas « hameçonnage
  ciblé » là où le client attend « spear phishing »).
