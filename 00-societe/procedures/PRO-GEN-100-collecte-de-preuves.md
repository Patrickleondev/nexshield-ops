# PRO-GEN-100 - Collecte et conservation des preuves

**Version** : v0.1 · **Service** : `pentest-audit` · **Phases PTES** : 2 à 6
**Responsable** : chaque testeur · **Sortant** : coffre chiffré + manifeste d'empreintes

---

## Pourquoi cette procédure existe

Une preuve mal collectée ne prouve rien. Une preuve mal conservée devient une
fuite de données client - c'est-à-dire la fin commerciale de la société.

Deux exigences opposées à tenir simultanément :

- **Prouver** ce qu'on avance, de façon reproductible et opposable ;
- **Ne pas détenir** les données du client plus que nécessaire.

---

## Ce qu'on collecte

| Type | Collecté | Remarque |
|---|---|---|
| Requête et réponse HTTP | Oui | Tronquées, sans données personnelles réelles |
| Capture d'écran | Oui | **Nettoyée avant enregistrement**, pas après |
| Sortie d'outil | Oui | Horodatée, avec la commande exacte |
| Journal de session | Oui | `script` ou équivalent, par phase |
| Extrait de base | Minimal | Une ligne anonymisée suffit à prouver l'accès |
| Dump complet | **Jamais** | Aucune justification acceptable |
| Identifiants découverts | **Jamais en clair** | Noter leur existence et leur emplacement |
| Données personnelles | **Jamais** | Constater, ne pas conserver |

**La règle** : la preuve doit établir l'accès, pas exploiter la donnée. Une
capture montrant l'en-tête d'une table et le nombre de lignes prouve autant qu'un
export complet, sans aucun des risques.

---

## Nettoyer une capture

À faire **avant** l'enregistrement, jamais après - une capture non nettoyée finit
toujours par circuler.

- [ ] Onglets du navigateur : aucun autre client visible
- [ ] Barre des tâches, notifications, horloge d'un autre fuseau
- [ ] Noms d'hôte et adresses IP hors périmètre
- [ ] Données personnelles réelles : noms, adresses, numéros, courriels
- [ ] Identifiants, jetons, cookies de session
- [ ] Chemins locaux révélant l'arborescence de votre poste

Masquer par un **aplat opaque**, jamais par un floutage : un floutage se
reconstruit.

---

## Nommage

```
<CLIENT>-<AAAA>-<NNN>-<nn>-<description>.<ext>
```

`ACME-2026-001-01-requete-injection.png`. Le préfixe est l'identifiant de la
vulnérabilité, ce qui permet de retrouver toutes les preuves d'une constatation
sans ouvrir un fichier.

---

## Conservation

Les preuves vivent dans le **coffre chiffré de mission**, jamais dans Git -
`SECURITY.md` §2. La CI bloque toute tentative.

1. Créer le conteneur chiffré au démarrage de la mission (VeraCrypt, `age`, ou
   équivalent), avec une clé propre à la mission.
2. La clé vit dans le gestionnaire de secrets de l'équipe, pas dans un message.
3. Aucune copie de travail hors du conteneur. Si vous en faites une, elle est
   supprimée le jour même.
4. Aucun envoi par messagerie, aucun service tiers non contractualisé.

### Manifeste d'empreintes

À chaque fin de journée de test :

```sh
find <coffre> -type f -exec sha256sum {} \; | sort -k2 > preuves.sha256
```

`preuves.sha256` est **versionné dans le dépôt de mission**. Il prouve, en cas de
contestation, que le rapport correspond aux preuves collectées - sans que les
preuves circulent.

---

## Journal des opérations

Chaque action offensive est consignée dans l'onglet **Journal** du classeur, en
temps réel et non de mémoire en fin de journée :

| Date | Heure | Opérateur | IP source | Actif | Action | Résultat | Autorisée par le RoE |

Cela vaut aussi pour les actions passant par un agent ou un serveur MCP :
« c'est l'outil qui l'a fait » n'est pas une ligne de journal recevable
(`30-outils/mcp/README.md`).

C'est cette feuille qui vous défend si le client attribue une indisponibilité à
vos tests.

---

## Destruction

À **J+90** après remise du rapport, sauf stipulation contraire du RoE :

1. Détruire le conteneur chiffré et sa clé.
2. Vérifier l'absence de copies : postes, sauvegardes, dossiers temporaires.
3. Émettre le **certificat de destruction** (`Modele-CERT-destruction-des-donnees.docx`)
   et le remettre au client.
4. Verser le certificat signé dans le dossier de mission.
5. Passer la mission au statut `clos`.

Le rapport et les documents contractuels sont conservés séparément, pour la durée
du contrat plus 3 ans.

---

## Critères de sortie

- [ ] Toutes les preuves sont dans le coffre chiffré
- [ ] Aucune copie hors coffre
- [ ] Captures nettoyées, vérifiées par un pair
- [ ] `preuves.sha256` à jour et versionné
- [ ] Journal des opérations complet et horodaté
- [ ] Date de destruction inscrite dans la fiche de mission
