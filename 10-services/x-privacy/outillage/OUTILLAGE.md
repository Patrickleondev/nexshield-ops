# Outillage - X-Privacy

**Version** : v0.1 · **Service** : `x-privacy`
**Dernière vérification des liens** : 12 août 2026

---

## 1. Règle préalable

**Ce service s'outille peu, et c'est normal.** La conformité se constate sur
pièce, par entretien et par test des droits. Aucun produit ne dit si une base
légale est défendable.

Les outils servent à deux choses seulement : **trouver les données que le client
a oubliées**, et **vérifier ce que son site fait réellement**.

Trois interdits, plus stricts ici que partout ailleurs :

- **Aucune base de données client dans nos systèmes.** Des extraits, jamais des
  copies. Nous serions sinon nous-mêmes un risque pour le client.
- **Aucune donnée personnelle réelle** dans un rapport, un exemple ou une capture.
- **Aucun outil qui téléverse des données vers un service tiers**, y compris les
  analyseurs en ligne : ce serait un transfert non fondé.

---

## 2. Socle retenu

| Besoin | Outil | Licence |
|---|---|---|
| Découverte de données personnelles | [Microsoft Presidio](https://github.com/microsoft/presidio) | MIT |
| Traceurs et cookies d'un site | [Blacklight](https://themarkup.org/blacklight) · outils du navigateur | Service public |
| En-têtes et transport | [testssl.sh](https://github.com/testssl/testssl.sh) | GPL-2.0 |
| Registre et analyses d'impact | Gabarits DOCX et XLSX de la société (`make juridique`, `make modeles`) | Interne |

Presidio s'exécute **localement**, sans appel externe : c'est la condition pour
qu'il soit utilisable ici. Il sert à repérer des données personnelles là où le
client n'en attendait pas - journaux, sauvegardes, environnements de test.

Le reste du travail se fait avec un tableur, des entretiens et des captures
d'écran de parcours réels.

---

## 3. Couverture réelle

| Domaine | Outillé | Manuel obligatoire |
|---|---|---|
| Découverte de données oubliées | Partiel | Interpréter, écarter les faux positifs |
| Traceurs d'un site | Oui | Rattacher chaque traceur à une base légale |
| Transport et chiffrement | Oui | Rien |
| **Base légale** | **Non** | Le cœur de la mission |
| **Minimisation** | **Non** | Champ par champ, contre la finalité |
| **Durées et suppression** | **Non** | Tester le mécanisme, pas lire la politique |
| **Droits des personnes** | **Non** | Les exercer réellement, mesurer les délais |
| **Analyses d'impact** | **Non** | Rédaction, du point de vue des personnes |

Sept lignes sur neuf sont manuelles. **Ce service se vend sur la compétence, pas
sur l'outillage** - c'est ce qui le rend défendable face à un logiciel de
conformité vendu en abonnement.

---

## 4. Ce que nous ne faisons pas

- **Aucun avis juridique.** Nous constatons des écarts et proposons des mesures.
  Sur une question de droit, renvoi vers un conseil.
- **Aucun dépôt de formalité à la place du client** auprès de l'IPDCP.
- **Aucun pronostic** sur la décision d'une autorité de contrôle.
- **Aucune certification.** Nous ne délivrons pas d'attestation de conformité.

Cette limite figure au contrat et se redit en restitution. Elle protège le client
autant que nous.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| RGPD, texte consolidé | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32016R0679 |
| Convention de Malabo | https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection |
| CERT.tg | https://www.cert.tg/ |
| CNIL, méthode d'analyse d'impact | https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd |
| ENISA, sécurité des données personnelles | https://www.enisa.europa.eu/ |

Loi togolaise n° 2019-014, décret n° 2020-111/PR et loi n° 2018-026 : références
et sources primaires dans
[`00-societe/juridique/CADRE-LEGAL.md`](../../../00-societe/juridique/CADRE-LEGAL.md).

---

## 6. Avant d'ajouter un outil

- [ ] S'exécute localement, sans transmettre de données à l'extérieur
- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Testé sur des données fictives avant toute mission
- [ ] Ajouté à ce document, avec sa couverture et ses limites
