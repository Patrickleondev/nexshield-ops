# Outillage

Nos outils, scripts et configurations. **Aucun secret, aucune licence, aucun
jeton**- voir `SECURITY.md`.

| Dossier | Contenu |
|---|---|
| `scripts/` | Scripts internes (création de mission, extraction de veille, conversions) |
| `sigma-rules/` | Nos règles de détection SIGMA - un actif réutilisable d'un client à l'autre |
| `wordlists/` | Listes personnalisées. Les grosses listes publiques ne se versionnent pas : un `sources.md` avec les liens suffit |
| `mcp/` | Configurations MCP (Burp, HexStrike, etc.) - **modèles uniquement**, jetons exclus |

## Règle d'usage

Les outils offensifs d'ici sont réservés aux **périmètres autorisés par écrit**.
Leur usage hors mission engage personnellement son auteur - voir `SECURITY.md` §6.

## Configurations MCP

Les serveurs MCP (Burp Suite, HexStrike-AI…) versionnent leur configuration sous
forme de `*.example.json`. La configuration réelle, avec ses jetons, reste locale
et n'entre jamais dans le dépôt.
