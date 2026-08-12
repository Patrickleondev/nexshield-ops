## Quoi

<Ce que change cette PR.>

## Pourquoi

<Le besoin, l'incident ou le RETEX à l'origine. Une PR sans pourquoi sera refusée.>

## Type

- [ ] Doctrine (procédure, méthodologie, checklist) → impose une version (§5 CONTRIBUTING)
- [ ] Juridique (`legal/`) → **2 approbations**, dont GRC
- [ ] Mission → **2 approbations**, dont 1 relecture qualité
- [ ] Documentation / veille
- [ ] Outillage / CI

## Impact sur la doctrine

- Service concerné : `<…>`
- Version : `v<X.Y>` → `v<X.Y>`
- [ ] Aucun changement de version (documentation seule)
- [ ] Change une mission **en cours**→ prévenir le chef de mission

## Contrôles

- [ ] `make check` passe (gitleaks + lint)
- [ ] **Aucun secret, aucune preuve brute** (`SECURITY.md` §1)
- [ ] Nommage conforme (`CONVENTIONS.md`)
- [ ] `CHANGELOG.md` mis à jour si la doctrine change
