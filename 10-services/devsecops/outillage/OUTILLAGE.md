# Outillage - DevSecOps

**Version** : v0.1 · **Service** : `devsecops`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

**Nous ne vendons pas des outils, nous vendons une trajectoire.** Le client peut
installer tout ce catalogue seul ; ce qu'il ne sait pas faire, c'est régler les
seuils pour que les contrôles survivent au premier trimestre.

Trois interdits :

- Aucun droit d'écriture sur une chaîne de production.
- Aucun secret client conservé dans nos systèmes, à aucun moment.
- Aucun test de validité d'un secret découvert sans accord écrit : ce serait un
  accès non autorisé au sens de la loi togolaise n° 2018-026.

---

## 2. Socle retenu

| Besoin | Outil | Licence |
|---|---|---|
| Secrets, flux | [gitleaks](https://github.com/gitleaks/gitleaks) | MIT |
| Secrets, historique | [trufflehog](https://github.com/trufflesecurity/trufflehog) | AGPL-3.0 |
| Dépendances et images | [Trivy](https://github.com/aquasecurity/trivy) | Apache-2.0 |
| Dépendances, précision | [OSV-Scanner](https://github.com/google/osv-scanner) | Apache-2.0 |
| Analyse statique | [Semgrep](https://github.com/semgrep/semgrep) | LGPL-2.1 |
| Infrastructure en code | [Checkov](https://github.com/bridgecrewio/checkov) | Apache-2.0 |
| Durcissement de la chaîne | [zizmor](https://github.com/zizmorcore/zizmor) | MIT |
| SBOM | [Syft](https://github.com/anchore/syft) | Apache-2.0 |
| Priorisation | [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [EPSS](https://www.first.org/epss/) | Publics |

Deux outils de détection de secrets, et ce n'est pas une redondance : `gitleaks`
est rapide et sert le flux avant fusion ; `trufflehog` vérifie l'existence réelle
d'un secret et sert le balayage d'historique.

---

## 3. Ordre d'installation

L'ordre est le même que dans `PRO-DSO-100`, et il n'est pas négociable : il va du
meilleur au pire rapport signal sur bruit.

| Rang | Contrôle | Bruit attendu |
|---|---|---|
| 1 | Secrets sur le flux | Quasi nul |
| 2 | Dépendances | Modéré, corrections souvent triviales |
| 3 | Durcissement de la chaîne | Nul, ce sont des corrections de configuration |
| 4 | Analyse statique | **Élevé** - à régler avant tout blocage |
| 5 | Conteneurs et infrastructure | Modéré |
| 6 | Analyse dynamique | Faible, mais recouvre `secu-applicative` |

**Un contrôle bloquant à plus de 20 % de faux positifs sera désactivé dans le
mois.** C'est la seule métrique qui décide du moment où l'on active le blocage.

---

## 4. Couverture réelle

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Secrets | Oui, très bien | Décider quoi révoquer, et dans quel ordre |
| Dépendances | Oui | Distinguer vulnérable et **atteignable** |
| Chaîne d'intégration | Partiel | Cartographier tous les chemins vers la production |
| Analyse statique | Oui | Régler les règles, juger les faux positifs |
| **Maturité SAMM** | **Non** | Entretiens, demande de preuve, notation |
| **Seuils de blocage** | **Non** | Le jugement qui décide de la survie des contrôles |

Les deux dernières lignes sont ce que le client ne peut pas obtenir seul.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| OWASP SAMM | https://owaspsamm.org/ |
| NIST SP 800-218 (SSDF) | https://csrc.nist.gov/pubs/sp/800/218/final |
| SLSA | https://slsa.dev/ |
| CIS Benchmarks | https://www.cisecurity.org/cis-benchmarks |
| CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| EPSS | https://www.first.org/epss/ |

---

## 6. Avant d'ajouter un outil

- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Ce qu'il envoie à l'extérieur est connu et documenté
- [ ] Aucun téléversement du code client vers un service tiers
- [ ] Testé sur un système interne avant toute mission
- [ ] Ajouté à ce document, avec sa couverture et ses limites
