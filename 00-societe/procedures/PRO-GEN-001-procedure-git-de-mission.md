# PRO-GEN-001 - Procédure Git d'une mission

**Version** : v0.1 · **Portée** : tous services · **Responsable** : chef de mission

Cette procédure décrit, commande par commande, le passage d'une demande client à
une mission close dans Git. Elle complète `CONTRIBUTING.md` §4, qui donne le
cycle ; ici, on donne les gestes.

**Règle qui commande tout le reste** : une mission vit sur **sa propre branche**,
du premier jour au tag de clôture. On ne travaille jamais une mission client
directement sur `main`.

---

## 1. Nommer la branche

```
mission/<client>-<service>[-<nn>]
```

| Élément | Règle | Exemple |
|---|---|---|
| `<client>` | Code client en **minuscules**, 3 à 8 lettres, sans accent | `acme` |
| `<service>` | Le **code de service en minuscules** (voir table ci-dessous) | `pentest` |
| `<nn>` | Numéro d'ordre, seulement à partir de la deuxième mission de même nature | `02` |

Le nom de la **branche** est en minuscules ; le nom du **dossier** de mission
porte le code client en majuscules (`20-missions/2026/ACME-pentest-01/`). Cette
différence est voulue : Git est sensible à la casse selon les systèmes, les
dossiers ne le sont pas partout.

### Table des correspondances

| Service | Code branche et dossier | Code document |
|---|---|---|
| `pentest-audit` | `pentest` | `PT` |
| `ai-redteaming` | `airt` | `AIRT` |
| `secu-applicative` | `app` | `APP` |
| `devsecops` | `devsecops` | `DSO` |
| `soc-ai-tools` | `soc` | `SOC` |
| `x-privacy` | `privacy` | `PRIV` |
| `sensibilisation` | `sensib` | `SENS` |
| `infra-vpn-cloudflare` | `infra` | `INFRA` |

Exemples valables :

```
mission/acme-pentest
mission/acme-airt-02
mission/bassar-privacy
```

Exemples à refuser en revue :

```
mission/ACME-Pentest      majuscules
mission/acme              service absent : on ne saura pas quoi appliquer
mission/pentest-acme      ordre inversé, le tri par client devient impossible
feat/mission-acme         mauvais préfixe : une mission n'est pas une évolution
```

> **Le service est dans le nom de la branche parce qu'il détermine la procédure
> à appliquer.** Quelqu'un qui reprend la mission doit savoir, sans ouvrir un
> fichier, s'il suit `PRO-PT-*` ou `PRO-AIRT-*`.

### Une mission qui couvre plusieurs services

Le service dominant donne son nom à la branche, et les autres sont écrits dans
la fiche de mission. Si aucun ne domine, on ouvre **deux missions** : deux
périmètres, deux RoE, deux rapports. C'est plus clair pour le client, et c'est
facturable séparément.

---

## 2. Ouvrir la mission

Toujours à partir d'une `main` à jour. Une branche partie d'une `main` périmée
appliquera une doctrine périmée.

```sh
git switch main
git pull --ff-only
git switch -c mission/acme-pentest
make mission CLIENT=ACME TYPE=pentest-audit
```

`make mission` crée `20-missions/<annee>/ACME-pentest-audit-01/`, y copie les
gabarits juridiques et le classeur de mission, et écrit la fiche.

Premier commit, avant toute action technique :

```sh
git add 20-missions/2026/ACME-pentest-audit-01
git commit -m "mission(acme): ouvre la mission pentest, perimetre pressenti"
git push -u origin mission/acme-pentest
```

Pousser tout de suite n'est pas une formalité : la branche devient visible par
l'équipe, et le travail n'est plus sur un seul poste.

---

## 3. Les deux verrous

Ils viennent de `CONTRIBUTING.md` §4 et ne se contournent pas.

### Verrou 1 - NDA signé

Avant toute discussion technique. Tant qu'il n'est pas signé, la mission reste
au niveau commercial : on ne décrit pas le système du client, on n'écrit pas de
périmètre technique dans le dépôt.

### Verrou 2 - RoE et autorisation de test signés

Avant la première commande, **reconnaissance passive comprise**.

```sh
git add 20-missions/2026/ACME-pentest-audit-01/roe/
git commit -m "mission(acme): verse le RoE et l'autorisation signes"
```

Les documents signés sont versés en PDF scanné. La fiche de mission passe au
statut `signe`.

> **Aucune commande n'est lancée tant que ce commit n'existe pas.** C'est la
> pièce qui rend nos tests licites au regard de la loi togolaise n° 2018-026, et
> c'est aussi la pièce qui nous défendra si le cadre est contesté.

---

## 4. Pendant l'exécution

### Ce qui est commité

| Oui | Non |
|---|---|
| Fiche de mission, statuts, dates | Captures d'écran de vulnérabilités |
| RoE et autorisations signés | Sorties d'outils brutes |
| Rapport en cours de rédaction | Extraits de données client |
| Manifeste d'empreintes `preuves.sha256` | Identifiants, jetons, clés |
| RETEX | Enregistrements de session |

Les preuves vivent au **coffre chiffré**, jamais dans Git. La CI bloque toute PR
contenant ces motifs, et ce n'est pas contournable (`SECURITY.md` §2).

### Rythme des commits

Un commit par jour de mission au minimum, même sans livrable fini. Un commit
quotidien vaut journal : si une contestation survient trois mois plus tard, la
chronologie est déjà établie.

```sh
git commit -m "mission(acme): journal du 15/08, phase de renseignement close"
```

### Format des messages

```
mission(<client>): <ce qui a ete fait, a l'imperatif>
```

Le client apparaît dans la portée. Le message ne contient **jamais** de détail
technique exploitable : `mission(acme): consigne 3 constatations` et non
`mission(acme): trouve une injection SQL sur /login`.

Un historique Git peut fuiter. Il est écrit comme s'il allait être lu par un
tiers.

---

## 5. Livrer

Le rapport passe par une **pull request**, comme tout le reste, avec **deux
approbations** (`CONTRIBUTING.md` §3). Aucun rapport ne part chez un client avant
la fusion de sa PR.

```sh
git switch mission/acme-pentest
git commit -m "mission(acme): rapport v1.0 pret pour relecture"
git push
```

La PR porte comme titre `Mission ACME - rapport pentest v1.0` et contient :

- Le périmètre, en une ligne
- Le nombre de constatations par sévérité
- Ce qui n'a pas été exécuté, et pourquoi
- La confirmation que la checklist de livraison est remplie **par le relecteur**

Après approbation :

```sh
git switch main
git pull --ff-only
git merge --squash mission/acme-pentest
git commit -m "mission(acme): pentest livre, rapport v1.0"
git tag -a mission-acme-20260815 -m "Mission ACME pentest, rapport v1.0"
git push origin main --tags
```

Le tag est la trace immuable de ce qui a été livré, à quelle date. C'est lui
qu'on ressortira en cas de litige.

---

## 6. Clôturer

Une mission n'est close qu'après **toutes** ces conditions :

- [ ] RETEX rempli, y compris quand la mission s'est bien passée
- [ ] Preuves détruites à J+90, certificat versé
- [ ] Comptes de test révoqués, confirmé par le client
- [ ] Attestation de nettoyage remise (pour les services qui interviennent)
- [ ] Statut de la fiche passé à `clos`

```sh
git switch -c docs/retex-acme-pentest
git commit -m "mission(acme): retex et certificat de destruction"
git switch main && git branch -d mission/acme-pentest
git push origin --delete mission/acme-pentest
```

La branche de mission est supprimée après fusion. Le tag conserve l'historique :
rien n'est perdu.

---

## 7. Cas particuliers

### Contre-vérification

Nouvelle branche, rattachée à la mission d'origine :

```
mission/acme-pentest-retest
```

Les identifiants de vulnérabilité **ne changent jamais** : `ACME-2026-001` reste
`ACME-2026-001` entre le rapport et sa contre-vérification. C'est ce qui permet
de suivre une correction dans le temps (`NOMENCLATURE.md` §10).

### Mission arrêtée en cours

Une mission arrêtée ne se supprime pas. On consigne :

```sh
git commit -m "mission(acme): mission arretee, motif consigne dans la fiche"
```

Statut `clos`, motif écrit dans la fiche. Une mission arrêtée pour compromission
préexistante est une information qui peut resservir.

### Correction après livraison

Une version livrée ne se modifie plus (`NOMENCLATURE.md` §6). Une correction
produit une `v1.1`, sur une nouvelle branche, avec sa propre PR et son tag.

---

## 8. Ce qui fait échouer une revue

| Motif | Pourquoi c'est bloquant |
|---|---|
| Branche sans code de service | On ne sait pas quelle procédure appliquer |
| Travail de mission commité sur `main` | Le cloisonnement par client disparaît |
| Preuve brute ou secret dans la PR | Bloqué par la CI, et faute au regard de `SECURITY.md` |
| Détail technique exploitable dans un message de commit | L'historique peut fuiter |
| Rapport poussé au client avant fusion | Contourne la double relecture |
| RoE versé après la première commande | Les tests étaient sans base légale |
| Branche supprimée sans tag | La trace de ce qui a été livré est perdue |

---

## 9. Aide-mémoire

```sh
# Ouvrir
git switch main && git pull --ff-only
git switch -c mission/<client>-<service>
make mission CLIENT=<CLIENT> TYPE=<service-complet>
git push -u origin mission/<client>-<service>

# Verrouiller (avant toute commande)
git commit -m "mission(<client>): verse le RoE et l'autorisation signes"

# Travailler (un commit par jour, sans detail technique)
git commit -m "mission(<client>): <ce qui a ete fait>"

# Livrer (PR, 2 approbations)
git merge --squash mission/<client>-<service>
git tag -a mission-<client>-<AAAAMMJJ> -m "<objet>"
git push origin main --tags

# Cloturer (RETEX, preuves detruites, comptes revoques)
git push origin --delete mission/<client>-<service>
```
