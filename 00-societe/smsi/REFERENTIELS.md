# Référentiels : choix, justification et implémentation de bout en bout

**Version** : v0.1 (brouillon) - **Statut** : à valider par les 5 associés

---

## 1. Le principe : une colonne vertébrale, pas huit doctrines

L'erreur classique d'un cabinet qui démarre est de choisir un référentiel par
service. Résultat au bout de six mois : huit vocabulaires, huit échelles de
sévérité, huit formats de rapport, et un client qui ne comprend pas qu'il parle à
la même société.

Notre architecture :

```
        ISO/IEC 27001:2022  ← notre SMSI : comment NOUS sommes gérés
                 │
        MITRE ATT&CK / ATLAS  ← langage commun de TOUS nos livrables
                 │
   ┌─────────────┼─────────────┬──────────────┐
 PTES/WSTG    OWASP LLM     NIST SSDF     RGPD/27701   ← exécution par métier
 ASVS/MASTG   MITRE ATLAS   SAMM/SLSA     NIST PF
```

- **ISO 27001** répond à « peut-on vous confier nos données ? »
- **ATT&CK / ATLAS** répond à « qu'avez-vous testé, exactement ? »
- Les référentiels métier répondent à « comment l'avez-vous testé ? »

---

## 2. Colonne vertébrale

### ISO/IEC 27001:2022 - notre système de management

**Ce que c'est** : la norme de management de la sécurité de l'information. Elle ne
décrit pas *comment* sécuriser, mais *comment piloter* la sécurité.

**Pourquoi celui-là plutôt qu'un autre**

1. **Commercialement exigible.** Dès que vous montez en gamme, un client sérieux
   vous demandera comment *vous* protégez les données de test qu'il vous confie.
   Sans réponse structurée, vous perdez les appels d'offres au profit d'un
   concurrent certifié - quelle que soit votre supériorité technique.
2. **Reconnu des deux côtés.** En Afrique de l'Ouest comme en Europe. Un
   référentiel purement américain (ex. SOC 2) parlerait moins à vos clients locaux.
3. **Coût d'entrée nul.** Vous n'avez pas besoin d'être certifiés maintenant. Vous
   avez besoin d'**écrire vos procédures au format 27001** dès aujourd'hui, pour
   que la certification dans 2-3 ans soit une formalité et non une refonte.
   Écrire une procédure « au format 27001 » ne coûte rien de plus que de
   l'écrire mal.
4. **Ça structure le dépôt.** L'Annexe A donne directement la liste des politiques
   à écrire dans `00-societe/smsi/` - vous n'avez pas à inventer le sommaire.

**Ce qu'on fait concrètement, dans l'ordre**

| Étape | Livrable | Où |
|---|---|---|
| 1 | Périmètre du SMSI (quelles activités, quels actifs) | `00-societe/smsi/POL-001-perimetre.md` |
| 2 | Analyse de risques + plan de traitement | `00-societe/smsi/risques/` |
| 3 | Déclaration d'applicabilité (SoA) - les 93 mesures de l'Annexe A | `00-societe/smsi/SoA.md` |
| 4 | Politiques : accès, cryptographie, incidents, fournisseurs, RH | `00-societe/smsi/POL-*.md` |
| 5 | Preuves d'application (revues d'accès, registre d'incidents) | `00-societe/smsi/registres/` |
| 6 | Audit interne, revue de direction | annuel |

> **Ne visez pas la certification avant d'avoir 8 à 10 missions livrées.** Avant
> ça, vous certifieriez un système que vous n'avez pas encore éprouvé.

### MITRE ATT&CK - le langage commun

Toutes nos constatations, dans **tous** les services, portent un identifiant
ATT&CK (ou ATLAS pour l'IA).

**L'avantage, et c'est un vrai argument commercial** : un rapport de pentest qui
mappe sur ATT&CK est directement injectable dans le SIEM du client. Il ne reçoit
pas une liste de failles, il reçoit une **liste de détections à écrire**. Nos
concurrents livrent des listes de CVE ; nous livrons de quoi agir. Et ça crée
mécaniquement la vente suivante (le service SOC).

---

## 3. Référentiels d'exécution par service

### 3.1 Pentest & audit - **PTES + OWASP WSTG + NIST SP 800-115**

| Référentiel | Rôle | Avantage décisif |
|---|---|---|
| **PTES** | Structure la mission en 7 phases | Les 7 phases deviennent les 7 sections du rapport. Le rapport s'écrit tout seul, et il est identique d'un consultant à l'autre. |
| **OWASP WSTG** | Catalogue de tests web avec identifiants | Prouve la **couverture**. « Nous avons exécuté 94 des 118 tests WSTG applicables » est vérifiable ; « nous avons testé l'application » ne l'est pas. |
| **NIST SP 800-115** | Cadre technique de référence | Gratuit, citable, autorité reconnue. Sert de caution quand un client demande « sur quelle base ? ». |

Ajouts : **OSSTMM** si un client exige une métrique de sécurité chiffrée,
**TIBER-EU** comme modèle si vous montez un jour une offre red team pilotée par
le renseignement (secteur bancaire).

### 3.2 AI RedTeaming - **OWASP Top 10 LLM + MITRE ATLAS + NIST AI RMF** C'est votre différenciateur. Personne n'est structuré là-dessus dans la région.

| Référentiel | Rôle | Avantage décisif |
|---|---|---|
| **OWASP Top 10 for LLM Applications** | Taxonomie des risques (injection de prompt, empoisonnement, fuite de données…) | Le seul vocabulaire que le marché commence à reconnaître. Rend l'offre lisible pour un acheteur non spécialiste. |
| **MITRE ATLAS** | TTP adverses contre les systèmes IA | Pendant exact d'ATT&CK → **cohérent avec la colonne vertébrale**. Un client qui connaît ATT&CK comprend ATLAS en dix minutes. |
| **NIST AI RMF 1.0**+ profil GenAI | Gouvernance du risque IA | Prépare le client à l'**EU AI Act**. Vend une offre de conformité en aval du test technique. |
| **ISO/IEC 42001** | Management de l'IA | À garder en réserve : offre « gouvernance IA » quand le marché mûrira. |

### 3.3 Sécurité applicative - **OWASP ASVS + MASTG****L'avantage d'ASVS est commercial avant d'être technique** : il transforme un
avis d'expert en **niveau d'assurance mesurable**. « Votre application satisfait
78 % des exigences ASVS niveau 2 » se contractualise, se met dans un appel
d'offres, et se re-mesure l'année suivante - donc se **refacture**.

ASVS L1 = applications non critiques · L2 = défaut recommandé · L3 = critique
(santé, finance, infrastructures).

### 3.4 DevSecOps - **NIST SSDF (SP 800-218) + OWASP SAMM + SLSA**

- **SSDF** : le *quoi* - 42 pratiques de développement sécurisé.
- **SAMM** : le *combien* - maturité par domaine sur 3 niveaux.
- **SLSA** : le *comment* pour la chaîne d'approvisionnement (niveaux 1 à 3).

**Avantage** : SAMM produit un score de maturité. Un score se **re-mesure**, donc
crée du revenu récurrent (audit de maturité annuel) au lieu d'une mission unique.
C'est le service qui stabilise votre trésorerie.

### 3.5 SOC AI Tools - **ATT&CK + D3FEND + SIGMA + NIST SP 800-61**

- **D3FEND** : le pendant défensif d'ATT&CK - chaque technique offensive a sa contre-mesure.
- **SIGMA** : format de règle **portable**, indépendant du SIEM. Vous écrivez une
  fois, ça se compile vers Splunk, Elastic, Wazuh, Sentinel. Vos règles deviennent
  un actif réutilisable (`30-outils/sigma-rules/`) au lieu d'être perdues chez un client.
- **NIST SP 800-61** : cycle de réponse à incident.
- **STIX/TAXII + OpenCTI** pour le renseignement sur les menaces.

### 3.6 X-Privacy - **RGPD + ISO/IEC 27701 + NIST Privacy Framework**

- **RGPD** : la référence mondiale de fait, même hors UE. Tout client avec des
  utilisateurs ou des partenaires européens y est soumis.
- **ISO 27701** : extension « vie privée » d'ISO 27001 → **s'emboîte directement
  dans votre colonne vertébrale**, sans second système à maintenir.
- **NIST Privacy Framework** : pour les clients allergiques au vocabulaire juridique.

> **Volet local - Togo.** Le cadre applicable est désormais établi :
> **loi n° 2019-014 du 29 octobre 2019** (données personnelles), autorité de
> contrôle **IPDCP** (décret n° 2020-111/PR), et **Convention de Malabo**
> ratifiée par le Togo, entrée en vigueur le 8 juin 2023. S'y ajoute, pour notre
> propre activité, la **loi n° 2018-026** sur la cybersécurité et la
> cybercriminalité, qui fonde l'exigence d'autorisation écrite.
> Analyse complète : [`../juridique/CADRE-LEGAL.md`](../juridique/CADRE-LEGAL.md).

### 3.7 Sensibilisation - **NIST SP 800-50r1 + ENISA****Avantage de 800-50** : il impose de **mesurer l'efficacité** du programme (taux
de clic sur simulation de phishing, taux de signalement). Une mesure justifie une
reconduction annuelle. Une sensibilisation non mesurée ne se vend qu'une fois.

Rattachement ISO 27001 : mesure **A.6.3**- vos livrables servent directement de
preuve à l'audit du client.

### 3.8 Infrastructure, VPN & Cloudflare - **CIS Benchmarks + ANSSI**

- **CIS Benchmarks** : scorables automatiquement (CIS-CAT, Lynis, OpenSCAP) → un
  audit de durcissement se produit en heures, pas en jours. Excellente marge.
- **Guides ANSSI** : crédibilité en environnement francophone, et référence
  attendue par les administrations.
- **CIS Controls v8** comme grille de maturité d'ensemble pour les PME.

---

## 4. Implémentation de bout en bout

Un référentiel non implémenté est un logo sur une plaquette. Voici la chaîne qui
le rend réel - chaque maillon est vérifiable dans le dépôt.

| Étape | Ce qui matérialise le référentiel | Contrôle |
|---|---|---|
| **Avant-vente** | La proposition cite le référentiel et le niveau visé (ex. ASVS L2) | Gabarit `PROPO` : champ obligatoire |
| **Cadrage** | Le RoE liste les identifiants de tests applicables au périmètre | Revue `legal/` à 2 |
| **Exécution** | Chaque checklist est structurée par identifiant du référentiel | `10-services/*/checklists/` |
| **Constatation** | Chaque vulnérabilité porte WSTG/ASVS + ATT&CK/ATLAS + CWE + CVSS v4.0 | `CONVENTIONS.md` ; contrôlé en revue de rapport |
| **Rapport** | Une annexe « couverture » liste les tests exécutés / non applicables / non exécutés **et pourquoi** | Gabarit de rapport : section non supprimable |
| **Livraison** | Le rapport indique la **version de doctrine** utilisée | `CONTRIBUTING.md` §5 |
| **Clôture** | Le RETEX remonte les manques du référentiel | `20-missions/*/retex.md` |
| **Amélioration** | Le manque devient une PR sur la méthodologie → nouvelle version | `CHANGELOG.md` |

La dernière ligne est la plus importante : **c'est la boucle de rétroaction**.
Sans elle, votre méthodologie sera périmée dans un an. Le RETEX de fin de mission
est obligatoire, y compris - surtout - quand la mission s'est bien passée.

### Le piège à éviter

Un référentiel est un **plancher, pas un plafond**. Une mission qui n'exécute que
la checklist est une mission médiocre : la valeur que vous facturez est dans ce
que la checklist ne prévoit pas (logique métier, enchaînement de failles mineures
en compromission majeure). La checklist garantit que **rien de connu n'est
oublié**; elle ne remplace pas le talent offensif.

C'est pourquoi chaque gabarit de rapport contient une section
**« Constatations hors référentiel »**. Si elle est vide sur plusieurs missions
d'affilée, le problème n'est pas dans le référentiel.

---

Toutes les sources officielles des référentiels cités : [`REFERENCES.md`](REFERENCES.md).

---

## 5. Feuille de route

| Horizon | Objectif |
|---|---|
| **0-3 mois** | Doctrine v1.0 des 3 services vendables tout de suite : `pentest-audit`, `secu-applicative`, `ai-redteaming`. Pack juridique relu par un juriste. |
| **3-6 mois** | Premières missions livrées. RETEX → doctrine v1.1. Rédaction des politiques SMSI de base. |
| **6-12 mois** | `devsecops` et `soc-ai-tools` en v1.0. Analyse de risques + SoA ISO 27001. |
| **12-24 mois** | Audit interne, revue de direction. `x-privacy` aligné sur le droit local définitif. |
| **24-36 mois** | Certification ISO 27001 si le marché la réclame - pas avant. |
