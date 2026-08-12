# Missions

Un dossier par mission : `<annee>/<CLIENT>-<type>-<nn>/`.

Créer une mission : `make mission CLIENT=ACME TYPE=pentest`

## Structure imposée

```
2026/ACME-pentest-01/
├── README.md            ← fiche mission : périmètre, dates, équipe, statut
├── roe/                 ← RoE + autorisation signée (PDF scanné)
├── rapport/             ← Markdown source ; le PDF est généré, pas versionné
├── preuves.sha256       ← manifeste d'empreintes
└── retex.md             ← retour d'expérience, obligatoire à la clôture
```

## Ce qu'on ne met JAMAIS ici

Captures d'écran de vulnérabilités, sorties d'outils, dumps, identifiants client,
enregistrements de session. **Tout ça vit au coffre chiffré**— voir `SECURITY.md` §2.
Le dépôt ne garde que le rapport et le manifeste d'empreintes.

La CI bloque toute PR contenant ces motifs. Ce n'est pas contournable.

## Statuts

`prospect` → `cadrage` → `signe` → `en-cours` → `livre` → `retest` → `clos`

Une mission passe à `clos` seulement après : RETEX rempli, preuves détruites,
certificat de destruction versé, comptes de test révoqués.
