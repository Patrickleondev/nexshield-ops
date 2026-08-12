# PRO-DSO-100 - Mise en œuvre des contrôles

**Version** : v0.1 · **Service** : `devsecops` · **Phase** : exécution
**Responsable** : intervenant DevSecOps · **Sortant** : contrôles en place + plan daté

**Préalable bloquant** : `PRO-DSO-001` close, seuils de blocage arrêtés.

---

## Principe

**On installe dans l'ordre du bénéfice, pas dans l'ordre du catalogue.**

Un contrôle qui produit du bruit dès la première semaine sera contourné. L'ordre
ci-dessous est retenu parce qu'il commence par ce qui a le meilleur rapport
signal sur bruit.

| Rang | Contrôle | Pourquoi en premier |
|---|---|---|
| 1 | Détection de secrets | Impact immédiat, presque aucun faux positif |
| 2 | Dépendances (SCA) | Volume maîtrisable, correction souvent triviale |
| 3 | Durcissement de la chaîne elle-même | Personne ne le fait, tout le monde en a besoin |
| 4 | Analyse statique (SAST) | Utile, mais bruyante : à régler avant d'imposer |
| 5 | Conteneurs et infrastructure | Selon la cible du client |
| 6 | Analyse dynamique (DAST) | Recouvre `secu-applicative`, à ne pas doubler |

---

## 1. Détection de secrets

Deux temps, et il ne faut pas les confondre :

- **Le flux** : un contrôle avant fusion refuse tout nouveau secret. Actif dès le
  premier jour, sans délai de grâce. Un secret est un défaut bloquant.
- **Le stock** : balayage de l'historique complet. Il produit toujours des
  résultats, souvent nombreux.

Conduite sur un secret trouvé dans l'historique, dans cet ordre :

1. **Le révoquer.** Réécrire l'historique ne suffit pas : le secret a été exposé.
2. Le remplacer par une référence à un coffre.
3. Seulement ensuite, décider si l'historique doit être purgé.

> Beaucoup d'équipes commencent par purger l'historique et oublient de révoquer.
> Le secret reste valide, et il a déjà été cloné. Ce point se dit à voix haute en
> restitution.

Nous ne testons jamais la validité d'un secret découvert sans accord écrit : ce
serait un accès non autorisé au sens de la loi togolaise n° 2018-026.

## 2. Dépendances

- Inventaire complet, production **et** développement
- Priorisation : sévérité, puis exploitabilité réelle, puis
  [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) et
  [EPSS](https://www.first.org/epss/)
- Production d'un SBOM, format CycloneDX ou SPDX
- Épinglage des versions et vérification d'intégrité

**Une alerte de sévérité élevée sur une dépendance non atteignable depuis le code
n'est pas une urgence.** Le dire évite de faire courir l'équipe pour rien, et
c'est ce qui distingue un conseil d'un tableau de bord.

## 3. Durcissement de la chaîne elle-même

Le point le plus négligé, et souvent le plus grave. La chaîne d'intégration a
accès à tout : au code, aux secrets, à la production.

- [ ] Actions et images tierces **épinglées par empreinte**, pas par étiquette
- [ ] Droits des jetons d'intégration réduits au strict nécessaire
- [ ] Chaînes déclenchées par une contribution externe : aucun accès aux secrets
- [ ] Branche principale protégée, revue obligatoire, historique linéaire
- [ ] Journalisation des exécutions conservée
- [ ] Séparation des environnements : la chaîne de test n'atteint pas la production

Référentiels : [SLSA](https://slsa.dev/) pour l'intégrité des artefacts,
[NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) `PO`, `PS`, `PW`, `RV`
pour les identifiants cités en recommandation.

## 4. Analyse statique

- Règles réglées **avant** activation du blocage, jamais l'inverse
- Faux positifs traités comme des défauts de configuration, pas comme du bruit
  acceptable
- Résultats remis aux développeurs dans leur outil, pas dans un tableau séparé

Règle de survie : **un contrôle bloquant à plus de 20 % de faux positifs sera
désactivé.** On règle d'abord, on bloque ensuite.

## 5. Conteneurs et infrastructure

- Images de base minimales, mises à jour, non exécutées en `root`
- Analyse des images au moment de la construction
- Configuration d'orchestration selon les
  [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- Infrastructure décrite en code : analyse avant application

## 6. Analyse dynamique

À brancher sur la préproduction, jamais sur la production sans clause.

Recouvre le service `secu-applicative` : ne pas facturer deux fois la même chose.
Ici, l'objectif est la **non-régression automatique**, pas la profondeur.

---

## Le plan remis au client

C'est le vrai livrable. Il tient sur une page et contient :

| Colonne | Contenu |
|---|---|
| Action | Une action, une seule, formulée à l'impératif |
| Pratique SAMM | La pratique visée |
| Niveau visé | Le niveau de maturité attendu après l'action |
| Responsable | **Un nom.** Une action sans nom n'existe pas |
| Échéance | Une date, pas un trimestre |
| Preuve attendue | Ce qui permettra de dire que c'est fait |

Trois horizons : 30 jours, 90 jours, 12 mois. Au-delà, personne ne suit.

---

## Critères de sortie

- [ ] Détection de secrets active sur le flux
- [ ] Historique balayé, secrets trouvés révoqués puis remplacés
- [ ] Inventaire des dépendances et SBOM produits
- [ ] Chaîne d'intégration durcie, actions épinglées par empreinte
- [ ] Analyse statique réglée avant tout blocage
- [ ] Seuils de blocage appliqués au flux, plan daté pour le stock
- [ ] Plan à 30, 90 et 365 jours remis, chaque action portant un nom et une date
- [ ] Score SAMM de sortie mesuré et comparé à celui du cadrage
