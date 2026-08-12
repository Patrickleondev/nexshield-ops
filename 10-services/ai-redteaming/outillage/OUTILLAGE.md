# Outillage - AI RedTeaming

**Version** : v0.1 · **Service** : `ai-redteaming`
**Dernière vérification des liens** : 12 août 2026

Ce document liste l'outillage retenu, ce que chaque outil couvre réellement, et
ce qu'il ne couvre pas. Il se lit avec [`PRO-AIRT-100`](../procedures/PRO-AIRT-100-tests-adverses.md).

---

## 1. Règle préalable

**Un scanner ne fait pas une mission.** Ces outils produisent du volume et de la
couverture ; ils ne produisent ni le raisonnement sur le périmètre, ni la
démonstration d'impact, qui sont ce que le client paye.

Trois interdits, valables sans exception :

- **Aucun outil n'est lancé avant la clôture de `PRO-AIRT-001`.** Chaque requête
  consomme le budget de jetons du client.
- **Aucun résultat d'outil n'entre au rapport sans avoir été rejoué à la main.**
  Les détecteurs automatiques produisent beaucoup de faux positifs sur des
  réponses de refus mal classées.
- **Aucun outil n'est pointé vers un système hors du périmètre signé**, y compris
  pour « essayer ».

---

## 2. Socle retenu

| Outil | Éditeur | Licence | Rôle chez nous |
|---|---|---|---|
| [garak](https://github.com/NVIDIA/garak) | NVIDIA | Apache-2.0 | Balayage large de première passe |
| [PyRIT](https://github.com/microsoft/PyRIT) | Microsoft | MIT | Attaques multi-tours orchestrées |
| [promptfoo](https://github.com/promptfoo/promptfoo) | promptfoo | MIT | Jeu rejouable et non-régression |
| [FuzzyAI](https://github.com/cyberark/FuzzyAI) | CyberArk | Apache-2.0 | Fuzzing de contournement |

> `Azure/PyRIT` est **archivé depuis mars 2026**. Le dépôt actif est
> `microsoft/PyRIT`. Toute documentation qui pointe encore vers `Azure/` est
> périmée.

### garak - première passe

« The LLM vulnerability scanner ». Sonde par familles : jailbreak, injection,
fuite de données, toxicité, désinformation.

Usage : **cadrer l'effort**, pas conclure. Il indique où insister.
Limite : il teste un modèle plus qu'une application. Il ne connaît ni les outils
de l'agent, ni les droits réels - donc rien de LLM06, l'essentiel de nos
constatations critiques.

### PyRIT - multi-tours

Orchestration d'attaques où un modèle adverse affine ses tentatives tour après
tour (crescendo, arbre d'attaques). C'est le seul du lot qui reproduit une
**charge progressive**, celle que `PRO-AIRT-100` demande sous LLM01.

Limite : consomme des jetons des deux côtés - attaquant et cible. À plafonner
strictement.

### promptfoo - le livrable durable

C'est l'outil qui porte notre **jeu de cas rejouable**. Il dispose d'un préréglage
OWASP LLM Top 10 :

```yaml
redteam:
  plugins:
    - owasp:llm
```

Cette seule ligne couvre LLM01 à LLM10. Le fichier de configuration se livre au
client : il pourra rejouer nos tests après correction, sans nous.

> **Le préréglage ne remplit pas la checklist de couverture.** Il exécute des
> sondes génériques ; nos scénarios d'abus propres au métier du client restent à
> écrire à la main.

### FuzzyAI - fuzzing

Génération automatique de variantes de contournement (ArtPrompt, PAIR,
algorithmes génétiques). Utile quand une catégorie résiste aux tentatives
manuelles et qu'il faut établir un **taux de réussite** sur beaucoup d'essais.

---

## 3. Couverture réelle par catégorie

Ce tableau est le plus important du document : il montre où l'outillage s'arrête.

| Réf. | Outillé | Manuel obligatoire |
|---|---|---|
| [LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | Oui, très bien | Injection **indirecte** par document métier réel |
| [LLM02](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/) | Partiel | Cloisonnement entre deux comptes de droits différents |
| [LLM03](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) | Non | Revue de provenance, serveurs MCP, dépendances |
| [LLM04](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/) | Non | Environnement isolé, persistance après redémarrage |
| [LLM05](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/) | Partiel | Chaînage vers l'application - relève de `secu-applicative` |
| [LLM06](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) | **Non** | Inventaire des outils, détournement, action irréversible |
| [LLM07](https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/) | Oui | Juger **ce que contient** le prompt fuité |
| [LLM08](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) | Non | Cloisonnement multi-locataires de la base vectorielle |
| [LLM09](https://genai.owasp.org/llmrisk/llm092025-misinformation/) | Partiel | Questions du domaine métier du client |
| [LLM10](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/) | Partiel | Coût réel d'une requête abusive, chiffré |

**Constat à retenir : LLM06 n'est couvert par aucun outil du marché**, parce
qu'aucun ne connaît les droits réels des outils de l'agent. C'est précisément la
catégorie qui produit les constatations critiques. Notre valeur est là, pas dans
le balayage.

---

## 4. Outils IA offensifs génériques

La veille (`40-veille/ai-redteaming.md`) contient de nombreux agents autonomes de
bug bounty et bundles de compétences. **Ils ne sont pas au socle**, pour trois
raisons :

1. **Confidentialité.** Ils transmettent le contexte client à un fournisseur
   tiers. Incompatible avec le NDA sans accord écrit explicite.
2. **Traçabilité.** `PRO-AIRT-100` exige un journal de chaque requête. Un agent
   autonome agit sans que nous puissions garantir ce journal.
3. **Périmètre.** Un agent qui décide seul de sa cible peut sortir du périmètre
   signé. C'est un risque pénal au regard de la loi togolaise 2018-026.

Usage autorisé : **en interne, sur nos propres systèmes, pour la montée en
compétence.** Jamais sur un système client sans clause dédiée au RoE.

Voir `30-outils/mcp/` pour les règles d'usage des serveurs MCP en mission.

---

## 5. Références normatives

| Ressource | Lien |
|---|---|
| OWASP Top 10 for LLM Applications 2025 | https://genai.owasp.org/llm-top-10/ |
| Version PDF citable | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf |
| MITRE ATLAS | https://atlas.mitre.org/ |
| NIST AI RMF 1.0 | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI 600-1 (profil IA générative) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |

Sources complètes : [`00-societe/smsi/REFERENCES.md`](../../../00-societe/smsi/REFERENCES.md).

---

## 6. Avant d'ajouter un outil

- [ ] Licence compatible avec un usage commercial, vérifiée dans le dépôt
- [ ] Dépôt actif : dernier commit de moins de six mois
- [ ] Ce qu'il envoie à l'extérieur est connu et documenté
- [ ] Testé sur un système interne avant toute mission
- [ ] Ajouté à ce document, avec sa couverture **et ses limites**
