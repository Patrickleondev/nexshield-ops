# Outillage - Sécurité applicative

**Version** : v0.1 · **Service** : `secu-applicative`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

**Le scanner ne trouve pas ce qui se vend.** Les défauts de contrôle d'accès et
de logique métier - ceux qui produisent nos constatations critiques - ne sont
trouvés par aucun produit, parce qu'aucun ne sait ce qu'un rôle a le droit de
faire.

Trois interdits :

- Aucun outil n'est lancé avant la clôture de `PRO-APP-001`.
- Aucun résultat de scanner n'entre au rapport sans avoir été rejoué à la main.
- Aucun scan actif en production sans clause explicite au RoE.

---

## 2. Socle retenu

| Outil | Rôle | Licence |
|---|---|---|
| [Burp Suite](https://portswigger.net/burp) | Mandataire d'interception, rejeu, cœur de la mission | Commerciale (Professional) |
| [OWASP ZAP](https://www.zaproxy.org/) | Alternative libre, utilisable en intégration continue | Apache-2.0 |
| [ffuf](https://github.com/ffuf/ffuf) | Découverte de contenu et de paramètres | MIT |
| [nuclei](https://github.com/projectdiscovery/nuclei) | Détection de failles connues par modèles | MIT |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | Confirmation d'injection SQL | GPL-2.0 |
| [Semgrep](https://github.com/semgrep/semgrep) | Analyse statique, revue de code L2 et L3 | LGPL-2.1 |
| [testssl.sh](https://github.com/testssl/testssl.sh) | Vérification TLS, chapitre ASVS V12 | GPL-2.0 |
| [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | Première passe mobile, MASTG | GPL-3.0 |

Burp Professional est le seul poste commercial indispensable du service. Le
rejeu manuel de requêtes avec substitution de session est ce qui produit les
constatations de contrôle d'accès.

---

## 3. Couverture réelle par domaine

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Injections | Oui, bien | Confirmation et démonstration d'impact |
| XSS | Oui | Contexte DOM, contournement de politique de contenu |
| TLS et en-têtes | Oui, entièrement | Rien |
| Failles connues de composants | Oui | Vérifier l'exploitabilité réelle |
| **Contrôle d'accès** | **Non** | Rejeu inter-comptes, tout le chapitre V8 |
| **Logique métier** | **Non** | Flux d'argent listés au cadrage |
| Authentification | Partiel | Enchaînements, second facteur, réinitialisation |
| Revue de code | Partiel | Semgrep signale, l'humain juge |

**Les deux lignes en gras sont notre valeur.** Le reste est du volume que
n'importe qui produit.

---

## 4. Ce que nous ne faisons pas

- **Aucun scan actif automatisé en production** sans clause dédiée : un scanner
  crée des enregistrements, déclenche des courriels, épuise des quotas.
- **Aucun outil qui téléverse le code du client vers un service tiers**, y compris
  les analyseurs en ligne. Incompatible avec le NDA.
- **Aucune capture de base de données** : une ligne suffit à démontrer un accès.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| OWASP ASVS 5.0.0 | https://github.com/OWASP/ASVS |
| OWASP WSTG | https://owasp.org/www-project-web-security-testing-guide/ |
| OWASP API Security Top 10 2023 | https://owasp.org/API-Security/editions/2023/en/0x11-t10/ |
| OWASP MASTG | https://mas.owasp.org/MASTG/ |
| OWASP Top 10 | https://owasp.org/www-project-top-ten/ |
| CWE | https://cwe.mitre.org/ |

---

## 6. Avant d'ajouter un outil

- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Ce qu'il envoie à l'extérieur est connu et documenté
- [ ] Testé sur un système interne avant toute mission
- [ ] Ajouté à ce document, avec sa couverture et ses limites
