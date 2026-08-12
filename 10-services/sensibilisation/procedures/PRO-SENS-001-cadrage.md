# PRO-SENS-001 - Cadrage d'un programme de sensibilisation

**Version** : v0.1 · **Service** : `sensibilisation` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : programme + charte de campagne signée

---

## Ce qui distingue ce cadrage

Ce service porte sur des **personnes**, pas sur des systèmes. Une campagne mal
cadrée ne produit pas une panne : elle produit de la défiance envers la direction
et envers nous, et cela ne se répare pas par un correctif.

Référentiel : [NIST SP 800-50r1](https://csrc.nist.gov/pubs/sp/800/50/r1/final),
« Building a Cybersecurity and Privacy Learning Program ».

---

## Étapes

### 1. Fixer l'objectif réel

La demande arrive presque toujours sous la forme « on veut sensibiliser tout le
monde ». Ce n'est pas un objectif, c'est un budget.

| Mauvais objectif | Objectif exploitable |
|---|---|
| Sensibiliser les équipes | Réduire le taux de clic sur hameçonnage, de X % à Y %, en douze mois |
| Former à la sécurité | Faire passer le délai moyen de signalement sous quinze minutes |
| Sensibiliser les dirigeants | Faire vérifier tout ordre de virement par un second canal |

**Le taux de signalement est un meilleur indicateur que le taux de clic.** Une
organisation où personne ne clique mais où personne ne signale n'a rien gagné :
la première attaque réussie passera inaperçue.

### 2. Identifier les publics

Un programme unique pour toute l'organisation ne fonctionne pas.

| Public | Risque dominant | Format |
|---|---|---|
| Direction | Fraude au virement, ciblage nominatif | Court, individuel, confidentiel |
| Finance et comptabilité | Fraude au virement, fausse facture | Atelier sur cas réels |
| Développement | Secrets, dépendances, environnements | Technique, avec `devsecops` |
| Support et accueil | Manipulation par téléphone, accès physique | Mise en situation |
| Tous | Hameçonnage, mots de passe, signalement | Court, répété, jamais annuel |

### 3. Établir la mesure de départ

Sans mesure initiale, aucun progrès ne sera démontrable.

- [ ] Campagne initiale d'hameçonnage simulé, **sans annonce préalable aux
      destinataires** mais avec accord écrit de la direction
- [ ] Taux de clic, taux de saisie d'identifiants, taux de signalement
- [ ] Délai moyen du premier signalement
- [ ] Le canal de signalement existe-t-il, et fonctionne-t-il

> Si le canal de signalement n'existe pas, **le créer est la première action du
> programme**. Demander aux gens de signaler sans leur donner où signaler est la
> faute la plus commune du métier.

### 4. Signer la charte de campagne

Document propre à ce service, distinct du RoE. Il engage la direction sur ce que
nous ferons et surtout sur ce que nous ne ferons pas.

**Règles non négociables**

| Règle | Raison |
|---|---|
| **Aucune sanction individuelle** fondée sur nos résultats | Une campagne devenue outil disciplinaire détruit le signalement pour des années |
| **Aucun résultat nominatif** communiqué à la hiérarchie | Statistiques par groupe, à partir de dix personnes |
| **Aucun thème abusif** | Ni prime, ni licenciement, ni décès, ni santé, ni sujet familial |
| **Aucune usurpation d'une personne réelle** | Ni un dirigeant, ni un salarié, ni un partenaire nommé |
| **Aucune collecte de mot de passe réel** | La page simulée n'enregistre jamais ce qui est saisi |
| **Débriefing immédiat** | La page de fin explique, elle ne culpabilise pas |

Ces règles se discutent avant signature. Un client qui exige des résultats
nominatifs pour sanctionner : **nous refusons la mission.** Cela se dit une fois,
calmement, et cela grandit la société.

### 5. Cadrer les aspects légaux

- Simuler une attaque sur des salariés est un traitement de données personnelles :
  loi togolaise n° 2019-014. Voir `x-privacy`.
- Information collective préalable des salariés sur l'**existence** du programme,
  sans en annoncer les dates.
- Représentants du personnel informés, si l'organisation en a.
- Domaines d'expédition : dédiés, jamais l'usurpation d'un domaine tiers réel.
- Conservation des résultats : durée courte, agrégation dès que possible.

### 6. Bâtir le calendrier

- Répétition **trimestrielle** au minimum. Une campagne annuelle ne produit rien
  de durable.
- Difficulté croissante, jamais l'inverse
- Formation immédiatement après chaque campagne, tant que le souvenir est vif
- Mesure finale sur les mêmes indicateurs qu'au départ, sinon la comparaison ne
  vaut rien

---

## Critères de sortie

- [ ] Objectif chiffré, avec un point de départ et une échéance
- [ ] Publics identifiés, format adapté à chacun
- [ ] Mesure initiale réalisée
- [ ] Canal de signalement existant et vérifié, ou création inscrite au programme
- [ ] Charte de campagne signée par la direction
- [ ] Absence de sanction individuelle actée par écrit
- [ ] Information collective des salariés effectuée
- [ ] Aspects données personnelles traités
- [ ] Calendrier trimestriel arrêté
- [ ] RoE signé

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Résultats nominatifs remis à la hiérarchie | Défiance durable, effondrement du signalement |
| Thème abusif : prime, licenciement, santé | Détresse réelle, et perte de légitimité du programme |
| Usurper l'identité d'un dirigeant réel | Atteinte à la personne, et risque juridique |
| Mesurer le clic sans mesurer le signalement | Indicateur flatteur, aucune capacité de détection gagnée |
| Campagne annuelle unique | Aucun effet mesurable, budget perdu |
| Aucun canal de signalement | On demande l'impossible aux salariés |
