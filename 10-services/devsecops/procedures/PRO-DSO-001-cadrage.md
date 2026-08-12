# PRO-DSO-001 - Cadrage d'une mission DevSecOps

**Version** : v0.1 · **Service** : `devsecops` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : périmètre signé + niveau SAMM de départ

---

## Ce qui distingue ce cadrage

Ce service ne produit pas un rapport de vulnérabilités : il produit une
**trajectoire de maturité**. Le client n'achète pas un constat, il achète un plan
sur douze mois qu'il pourra suivre et mesurer.

Deux conséquences immédiates :

- L'interlocuteur n'est pas le RSSI mais le **responsable d'ingénierie**. Le
  discours change : ce qui compte pour lui, c'est le temps de cycle, pas la
  conformité.
- Une mission mal cadrée devient un audit qui ralentit les équipes. C'est le
  reproche le plus fréquent adressé à ce métier, et il est souvent mérité.

---

## Étapes

### 1. Fiche de la chaîne de livraison

| Élément | À obtenir |
|---|---|
| Forge | GitHub, GitLab, Bitbucket, auto-hébergée |
| Intégration continue | Outil, où s'exécutent les agents, qui peut les modifier |
| Artefacts | Registre d'images, dépôt de paquets, signature |
| Déploiement | Cible, mécanisme, qui a le droit de déployer en production |
| Environnements | Combien, qui y accède, quelles données ils contiennent |
| Secrets | Où ils vivent aujourd'hui : coffre, variables, fichiers |
| Cadence | Nombre de déploiements par semaine |
| Équipes | Combien de développeurs, combien d'équipes, quelle organisation |

**La question centrale** : *qui peut faire arriver du code en production, et par
combien de chemins différents ?* Presque toujours, il en existe un que personne
n'avait mentionné.

### 2. Mesurer la maturité de départ

Référentiel : [OWASP SAMM](https://owaspsamm.org/) - cinq fonctions métier,
quinze pratiques, trois niveaux de maturité.

L'évaluation se fait **par entretien, avec preuve**. Une pratique déclarée mais
non prouvée est notée à son niveau réel, pas au niveau annoncé. C'est le point
qui rend l'évaluation crédible, et c'est aussi celui qui fâche.

- [ ] Cinq fonctions parcourues : Gouvernance, Conception, Implémentation,
      Vérification, Opérations
- [ ] Une preuve demandée pour chaque niveau revendiqué
- [ ] Note de départ consignée dans le classeur, avec sa date

> Le score de départ n'est pas un jugement. C'est la seule chose qui permettra de
> démontrer un progrès dans un an. Le dire ainsi au client évite la posture
> défensive.

### 3. Retenir le référentiel d'exécution

| Besoin | Référentiel |
|---|---|
| Maturité et trajectoire | [OWASP SAMM](https://owaspsamm.org/) |
| Pratiques de développement | [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) |
| Intégrité de la chaîne d'approvisionnement | [SLSA](https://slsa.dev/) |
| Conteneurs et orchestration | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) |

SSDF sert de langage commun avec les développeurs : ses identifiants
(`PO`, `PS`, `PW`, `RV`) se citent dans les recommandations.

### 4. Fixer le seuil de blocage

Point le plus délicat de la mission. Un contrôle qui bloque trop tôt est
désactivé dans le mois, et la mission a échoué.

- Quelle sévérité bloque une fusion ? Quelle sévérité bloque un déploiement ?
- Quel délai de grâce sur l'existant ? **Le stock ne se traite pas comme le flux.**
- Qui peut déroger, et où la dérogation est-elle tracée ?

Règle que nous défendons : **on bloque d'abord le flux, jamais le stock.** Le
nouveau code respecte le seuil dès le premier jour ; l'existant est résorbé selon
un plan daté.

### 5. Délimiter le périmètre

- Dépôts inclus, un par un
- Chaînes d'intégration incluses
- Ce qui est explicitement exclu, et pourquoi
- Accès nécessaires : lecture des dépôts, lecture des configurations
  d'intégration, **jamais de droit d'écriture en production**

### 6. Rédiger le RoE

Clauses propres au service :

- Accès en lecture seule, périmètre nominatif
- Interdiction de modifier une chaîne de production sans validation écrite
- Traitement des secrets découverts : signalement immédiat, jamais de
  conservation, jamais de test de validité sans accord écrit
- Confidentialité du code source, durée de conservation, destruction à J+90

> **Une mission DevSecOps trouve presque toujours des secrets en clair dans
> l'historique.** La conduite à tenir se décide au cadrage, pas au moment de la
> découverte.

---

## Critères de sortie

- [ ] Fiche de la chaîne complète, chemins vers la production tous identifiés
- [ ] Évaluation SAMM de départ faite, avec preuve pour chaque niveau revendiqué
- [ ] Seuils de blocage arrêtés, distinction flux et stock actée
- [ ] Périmètre des dépôts et des chaînes écrit un par un
- [ ] Accès en lecture obtenus et testés
- [ ] Conduite à tenir sur les secrets découverts écrite au RoE
- [ ] RoE signé

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Bloquer le stock dès le premier jour | Contrôles désactivés, mission discréditée |
| Évaluer SAMM sur déclaration | Score faux, progrès indémontrable l'année suivante |
| Oublier un chemin vers la production | Le plan sécurise une porte et en laisse une ouverte |
| Parler conformité à des développeurs | Rejet immédiat, coopération perdue |
| Découvrir un secret sans conduite prévue | Décision prise dans l'urgence, souvent mauvaise |
