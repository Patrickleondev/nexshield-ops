# Conventions de nommage

Objectif : que n'importe quel membre retrouve et comprenne un document sans
demander à son auteur.

---

## Documents

```
AAAAMMJJ-<CLIENT>-<TYPE>-<titre-en-minuscules>-v<X.Y>.<ext>
```

- `AAAAMMJJ` - date de **publication** de la version, pas de création.
- `<CLIENT>` - code client en MAJUSCULES (3 à 8 lettres). `INTERNE` si document interne.
- `<TYPE>` - voir table ci-dessous.
- `<titre>` - minuscules, tirets, sans accent, sans espace.
- `v<X.Y>` - `v0.x` = brouillon, `v1.0` = première version livrée au client.

```
20260815-ACME-ROE-pentest-webapp-v1.0.md
20260820-ACME-RAPPORT-pentest-webapp-v1.0.md
20260901-INTERNE-PROC-cadrage-mission-v1.2.md
```

### Codes de type

| Code | Document |
|---|---|
| `NDA` | Accord de confidentialité |
| `MSA` | Contrat-cadre de services |
| `SOW` | Énoncé des travaux / bon de commande |
| `ROE` | Rules of Engagement (règles d'engagement techniques) |
| `AUTH` | Autorisation de test signée |
| `PROPO` | Proposition commerciale |
| `RAPPORT` | Rapport de mission |
| `SYNTH` | Synthèse exécutive (document séparé, pour la direction du client) |
| `RETEST` | Rapport de contre-vérification |
| `PROC` | Procédure interne (SOP) |
| `POL` | Politique interne (SMSI) |
| `ADR` | Décision d'architecture / de doctrine |
| `ATTEST` | Attestation de test (pour audit, assurance, appel d'offres) |

---

## Procédures internes (SOP)

```
PRO-<SERVICE>-<NNN>-<titre>.md
```

`<SERVICE>` : `PT` (pentest), `AIRT` (AI redteaming), `APP` (sécu applicative),
`DSO` (devsecops), `SOC`, `PRIV` (x-privacy), `SENS` (sensibilisation),
`INFRA`, `GEN` (transverse).

```
PRO-PT-001-cadrage-et-perimetre.md
PRO-PT-002-collecte-de-preuves.md
PRO-GEN-001-onboarding-membre.md
```

Numérotation par centaines : `001-099` cadrage, `100-199` exécution,
`200-299` livraison, `300-399` clôture.

---

## Missions

```
20-missions/<annee>/<CLIENT>-<type>-<nn>/
```

`20-missions/2026/ACME-pentest-01/` - le `-01` permet une deuxième mission du
même type pour le même client dans l'année.

Contenu obligatoire de chaque dossier de mission :

```
README.md               ← fiche mission : périmètre, dates, équipe, statut
roe/                    ← RoE + autorisation signée (PDF scanné)
rapport/                ← Markdown source + PDF généré
preuves.sha256          ← manifeste d'empreintes (les preuves sont au coffre)
retex.md                ← retour d'expérience, rempli à la clôture
```

---

## Dossiers

Minuscules, tirets, sans accent, sans espace, sans majuscule. Un dossier se lit
dans une URL, dans un terminal et sur trois systèmes d'exploitation différents :
tout le reste crée des problèmes tôt ou tard.

```
10-services/secu-applicative/        correct
10-services/Sécurité Applicative/    à proscrire
```

**Exception unique** : les dossiers de mission, qui portent un code client en
majuscules pour être repérables d'un coup d'œil - `20-missions/2026/ACME-pentest-01/`.

Le préfixe numérique des dossiers racine (`00-`, `10-`, `20-`…) fixe l'ordre
d'affichage et donc l'ordre de lecture. Il est espacé par dizaines pour pouvoir
intercaler un domaine sans tout renuméroter.

---

## Renommer un fichier ou un dossier

Un renommage mal fait casse des liens, perd l'historique et rend une PR
illisible. La procédure n'est pas facultative.

### La règle

**Toujours `git mv`, jamais supprimer puis recréer.**

```sh
git mv ancien-nom.md nouveau-nom.md
```

`git mv` préserve l'historique du fichier : `git log --follow` continue de
fonctionner, et la PR affiche « renommé » au lieu de « 200 lignes supprimées,
200 lignes ajoutées ». C'est la différence entre une revue de trente secondes et
une revue impossible.

### La procédure complète

1. **Une PR dédiée au renommage.** Ne jamais renommer et modifier le contenu
   dans le même commit : la détection de renommage de Git ne survit pas à un
   contenu trop modifié, et la revue redevient illisible.
2. `git mv` pour chaque fichier ou dossier concerné.
3. **Mettre à jour tous les liens entrants** :
   ```sh
   grep -rn "ancien-nom" --include='*.md' --include='*.py' .
   ```
   Un lien mort dans la doctrine est un lecteur perdu.
4. Vérifier les références dans les scripts, le `Makefile`, `CODEOWNERS` et les
   workflows CI - ce sont les oublis classiques.
5. `make links` pour confirmer qu'aucun lien n'est cassé.
6. **Consigner dans `CHANGELOG.md`**, section « Modifié ». Un renommage est un
   changement visible : quelqu'un cherchera l'ancien nom.

### Ce qui ne se renomme jamais

| Élément | Pourquoi |
|---|---|
| Un document **déjà livré** à un client | Il est référencé dans un contrat et dans le rapport du client |
| Un dossier de mission **close** | Il est référencé dans le portefeuille et dans les archives |
| Un identifiant de vulnérabilité | Il suit la vulnérabilité jusqu'à sa contre-vérification |

Si le nom d'un livrable est vraiment mauvais, on publie une **nouvelle version**
sous le bon nom, et l'ancienne reste en place. On ne réécrit pas le passé.

### Renommer la société

`make rename NOM="NouveauNom"`. Relire ensuite `CODEOWNERS`,
`30-outils/scripts/charte.py` et les documents déjà générés - la commande ne
touche pas aux binaires.

---

## Versionner un document

Le numéro de version vit **à trois endroits**, et les trois doivent concorder :

1. dans le **nom du fichier** - `…-v1.0.docx` ;
2. sur la **page de garde** du document ;
3. dans le tableau **Historique des versions**, en fin de document.

### L'échelle

| Version | Signification |
|---|---|
| `v0.1` à `v0.9` | Brouillon interne. **Ne sort jamais de la société.** |
| `v1.0` | Première version livrée au client |
| `v1.1`, `v1.2` | Correction ou précision après retour du client |
| `v2.0` | Refonte, ou nouvelle campagne sur le même périmètre |

### La règle d'immutabilité

**Une version livrée ne se modifie plus.** Jamais, même pour une coquille.

Le client a reçu un fichier, il l'a peut-être transmis à son assureur ou à son
auditeur. Deux fichiers différents portant le même numéro de version, c'est un
problème de confiance qu'on ne rattrape pas.

Une correction produit une `v1.1`, accompagnée d'un courriel qui dit ce qui a
changé et pourquoi. C'est plus coûteux, et c'est la seule option défendable.

### Version de doctrine et version de document

Ce sont deux choses distinctes, et un rapport porte les deux :

- **Version du document** : `v1.0` - cette instance du rapport.
- **Version de doctrine** : `pentest-audit v1.2` - la méthodologie sous laquelle
  la mission a été menée.

C'est cette seconde information qui vous protège en cas de contestation : elle
prouve quel était votre standard à la date des tests. Voir
[`CONTRIBUTING.md`](CONTRIBUTING.md) §5.

---

## Branches et commits

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Sévérités

Une seule échelle, partout, pour tous les services. **CVSS v4.0** pour le score
technique, complété d'une **criticité métier** décidée avec le client.

| Niveau | CVSS v4.0 | Délai de correction recommandé |
|---|---|---|
| Critique | 9.0 - 10.0 | Immédiat (< 72 h), notification pendant la mission |
| Élevée | 7.0 - 8.9 | 30 jours |
| Moyenne | 4.0 - 6.9 | 90 jours |
| Faible | 0.1 - 3.9 | Prochain cycle de maintenance |
| Information | 0.0 | Aucune obligation |

Un score CVSS **seul** ne justifie jamais une sévérité dans un rapport : la
criticité affichée doit tenir compte de l'exposition réelle et de la valeur métier
de l'actif. Toute divergence entre CVSS et criticité affichée est **justifiée par
écrit**dans la fiche de vulnérabilité.

### Identifiants de vulnérabilité

```
<CLIENT>-<AAAA>-<NNN>
```

`ACME-2026-001`. Numérotation continue par client et par année, tous types de
missions confondus - pour pouvoir suivre une vulnérabilité d'un pentest à sa
contre-vérification.

---

## Référencement des standards

Toute vulnérabilité d'un rapport porte, quand c'est applicable :

- son identifiant **OWASP WSTG** (`WSTG-ATHN-01`) ou **ASVS** (`V2.1.1`) ;
- sa **technique MITRE ATT&CK** (`T1190`) ou **ATLAS** (`AML.T0051`) pour l'IA ;
- son **CWE** (`CWE-89`).

C'est ce qui rend nos rapports directement exploitables par le SOC du client, et
ce qui prouve la couverture de notre méthodologie.
