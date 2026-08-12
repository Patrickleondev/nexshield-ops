# Pilotage : tâches, répartition, délais

**Version** : v0.1 — **Statut** : à valider par les 5 associés

Ce document répond à une seule question : **qui fait quoi, pour quand, et
comment on le sait**. À cinq, on tient par la discussion. À huit, on ne tient
plus. Ce cadre est écrit maintenant, pendant qu'il est encore facile à appliquer.

---

## 1. Les trois niveaux de pilotage

| Niveau | Horizon | Outil | Cadence |
|---|---|---|---|
| **Société** | Année | `Pilotage-societe.xlsx` — portefeuille, plan de charge, compétences | Revue mensuelle |
| **Mission** | Semaines | `Classeur-mission.xlsx` — onglet Tâches | Point quotidien de 10 min |
| **Doctrine** | Continu | Issues et PR GitHub | Au fil de l'eau |

Trois niveaux, trois outils, aucun recouvrement. Une tâche de mission ne va pas
dans GitHub ; une évolution de méthodologie ne va pas dans un classeur.

---

## 2. La règle de la tâche

**Une tâche sans responsable nommé et sans échéance n'existe pas.**

Pas « l'équipe technique », pas « quelqu'un » : un nom. Une tâche portée par deux
personnes n'est portée par personne. On désigne un **responsable** et,
éventuellement, un **appui** — le responsable reste seul comptable.

Chaque tâche porte :

| Champ | Pourquoi |
|---|---|
| Responsable | Un seul nom |
| Échéance | Une date, jamais « dès que possible » |
| Charge estimée | En jours, avant de commencer |
| Charge réelle | En jours, à la fin — c'est ce qui rend les devis suivants justes |
| Statut | À faire · En cours · Bloqué · En revue · Terminé |
| Bloqué par | Obligatoire si le statut est « Bloqué » |

Le classeur colore automatiquement en rouge une tâche bloquée et une échéance
dépassée. Le rouge n'est pas un reproche : c'est un appel à l'aide qui doit être
traité au point suivant.

---

## 3. Estimation et délais

### Comment on estime

Estimation en **jours-homme**, par la personne qui exécutera. Jamais par le
commercial, jamais par le chef de mission seul.

Règles de prudence, apprises par tout le monde à ses dépens :

- **Multiplier par 1,5** une estimation portant sur une technologie qu'on n'a
  jamais testée.
- **Ajouter 20 %** de marge de rédaction : le rapport prend toujours plus de
  temps que prévu, et c'est le livrable que le client juge.
- **Ne jamais compter plus de 4 jours facturables par semaine** et par personne.
  Le cinquième part en administratif, en veille et en imprévus. Une planification
  à 5 jours/semaine produit mécaniquement du retard.

### Délais type par mission

À affiner après vos cinq premières missions — ce sont des ordres de grandeur de
départ, pas des engagements.

| Mission | Exécution | Rédaction | Total | Personnes |
|---|---|---|---|---|
| Pentest applicatif web | 5-8 j | 2-3 j | 8-11 j | 2 |
| Pentest externe | 3-5 j | 2 j | 5-7 j | 1-2 |
| Pentest interne / AD | 5-10 j | 3 j | 8-13 j | 2 |
| AI RedTeaming (LLM applicatif) | 4-6 j | 2-3 j | 6-9 j | 1-2 |
| Évaluation ASVS L2 | 6-10 j | 3 j | 9-13 j | 1-2 |
| Audit de maturité SAMM | 4-6 j | 3 j | 7-9 j | 1-2 |
| Audit de durcissement CIS | 2-4 j | 2 j | 4-6 j | 1 |
| Campagne de sensibilisation | 2 j | 1 j | 3 j + suivi | 1 |

**Toujours annoncer au client la date de remise du rapport, pas la date de fin
des tests.** C'est le rapport qu'il attend.

### La marge de sécurité

Entre la fin des tests et la remise du rapport : **au moins 3 jours ouvrés**.
Ils servent à la double relecture (`CONTRIBUTING.md` §3). Un rapport relu à la
va-vite, remis à l'heure, coûte plus cher en crédibilité qu'un rapport remis avec
deux jours de retard annoncés à l'avance.

---

## 4. Cadence

| Rituel | Quand | Durée | Objet |
|---|---|---|---|
| **Point mission** | Chaque matin en mission | 10 min | Ce que j'ai fait, ce que je fais, ce qui me bloque |
| **Revue de mission** | Fin de chaque mission | 1 h | RETEX, écarts d'estimation, actions de doctrine |
| **Revue société** | 1er lundi du mois | 1 h 30 | Portefeuille, plan de charge, trésorerie, compétences |
| **Revue de doctrine** | Trimestrielle | 2 h | PR de méthodologie en attente, versions à publier |
| **Revue des accès** | Trimestrielle | 30 min | Qui a accès à quoi (exigence ISO 27001) |

Le point quotidien tient en 10 minutes **debout**. S'il dure 40 minutes, c'est
qu'un sujet mérite une réunion dédiée — on le sort et on continue.

---

## 5. Quand une mission dérape

Le dérapage n'est pas une faute. Le **dérapage caché** en est une.

1. Dès que l'écart dépasse **20 % de la charge estimée**, le responsable prévient
   le chef de mission. Le jour même.
2. Le chef de mission arbitre : réduire le périmètre, ajouter du monde, ou
   décaler la remise.
3. **Si la date de remise bouge, le client est prévenu avant l'échéance, jamais
   après.** Un report annoncé trois jours avant est un aléa professionnel ; un
   report annoncé le jour J est une faute.
4. L'écart et sa cause sont consignés dans le RETEX.

---

## 6. Comment on dit non

Le plan de charge société colore en rouge tout membre au-delà de **85 %**.
Au-delà de ce seuil, on ne prend plus de mission. La marge restante absorbe les
imprévus, la veille et la R&D.

Accepter une mission qu'on ne peut pas tenir coûte : la mission, le client, et la
réputation. Refuser coûte une mission. Le calcul est vite fait.

Formulation à un prospect : « Nous sommes complets jusqu'au <date>. Nous pouvons
démarrer le <date> — ou vous orienter vers un confrère si votre échéance est plus
courte. » Orienter vers un confrère vous fait gagner un client la fois suivante.
