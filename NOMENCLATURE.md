# Nomenclature - table de référence

Une seule page pour retrouver n'importe quel code. Les **règles** sont dans
[`CONVENTIONS.md`](CONVENTIONS.md) ; ceci en est l'aide-mémoire.

À afficher, à imprimer, à donner à tout nouvel arrivant.

---

## 1. Codes de service

| Code | Service | Dossier |
|---|---|---|
| `PT` | Pentest et audit | `10-services/pentest-audit/` |
| `AIRT` | AI RedTeaming | `10-services/ai-redteaming/` |
| `APP` | Sécurité applicative | `10-services/secu-applicative/` |
| `DSO` | DevSecOps | `10-services/devsecops/` |
| `SOC` | SOC et outillage IA défensif | `10-services/soc-ai-tools/` |
| `PRIV` | X-Privacy | `10-services/x-privacy/` |
| `SENS` | Sensibilisation | `10-services/sensibilisation/` |
| `INFRA` | Infrastructure, VPN, Cloudflare | `10-services/infra-vpn-cloudflare/` |
| `GEN` | Transverse, tous services | - |

---

## 2. Types de document

| Code | Document | Signé par |
|---|---|---|
| `NDA` | Accord de confidentialité | Les deux directions |
| `MSA` | Contrat-cadre de services | Les deux directions |
| `SOW` | Énoncé des travaux | Direction client |
| `ROE` | Règles d'engagement | Contact technique + direction |
| `AUTH` | Autorisation de test | Personne ayant autorité sur les actifs |
| `PROPO` | Proposition commerciale | - |
| `RAPPORT` | Rapport de mission | - |
| `SYNTH` | Synthèse exécutive | - |
| `RETEST` | Rapport de contre-vérification | - |
| `ATTEST` | Attestation de test | Prestataire |
| `CERT` | Certificat de destruction | Prestataire |
| `PROC` | Procédure interne | - |
| `POL` | Politique interne (SMSI) | - |
| `ADR` | Décision d'architecture ou de doctrine | - |

Les cinq premiers sont **bloquants** : aucune commande n'est lancée sans eux.

---

## 3. Formats de nommage

### Document daté

```
AAAAMMJJ-<CLIENT>-<TYPE>-<titre-en-minuscules>-v<X.Y>.<ext>
20260815-ACME-RAPPORT-pentest-webapp-v1.0.docx
```

`<CLIENT>` en majuscules, 3 à 8 lettres. `INTERNE` pour un document interne.
La date est celle de **publication de la version**, pas de création.

### Procédure interne

```
PRO-<SERVICE>-<NNN>-<titre>.md
PRO-PT-001-cadrage-et-perimetre.md
```

Numérotation par centaines : `001-099` cadrage · `100-199` exécution ·
`200-299` livraison · `300-399` clôture.

### Politique SMSI

```
POL-<NNN>-<titre>.md
POL-001-perimetre.md
```

### Mission

```
20-missions/<annee>/<CLIENT>-<type>-<nn>/
20-missions/2026/ACME-pentest-01/
```

### Vulnérabilité

```
<CLIENT>-<AAAA>-<NNN>
ACME-2026-001
```

Numérotation continue par client et par année, **tous types de missions
confondus** - pour suivre une vulnérabilité d'un pentest à sa contre-vérification.

### Preuve

```
<CLIENT>-<AAAA>-<NNN>-<nn>-<description>.<ext>
ACME-2026-001-01-requete-injection.png
```

### Branche Git

```
feat/<sujet>     fix/<sujet>      docs/<sujet>
legal/<sujet>    mission/<client>-<type>    chore/<sujet>
```

### Commit

```
<type>(<portée>): <résumé à l'impératif>
```

Types : `feat`, `fix`, `docs`, `chore`, `refactor`, `sec`, `legal`, `mission`.

---

## 4. Sévérité

Échelle unique, tous services confondus. **CVSS v4.0** pour le score technique.

| Sévérité | CVSS v4.0 | Délai recommandé | Couleur |
|---|---|---|---|
| Critique | 9.0 - 10.0 | < 72 h, notification pendant la mission | `#991B1B` |
| Élevée | 7.0 - 8.9 | 30 jours | `#C2410C` |
| Moyenne | 4.0 - 6.9 | 90 jours | `#A16207` |
| Faible | 0.1 - 3.9 | Prochain cycle de maintenance | `#0369A1` |
| Information | 0.0 | Aucune obligation | `#475569` |
| Corrigée | - | - | `#15803D` |

Ces couleurs ne changent jamais, dans aucun document. La couleur n'est jamais
seule porteuse d'information : la sévérité s'écrit toujours en toutes lettres.

---

## 5. Statuts

| Objet | Valeurs |
|---|---|
| **Mission** | `prospect` → `cadrage` → `signé` → `en-cours` → `livré` → `retest` → `clos` |
| **Vulnérabilité** | Ouverte · En cours · Corrigée · Acceptée · Faux positif |
| **Tâche** | À faire · En cours · Bloqué · En revue · Terminé |
| **Test (couverture)** | Exécuté · Non applicable · Non exécuté *(motif obligatoire)* |
| **Mesure SoA** | Non commencé · En cours · Mis en œuvre · Vérifié |
| **Article** | Brouillon → En relecture → Prêt → Publié |

---

## 6. Versions

| Version | Signification |
|---|---|
| `v0.1` à `v0.9` | Brouillon interne. **Ne sort jamais de la société.** |
| `v1.0` | Première version livrée au client |
| `v1.1`, `v1.2` | Correction après retour du client |
| `v2.0` | Refonte, ou nouvelle campagne sur le même périmètre |

**Une version livrée ne se modifie plus**, même pour une coquille. Une correction
produit une `v1.1`.

Le numéro vit à trois endroits qui doivent concorder : nom du fichier, page de
garde, tableau d'historique des versions.

### Version de doctrine

Distincte de la version du document. Un rapport porte les deux :
`v1.0` pour le rapport, `pentest-audit v1.2` pour la méthodologie appliquée.

| Incrément | Quand |
|---|---|
| MAJEUR | Change ce qui invalide une mission en cours |
| MINEUR | Nouvelle étape, nouveau test, nouvelle checklist |
| CORRECTIF | Clarification, coquille |

---

## 7. Séniorité et compétences

| Niveau | Autonomie |
|---|---|
| Junior | Toujours accompagné |
| Confirmé | Autonome sur périmètre cadré |
| Senior | Autonome, forme les juniors |
| Expert | Référent d'un domaine, définit la doctrine |

Matrice de compétences, notation par domaine :

| Note | Signification |
|---|---|
| 0 | Aucune notion |
| 1 | Notions |
| 2 | Autonome accompagné |
| 3 | Autonome |
| 4 | Référent, capable de former |

Un domaine noté ≥ 3 par **une seule personne** est une dépendance à un seul
homme, donc un risque signalé en orange dans le classeur de pilotage.

---

## 8. Référentiels cités dans un livrable

| Identifiant | Format | Exemple |
|---|---|---|
| OWASP WSTG | `WSTG-<CAT>-<NN>` | `WSTG-ATHN-01` |
| OWASP ASVS | `V<x.y.z>` | `V2.1.1` |
| OWASP Top 10 LLM | `LLM<NN>:2025` | `LLM01:2025` |
| MITRE ATT&CK | `T<NNNN>[.<NNN>]` | `T1190` |
| MITRE ATLAS | `AML.T<NNNN>` | `AML.T0051` |
| CWE | `CWE-<NNN>` | `CWE-89` |
| CVE | `CVE-<AAAA>-<NNNN+>` | `CVE-2026-1234` |
| ISO 27001 Annexe A | `A.<n>.<n>` | `A.8.24` |
| NIST SSDF | `<PO/PS/PW/RV>.<n>` | `PW.4` |
| CIS Benchmark | `<n>.<n>.<n>` | `5.2.4` |

**Un identifiant ne se cite jamais sans avoir ouvert sa page.** Un identifiant
inventé ou périmé détruit la crédibilité de tout le document. Sources :
[`00-societe/smsi/REFERENCES.md`](00-societe/smsi/REFERENCES.md).

---

## 9. Dossiers

Minuscules, tirets, sans accent, sans espace, sans majuscule.

Exception : les dossiers de mission, qui portent le code client en majuscules.

Les préfixes numériques des dossiers racine (`00-`, `10-`, `20-`…) fixent l'ordre
de lecture et sont espacés par dizaines pour pouvoir intercaler un domaine sans
tout renuméroter.

---

## 10. Renommer

**Toujours `git mv`**, jamais supprimer puis recréer - sinon l'historique est
perdu et la revue devient illisible. Une PR dédiée, jamais renommage et
modification dans le même commit.

**Ne se renomment jamais** : un document déjà livré, un dossier de mission close,
un identifiant de vulnérabilité.
