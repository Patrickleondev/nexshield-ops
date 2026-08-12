# Charte documentaire

**Le principe** : on écrit en Markdown, on **génère** le DOCX et le PDF.

Personne n'édite un `.docx` à la main pour le committer ensuite. Un `.docx` est un
binaire : il ne se diffe pas, il ne se fusionne pas, et à cinq vous produiriez en
trois mois cinq chartes graphiques différentes sans vous en rendre compte.

```
rapport.md ──pandoc──┬──> rapport.docx   (reference.docx = la charte Word)
                     └──> rapport.pdf    (style.css = la même charte, en CSS)
```

Modifier `reference.docx` **une fois**→ **tous** les documents de la société
changent au prochain build. C'est ça, une identité visuelle unique et tenable.

---

## Palette

Alignée sur le site (`nexshieldsec.netlify.app`) — l'identité est la même sur le
web et sur les livrables.

| Rôle | Couleur | Hex | Usage |
|---|---|---|---|
| Primaire | Bleu nuit | `#0B1220` | Titres de niveau 1, bandeaux, couverture |
| Secondaire | Ardoise | `#1E293B` | Titres 2 et 3, filets |
| Accent | Cyan | `#06B6D4` | Liens, éléments mis en avant, filets de couverture |
| Texte | Ardoise foncée | `#0F172A` | Corps de texte |
| Texte secondaire | Gris ardoise | `#475569` | Légendes, notes de bas de page |
| Fond alterné | Gris très clair | `#F1F5F9` | Lignes paires de tableau |

### Sévérités — couleurs figées

Ces six couleurs ne changent jamais, dans aucun document, dans aucun graphique.
Un client doit reconnaître « rouge = critique » d'un rapport à l'autre.

| Sévérité | Hex | Contraste sur blanc |
|---|---|---|
| Critique | `#991B1B` | 8.6:1 Oui |
| Élevée | `#C2410C` | 4.9:1 Oui |
| Moyenne | `#A16207` | 4.8:1 Oui |
| Faible | `#0369A1` | 6.1:1 Oui |
| Information | `#475569` | 7.5:1 Oui |
| Corrigée | `#15803D` | 4.8:1 Oui |

Tous les ratios dépassent 4.5:1 (WCAG AA). **La couleur n'est jamais le seul
porteur d'information**: une sévérité s'écrit toujours en toutes lettres à côté
de sa pastille — un lecteur daltonien, ou un rapport imprimé en noir et blanc,
doit rester exploitable.

---

## Typographie

| Usage | Police | Repli | Taille |
|---|---|---|---|
| Titres | Inter SemiBold | Calibri, sans-serif | 20 / 16 / 13 pt |
| Corps | Inter Regular | Calibri | 10.5 pt, interligne 1.4 |
| Code, identifiants | JetBrains Mono | Consolas | 9.5 pt |
| Légendes | Inter Regular | Calibri | 9 pt, gris `#475569` |

Ce sont les polices du site — cohérence web / documents. Prévoir les replis :
le client n'aura pas Inter installé.

---

## Règles de mise en page

- **Couverture** : logo, titre, client, version, date, mention de classification,
  filet cyan. Aucune information technique.
- **Pied de page** : `<CLIENT> — CONFIDENTIEL — page X / Y`. Sur **toutes** les pages.
- **En-tête** : nom du document à droite, à partir de la page 2.
- **Marges** : 2,5 cm. Les rapports s'impriment et s'annotent encore.
- **Tableaux** : en-tête sur fond primaire, texte blanc, lignes paires `#F1F5F9`.
  Pas de bordures verticales.
- **Blocs de code** : fond `#F1F5F9`, filet gauche cyan de 3 pt.
- **Captures** : largeur maximale, légende numérotée en dessous, **toujours
  anonymisées**avant insertion.

## Ton rédactionnel

- Factuel. On décrit ce qu'on a observé, pas ce qu'on suppose.
- Impact métier avant détail technique. Toujours.
- Pas de dramatisation : un rapport qui exagère perd sa crédibilité sur la
  constatation suivante.
- Pas de nom de personne dans un constat. On décrit un système, jamais un employé.
- Vouvoiement, présent de l'indicatif, phrases courtes.

---

## À produire

- [ ] `reference.docx` — styles Word (Titre 1-4, Corps, Code, Tableau, Légende)
- [ ] `couverture.docx` — page de garde
- [ ] `style.css` — même charte pour la sortie PDF (WeasyPrint)
- [ ] Logo en SVG et PNG, versions claire et sombre

> **Comment produire `reference.docx`** : `pandoc -o reference.docx --print-default-data-file reference.docx`
> puis ouvrir dans Word/LibreOffice et **modifier les styles** (pas le contenu).
