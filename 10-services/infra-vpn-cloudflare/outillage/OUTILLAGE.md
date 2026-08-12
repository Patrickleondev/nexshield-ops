# Outillage - Infrastructure, VPN et Cloudflare

**Version** : v0.1 · **Service** : `infra-vpn-cloudflare`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

C'est le seul service où **nous modifions des systèmes en production**. L'outil
qui mesure n'est pas dangereux ; l'outil qui applique l'est.

Trois interdits :

- **Aucun changement appliqué automatiquement en masse.** Un script de
  durcissement lancé sur un parc entier coupe le parc entier.
- **Aucun balayage du périmètre sans autorisation écrite** : ce serait un accès
  non autorisé au sens de la loi togolaise n° 2018-026.
- **Aucune action hors fenêtre convenue**, quelle que soit l'urgence apparente.

---

## 2. Socle retenu

### Mesurer

| Besoin | Outil | Licence |
|---|---|---|
| Découverte de services exposés | [nmap](https://nmap.org/) | NPSL |
| Recensement d'exposition | [ProjectDiscovery](https://github.com/projectdiscovery) (`naabu`, `httpx`, `dnsx`) | MIT |
| Failles connues | [nuclei](https://github.com/projectdiscovery/nuclei) | MIT |
| Écart CIS | [OpenSCAP](https://github.com/OpenSCAP/openscap) · [Lynis](https://github.com/CISOfy/lynis) | GPL |
| TLS | [testssl.sh](https://github.com/testssl/testssl.sh) | GPL-2.0 |
| Courriel | [DMARC](https://dmarc.org/) et vérificateurs publics | Service public |
| Active Directory | [PingCastle](https://github.com/netwrix/pingcastle) | Propriétaire, usage gratuit encadré |

### Appliquer

| Besoin | Outil | Licence |
|---|---|---|
| Accès distant | [WireGuard](https://www.wireguard.com/) | GPL-2.0 |
| Configuration reproductible | [Ansible](https://github.com/ansible/ansible) | GPL-3.0 |
| Bordure | Cloudflare, console et API | Service commercial |

**WireGuard est retenu** pour sa simplicité d'audit : une configuration courte,
lisible, sans surface superflue. Il ne fait pas de contrôle d'accès applicatif :
celui-ci se pose au-dessus, conformément à
[NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).

Ansible sert à rendre les changements **reproductibles et réversibles**, pas à
aller plus vite. Un rôle Ansible s'exécute sur un système de test avant tout
système de production.

---

## 3. Couverture réelle

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Découverte d'exposition | Oui, bien | Comparer au déclaré, juger la justification métier |
| Écart CIS | Oui | Trier ce qui casse, décider ce qu'on assume |
| TLS et courriel | Oui | Rien |
| Failles connues | Oui | Vérifier l'exploitabilité réelle |
| **Segmentation** | **Non** | Concevoir, observer, puis refuser |
| **Qui doit atteindre quoi** | **Non** | Le cœur d'une mission d'accès distant |
| **Décision d'assumer un écart** | **Non** | Le jugement, avec le client |
| **Retour arrière** | **Non** | Écrit à la main, avant le changement |

---

## 4. Ce que nous ne faisons pas

- **Aucun test de disponibilité ni de charge**, sauf clause explicite au RoE.
- **Aucun durcissement appliqué sans mesure préalable de l'écart** : sans point de
  départ, aucun progrès n'est démontrable.
- **Aucun changement groupé** pour gagner du temps : un lot, une fenêtre.
- **Aucune reprise de l'exploitation courante** : nous intervenons, nous
  documentons, nous remettons. L'exploitation reste au client, sauf contrat
  distinct.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| CIS Benchmarks | https://www.cisecurity.org/cis-benchmarks |
| ANSSI, publications | https://cyber.gouv.fr/publications |
| NIST SP 800-207 (Zero Trust) | https://csrc.nist.gov/pubs/sp/800/207/final |
| MITRE ATT&CK | https://attack.mitre.org/ |
| CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| CERT.tg | https://www.cert.tg/ |

---

## 6. Avant d'ajouter un outil

- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Distinguer clairement s'il **mesure** ou s'il **applique**
- [ ] Pour un outil qui applique : retour arrière possible et documenté
- [ ] Testé sur un système interne avant toute mission
- [ ] Ajouté à ce document, avec sa couverture et ses limites
