# PRO-APP-001 - Cadrage d'une évaluation de sécurité applicative

**Version** : v0.1 · **Service** : `secu-applicative` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : RoE signé + niveau ASVS arrêté

---

## Ce qui distingue ce cadrage

Une mission applicative se vend et se mesure sur un **niveau d'assurance**, pas
sur un nombre de jours. C'est ce qui la rend re-mesurable l'année suivante, donc
refacturable. Le niveau se décide ici, avec le client, et il est écrit au RoE.

---

## Étapes

### 1. Fiche de l'application

| Élément | À obtenir |
|---|---|
| Type | Web, mobile (iOS, Android), API, ou combinaison |
| Pile technique | Langages, cadriciels, versions |
| Hébergement | Sur site, cloud, conteneurs |
| Authentification | Locale, SSO, OAuth 2.0, OIDC, fédération |
| Rôles | Liste exhaustive, avec ce que chacun a le droit de faire |
| Multi-locataire | Oui ou non - change tout sur le contrôle d'accès |
| Données manipulées | Personnelles, bancaires, de santé |
| Flux d'argent | Paiement, virement, remboursement, avoir |
| Intégrations | Services tiers appelés, webhooks reçus |

### 2. Choisir le niveau ASVS visé

Référentiel : [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS) (mai 2025),
17 chapitres, trois niveaux.

| Niveau | Pour qui | Effort |
|---|---|---|
| **L1** | Application sans donnée sensible, première évaluation | Tests dynamiques, sans code |
| **L2** | Cas nominal : données personnelles, comptes utilisateurs, argent | Dynamique + revue de code ciblée |
| **L3** | Applications critiques : santé, finance, vies humaines | Revue de code étendue, architecture |

> **Le niveau ne se choisit pas par ambition, mais par risque.** Un client qui
> demande L3 sur une vitrine paye pour du vent. Nous le disons.

Ce que le niveau implique, à annoncer avant signature :

- **L2 et L3 exigent l'accès au code.** Sans code, le niveau atteignable est L1,
  et c'est écrit au rapport. Ce point est le plus fréquent motif de déception.
- Un niveau **visé** n'est pas un niveau **atteint**. Le rapport donne l'écart.

### 3. Obtenir les comptes de test

Bloquant. Une mission applicative sans jeu de comptes complet ne teste pas le
contrôle d'accès, donc ne teste pas l'essentiel.

- [ ] **Deux comptes par rôle**, au minimum. Un seul compte ne permet pas de
      démontrer un accès horizontal entre pairs.
- [ ] Un compte par niveau de privilège, administrateur compris
- [ ] Sur une application multi-locataire : **deux locataires distincts**
- [ ] Comptes non liés à des personnes réelles, réinitialisables
- [ ] Jeu de données de test représentatif, sans donnée personnelle réelle

### 4. Arrêter l'environnement

| Environnement | Réserve |
|---|---|
| Production | Aucun test destructif, aucun test de charge, alerte préalable de l'hébergeur |
| Préproduction | À privilégier ; vérifier qu'elle a la même configuration que la production |
| Recette | Souvent trop différente pour que les résultats vaillent |

Une préproduction qui ne reflète pas la production produit un rapport qui ne vaut
rien. Le vérifier, pas le supposer.

### 5. Délimiter le périmètre

- Domaines, sous-domaines et points d'accès d'API inclus, **écrits un par un**
- Ce qui est explicitement exclu, et pourquoi
- Services tiers : **hors périmètre par défaut**. Tester le prestataire de
  paiement du client sans son accord est un délit.
- Comportement attendu face aux protections : WAF laissé actif, ou liste
  d'autorisation pour nos adresses. Les deux se défendent, il faut choisir.

### 6. Référentiels complémentaires retenus

| Périmètre | Référentiel |
|---|---|
| Web | [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) |
| Exigences | [OWASP ASVS 5.0](https://github.com/OWASP/ASVS) |
| API | [OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) |
| Mobile | [OWASP MASTG](https://mas.owasp.org/MASTG/) et MASVS |

### 7. Rédiger le RoE

Gabarit : `Modele-ROE-regles-engagement.docx`. Clauses propres au service :

- Niveau ASVS visé et conséquence de l'absence d'accès au code
- Liste des comptes fournis, et par qui ils sont réinitialisés
- Interdiction des tests de disponibilité et de charge
- Traitement des données découvertes : aucune extraction au-delà de la preuve
- Fenêtre de test et personne à joindre en cas d'incident

---

## Critères de sortie

- [ ] Fiche d'application complète, rôles listés un par un
- [ ] Niveau ASVS arrêté et justifié par le risque
- [ ] Accès au code obtenu, ou limitation à L1 actée par écrit
- [ ] Deux comptes par rôle, testés et fonctionnels avant le jour 1
- [ ] Environnement arrêté, écart avec la production vérifié
- [ ] Périmètre écrit point d'accès par point d'accès
- [ ] Position sur le WAF tranchée
- [ ] RoE et autorisation de test signés

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Un seul compte par rôle | Aucun test d'accès horizontal possible |
| Comptes fournis le jour 1 | Une journée perdue, facturée au client |
| Niveau ASVS non écrit | Désaccord à la restitution, sur la valeur même du rapport |
| Périmètre exprimé par un domaine générique | Découverte d'actifs hors périmètre en pleine mission |
| Promettre L2 sans accès au code | Promesse intenable, écart découvert trop tard |
