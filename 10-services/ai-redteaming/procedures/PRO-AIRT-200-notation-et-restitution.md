# PRO-AIRT-200 - Notation et restitution

**Version** : v0.1 · **Service** : `ai-redteaming` · **Phase** : restitution
**Responsable** : chef de mission · **Sortant** : rapport, synthèse, jeu rejouable

---

## Le problème de la notation

**CVSS a été conçu pour des vulnérabilités déterministes.** Sur un système à base
d'IA, deux difficultés apparaissent :

1. Une attaque réussit *parfois*. Le vecteur CVSS n'a pas de champ pour ça.
2. L'impact dépend moins de la faille que de ce que le modèle a le **droit de
   faire**. La même injection de prompt est anodine sur un agent conversationnel
   et critique sur un agent qui envoie des courriels.

Nous conservons CVSS v4.0 - c'est le langage que le client connaît, et l'échelle
de sévérité est unique pour toute la société (`NOMENCLATURE.md` §4). Mais nous le
complétons de deux éléments, et nous **justifions systématiquement par écrit**
tout écart entre le score CVSS et la sévérité affichée.

---

## Les trois dimensions

### 1. Impact - ce que l'attaque permet réellement

C'est la dimension dominante. Elle se lit dans la fiche système du cadrage :
que peut faire le modèle ?

| Niveau | Ce que l'attaque obtient |
|---|---|
| Majeur | Action irréversible, accès à des données d'autres utilisateurs, exécution de code |
| Important | Action réversible non prévue, accès à des données internes non publiques |
| Modéré | Contournement d'une règle métier, production de contenu interdit |
| Faible | Comportement dégradé sans conséquence exploitable |

### 2. Taux de réussite - la reproductibilité

| Taux sur N tentatives | Qualification |
|---|---|
| ≥ 80 % | Fiable - exploitable en pratique par un attaquant |
| 30 - 79 % | Reproductible - l'attaquant réessaie, c'est gratuit |
| 5 - 29 % | Intermittent |
| < 5 % | Anecdotique - signalé, non priorisé |

> **Un taux faible ne dégrade pas la sévérité autant qu'on le croit.** Réessayer
> ne coûte rien à un attaquant. Une attaque à 10 % de réussite sur une action
> irréversible reste critique. Le taux nuance la priorisation, pas l'existence.

### 3. Accessibilité - qui peut déclencher l'attaque

| Niveau | Qui |
|---|---|
| Public | N'importe qui, sans compte |
| Authentifié | Un utilisateur légitime |
| Indirect | Quiconque peut faire entrer un document dans le système |
| Privilégié | Un administrateur |

L'accessibilité **indirecte** est systématiquement sous-évaluée. Si un document
transmis par courriel finit dans le contexte du modèle, la surface est publique
en pratique.

---

## Grille de synthèse

| Impact | Accessibilité publique ou indirecte | Authentifié | Privilégié |
|---|---|---|---|
| Majeur | Critique | Élevée | Moyenne |
| Important | Élevée | Moyenne | Moyenne |
| Modéré | Moyenne | Faible | Faible |
| Faible | Faible | Information | Information |

Puis ajustement d'un cran vers le bas si le taux est inférieur à 5 %, **sauf si
l'impact est majeur** - auquel cas on ne descend pas.

Le score CVSS reste calculé et affiché. La justification de l'écart est
obligatoire dans la fiche de constatation.

---

## Rédiger la constatation

Gabarit : `Modele-rapport-ai-redteaming.docx` (`make livrables`).

Champs propres au service, en plus du socle commun :

| Champ | Contenu |
|---|---|
| OWASP LLM | `LLM01:2025` à `LLM10:2025` |
| MITRE ATLAS | `AML.T<NNNN>`, avec la version d'ATLAS appliquée |
| Taux de réussite | `7/20 - 35 %` |
| Reproductibilité | Déterministe, stochastique, dépendante du contexte |
| Modèle et version | Le comportement peut changer à la version suivante |
| Accessibilité | Public, authentifié, indirect, privilégié |

### La mention de version, non négociable

Le modèle du client peut être mis à jour la semaine suivante, avec un
comportement différent. Chaque constatation indique **le modèle, sa version et la
date des tests**. Sans cela, la constatation devient indéfendable dès la première
mise à jour du fournisseur.

C'est aussi ce qui justifie une **contre-vérification** : c'est un argument
honnête, pas une vente forcée.

---

## Recommandations

Trois niveaux, comme pour un pentest, mais avec une hiérarchie propre à l'IA :

| Rang | Nature | Exemple |
|---|---|---|
| 1 | **Réduire les droits du modèle** | Retirer un outil, restreindre sa portée, exiger une validation humaine |
| 2 | **Contrôler les sorties** | Échapper, valider, ne jamais exécuter directement |
| 3 | **Contrôler les entrées** | Filtrer, isoler le contenu non fiable du contexte de consigne |
| 4 | **Renforcer les garde-fous** | Filtres, modération, listes de refus |

**Cet ordre est délibéré et il faut l'expliquer au client.** Le réflexe habituel
est de commencer par le rang 4 - « on va durcir le prompt système ». C'est le
moins efficace : un garde-fou par consigne se contourne, une permission retirée
ne se contourne pas.

Formulation utile en restitution : « Tant que l'agent peut envoyer un courriel,
aucune consigne ne garantira qu'il ne le fera pas. »

---

## Détection

Section obligatoire, comme pour tous nos rapports. Ce que le client peut
surveiller :

- Requêtes contenant des motifs d'injection connus
- Écarts de comportement : longueur, langue, refus soudains
- Appels d'outils inhabituels ou hors séquence attendue
- Pics de consommation de jetons
- Récupérations RAG portant sur des documents hors du profil de l'utilisateur

Renvoyer vers le service `soc-ai-tools` quand la mise en œuvre dépasse le rapport.

---

## Restitution orale

Support : `Modele-restitution.pptx`.

Trois messages à faire passer, dans cet ordre :

1. **Ce que le modèle a le droit de faire** - la surface réelle, souvent découverte
   par le client lui-même pendant la présentation.
2. **Une démonstration** - un cas, joué en direct si possible. C'est ce qui
   convainc, bien plus qu'un tableau de scores.
3. **La hiérarchie des corrections** - permissions avant garde-fous.

À dire explicitement : **nous n'avons pas testé le modèle du fournisseur, mais
l'application du client.** Le répéter en restitution évite le malentendu qui
revient systématiquement.

---

## Critères de sortie

- [ ] Chaque constatation porte OWASP LLM, ATLAS, taux, modèle et version
- [ ] Écarts entre CVSS et sévérité affichée justifiés par écrit
- [ ] Section Détection présente sur chaque constatation
- [ ] Jeu de cas rejouable livré et documenté
- [ ] Coût d'inférence réel communiqué au client
- [ ] Annexe de couverture OWASP LLM complète, non exécutés motivés
- [ ] Double relecture effectuée
- [ ] Contre-vérification proposée, avec sa justification
