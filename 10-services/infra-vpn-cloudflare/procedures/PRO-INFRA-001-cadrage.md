# PRO-INFRA-001 - Cadrage d'une mission infrastructure

**Version** : v0.1 · **Service** : `infra-vpn-cloudflare` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : périmètre + fenêtres d'intervention

---

## Ce qui distingue ce cadrage

C'est le seul service où **nous modifions des systèmes en production**. Les autres
constatent ; celui-ci intervient. Une erreur ne produit pas un rapport contestable,
elle produit une coupure.

Deux conséquences qui structurent tout le cadrage :

- Chaque changement doit être **réversible**, et le retour arrière doit être écrit
  avant le changement.
- Chaque intervention a une **fenêtre**, une personne à joindre et un critère
  d'arrêt.

---

## Étapes

### 1. Fiche de l'infrastructure

| Élément | À obtenir |
|---|---|
| Périmètre exposé | Adresses publiques, domaines, services accessibles depuis Internet |
| Systèmes | Systèmes d'exploitation et versions, nombre de machines |
| Réseau | Segmentation existante, ou son absence |
| Accès distant | VPN actuel, qui l'utilise, avec quel second facteur |
| Identité | Annuaire, comptes à privilèges, comptes de service |
| Bordure | Cloudflare ou autre, ce qui est déjà configuré |
| Sauvegardes | Existence, fréquence, **restauration déjà testée ou non** |
| Journalisation | Ce qui est collecté, et vers où |
| Dépendances métier | Ce qui tombe si un service s'arrête |

**La question centrale** : *si nous coupons ce service dix minutes, qui s'en
aperçoit et que perd le client ?* La réponse détermine la fenêtre d'intervention.

### 2. Vérifier les sauvegardes avant toute chose

Bloquant, et non négociable.

- [ ] Une sauvegarde récente existe pour chaque système touché
- [ ] **Une restauration a été testée**, pas seulement une sauvegarde effectuée
- [ ] Le client sait qui restaure, et en combien de temps

> Une sauvegarde jamais restaurée n'est pas une sauvegarde, c'est une intention.
> Nous ne touchons pas à un système dont le retour arrière est théorique.

### 3. Recenser l'exposition réelle

Avant toute recommandation, établir ce qui est réellement joignable depuis
Internet. L'écart avec ce que le client croit exposer est presque toujours grand.

- Balayage des adresses publiques du périmètre, avec autorisation écrite
- Services découverts comparés à l'inventaire déclaré
- Interfaces d'administration exposées : le constat le plus fréquent et le plus
  grave
- Certificats : validité, couverture, expiration proche

### 4. Choisir les référentiels de durcissement

| Périmètre | Référentiel |
|---|---|
| Systèmes, conteneurs, cloud | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) |
| Recommandations générales | [Guides de l'ANSSI](https://cyber.gouv.fr/publications) |
| Architecture d'accès | [NIST SP 800-207, Zero Trust](https://csrc.nist.gov/pubs/sp/800/207/final) |
| Techniques adverses | [MITRE ATT&CK](https://attack.mitre.org/) |

Le niveau CIS visé (L1 ou L2) se choisit avec le client, service par service.
**Le niveau L2 casse des choses** sur des systèmes anciens : le dire avant, pas
après.

### 5. Cadrer l'accès distant

Le VPN est le sujet le plus demandé et le plus mal posé. La question n'est pas
« quel VPN », mais **« qui doit atteindre quoi »**.

- [ ] Population des utilisateurs distants, et ce que chacun doit atteindre
- [ ] Second facteur : obligatoire, sans exception, y compris pour la direction
- [ ] Accès des prestataires : comptes nominatifs et limités dans le temps
- [ ] Postes personnels : autorisés ou non, et conséquences assumées
- [ ] Journalisation des connexions, et vers où elle part

Position que nous défendons : **un VPN qui donne accès à tout le réseau est un
mauvais VPN.** L'accès se donne par application, selon le principe du moindre
privilège (NIST SP 800-207). Cela demande plus de travail, et c'est ce qui
distingue une prestation d'une installation.

### 6. Arrêter les fenêtres d'intervention

Pour chaque changement prévu :

| Élément | Contenu |
|---|---|
| Fenêtre | Date, heure de début, durée maximale |
| Personne à joindre | Un nom, un numéro, disponible pendant la fenêtre |
| Critère d'arrêt | Ce qui déclenche le retour arrière, décidé à l'avance |
| Retour arrière | Écrit, testé si possible, avant le changement |
| Validation | Qui confirme que le service fonctionne après |

### 7. Rédiger le RoE

Clauses propres au service :

- Liste des systèmes sur lesquels nous avons un droit de modification
- Fenêtres d'intervention et critères d'arrêt
- Interdiction de toute action hors fenêtre sans accord écrit
- Responsabilité en cas d'indisponibilité : plafonnée, adossée à l'assurance
- Remise des configurations produites, et leur propriété

---

## Critères de sortie

- [ ] Fiche d'infrastructure complète, dépendances métier comprises
- [ ] Sauvegardes vérifiées, **restauration déjà testée**
- [ ] Exposition réelle établie, écart avec l'inventaire déclaré consigné
- [ ] Référentiel et niveau CIS arrêtés, service par service
- [ ] Population des accès distants définie, avec le besoin réel de chacun
- [ ] Second facteur acté sans exception
- [ ] Fenêtres, personnes à joindre et critères d'arrêt écrits pour chaque changement
- [ ] Retours arrière écrits avant les changements
- [ ] RoE et autorisation signés

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Intervenir sans restauration testée | Coupure sans retour arrière possible |
| Appliquer un CIS L2 sur un système ancien | Services cassés, confiance perdue |
| VPN donnant accès à tout le réseau | Un poste compromis ouvre l'ensemble |
| Exception de second facteur pour la direction | Le compte le plus ciblé est le moins protégé |
| Changement sans critère d'arrêt écrit | Décision prise dans l'urgence, à 2 h du matin |
| Se fier à l'inventaire déclaré | Des interfaces d'administration restent exposées |
