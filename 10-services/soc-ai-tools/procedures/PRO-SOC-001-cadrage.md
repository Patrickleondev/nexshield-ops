# PRO-SOC-001 - Cadrage d'une mission SOC et détection

**Version** : v0.1 · **Service** : `soc-ai-tools` · **Phase** : cadrage
**Responsable** : chef de mission · **Sortant** : périmètre + couverture ATT&CK de départ

---

## Ce qui distingue ce cadrage

Ce service se mesure sur une **couverture de détection**, pas sur un nombre de
règles. Cinquante règles qui couvrent trois techniques valent moins que dix
règles qui en couvrent dix.

Le piège commercial du métier : promettre une couverture ATT&CK élevée. Une
couverture affichée à 80 % est presque toujours fausse - elle compte des
techniques partiellement détectées comme couvertes. Nous comptons autrement, et
c'est notre argument.

---

## Étapes

### 1. Fiche de l'existant

| Élément | À obtenir |
|---|---|
| Collecte | Quelles sources de journaux, depuis quand, rétention |
| Plateforme | SIEM, pile de journaux, ou rien |
| Terminaux | EDR déployé ? Sur quel taux du parc, réellement |
| Réseau | Pare-feu, mandataire, DNS : journaux exploitables ou non |
| Identité | Annuaire, authentification, journaux d'accès |
| Cloud | Fournisseurs, journaux d'audit activés |
| Équipe | Qui regarde les alertes, à quelles heures, combien de personnes |
| Réponse | Existe-t-il une procédure écrite, a-t-elle déjà servi |

**La question centrale** : *quand une alerte se déclenche à 3 h du matin, qui la
voit et que fait-il ?* Si la réponse est « personne », la mission commence par la
réponse à incident, pas par la détection.

### 2. Vérifier ce qui est réellement collecté

Bloquant. **Une source déclarée n'est pas une source collectée.**

- [ ] Pour chaque source annoncée : un événement récent retrouvé dans la plateforme
- [ ] Rétention réelle vérifiée, pas celle de la documentation
- [ ] Horloges synchronisées entre les sources
- [ ] Champs nécessaires effectivement présents, pas tronqués
- [ ] Volume quotidien mesuré, et son coût connu du client

Écrire une règle sur une source non collectée est le premier motif d'échec de ce
métier. On vérifie avant, pas après.

### 3. Mesurer la couverture ATT&CK de départ

Référentiel : [MITRE ATT&CK](https://attack.mitre.org/), matrice Enterprise.

Notation en trois états, jamais en deux :

| État | Signification |
|---|---|
| **Détectée** | Une règle existe, elle a été éprouvée, elle se déclenche |
| **Partielle** | Une règle existe mais ne couvre qu'une variante, ou n'a pas été éprouvée |
| **Absente** | Rien |

> Compter les « partielles » comme couvertes est la façon dont on obtient 80 % de
> couverture affichée. Nous les comptons séparément, et nous l'expliquons. C'est
> moins flatteur au premier rendez-vous, et bien plus solide au second.

### 4. Prioriser par la menace, pas par la matrice

Couvrir ATT&CK en entier n'a aucun sens et coûte cher. On priorise :

1. Les techniques observées sur le secteur et la zone du client
2. Les techniques atteignant les actifs critiques identifiés avec lui
3. Les techniques figurant au
   [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) pour
   les vulnérabilités réellement exploitées
4. Le reste, si le budget le permet

Sortant : une liste de vingt à quarante techniques prioritaires, validée par le
client. Pas plus. Une liste de deux cents techniques ne sera jamais traitée.

### 5. Arrêter le mode de fonctionnement

| Mode | Ce que nous faisons | Ce que le client garde |
|---|---|---|
| Conception | Nous écrivons les règles, le client les exploite | Toute l'exploitation |
| Accompagnement | Nous écrivons et nous formons l'équipe | L'exploitation, avec appui |
| Surveillance | Nous exploitons | La décision de réponse |

Le mode **Surveillance** implique un engagement de service, des astreintes et une
assurance. **Nous ne le vendons pas tant que l'équipe ne peut pas le tenir.** Le
dire au client vaut mieux que de le décevoir.

### 6. Rédiger le RoE

Clauses propres au service :

- Accès en lecture aux journaux, périmètre nominatif
- Confidentialité : les journaux contiennent des données personnelles, donc la
  loi togolaise n° 2019-014 s'applique. Voir `x-privacy`.
- Simulations d'attaque pour éprouver les règles : autorisation écrite distincte,
  fenêtre convenue, personne à joindre
- Conservation et destruction des extraits de journaux à J+90

> **Éprouver une règle demande de déclencher l'attaque correspondante.** C'est un
> test d'intrusion en miniature, il se cadre comme tel.

---

## Critères de sortie

- [ ] Fiche de l'existant complète, y compris qui regarde les alertes et quand
- [ ] Chaque source déclarée vérifiée par un événement réellement retrouvé
- [ ] Rétention et volumes mesurés, coût connu du client
- [ ] Couverture ATT&CK de départ mesurée en trois états
- [ ] Liste de 20 à 40 techniques prioritaires, validée par le client
- [ ] Mode de fonctionnement arrêté, et tenable par l'équipe
- [ ] Autorisation écrite pour les simulations d'attaque
- [ ] RoE signé

---

## Erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Écrire des règles sur une source non collectée | Règles muettes, mission sans effet |
| Compter les couvertures partielles comme acquises | Faux sentiment de sécurité, découvert lors d'un incident |
| Viser toute la matrice ATT&CK | Budget épuisé, priorités jamais traitées |
| Vendre de la surveillance sans astreinte | Engagement intenable, réputation perdue |
| Simuler une attaque sans autorisation écrite | Infraction pénale, quelle que soit l'intention |
