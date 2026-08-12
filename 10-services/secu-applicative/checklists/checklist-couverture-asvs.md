# Checklist - couverture OWASP ASVS 5.0.0

**Version** : v0.1 · Se recopie dans l'annexe de couverture du rapport.

**Référentiel appliqué** : [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS),
mai 2025, 17 chapitres, trois niveaux d'assurance.

Trois statuts : **Exécuté**, **Non applicable** (avec la raison technique),
**Non exécuté** (avec le motif). Un statut « Non exécuté » n'est pas une faute.
Le taire en est une.

Le **niveau visé** est celui arrêté au RoE. Le rapport affiche l'écart entre le
niveau visé et le niveau atteint, chapitre par chapitre.

---

## Chapitres

| # | Chapitre | Statut | Niveau atteint |
|---|---|---|---|
| V1 | Encoding and Sanitization | | |
| V2 | Validation and Business Logic | | |
| V3 | Web Frontend Security | | |
| V4 | API and Web Service | | |
| V5 | File Handling | | |
| V6 | Authentication | | |
| V7 | Session Management | | |
| V8 | Authorization | | |
| V9 | Self-contained Tokens | | |
| V10 | OAuth and OIDC | | |
| V11 | Cryptography | | |
| V12 | Secure Communication | | |
| V13 | Configuration | | |
| V14 | Data Protection | | |
| V15 | Secure Coding and Architecture | | |
| V16 | Security Logging and Error Handling | | |
| V17 | WebRTC | | |

> **V15** ne se renseigne honnêtement qu'avec l'accès au code. Sans code :
> « Non exécuté - absence d'accès au code source ».
> **V17** est « Non applicable » sur la grande majorité des applications.

---

## Points d'exécution, par domaine

### Authentification et session

- [ ] Politique de mot de passe et limitation des tentatives
- [ ] Réinitialisation : jeton non devinable, à usage unique, expirant
- [ ] Second facteur non contournable par rejeu d'étape
- [ ] Identifiant de session régénéré après connexion
- [ ] Déconnexion effective côté serveur
- [ ] Jeton autoportant : signature vérifiée, algorithme `none` refusé
- [ ] OAuth et OIDC : `redirect_uri` contrôlée, `state` vérifié, PKCE

### Contrôle d'accès

- [ ] Accès horizontal entre deux comptes du même rôle
- [ ] Accès vertical vers une fonction d'administration
- [ ] Modification d'un champ non prévu dans le corps de la requête
- [ ] Cloisonnement entre deux locataires
- [ ] Chaque requête rejouée sans session du tout
- [ ] Contrôle appliqué côté serveur, pas seulement masqué à l'affichage

### Entrées et injections

- [ ] Injection SQL, NoSQL, commandes, LDAP, template côté serveur
- [ ] XSS réfléchi, stocké, fondé sur le DOM
- [ ] Désérialisation de données non fiables
- [ ] Traversée de chemin, téléversement de fichier
- [ ] SSRF sur tout champ contenant une URL

### Logique métier

- [ ] Étapes enchaînées dans un ordre non prévu
- [ ] Rejeu d'une opération à usage unique
- [ ] Valeurs négatives, nulles, arrondis
- [ ] Course entre requêtes simultanées
- [ ] Contournement de quota, de plafond ou de remise

### API

- [ ] Inventaire réel comparé à la documentation (API9:2023)
- [ ] Limitation de consommation de ressources (API4:2023)
- [ ] Consommation d'API tierces vérifiée (API10:2023)

### Configuration et données

- [ ] TLS : versions, suites, certificat, HSTS
- [ ] En-têtes de sécurité et politique de sécurité de contenu
- [ ] Aucun secret dans le paquet JavaScript ni dans une réponse
- [ ] Messages d'erreur sans trace de pile en production
- [ ] Un accès non autorisé laisse une trace exploitable

---

## Avant de clore

- [ ] Niveau visé et niveau atteint affichés par chapitre
- [ ] Chaque constatation porte son identifiant WSTG et son CWE
- [ ] Écarts entre niveau visé et atteint expliqués, sans détour
- [ ] Version d'ASVS appliquée notée au rapport
- [ ] Correction proposée pour chaque constatation, exploitable par un développeur
- [ ] Double relecture effectuée
