# PRO-APP-100 - Exécution des tests applicatifs

**Version** : v0.1 · **Service** : `secu-applicative` · **Phase** : exécution
**Responsable** : testeur · **Sortant** : constatations + matrice ASVS renseignée

**Préalable bloquant** : `PRO-APP-001` close, tous critères de sortie cochés.

---

## Principe

Deux fils conduits en parallèle, et il faut les mener tous les deux :

1. **Le fil ASVS** - parcours des exigences, chapitre par chapitre. Il donne la
   couverture et le niveau d'assurance. C'est ce qui se vend.
2. **Le fil WSTG** - tests offensifs guidés par l'architecture. Il donne les
   constatations. C'est ce qui marque.

Un rapport qui n'a que le premier est un audit de conformité sans preuve. Un
rapport qui n'a que le second n'est pas re-mesurable l'année suivante.

---

## Ordre d'exécution

L'ordre importe : chaque étape informe la suivante.

### 1. Cartographie

- Recensement des points d'entrée, des paramètres, des points d'accès d'API
- Repérage des technologies et des versions
- Récupération de la documentation d'API si elle existe (OpenAPI, Swagger)
- **Différence entre l'API documentée et l'API réelle** : c'est
  [API9:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/), et
  c'est souvent le premier constat exploitable

Sortant : un inventaire, dans le classeur de mission. Rien n'est testé avant.

### 2. Authentification et session

Chapitres ASVS **V6 Authentication**, **V7 Session Management**,
**V9 Self-contained Tokens**, **V10 OAuth and OIDC**.

- Politique de mot de passe, limitation des tentatives, verrouillage
- Réinitialisation de mot de passe : le jeton est-il devinable, réutilisable,
  expire-t-il ?
- Second facteur : peut-on le contourner en rejouant une étape ?
- Session : entropie, régénération après connexion, expiration réelle,
  déconnexion effective côté serveur
- Jetons autoportants : signature vérifiée, algorithme `none` refusé, durée de
  vie, révocation possible
- OAuth et OIDC : `redirect_uri` contrôlée, `state` vérifié, PKCE

### 3. Contrôle d'accès

Chapitre ASVS **V8 Authorization**. **C'est ici que se trouve la valeur.**

Aucun outil ne trouve ces défauts, parce qu'aucun outil ne sait ce qu'un rôle a
le droit de faire. C'est pour cela que le cadrage exige deux comptes par rôle.

| Test | Référence |
|---|---|
| Accès horizontal : le compte A atteint l'objet de B | [API1:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) |
| Accès vertical : un utilisateur atteint une fonction d'administration | API5:2023 |
| Propriété d'objet : modifier un champ non prévu (`role`, `solde`, `statut`) | API3:2023 |
| Cloisonnement entre locataires | API1:2023 |
| Accès direct à une ressource par son identifiant | API1:2023 |

Méthode : rejouer chaque requête d'un rôle avec la session d'un autre rôle, et
avec aucune session. Trois passages, systématiquement.

### 4. Validation des entrées et injections

Chapitres ASVS **V1 Encoding and Sanitization**, **V2 Validation and Business
Logic**, **V5 File Handling**.

- Injection SQL, NoSQL, commandes, LDAP, templates côté serveur
- XSS réfléchi, stocké, fondé sur le DOM
- Désérialisation de données non fiables
- Traversée de chemin et téléversement de fichiers
- SSRF - [API7:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/),
  à tester dès qu'un champ contient une URL

### 5. Logique métier

Le domaine le plus rentable et le moins outillé. À conduire à partir des flux
d'argent listés au cadrage.

- Enchaînement d'étapes dans un ordre non prévu
- Rejeu d'une opération qui ne devrait avoir lieu qu'une fois
- Valeurs négatives, quantités nulles, arrondis
- Course entre deux requêtes simultanées sur la même ressource
- Contournement d'une limite censée s'appliquer (quota, plafond, remise)

Référence : API6:2023, accès non restreint à des flux métier sensibles.

### 6. Configuration, transport et données

Chapitres ASVS **V11 Cryptography**, **V12 Secure Communication**,
**V13 Configuration**, **V14 Data Protection**, **V16 Security Logging**.

- TLS : versions, suites, certificat, HSTS
- En-têtes de sécurité, politique de sécurité de contenu
- Secrets exposés dans le paquet JavaScript, dans un dépôt, dans une réponse
- Messages d'erreur trop bavards, traces de pile en production
- Journalisation : un accès non autorisé laisse-t-il une trace exploitable ?

### 7. Revue de code (L2 et L3 seulement)

Chapitre ASVS **V15 Secure Coding and Architecture**.

Ciblée, jamais exhaustive. Trois priorités, dans cet ordre :

1. Les points où une constatation dynamique demande confirmation
2. La gestion des secrets et la cryptographie
3. Les fonctions d'autorisation, pour vérifier qu'elles sont appliquées partout

### 8. Mobile (si applicable)

Référentiel [OWASP MASTG](https://mas.owasp.org/MASTG/) et MASVS. Stockage local,
épinglage de certificat, protection contre la rétro-ingénierie, secrets dans le
paquet applicatif.

---

## Règles d'exécution

- **Aucun test de disponibilité ni de charge**, sauf clause explicite au RoE.
- **Aucune extraction de données réelles** au-delà de ce que la preuve exige :
  une capture montrant une ligne suffit à démontrer un accès, pas une base entière.
- **Journal horodaté** de chaque campagne, y compris les actions passant par un
  outil automatique ou un serveur MCP.
- **Notification sous 2 h** en cas de constatation critique, sans attendre le
  rapport. Prévue au RoE.
- **Arrêt immédiat** si un test provoque un effet non prévu en production.

Collecte et destruction des preuves : procédure commune
[`PRO-GEN-100`](../../../00-societe/procedures/PRO-GEN-100-collecte-de-preuves.md).

---

## Critères de sortie

- [ ] Inventaire des points d'entrée complet, et comparé à la documentation d'API
- [ ] Chaque exigence ASVS du niveau visé porte un statut
- [ ] Contrôle d'accès testé avec deux comptes par rôle, et sans session
- [ ] Flux métier listés au cadrage tous éprouvés
- [ ] Revue de code faite si le niveau est L2 ou L3
- [ ] Chaque constatation porte son identifiant WSTG et son CWE
- [ ] Journal des opérations complet
- [ ] Preuves au coffre, manifeste d'empreintes produit
