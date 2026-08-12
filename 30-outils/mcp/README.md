# Serveurs MCP

Le **Model Context Protocol** permet à un assistant IA de piloter des outils
(Burp, scanners, bases de connaissances). C'est puissant, et c'est exactement le
genre de puissance qui doit être encadrée par écrit avant d'être utilisée en
mission.

---

## 1. Règles d'usage - à lire avant de brancher quoi que ce soit

### Un MCP ne crée aucun droit

Brancher un MCP offensif ne change rien au cadre : **périmètre autorisé par
écrit, RoE, autorisation signée**. Un assistant qui propose de scanner un hôte
hors périmètre se refuse, comme on refuserait la même proposition d'un stagiaire.

### Aucun jeton dans le dépôt

Les configurations versionnées ici sont des `*.example.json`. La configuration
réelle vit **hors dépôt**, dans le fichier de configuration local du client MCP,
et ses secrets dans le gestionnaire de secrets de l'équipe.

### Données client et modèles distants

Un MCP branché sur un modèle **hébergé chez un tiers** envoie à ce tiers ce qu'il
lui transmet. Avant toute mission :

| Question | Exigence |
|---|---|
| Le modèle est-il hébergé chez un tiers ? | Si oui, le RoE doit l'autoriser explicitement |
| Des données client transitent-elles ? | Interdit sans clause contractuelle (`SECURITY.md` §1) |
| Le fournisseur s'entraîne-t-il sur les entrées ? | Vérifier et désactiver. Documenter la vérification. |
| Journalisation côté fournisseur ? | À mentionner au client avant la mission |

**Par défaut** : en mission client, on utilise un modèle **local** (Ollama,
llama.cpp) ou un fournisseur explicitement autorisé au contrat. Le confort ne
justifie pas d'exporter le périmètre d'un client chez un tiers.

### Traçabilité

Toute action offensive exécutée via un MCP est journalisée dans l'onglet
**Journal** du classeur de mission, au même titre qu'une commande tapée à la
main. « C'est l'IA qui l'a fait » n'est pas une ligne de journal recevable.

### Revue humaine

Aucune action **destructive ou modifiante** n'est déléguée à un agent sans
validation humaine explicite : exploitation menant à une écriture, changement de
configuration, envoi de courriel, création de compte.

---

## 2. Inventaire

À compléter avec vos configurations réelles.

| Serveur MCP | Usage | Service | Réseau | Statut |
|---|---|---|---|---|
| Burp Suite | Pilotage du proxy, rejeu de requêtes, scan | `secu-applicative` | Local | À documenter |
| HexStrike AI | Orchestration d'outils offensifs | `pentest-audit` | Local | À documenter |
| Recherche / veille | Interrogation de la veille et des CVE | Transverse | Sortant | À documenter |
| Base de connaissances | Accès à la doctrine du dépôt | Transverse | Local | À documenter |

Pour chaque serveur, une fiche `<nom>.md` dans ce dossier :

```markdown
# <Nom du serveur MCP>

- Dépôt / éditeur :
- Version épinglée :
- Ce qu'il permet de faire :
- Ce qu'il ne doit PAS faire en mission :
- Réseau : local / sortant vers <hôte>
- Secrets requis : <lesquels, et où ils vivent - jamais leur valeur>
- Autorisé pour les services : <…>
- Validation humaine obligatoire pour : <actions>
```

---

## 3. Modèle de configuration

Voir [`configuration.example.json`](configuration.example.json).

Les valeurs sensibles sont référencées par variable d'environnement, jamais
écrites en clair. Copier le fichier hors dépôt, le compléter, ne jamais le
recommitter.

---

## 4. Épinglage des versions

Un serveur MCP exécute du code sur votre poste, avec vos accès, pendant une
mission client. **Épinglez les versions.** Une mise à jour automatique en pleine
mission est un risque que vous ne pouvez pas expliquer au client.

- Version épinglée dans la configuration
- Empreinte du binaire ou du dépôt notée dans la fiche
- Mise à jour testée hors mission, sur un lab, avant adoption
