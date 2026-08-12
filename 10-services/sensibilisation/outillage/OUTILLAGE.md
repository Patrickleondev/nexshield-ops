# Outillage - Sensibilisation

**Version** : v0.1 · **Service** : `sensibilisation`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

Ce service manipule des données sur des **personnes identifiées**, dans un
contexte de subordination. C'est le service où une erreur d'outillage se paye le
plus cher, et où elle ne se répare pas.

Trois interdits, sans exception technique possible :

- **Aucune saisie réelle enregistrée.** La page simulée compte qu'une saisie a eu
  lieu ; elle n'enregistre jamais ce qui a été tapé. Cela se vérifie dans la
  configuration, avant chaque campagne.
- **Aucun résultat nominatif** conservé au-delà de l'agrégation, ni communiqué.
- **Aucune plateforme hébergée à l'étranger sans base légale** pour le transfert :
  les adresses des salariés sont des données personnelles (loi n° 2019-014).

---

## 2. Socle retenu

| Besoin | Outil | Licence |
|---|---|---|
| Campagnes d'hameçonnage simulé | [GoPhish](https://github.com/gophish/gophish) | MIT |
| Manipulation par téléphone et accès physique | Scénarios internes, sans outil | Interne |
| Supports de formation | Gabarits PPTX de la société (`make modeles`) | Interne |
| Suivi des indicateurs | Classeur de mission (`make modeles`) | Interne |

**GoPhish est auto-hébergé**, et c'est la raison du choix : les adresses des
salariés du client ne quittent pas une infrastructure que nous maîtrisons. Une
plateforme en abonnement hébergée à l'étranger poserait un problème de transfert
que le client ne pourrait pas fonder.

Configuration obligatoire avant toute campagne :

- [ ] Capture des identifiants **désactivée**, vérifiée dans la configuration
- [ ] Redirection immédiate vers la page de débriefing
- [ ] Domaine d'expédition dédié, avec SPF, DKIM et DMARC correctement posés
- [ ] Base de données de la plateforme chiffrée
- [ ] Purge programmée après agrégation

---

## 3. Couverture réelle

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Envoi et suivi de campagne | Oui | Rien |
| Mesure du clic et de la saisie | Oui | Rien |
| **Choix du prétexte** | **Non** | Le jugement éthique, campagne par campagne |
| **Page de débriefing** | **Non** | Rédaction : c'est le moment pédagogique |
| **Formation** | **Non** | Toute la valeur du service |
| **Restitution** | **Non** | Agrégation, et refus des demandes nominatives |

L'outil ne fait qu'envoyer des courriels. **Le programme, la retenue dans le
choix des prétextes et la formation sont le service.**

---

## 4. Ce que nous refusons

- **Communiquer des résultats nominatifs**, même à la demande de la direction.
  La charte de campagne est signée avant, précisément pour que ce refus ne se
  discute pas au moment où la demande arrive.
- **Prêter la campagne à une procédure disciplinaire.**
- **Utiliser un prétexte à charge émotionnelle**, même s'il serait plus efficace.
- **Usurper l'identité d'une personne réelle**, dirigeant compris.
- **Publier un classement entre services.** Cela produit de la honte, pas de
  l'apprentissage.

Un client qui exige l'un de ces points : nous déclinons la mission. Cela se dit
une fois, calmement.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| NIST SP 800-50r1 | https://csrc.nist.gov/pubs/sp/800/50/r1/final |
| NIST SP 800-61r3 (réponse à incident) | https://csrc.nist.gov/pubs/sp/800/61/r3/final |
| CERT.tg | https://www.cert.tg/ |
| ANSSI, guides et bonnes pratiques | https://cyber.gouv.fr/ |

Cadre des données personnelles :
[`00-societe/juridique/CADRE-LEGAL.md`](../../../00-societe/juridique/CADRE-LEGAL.md).

---

## 6. Avant d'ajouter un outil

- [ ] Auto-hébergeable, ou base légale du transfert établie
- [ ] Capture d'identifiants désactivable, et désactivée
- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Purge des données individuelles possible et programmée
- [ ] Testé sur une campagne interne avant tout usage client
- [ ] Ajouté à ce document, avec sa couverture et ses limites
