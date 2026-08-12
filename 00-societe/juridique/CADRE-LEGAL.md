# Cadre légal applicable

**Version** : v0.1 - **Statut** : rédigé à partir des sources officielles, **non
relu par un juriste**. À faire valider avant tout usage contractuel.

Trois cercles nous concernent : le **Togo** (pays d'exercice), l'**Afrique**
(cadre régional), l'**Union européenne** (clients européens et clients togolais
exposés à l'Europe).

---

## 1. Togo

### 1.1 Cybersécurité et cybercriminalité - Loi n° 2018-026

**Loi n° 2018-026 du 7 décembre 2018** relative à la cybersécurité et à la lutte
contre la cybercriminalité, **modifiée par la loi n° 2022-009**.

C'est le texte le plus important pour nous, et pour une raison simple : **il
pénalise l'accès et le maintien frauduleux dans un système d'information**. Notre
métier consiste précisément à faire cela - la seule chose qui nous en distingue
juridiquement est **l'autorisation écrite du propriétaire du système**.

Conséquences pratiques, non négociables :

| Règle | Fondement |
|---|---|
| Aucun test sans autorisation écrite signée par une personne ayant autorité | L'autorisation est le fait justificatif. Sans elle, l'infraction est constituée. |
| L'autorisation nomme les systèmes **et** les personnes autorisées | Un testeur non nommé n'est pas couvert |
| L'autorisation est datée et bornée dans le temps | Un test hors période n'est plus couvert |
| Reconnaissance passive incluse dans le périmètre autorisé | Le texte ne distingue pas selon l'intensité |
| Conservation de l'autorisation signée pendant toute la durée des tests | C'est la pièce à produire en cas de contrôle |

Notre modèle `Modele-AUTH-autorisation-de-test.docx` (`make juridique`)
est construit pour cela : il tient sur une page pour pouvoir être lu en trente
secondes par un responsable inquiet, et il nomme systèmes, personnes et période.

### 1.2 L'ANCy et les règles de cybersécurité

L'**Agence Nationale de la Cybersécurité (ANCy)** est le régulateur. Elle a
adopté les **règles de cybersécurité** applicables aux **opérateurs de services
essentiels** (arrêté n° 2022-040/PMRT).

Pourquoi ça nous intéresse commercialement : si un prospect est **opérateur de
service essentiel** (banque, télécom, énergie, santé, administration), il a des
obligations réglementaires. Notre offre cesse d'être un confort et devient un
moyen de conformité. **C'est la question à poser au premier rendez-vous.**

Le **CERT.tg** est le centre national de réponse aux incidents. À connaître pour
la clause de notification de nos RoE : en cas de découverte de compromission
préexistante chez un opérateur de service essentiel, le client peut avoir une
obligation de déclaration. Ce n'est pas à nous de déclarer à sa place, mais c'est
à nous de le lui rappeler par écrit.

### 1.3 Données à caractère personnel - Loi n° 2019-014

**Loi n° 2019-014 du 29 octobre 2019** relative à la protection des données à
caractère personnel. Autorité de contrôle : l'**Instance de protection des
données à caractère personnel (IPDCP)**, organisée par le **décret n° 2020-111/PR**.

Ce qui nous concerne directement :

- Pendant une mission, nous pouvons **rencontrer** des données personnelles. Nous
  les anonymisons dans le rapport et ne les conservons pas - c'est déjà notre
  règle (`SECURITY.md` §2), elle a maintenant un fondement légal local.
- Nous traitons des données personnelles de nos clients (contacts, comptes de
  test) : nous sommes nous-mêmes soumis à la loi.
- **À vérifier auprès de l'IPDCP** : le régime applicable à notre activité
  (déclaration, autorisation, ou dispense) et les formalités de constitution.
  C'est une démarche à faire avant la première mission, pas après.

### 1.4 Ce qui reste à vérifier

Points que je n'ai pas pu établir avec certitude et qui doivent être tranchés
avec un juriste togolais :

- [ ] Forme sociale et régime fiscal les plus adaptés
- [ ] Existence d'un agrément ou d'une déclaration d'activité pour les prestataires
      de sécurité informatique au Togo
- [ ] Formalités exactes auprès de l'IPDCP pour notre propre activité
- [ ] Obligation d'assurance responsabilité civile professionnelle
- [ ] Régime de la preuve numérique en cas de litige

---

## 2. Afrique

### Convention de Malabo

**Convention de l'Union africaine sur la cybersécurité et la protection des
données à caractère personnel**, adoptée le **27 juin 2014**, **entrée en vigueur
le 8 juin 2023** après la 15ᵉ ratification.

**Le Togo l'a ratifiée.** Elle harmonise les législations africaines sur le
commerce électronique, la protection des données, la cybersécurité et la
cybercriminalité.

Intérêt pour nous : c'est le **socle commun** qui rendra une expansion régionale
(Bénin, Côte d'Ivoire, Ghana, Sénégal…) beaucoup moins coûteuse en adaptation
juridique. À citer dans les propositions à des clients panafricains.

Attention : la Convention est un cadre d'harmonisation, pas un texte directement
applicable en lieu et place du droit national. **Le droit du pays où sont situés
les systèmes testés reste la référence.** Pour une mission transfrontalière, la
question du droit applicable se pose explicitement dans le MSA.

### CEDEAO

Il existe des actes communautaires CEDEAO sur la cybercriminalité et la
protection des données. Je ne les ai pas vérifiés en source primaire - à faire
avant toute mission dans un autre État membre.

---

## 3. Union européenne

Pertinent dans trois cas : client européen, client togolais avec des utilisateurs
ou partenaires européens, ou sous-traitance pour un prestataire européen.

### RGPD - Règlement (UE) 2016/679

La référence mondiale de fait. Points qui nous concernent :

- En mission, nous sommes généralement **sous-traitant** au sens du RGPD → un
  **contrat de sous-traitance** (article 28) est obligatoire, avec les mentions
  imposées : objet, durée, nature du traitement, obligations, sort des données.
- **Transfert hors UE** : si des données de clients européens sont traitées
  depuis le Togo, il faut un mécanisme de transfert valide (clauses
  contractuelles types). Point technique, à traiter avec un juriste - c'est
  souvent ce qui bloque un contrat européen.
- Violation de données : notification sous 72 heures. À articuler avec nos
  clauses d'incident.

### NIS2 - Directive (UE) 2022/2555

Élargit les obligations de cybersécurité à de nombreux secteurs et impose une
**responsabilité de la chaîne d'approvisionnement**. Effet commercial direct :
une entreprise européenne soumise à NIS2 doit évaluer la sécurité de ses
fournisseurs - donc, potentiellement, la nôtre. C'est un argument pour notre
propre démarche ISO 27001.

### Règlement sur l'intelligence artificielle (AI Act)

Applicable par étapes. Pertinent pour l'offre `ai-redteaming` : il impose, pour
les systèmes à haut risque, des obligations de gestion des risques et de
robustesse. Notre offre alignée NIST AI RMF prépare le client à s'y conformer.

### France

Pour un client français : la **CNIL** est l'autorité de protection des données,
l'**ANSSI** l'autorité de cybersécurité. Les guides ANSSI sont une référence
attendue - les citer dans nos livrables destinés à des clients francophones
renforce notre crédibilité, sans coût.

Le droit pénal français réprime également l'accès frauduleux à un système de
traitement automatisé de données. **La règle de l'autorisation écrite préalable
est donc identique, quel que soit le pays.** C'est rassurant : une seule
discipline, partout.

---

## 4. Ce qui découle de tout ça

Le cadre légal, à trois pays près, dit la même chose :

1. **L'autorisation écrite est ce qui sépare notre métier d'un délit.** Elle
   n'est pas une formalité administrative, c'est le fondement juridique de toute
   l'activité.
2. **Les données rencontrées ne nous appartiennent pas.** Anonymisation,
   chiffrement, destruction à date, certificat à l'appui.
3. **Le droit applicable est celui du lieu des systèmes testés**, pas celui de
   notre siège. À trancher explicitement dans chaque contrat transfrontalier.

Ces trois règles sont déjà celles de `SECURITY.md` et de nos modèles de RoE.
Elles ont maintenant leur fondement écrit.

---

## Sources

- [Loi n° 2018-026 du 7 décembre 2018 (cybersécurité et cybercriminalité)](https://ancy.gouv.tg/wp-content/uploads/2022/02/Loi_n2018-026_du_07_decembre_2018_cybersecurite_et_cybercriminalite.pdf) - ANCy
- [Journal officiel de la République togolaise](https://jo.gouv.tg/) - texte de référence
- [Réglementations - Agence Nationale de la Cybersécurité (ANCy)](https://ancy.gouv.tg/reglementations/)
- [Arrêté n° 2022-040/PMRT portant adoption des règles de cybersécurité](https://cert.tg/wp-content/uploads/2022/07/20220705-Arrete-n%C2%B0-2022-040-PMRT-portant-adoption-des-regles-de-cybersecurite-en-Republique-togolaise.pdf) - CERT.tg
- [Loi n° 2019-014 du 29 octobre 2019 (protection des données à caractère personnel)](https://www.afapdp.org/archives/download-view/togo-loi-n-2019-014-du-29-octobre-2019-relative-a-la-protection-des-donnees-a-caractere-personnel) - AFAPDP
- [Cadre juridique - IPDCP](https://ipdcp.tg/ipdcp/cadre-juridique/)
- [Ministère de la Transformation numérique - décret IPDCP](https://numerique.gouv.tg/le-gouvernement-adopte-le-decret-portant-organisation-et-fonctionnement-de-linstance-de-protection-des-donnees-a-caractere-personnel-ipdcp/)
- [Convention de Malabo - entrée en vigueur](https://blog.africadataprotection.org/blog/2024/01/31/lentree-en-vigueur-de-la-convention-de-lunion-africaine-sur-la-cybersecurite-et-la-protection-des-donnees-quelle-pertinence-neuf-ans-plus-tard/) - Africa Data Protection
