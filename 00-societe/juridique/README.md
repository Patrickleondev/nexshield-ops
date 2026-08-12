# Juridique

**Aucun de ces modèles n'a été relu par un conseil juridique.** Ce sont des bases
de travail structurées selon les pratiques du métier, à faire valider avant tout
usage réel — en particulier les clauses de responsabilité, de propriété
intellectuelle, d'assurance et de droit applicable.

Le cadre légal applicable est analysé dans [`CADRE-LEGAL.md`](CADRE-LEGAL.md)
(Togo, Afrique, Union européenne), avec ses sources primaires.

---

## Les modèles sont des DOCX, pas des Markdown

Un contrat se signe, s'annote, circule entre juristes et se classe. Il est donc
produit en **DOCX**, à la charte, avec page de garde, sommaire, blocs de
signature et historique des versions.

```sh
make juridique      # régénère le pack dans 90-templates/build/juridique/
```

La source est le script [`../../30-outils/scripts/generer_juridique.py`](../../30-outils/scripts/generer_juridique.py).
On modifie le script en PR — jamais le DOCX généré : sinon la modification est
perdue à la régénération suivante, et elle n'a pas été relue.

---

## Le pack minimal avant toute mission

| # | Document | Quand | Signé par | Bloquant |
|---|---|---|---|---|
| 1 | **NDA** — accord de confidentialité | Avant la première réunion technique | Les deux directions | Oui |
| 2 | **MSA** — contrat-cadre | Une fois, puis réutilisé | Les deux directions | Oui |
| 3 | **SOW** — énoncé des travaux | Par mission | Direction client | Oui |
| 4 | **ROE** — règles d'engagement | Par mission, avant exécution | Contact technique + direction | Oui |
| 5 | **AUTH** — autorisation de test | Par mission | Personne ayant autorité sur les actifs | Oui |
| 6 | **ATTEST** — attestation de test | À la livraison | Prestataire | Non |
| 7 | **CERT** — certificat de destruction | À J+90 | Prestataire | Non |

Les cinq premiers sont bloquants : **aucune commande n'est lancée tant qu'ils ne
sont pas signés.** La loi togolaise n° 2018-026 pénalise l'accès frauduleux à un
système d'information ; l'autorisation écrite est ce qui rend nos tests licites.

---

## Structure du RoE

Le modèle suit le standard **PTES**, section « Pre-engagement Interactions »,
qui normalise ce qu'un RoE doit contenir : chronologie, lieux, traitement des
données sensibles, gestion des preuves, fréquence des réunions de suivi, heures
de test, protocole de blocage, autorisation écrite, et approbations des tiers.

Nous n'avons pas inventé cette structure : c'est celle que le métier utilise.
Source : [pentest-standard.readthedocs.io](https://pentest-standard.readthedocs.io/en/latest/preengagement_interactions.html).

Deux sections souvent oubliées, et qui coûtent cher :

- **Le protocole de blocage** (« shunning »). Si le client bloque vos adresses
  sans prévenir, vous perdez des journées de test sans comprendre pourquoi.
- **Les approbations de tiers.** Un actif hébergé chez Cloudflare, AWS ou un
  hébergeur local relève des conditions de ce fournisseur. C'est au client de
  les obtenir, et c'est la cause n° 1 de report de démarrage.

---

## Documents distincts, lecteurs distincts

| Document | Contient des vulnérabilités | Peut circuler |
|---|---|---|
| Rapport technique | Oui | Non — destinataires nommés uniquement |
| Synthèse exécutive | Partiellement | Direction du client |
| **Attestation de test** | **Non** | **Oui** — assureur, auditeur, appel d'offres |

L'attestation existe précisément pour que le client puisse prouver qu'un test a
eu lieu sans exposer ses failles. C'est un document que peu de concurrents
fournissent spontanément.

---

## Reste à faire

- [ ] Faire relire l'intégralité du pack par un juriste togolais
- [ ] Fixer le plafond de responsabilité du MSA, cohérent avec l'assurance RC pro
- [ ] Souscrire l'assurance RC professionnelle (préalable au point précédent)
- [ ] Vérifier auprès de l'IPDCP le régime applicable à notre activité
- [ ] Version anglaise du pack pour les clients internationaux
