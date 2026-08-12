# Politique de sécurité du dépôt

Nous vendons de la sécurité. Une fuite depuis ce dépôt ne serait pas un incident,
ce serait la **fin commerciale de la société**. Cette politique n'est pas négociable.

---

## 1. Ce qui n'entre JAMAIS dans ce dépôt

### Secrets

- Mots de passe, jetons d'API, clés privées (`*.key`, `*.pem`, `*.p12`, `*.pfx`, `id_rsa`).
- Fichiers `.env`, `secrets.*`, `credentials`, `.creds`, `*token*.json`.
- Clés cloud (AWS, GCP, Azure), jetons Cloudflare, licences Burp, clés d'API IA
  (Anthropic, OpenAI…), jetons de bug bounty.

### Données de mission

- **Preuves brutes** : captures d'écran de vulnérabilités, sorties d'outils
  (Nmap, Nuclei, Burp), dumps de base, exports de session, enregistrements.
- Identifiants de test fournis par le client (comptes, VPN, jetons).
- Périmètres non anonymisés : IP publiques réelles, sous-domaines, noms de serveurs.
- Toute donnée à caractère personnel appartenant au client ou à ses utilisateurs.

### Divers

- Binaires lourds hors Git LFS, exports de navigateur bruts, archives de node_modules.

---

## 2. Où vivent les preuves

Les preuves d'une mission vivent dans le **coffre chiffré de mission**, jamais dans Git.

| Élément | Emplacement | Rétention |
|---|---|---|
| Preuves brutes, captures, sorties d'outils | Coffre chiffré (VeraCrypt / age / SOPS), stockage dédié | 90 jours après livraison, puis destruction |
| Identifiants client | Gestionnaire de secrets de l'équipe | Révoqués à la fin de mission |
| Rapport final (Markdown + PDF signé) | `20-missions/<annee>/<client>-<mission>/` | Durée du contrat + 3 ans |
| Empreintes SHA-256 des preuves | `20-missions/.../preuves.sha256` | Idem rapport |

Le dépôt ne garde que le **rapport** et le **manifeste d'empreintes**. Ce manifeste
prouve, en cas de litige, que le rapport correspond bien aux preuves collectées —
sans que les preuves elles-mêmes ne circulent.

**Destruction** : à J+90, la suppression du coffre est actée par un
`certificat-destruction.md` signé, versé dans le dossier de mission.

---

## 3. Garde-fous techniques

Installés par `make setup` :

- **gitleaks** en hook `pre-commit` **et** en CI (bloquant sur PR).
- `.gitignore` couvrant les motifs de secrets et de preuves.
- **SOPS** (chiffrement `age`) pour le peu de données sensibles qui doivent vivre
  dans le dépôt (contacts d'urgence RoE, périmètres IP) : fichiers `*.enc.yml`.
- `make secrets-scan` avant toute PR.

Un garde-fou technique ne remplace pas la relecture. **Vous** êtes le contrôle final.

---

## 4. Accès

- Dépôt **privé**, branche `main` protégée.
- **MFA obligatoire** sur le compte GitHub de chaque membre — sans exception.
- Principe du moindre privilège : accès en écriture pour les 5 membres, accès
  lecture seule pour tout prestataire ou stagiaire.
- Revue des accès **trimestrielle**, consignée dans `00-societe/smsi/`.
- Départ d'un membre : accès révoqués **le jour même**, secrets partagés tournés
  dans les 48 h.

---

## 5. Si un secret a fuité

1. **Le considérer comme compromis.** Le révoquer / le changer immédiatement —
   avant même de nettoyer l'historique.
2. Purger l'historique (`git filter-repo`), forcer la réécriture, prévenir tous
   les membres de re-cloner.
3. Ouvrir une fiche d'incident dans `00-societe/smsi/incidents/`.
4. Si le secret appartenait à un client : **le notifier**, dans les délais prévus
   au contrat. Ne jamais dissimuler.

---

## 6. Éthique et cadre légal

Aucun test, aucun scan, aucune reconnaissance — même passive — sans **autorisation
écrite signée**par une personne ayant autorité sur les actifs visés
(gabarit `Modele-AUTH-autorisation-de-test.docx`, produit par `make juridique`).

Cette règle s'applique aussi aux « petits essais rapides », aux démonstrations
commerciales et à la reconnaissance OSINT avant-vente. Il n'y a pas d'exception.

Les outils offensifs de `30-outils/` sont réservés aux périmètres autorisés.
Leur usage hors mission engage personnellement son auteur.
