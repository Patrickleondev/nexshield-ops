# PRO-PRIV-100 - Évaluation de conformité

**Version** : v0.1 · **Service** : `x-privacy` · **Phase** : exécution
**Responsable** : responsable GRC · **Sortant** : registre à jour + écarts + plan de mise en conformité

**Préalable bloquant** : `PRO-PRIV-001` close, statut de sous-traitant contractualisé.

---

## Principe

**On vérifie sur pièce, jamais sur déclaration.**

Une durée de conservation annoncée à trois ans se vérifie en regardant si un
mécanisme de suppression existe réellement. Dans la majorité des cas, il n'existe
pas : la donnée est conservée indéfiniment, et personne dans l'organisation ne le
sait. C'est le constat le plus fréquent de ce service.

---

## 1. Consolider le registre

Le registre est le socle. Trois vérifications par traitement :

| Vérification | Comment |
|---|---|
| Le traitement existe vraiment | Le voir fonctionner, pas seulement le lire |
| La finalité déclarée est la seule | Chercher les usages secondaires non déclarés |
| Les données listées sont les seules | Comparer au schéma réel de la base |

L'usage secondaire non déclaré est le point le plus rentable de l'audit : les
données collectées pour une finalité et réutilisées pour une autre, presque
toujours sans base légale.

## 2. Éprouver chaque principe

### Base légale

- [ ] Une base légale par traitement, identifiée et défendable
- [ ] Consentement : libre, spécifique, éclairé, **révocable aussi facilement
      qu'il a été donné**
- [ ] Preuve du consentement conservée, et retrouvable pour une personne donnée
- [ ] Intérêt légitime : mise en balance écrite, pas invoquée oralement

### Minimisation

- [ ] Chaque champ collecté sert la finalité déclarée
- [ ] Champs collectés « au cas où » identifiés et remis en cause
- [ ] Formulaires comparés au registre : ils collectent souvent davantage

### Durées de conservation

- [ ] Une durée chiffrée par catégorie de données
- [ ] **Un mécanisme de suppression existe et fonctionne** - le vérifier
- [ ] Sauvegardes couvertes par la politique, ou écart consigné
- [ ] Archivage distingué de la conservation active

### Droits des personnes

Éprouver, pas lire la procédure. Exercer réellement chaque droit.

- [ ] Information : mentions présentes, lisibles, au moment de la collecte
- [ ] Accès : délai réel mesuré
- [ ] Rectification, effacement, opposition : chemin existant et testé
- [ ] Portabilité, quand elle s'applique
- [ ] Décision automatisée : intervention humaine réellement possible
- [ ] Un canal de contact identifié, et surveillé

### Sécurité

- [ ] Chiffrement au repos et en transit
- [ ] Contrôle d'accès selon le besoin d'en connaître
- [ ] Journalisation des accès aux données sensibles
- [ ] Cloisonnement entre production et environnements de test
- [ ] **Données réelles en environnement de test** : écart fréquent et grave

### Sous-traitants

- [ ] Liste complète, y compris les services en ligne utilisés sans contrat
- [ ] Contrat de sous-traitance signé pour chacun
- [ ] Localisation d'hébergement connue
- [ ] Transferts hors du pays : fondement identifié
- [ ] Sous-traitants ultérieurs connus du responsable de traitement

### Violations de données

- [ ] Procédure écrite, avec des délais
- [ ] Qui décide de notifier, et sous quel délai
- [ ] Destinataires connus : **IPDCP** pour les données personnelles,
      **ANCy** et **CERT.tg** pour l'incident de sécurité
- [ ] Registre des violations tenu, y compris pour celles non notifiées
- [ ] La procédure a déjà été éprouvée au moins une fois

## 3. Analyse d'impact

Obligatoire pour les traitements repérés au cadrage. Structure retenue :

1. Description du traitement et de ses finalités
2. Nécessité et proportionnalité au regard de la finalité
3. Risques pour les personnes : accès illégitime, modification, disparition
4. Mesures existantes et mesures proposées
5. Risque résiduel, et décision du responsable de traitement

> L'analyse d'impact protège les **personnes**, pas l'organisation. Une analyse
> rédigée du point de vue du risque d'entreprise est à refaire.

## 4. Rédiger les écarts

Chaque écart porte :

| Champ | Contenu |
|---|---|
| Traitement | Lequel |
| Principe | Base légale, minimisation, durée, droits, sécurité, sous-traitance |
| Régime | Loi n° 2019-014, RGPD, ou les deux |
| Constat | Ce qui a été vu, avec la pièce |
| Exposition | Pour les personnes d'abord, pour l'organisation ensuite |
| Mesure proposée | Concrète, avec un responsable et une échéance |

Sévérité selon l'échelle unique de la société (`NOMENCLATURE.md` §4), avec un
critère propre au service : **l'exposition des personnes prime sur l'exposition
de l'organisation.**

---

## Règles d'exécution

- **Minimisation appliquée à nous-mêmes** : extraits, jamais de base entière.
- Aucune donnée personnelle réelle dans le rapport, ni dans nos exemples.
- Coffre chiffré, destruction à J+90, certificat produit.
- Aucun avis juridique : sur une question de droit, renvoi vers un conseil.

---

## Critères de sortie

- [ ] Registre consolidé, chaque traitement vérifié sur pièce
- [ ] Usages secondaires non déclarés recherchés
- [ ] Base légale défendable pour chaque traitement
- [ ] Mécanismes de suppression réellement testés
- [ ] Chaque droit des personnes exercé pour de bon, délais mesurés
- [ ] Aucune donnée réelle en environnement de test, ou écart consigné
- [ ] Sous-traitants listés, contrats vérifiés, transferts fondés
- [ ] Procédure de violation écrite, destinataires et délais connus
- [ ] Analyses d'impact produites pour les traitements concernés
- [ ] Plan de mise en conformité daté, chaque action portant un nom
- [ ] Données client détruites, certificat produit
