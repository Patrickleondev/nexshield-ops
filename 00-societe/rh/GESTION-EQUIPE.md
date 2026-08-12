# Gestion de l'équipe

**Version** : v0.1 — **Statut** : à valider par les 5 associés

À cinq, tout le monde sait ce que tout le monde fait. Ce document existe pour le
jour où ce ne sera plus vrai — et ce jour arrive plus vite qu'on ne le croit.

---

## 1. Rôles

Un rôle n'est pas une personne : c'est une **responsabilité**. À cinq, une
personne porte plusieurs rôles. En grandissant, on les sépare. Le tableau ne
change pas ; seule la colonne « titulaire » change.

| Rôle | Responsabilité | Titulaire |
|---|---|---|
| **Direction** | Stratégie, signature des contrats, arbitrages | `<…>` |
| **Référent technique offensif** | Doctrine pentest, AI RedTeaming, sécurité applicative | `<…>` |
| **Référent défensif** | Doctrine SOC, détection, CTI | `<…>` |
| **Référent DevSecOps** | Doctrine CI/CD, infrastructure, durcissement | `<…>` |
| **Référent GRC** | ISO 27001, RGPD, relecture juridique, sensibilisation | `<…>` |
| **Responsable sécurité interne** | Dépôt, accès, secrets, incidents internes | `<…>` |
| **Responsable qualité** | Relecture finale de tout livrable client | `<…>` |
| **Responsable commercial** | Avant-vente, propositions, relation client | `<…>` |

Chaque rôle correspond à une entrée de `CODEOWNERS`. Un rôle sans titulaire
nommé est un risque : il apparaît dans la matrice de compétences comme
« Aucune couverture ».

**Règle de continuité** : tout rôle a un **suppléant** désigné. Personne ne part
en congés sans que son suppléant soit à jour.

---

## 2. Qui décide quoi

| Décision | Qui décide | Qui est consulté |
|---|---|---|
| Accepter une mission | Direction | Référent du service, plan de charge |
| Périmètre et RoE | Chef de mission | Référent technique, GRC |
| Sévérité d'une vulnérabilité | Testeur | Chef de mission (arbitre si désaccord) |
| Publier un rapport | Responsable qualité | Chef de mission |
| Faire évoluer une doctrine | Référent du service | Toute l'équipe, par PR |
| Engager une dépense | Direction | — |
| Recruter | Direction | Référent du domaine concerné |
| Arrêter une mission en urgence | **N'importe qui** | Personne — on arrête d'abord, on discute après |

La dernière ligne est délibérée. Dans notre métier, l'hésitation à interrompre
coûte plus cher que l'interruption injustifiée.

---

## 3. Séniorité

| Niveau | Ce qu'on attend | Autonomie |
|---|---|---|
| **Junior** | Exécute une checklist, rédige des constatations | Toujours accompagné |
| **Confirmé** | Mène une phase seul, rédige un chapitre | Autonome sur périmètre cadré |
| **Senior** | Mène une mission, arbitre les sévérités, relit | Autonome, forme les juniors |
| **Expert** | Définit la doctrine, traite les cas hors référentiel | Référent d'un domaine |

La progression se mesure sur la **matrice de compétences**
(`Pilotage-societe.xlsx`, onglet Compétences), notée de 0 à 4 par domaine, revue
deux fois par an. Un domaine noté ≥ 3 par une seule personne apparaît en orange :
c'est une dépendance à un seul homme, donc un risque pour la société.

**Objectif permanent : aucun domaine vendu ne repose sur une seule personne.**
C'est la première question à se poser avant d'ouvrir une nouvelle offre.

---

## 4. Accueil d'un nouveau membre

### Avant le premier jour

- [ ] Contrat et **charte éthique** signés
- [ ] Compte GitHub créé, **MFA activé et vérifié** — bloquant
- [ ] Accès en lecture seule au dépôt (l'écriture vient après la semaine 1)
- [ ] Poste chiffré, gestionnaire de mots de passe installé
- [ ] Parrain désigné parmi les associés

### Semaine 1 — comprendre

- [ ] Lire `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CONVENTIONS.md`
- [ ] Lire `00-societe/smsi/REFERENTIELS.md` — c'est le document fondateur
- [ ] Lire `00-societe/commercial/POSTURE.md` — comment on parle aux clients
- [ ] `make setup` et vérifier que gitleaks bloque bien un faux secret
- [ ] **Première PR** : corriger une coquille dans la doctrine. Objectif : valider
      que le circuit fonctionne, pas produire de la valeur.

### Semaines 2 à 4 — observer

- [ ] Lire deux rapports de missions passées, de bout en bout
- [ ] Assister à une restitution client sans intervenir
- [ ] Refaire une mission passée en environnement de lab, comparer son travail au
      rapport livré. C'est l'exercice le plus formateur qui existe.
- [ ] Auto-évaluation sur la matrice de compétences, avec le parrain

### Mois 2 et 3 — contribuer

- [ ] Première mission en binôme, sur une phase délimitée
- [ ] Rédiger un chapitre de rapport, relu ligne à ligne par le parrain
- [ ] Accès en écriture au dépôt
- [ ] Point à 90 jours : bilan, ajustement du plan de montée en compétence

**Un nouveau ne touche jamais un système client seul avant d'avoir livré deux
missions en binôme.** Sans exception, quelle que soit son expérience antérieure.

---

## 5. Départ d'un membre

| Quand | Action |
|---|---|
| Jour de l'annonce | Retrait des missions en cours d'engagement nouveau |
| Avant le départ | Passation écrite de chaque rôle porté, au suppléant |
| **Jour du départ** | Révocation de tous les accès — dépôt, cloud, coffre, messagerie |
| J+2 | Rotation de tous les secrets partagés qu'il connaissait |
| J+7 | Revue : que savait-il que personne d'autre ne sait ? Combler. |

Le rappel des obligations de confidentialité se fait par écrit, sans affect.
C'est une procédure, pas un jugement.

---

## 6. Faire grandir l'équipe

### Quand recruter

Quand le plan de charge dépasse **85 % sur trois mois consécutifs**, ou quand un
domaine vendu repose sur une seule personne. Pas avant : un recrutement trop tôt
consomme la trésorerie et le temps d'encadrement.

### Dans quel ordre

1. **Un rédacteur-testeur confirmé** — le goulot d'étranglement est toujours la
   rédaction, jamais l'exécution.
2. **Un second profil défensif** — pour ne pas dépendre d'une personne sur le SOC.
3. **Un profil avant-vente** — quand la direction passe plus de temps à vendre
   qu'à produire.

### Ce qu'on regarde en entretien

- Un **écrit**. Faire rédiger une constatation à partir d'une faille donnée. Ça
  révèle plus que trois heures de questions techniques.
- La **capacité à dire « je ne sais pas »**. Dans ce métier, celui qui bluffe est
  dangereux pour le client et pour la société.
- Le rapport à l'**autorisation**. « Qu'auriez-vous fait si vous aviez trouvé un
  serveur vulnérable hors périmètre ? » — une seule bonne réponse.
