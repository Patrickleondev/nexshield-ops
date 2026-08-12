# PRO-PRIV-001 - Cadrage d'une mission vie privée

**Version** : v0.1 · **Service** : `x-privacy` · **Phase** : cadrage
**Responsable** : responsable GRC · **Sortant** : périmètre + régimes applicables identifiés

---

## Ce qui distingue ce cadrage

C'est le seul service où **le référentiel est une loi**. On ne choisit pas son
niveau d'ambition : soit le traitement est conforme, soit il ne l'est pas.

Conséquence directe sur la posture : nous constatons des écarts et nous
proposons des mesures. **Nous ne rendons pas d'avis juridique.** Cette limite est
écrite au contrat et redite en restitution. Un cabinet d'avocats prend le relais
quand la question devient une question de droit.

---

## Étapes

### 1. Identifier les régimes applicables

Bloquant, et souvent mal fait. Un même client peut relever de plusieurs régimes
simultanément.

| Régime | S'applique si |
|---|---|
| **Loi togolaise n° 2019-014** du 29 octobre 2019 | Le responsable de traitement est établi au Togo, ou traite des données de personnes au Togo |
| **Décret n° 2020-111/PR** | Précise les modalités d'application de la loi de 2019 |
| **Convention de Malabo** | Cadre continental, ratifié par le Togo, en vigueur depuis le 8 juin 2023 |
| **RGPD (UE 2016/679)** | Établissement dans l'UE, ou offre de biens et services à des personnes dans l'UE, ou suivi de leur comportement |
| **Autres droits africains** | Selon les pays où le client opère réellement |

> **L'erreur classique** : un client togolais qui vend en ligne à des clients
> européens relève des deux régimes. Il l'ignore presque toujours.

Autorité de contrôle togolaise : **IPDCP** (Instance de protection des données à
caractère personnel). Autorité de cybersécurité : **ANCy**.

### 2. Recenser les traitements

Sans registre, aucune mission de conformité n'est possible. S'il n'existe pas,
le construire **est** la première partie de la mission, et cela se facture.

Pour chaque traitement :

| Élément | À obtenir |
|---|---|
| Finalité | Pourquoi, en une phrase, sans jargon |
| Base légale | Consentement, contrat, obligation légale, intérêt légitime |
| Catégories de personnes | Clients, salariés, prospects, mineurs |
| Catégories de données | Dont les données sensibles, à isoler |
| Destinataires | Internes, sous-traitants, autorités |
| Transferts hors du pays | Vers où, sur quel fondement |
| Durée de conservation | Une durée chiffrée, pas « le temps nécessaire » |
| Mesures de sécurité | Ce qui existe réellement |

### 3. Repérer ce qui déclenche une obligation renforcée

- [ ] Données sensibles : santé, biométrie, opinions, appartenance syndicale
- [ ] Données de mineurs
- [ ] Surveillance systématique : vidéoprotection, géolocalisation, contrôle
      d'activité des salariés
- [ ] Décision automatisée produisant des effets juridiques
- [ ] Croisement de fichiers à grande échelle
- [ ] Transferts hors du Togo, ou hors de l'UE selon le régime

Chacun de ces points appelle une analyse d'impact. Le repérer au cadrage évite de
découvrir l'obligation à mi-mission.

### 4. Vérifier les formalités auprès de l'IPDCP

La loi togolaise prévoit des formalités préalables selon la nature du traitement.
**Nous vérifions leur état réel** : accomplies, en cours, jamais faites.

- [ ] Formalités identifiées pour chaque traitement
- [ ] État réel vérifié, avec pièce à l'appui
- [ ] Écarts consignés, avec leur exposition

Nous ne déposons rien à la place du client, et nous ne préjugeons pas de la
décision de l'autorité. Nous constatons et nous documentons.

### 5. Arrêter le périmètre

- Traitements inclus, un par un
- Entités et pays couverts
- Sous-traitants examinés, ou explicitement exclus
- Ce qui relève de l'avis juridique et sort donc du périmètre

### 6. Rédiger le contrat et le RoE

Clauses propres au service :

- **Nous accédons à des données personnelles réelles.** Le contrat doit prévoir
  notre statut de sous-traitant, avec les clauses correspondantes.
- Minimisation : nous demandons des extraits, jamais des bases entières
- Interdiction de conservation au-delà de la mission, destruction à J+90
- Limite explicite : constat de conformité, pas avis juridique
- Confidentialité renforcée : un rapport de conformité est une cartographie des
  écarts, donc un document sensible

---

## Critères de sortie

- [ ] Tous les régimes applicables identifiés, y compris cumulés
- [ ] Registre des traitements existant, ou sa construction inscrite au périmètre
- [ ] Traitements à obligation renforcée repérés
- [ ] État réel des formalités IPDCP vérifié, pièces à l'appui
- [ ] Périmètre écrit traitement par traitement
- [ ] Statut de sous-traitant contractualisé
- [ ] Limite « pas d'avis juridique » écrite au contrat
- [ ] RoE signé

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Ne retenir que le RGPD | La loi togolaise, seule applicable localement, est ignorée |
| Ne retenir que la loi togolaise | Exposition européenne non traitée pour un client qui exporte |
| Accepter un registre déclaratif | Mission fondée sur des traitements qui n'existent pas, et angles morts |
| Recevoir une base entière | Nous devenons nous-mêmes un risque pour le client |
| Donner un avis juridique | Hors de notre compétence, et hors de notre assurance |
