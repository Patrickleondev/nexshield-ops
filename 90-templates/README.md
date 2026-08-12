# Gabarits documentaires

## Pourquoi la doctrine est en Markdown — et pourquoi les livrables ne le sont pas

Ce sont deux besoins différents, et c'est la raison de la séparation.

**La doctrine interne est en Markdown** parce qu'elle est vivante et relue.
Un `.docx` est un binaire : il ne se compare pas d'une version à l'autre, deux
personnes ne peuvent pas le modifier en parallèle, et une revue devient
impossible. Une procédure qu'on ne peut pas relire ligne à ligne en PR n'évolue
jamais. C'est aussi ce qui garantit que la charte graphique ne dérive pas : à
cinq, cinq `.docx` retouchés à la main donnent cinq mises en page en trois mois.

**Les livrables et les outils de travail sont en DOCX, XLSX et PPTX** parce que
c'est ce que le client ouvre, annote et fait circuler, et parce qu'un tableau de
suivi a besoin de formules, de listes déroulantes et de mise en forme
conditionnelle — ce qu'un fichier texte ne fera jamais.

La règle : **on n'édite jamais un gabarit à la main pour le committer**.
Les gabarits sont produits par script, en PR, à partir d'une charte unique.

```
30-outils/scripts/charte.py        ← palette, polices, sévérités : source unique
        │
        ├── generer_classeurs.py   → XLSX  (openpyxl)
        └── generer_documents.py   → DOCX, PPTX (python-docx, python-pptx)
                                   → PDF via LibreOffice
```

Modifier une couleur dans `charte.py` met à jour **tous** les formats d'un coup.

---

## Utilisation

```sh
make modeles                              # régénère tout dans 90-templates/build/
make pdf FILE=90-templates/build/Modele-rapport.docx
```

Prérequis : `pip install openpyxl python-docx python-pptx`, et LibreOffice pour
la conversion PDF.

---

## Ce qui est produit

| Fichier | Format | Usage |
|---|---|---|
| `Modele-rapport.docx` | DOCX | Rapport client. Styles définis : modifier un style met à jour tout le document. Sommaire automatique (F9 dans Word). |
| `Modele-restitution.pptx` | PPTX | Support de restitution de fin de mission |
| `Modele-presentation.pptx` | PPTX | Présentation de la société, avant-vente |
| `Classeur-mission.xlsx` | XLSX | Suivi d'une mission : synthèse, vulnérabilités, tâches, plan de charge, couverture, journal |
| `Pilotage-societe.xlsx` | XLSX | Portefeuille, plan de charge annuel, matrice de compétences, grille tarifaire |
| `SoA-ISO27001.xlsx` | XLSX | Déclaration d'applicabilité, 93 mesures de l'Annexe A |

Les consignes de rédaction sont intégrées **dans** les gabarits, en cyan, sous
la mention « Consigne interne — supprimer avant remise ». Elles disent quoi
écrire dans chaque section et pourquoi certaines ne sont pas supprimables.

---

## Ce qui est automatisé dans les classeurs

Ce ne sont pas des tableaux vides — c'est ce qui fait la différence à l'usage :

- **Listes déroulantes** sur sévérité, statut, phase PTES, séniorité — impossible
  de saisir une valeur hors référentiel
- **Couleurs de sévérité** appliquées automatiquement, identiques aux documents
- **Échéance dépassée** surlignée en rouge
- **Tâche bloquée** surlignée en rouge
- **Charge > 85 %** surlignée : signal de refus de nouvelle mission
- **Dépendance à une seule personne** détectée dans la matrice de compétences
- Synthèse de mission alimentée par formules depuis les autres onglets
- Volets figés et filtres sur tous les tableaux

---

## Reste à faire

- [ ] Insérer le logo dans la couverture DOCX et PPTX (`design/`)
- [ ] Gabarits de rapport propres à `ai-redteaming`, `secu-applicative`, `devsecops`
- [ ] `synthese-executive.docx` — document séparé pour la direction du client
- [ ] `proposition-commerciale.docx`
- [ ] `attestation-de-test.docx` et `certificat-destruction.docx`
- [ ] Installer les polices Inter et JetBrains Mono sur les postes de l'équipe

---

## Règle

Un gabarit se modifie **par PR sur le script**, jamais dans un dossier de
mission. Si vous adaptez un gabarit pour un client, demandez-vous d'abord si
l'adaptation ne devrait pas profiter à tout le monde.
