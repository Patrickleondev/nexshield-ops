# Outillage - SOC et outillage IA défensif

**Version** : v0.1 · **Service** : `soc-ai-tools`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

**On collecte avant d'écrire, on éprouve avant de livrer.** Aucun outil de cette
liste ne remplace ces deux règles.

Trois interdits :

- Aucune simulation d'attaque sans autorisation écrite et fenêtre convenue.
- Aucun extrait de journal client hors du coffre chiffré. Les journaux
  contiennent des données personnelles : loi togolaise n° 2019-014.
- Aucune règle livrée sans avoir été déclenchée volontairement au moins une fois.

---

## 2. Socle retenu

| Besoin | Outil | Licence |
|---|---|---|
| Écriture de règles | [SIGMA](https://github.com/SigmaHQ/sigma) | DRL / Apache-2.0 |
| Conversion vers un SIEM | [sigma-cli / pySigma](https://github.com/SigmaHQ/sigma-cli) | LGPL-3.0 |
| Simulation d'attaque | [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | MIT |
| Cartographie de couverture | [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) | Apache-2.0 |
| Détection sur terminal | [Wazuh](https://github.com/wazuh/wazuh) | GPL-2.0 |
| Détection réseau | [Suricata](https://github.com/OISF/suricata) | GPL-2.0 |
| Visibilité fine | [osquery](https://github.com/osquery/osquery) | GPL-2.0 / Apache-2.0 |
| Enrichissement de menace | [MISP](https://github.com/MISP/MISP) | AGPL-3.0 |

Le choix de SIGMA est structurant : la règle est écrite une fois et se convertit
vers la plateforme du client. Si le client change de SIEM, notre travail survit.
C'est un argument à donner au cadrage, pas à la restitution.

Atomic Red Team fournit des tests rattachés aux techniques ATT&CK : c'est
l'outil qui rend l'étape « déclencher l'attaque » réalisable en une journée
plutôt qu'en une semaine.

---

## 3. Couverture réelle

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Écriture de règles | Oui | La logique de détection elle-même |
| Simulation de technique | Oui, bien | Les variantes propres au contexte du client |
| Conversion vers le SIEM | Oui | Vérifier que la conversion n'a rien perdu |
| **Vérification des sources** | **Non** | Retrouver un événement réel, source par source |
| **Réglage du bruit** | **Non** | Décider ce qu'on exclut, et l'assumer par écrit |
| **Conduite à tenir** | **Non** | La fiche de réponse, sans laquelle l'alerte est du bruit |

Les trois dernières lignes sont ce qui distingue une prestation d'une
installation.

---

## 4. Sur l'IA défensive

Le nom du service annonce de l'outillage IA. Ce que nous en faisons, et ce que
nous n'en faisons pas :

**Usages retenus**

- Résumé d'un ensemble d'alertes corrélées, pour l'analyste
- Aide à la rédaction de la fiche de conduite à tenir
- Traduction d'une règle d'un format vers un autre, avec relecture humaine
- Recherche dans la documentation de menace

**Usages écartés, et pourquoi**

- **Décision automatique de blocage** : un faux positif traité par une machine
  coupe la production du client.
- **Envoi de journaux clients à un service tiers** : incompatible avec le NDA et
  avec la loi n° 2019-014.
- **Détection d'anomalie sans référence** : produit un volume d'alertes
  invérifiables, exactement ce que `PRO-SOC-100` interdit.

> Une alerte produite par un modèle et qu'aucun humain ne sait justifier ne se
> livre pas. La règle vaut aussi pour nous.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| MITRE ATT&CK | https://attack.mitre.org/ |
| MITRE D3FEND | https://d3fend.mitre.org/ |
| SIGMA | https://github.com/SigmaHQ/sigma |
| NIST SP 800-61r3 (réponse à incident) | https://csrc.nist.gov/pubs/sp/800/61/r3/final |
| CISA KEV | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| CERT.tg | https://www.cert.tg/ |

---

## 6. Avant d'ajouter un outil

- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Ce qu'il envoie à l'extérieur est connu et documenté
- [ ] Aucun journal client transmis à un service tiers
- [ ] Testé sur un système interne avant toute mission
- [ ] Ajouté à ce document, avec sa couverture et ses limites
