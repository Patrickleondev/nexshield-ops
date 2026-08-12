# PRO-INFRA-100 - Durcissement et mise en œuvre

**Version** : v0.1 · **Service** : `infra-vpn-cloudflare` · **Phase** : exécution
**Responsable** : intervenant infrastructure · **Sortant** : configurations livrées + écart CIS mesuré

**Préalable bloquant** : `PRO-INFRA-001` close, sauvegardes restaurables vérifiées.

---

## Principe

**Un changement, une fenêtre, un retour arrière.**

On ne groupe pas les changements pour aller plus vite. Quand trois modifications
sont appliquées ensemble et qu'un service tombe, personne ne sait laquelle est en
cause, et le retour arrière annule aussi ce qui fonctionnait.

Ordre d'intervention, du plus rentable au plus coûteux :

| Rang | Action | Pourquoi ce rang |
|---|---|---|
| 1 | Réduire l'exposition | Ce qui n'est pas joignable ne s'attaque pas |
| 2 | Second facteur sur les accès | Coupe la majorité des compromissions d'identifiants |
| 3 | Segmentation | Limite la propagation, sans rien casser si bien faite |
| 4 | Durcissement des systèmes | Utile, mais c'est là que les choses cassent |
| 5 | Bordure et filtrage | Complète, ne remplace pas ce qui précède |
| 6 | Journalisation | Passe la main à `soc-ai-tools` |

---

## 1. Réduire l'exposition

Le meilleur durcissement est la suppression.

- [ ] Toute interface d'administration retirée d'Internet, sans exception
- [ ] Services exposés sans justification métier : fermés
- [ ] Ports ouverts « historiquement » : fermés après confirmation d'usage
- [ ] Environnements de test et de recette non exposés
- [ ] Certificats valides, couvrants, avec renouvellement automatique

> Avant de durcir un service exposé, demander s'il doit l'être. La moitié du
> temps, la réponse est non, et le durcissement devient inutile.

## 2. Accès distant et second facteur

- [ ] Second facteur sur tous les accès distants, **direction comprise**
- [ ] Second facteur sur les comptes à privilèges
- [ ] Accès donné **par application**, pas au réseau entier (NIST SP 800-207)
- [ ] Comptes de prestataires nominatifs et limités dans le temps
- [ ] Comptes de service : sans interface interactive, secrets en coffre
- [ ] Journalisation des connexions, envoyée hors du système journalisé

Le second facteur par message texte vaut mieux que rien, et moins qu'une clé ou
une application dédiée. Le dire, sans transformer le mieux en ennemi du bien : un
client qui n'a rien gagne davantage à passer au message texte tout de suite qu'à
attendre un projet de clés matérielles qui n'arrivera pas.

## 3. Segmentation

- [ ] Postes utilisateurs séparés des serveurs
- [ ] Serveurs séparés entre eux selon leur exposition
- [ ] Administration sur un chemin dédié
- [ ] Flux autorisés listés explicitement, le reste refusé par défaut
- [ ] Systèmes obsolètes isolés, à défaut d'être remplacés

La segmentation casse rarement quelque chose si elle est appliquée d'abord en
**observation** : journaliser les flux refusés pendant deux semaines avant de
refuser réellement.

## 4. Durcissement des systèmes

Référentiel : [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks),
au niveau arrêté au cadrage.

Méthode, sans raccourci possible :

1. Mesurer l'écart avant tout changement
2. Trier : ce qui est sans risque, ce qui demande un test, ce qui casse
3. Appliquer par lots, **une fenêtre par lot**
4. Vérifier le service après chaque lot
5. Re-mesurer l'écart

Les recommandations non appliquées sont **consignées avec leur motif**. Un écart
assumé et documenté vaut mieux qu'un durcissement qui casse la production.

## 5. Bordure et filtrage

Pour un périmètre Cloudflare ou équivalent :

- [ ] Origine non joignable directement : sinon le filtrage se contourne
- [ ] TLS de bout en bout, mode strict
- [ ] Règles de filtrage applicatif activées, **d'abord en observation**
- [ ] Limitation de débit sur les points sensibles : authentification,
      réinitialisation de mot de passe, formulaires
- [ ] Protection contre les robots réglée pour ne pas bloquer les usages légitimes
- [ ] En-têtes de sécurité posés à la bordure quand l'application ne les pose pas
- [ ] DNS : enregistrements obsolètes supprimés, SPF, DKIM et DMARC posés

**L'origine joignable en direct est le défaut le plus fréquent** : le client paye
une protection que l'attaquant contourne en s'adressant à l'adresse d'origine.

## 6. Journalisation

- [ ] Journaux envoyés hors du système qui les produit
- [ ] Rétention conforme au besoin, et son coût connu
- [ ] Horloges synchronisées
- [ ] Sources rendues exploitables pour `soc-ai-tools`

---

## Règles d'exécution

- **Une fenêtre par lot de changements.** Jamais de groupement pour gagner du temps.
- **Retour arrière écrit avant le changement**, jamais improvisé.
- **Vérification de service après chaque lot**, par le client ou avec lui.
- **Arrêt immédiat** dès qu'un critère d'arrêt est atteint, sans discussion.
- Aucune action hors fenêtre sans accord écrit.
- Journal des opérations horodaté : ce qui a été changé, quand, par qui.

---

## Critères de sortie

- [ ] Exposition réduite : aucune interface d'administration sur Internet
- [ ] Second facteur sur tous les accès distants et à privilèges, sans exception
- [ ] Accès distant donné par application, pas au réseau entier
- [ ] Segmentation appliquée après une phase d'observation
- [ ] Écart CIS mesuré avant et après, au niveau arrêté
- [ ] Recommandations non appliquées consignées avec leur motif
- [ ] Origine non joignable directement derrière la bordure
- [ ] Règles de filtrage passées en observation avant blocage
- [ ] SPF, DKIM et DMARC posés
- [ ] Journaux exportés hors des systèmes, horloges synchronisées
- [ ] Configurations remises au client, documentées et modifiables
- [ ] Journal des opérations complet
