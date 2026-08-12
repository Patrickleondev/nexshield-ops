# PRO-SENS-100 - Campagnes et formation

**Version** : v0.1 · **Service** : `sensibilisation` · **Phase** : exécution
**Responsable** : intervenant sensibilisation · **Sortant** : résultats agrégés + progression mesurée

**Préalable bloquant** : `PRO-SENS-001` close, charte de campagne signée.

---

## Principe

**On mesure une capacité collective, jamais une faute individuelle.**

Toute décision de ce document découle de cette phrase. En cas de doute sur une
conduite à tenir, c'est elle qui tranche.

---

## 1. Préparer une campagne

### Choisir le prétexte

Le prétexte doit être **plausible et sans charge émotionnelle**. Ces deux
critères se contredisent souvent : les prétextes les plus efficaces sont les plus
abusifs. Nous choisissons la retenue, et nous l'assumons devant le client.

| Autorisé | Interdit |
|---|---|
| Notification d'un outil interne | Prime, augmentation, intéressement |
| Livraison, facture, note de frais | Licenciement, sanction, convocation RH |
| Mise à jour de mot de passe | Santé, décès, sujet familial |
| Invitation à une réunion | Usurpation d'une personne réelle nommée |

### Préparer l'infrastructure

- [ ] Domaine d'expédition **dédié à nous**, jamais un domaine tiers réel
- [ ] Domaine ressemblant sans usurper une marque existante
- [ ] Page de destination qui **n'enregistre jamais** ce qui est saisi - seul le
      fait qu'une saisie a eu lieu est compté
- [ ] Page de débriefing prête, testée
- [ ] Adresses des destinataires minimisées, chiffrées, supprimées après
      agrégation

### Prévenir les bonnes personnes

- [ ] Direction : informée des dates
- [ ] Équipe technique et support : informés, sinon ils traiteront la campagne
      comme un incident réel et perdront une journée
- [ ] Destinataires : **non prévenus** des dates, mais informés de l'existence du
      programme, conformément au cadrage

## 2. Exécuter

- Envoi étalé, jamais en une seule vague : une vague unique se propage par le
  bouche-à-oreille en dix minutes et fausse tout
- Suivi en temps réel du taux de signalement
- **Arrêt immédiat** si la campagne provoque une réaction disproportionnée :
  panique, plainte, saturation du support

Indicateurs relevés :

| Indicateur | Ce qu'il mesure |
|---|---|
| Taux d'ouverture | Peu utile seul |
| Taux de clic | L'exposition |
| Taux de saisie | La vulnérabilité réelle |
| **Taux de signalement** | **La capacité de détection - le plus important** |
| Délai du premier signalement | La vitesse de réaction |
| Délai de traitement par le support | La chaîne complète |

## 3. Débriefer immédiatement

La page affichée après un clic est le moment pédagogique. Elle décide de la
réussite du programme.

**Ce qu'elle contient**

- Ce qui vient de se passer, en deux phrases
- Les trois indices qui auraient permis de repérer le courriel, sur le courriel
  lui-même
- Où signaler la prochaine fois, avec le chemin exact
- Une phrase qui déculpabilise

**Ce qu'elle ne contient jamais**

- Un reproche, un ton moralisateur, un compte à rebours
- Une menace de suivi hiérarchique
- Un questionnaire obligatoire

> Une personne qui a cliqué et qui se sent humiliée ne signalera jamais. On perd
> davantage qu'on ne gagne.

## 4. Restituer

**Résultats agrégés uniquement.** Aucun nom, à aucun moment, à personne.

- Agrégation par groupe, à partir de **dix personnes**. En dessous, on ne
  publie pas : le groupe est identifiant.
- Comparaison avec la mesure précédente, sur les mêmes indicateurs
- Progression du taux de signalement mise en avant avant le taux de clic

Si la direction demande les noms : refus, en rappelant la charte signée. Ce refus
n'est pas négociable et se dit calmement.

## 5. Former, immédiatement après

La formation suit la campagne de quelques jours au plus. Passé deux semaines,
l'effet est perdu.

| Public | Contenu | Durée |
|---|---|---|
| Tous | Résultats collectifs, trois réflexes, où signaler | 45 min |
| Finance | Fraude au virement, vérification par second canal | 1 h 30, cas réels |
| Direction | Ciblage nominatif, exposition publique | 1 h, individuel |
| Développement | Secrets, dépendances, données de test | 2 h, avec `devsecops` |
| Support | Manipulation par téléphone, vérification d'identité | 1 h 30, mise en situation |

Un principe : **une session se conclut par un geste concret**, pas par une
sensibilisation générale. Activer un second facteur, enregistrer l'adresse de
signalement, vérifier un ordre de virement par téléphone.

## 6. Suivre dans la durée

- Campagne trimestrielle, difficulté croissante
- Mêmes indicateurs à chaque fois, sinon la comparaison est fausse
- Objectifs révisés annuellement avec la direction
- Nouveaux arrivants intégrés au programme dès leur arrivée

---

## Règles d'exécution

- **Aucun mot de passe réel enregistré.** Jamais, sous aucun prétexte technique.
- **Aucun résultat nominatif** communiqué, ni conservé au-delà de l'agrégation.
- **Aucune sanction** fondée sur nos résultats : c'est écrit à la charte.
- Adresses et résultats détruits après agrégation, certificat produit.
- Les données de campagne sont des données personnelles : loi n° 2019-014.

---

## Critères de sortie

- [ ] Prétexte conforme à la liste des thèmes autorisés
- [ ] Domaine dédié, aucune usurpation de marque ou de personne réelle
- [ ] Aucune saisie réelle enregistrée, vérifié techniquement
- [ ] Équipes technique et support prévenues
- [ ] Envoi étalé, suivi en temps réel
- [ ] Page de débriefing affichée, sans reproche
- [ ] Résultats agrégés par groupes d'au moins dix personnes
- [ ] Aucun nom communiqué, à personne
- [ ] Formation tenue dans les deux semaines
- [ ] Chaque session conclue par un geste concret
- [ ] Progression mesurée sur les mêmes indicateurs qu'au départ
- [ ] Adresses et résultats individuels détruits, certificat produit
