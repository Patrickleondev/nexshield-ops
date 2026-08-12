# Notes de l'orateur - présentation du dépôt aux associés

**Version** : v0.1 · **Support** : `nexshield_presentation.pptx`, 12 diapositives
**Durée visée** : 45 minutes de présentation, 30 minutes de discussion

Ce document accompagne le support. Il donne, pour chaque diapositive, **ce qu'il
faut dire** et non ce qui est affiché. Une diapositive lue à voix haute est une
diapositive perdue.

---

## Avant de commencer

**Trois choses à préparer.**

1. Le dépôt ouvert sur un second écran. À plusieurs moments, il vaut mieux
   montrer le fichier que la diapositive.
2. La question de clôture écrite au tableau dès le début : *« validons-nous les
   trois règles ? »* Elle oriente toute la séance.
3. Savoir qu'on ne finira pas tout. Si le temps manque, on saute les
   diapositives 08 et 09, jamais la 10.

**Le piège de cette réunion** : passer une heure à décrire une arborescence.
Personne ne retient une arborescence. Ce qu'on veut, c'est que chacun reparte
avec un point d'entrée et une action.

---

## 01 - Couverture

**Temps** : 1 minute.

Une seule phrase à faire passer : **le dépôt n'est pas du code, c'est notre
mémoire opérationnelle.**

Dire pourquoi la réunion existe : nous sommes cinq, nous allons vendre les mêmes
services, et il faut que le client reçoive la même qualité quel que soit celui
d'entre nous qui exécute.

Ne pas commencer par l'arborescence. Ne pas commencer par les outils.

---

## 02 - Le point de départ

**Temps** : 4 minutes. **C'est la diapositive qui décide de l'attention du
reste de la séance.**

Ne pas lire les cinq points. En raconter **un seul**, concrètement :

> « Imaginons que Laurent cadre une mission chez un client, tombe malade, et que
> Winero reprenne. Sans doctrine écrite : quel périmètre ? quelle sévérité pour
> telle faille ? où sont les preuves ? Le client s'en aperçoit, et c'est là qu'on
> perd un client. »

Puis la phrase de bascule : **le dépôt transforme les décisions qu'on prend
chaque fois en règles qu'on prend une fois.**

Anticiper l'objection qui vient toujours : *« on n'est que cinq, on se parle ».*
Réponse : « aujourd'hui oui. Le jour où un sixième arrive, ou le jour où un
client conteste un test six mois après, ce qui n'est pas écrit n'existe pas. »

---

## 03 - La réponse en une image

**Temps** : 4 minutes.

Trois couches, trois questions. Le faire dire par l'image, pas par la voix.

- **ISO 27001** répond à : *peut-on nous confier des données ?*
- **ATT&CK** répond à : *qu'avez-vous testé, exactement ?*
- **Les référentiels métier** répondent à : *comment l'avez-vous testé ?*

Insister sur ATT&CK, parce que c'est notre argument de vente le plus concret :
un rapport rattaché à ATT&CK est directement exploitable par l'équipe de
détection du client. La plupart de nos concurrents livrent une liste de failles ;
nous livrons quelque chose qui se branche sur leur défense.

Pour Herbert et Dora : préciser que ces trois noms reviendront dans tous les
appels d'offres. Les connaître, c'est parler la langue du client.

---

## 04 - Le dépôt en un coup d'œil

**Temps** : 3 minutes. Aller vite, c'est du repérage.

Une seule règle à retenir, et c'est celle qui évite le désordre :

> **Si on écrit deux fois la même chose dans deux missions, cela appartient à
> `10-services/`.**

Montrer la structure identique des huit services : `methodologie/`,
`procedures/`, `checklists/`, `livrables/`, `juridique/`, `outillage/`.
**Qui connaît un service sait naviguer dans les sept autres.** C'est le point
qui rassure les non-techniques.

---

## 05 - Une carte de démarrage

**Temps** : 5 minutes. C'est la diapositive la plus utile pour l'audience.

Ne pas la commenter en bloc. **Nommer chaque personne et s'arrêter une seconde**
sur ses trois documents.

Puis le principe, qui est le vrai sujet :

> Une responsabilité a un **titulaire** et un **suppléant**. Un domaine tenu par
> une seule personne est un risque, pas une force.

C'est le moment de dire clairement que les titulaires affichés sont une
proposition, pas une décision. La décision se prend à la diapositive 11.

---

## 06 - Le cycle d'une mission

**Temps** : 6 minutes.

Dérouler les dix étapes rapidement, puis **s'arrêter longuement sur les deux
verrous**, parce que ce sont eux qui protègent la société.

- **Pas de NDA ? On ne parle pas du système.** Même en réunion, même
  informellement. La discussion reste commerciale.
- **Pas d'autorisation signée ? Aucune commande.** Y compris un `whois`, y
  compris une recherche de sous-domaines, y compris « juste pour préparer le
  devis ».

La phrase à faire retenir : **la reconnaissance passive est déjà un acte de
collecte.** C'est contre-intuitif et c'est exactement là que les gens se
trompent de bonne foi.

Renvoyer vers `PRO-GEN-001` pour les gestes Git : une branche par mission,
nommée par client **et par service**.

---

## 07 - Le cadre qui rend le test licite

**Temps** : 5 minutes. **Diapositive à ne jamais sauter.**

La loi togolaise n° 2018-026 pénalise l'accès frauduleux à un système
d'information. Ce qui nous sépare du délit n'est pas notre intention, ni notre
compétence : **c'est un papier signé par quelqu'un qui a autorité sur les
actifs.**

Les quatre mentions d'une autorisation valable : les systèmes, les personnes, la
période, la conservation. Insister sur « les personnes » : une autorisation qui
ne nomme pas les testeurs ne protège personne.

**Être honnête sur l'état** : notre pack juridique est en v0.1 et n'a pas été
relu par un juriste togolais. C'est écrit sur la diapositive, il faut le dire à
voix haute. Un associé qui découvre cette limite plus tard perdra confiance dans
tout le reste.

---

## 08 - Les documents que nous produisons

**Temps** : 3 minutes. Sautable si le temps manque.

Le message : **la qualité naît dans le gabarit, pas au moment de rendre le
rapport.** Une charte unique, des structures réutilisables, et le RETEX qui
referme la boucle.

Montrer un DOCX généré plutôt que de le décrire. Trente secondes de démonstration
valent mieux que trois minutes d'explication.

---

## 09 - Le mode de collaboration

**Temps** : 4 minutes. Adapter au public : Dora et Herbert ne pratiquent pas Git.

Ne pas expliquer Git. Expliquer **le principe** : rien n'entre dans la doctrine
commune sans qu'une deuxième personne l'ait lu.

Les seuils à retenir :

- Documentation : **un** relecteur
- Juridique et rapport client : **deux**
- Un rapport client ne part **jamais** avant la fusion de sa demande

Et la règle qui compte le plus, à dire lentement :

> **N'importe qui peut arrêter une mission. On arrête d'abord, on discute
> après.**

Personne ne doit avoir à demander la permission d'arrêter. C'est ce qui évite
qu'un incident devienne une catastrophe.

---

## 10 - Les trois règles non négociables

**Temps** : 8 minutes. **C'est le cœur de la réunion.**

Les énoncer une par une, et **demander un accord explicite à chacun**. Pas un
hochement de tête collectif : faire dire oui, personne par personne. Une règle
acceptée en silence n'est pas acceptée.

1. **Aucune action technique sans autorisation écrite.** Y compris avant-vente.
2. **Aucune preuve brute ni secret dans le dépôt.** Coffre chiffré, destruction
   à J+90.
3. **Personne ne publie son propre travail sans relecture.** Y compris le
   fondateur - le dire de soi-même désamorce l'objection.

Laisser la discussion avoir lieu. Si quelqu'un conteste, c'est le bon moment :
mieux vaut un désaccord ici qu'un contournement dans six mois.

---

## 11 - Décider et agir

**Temps** : 6 minutes.

**Première partie, l'état réel.** Ne rien enjoliver.

Ce qui est vrai aujourd'hui : les huit services ont leur socle écrit - cadrage,
exécution, checklist, outillage. **Mais tout est en `v0.1` : rien n'a été éprouvé
sur une mission réelle**, et le pack juridique n'a pas été relu par un juriste.

Le dire ainsi protège la crédibilité de tout le reste. Une équipe à qui on
annonce une doctrine achevée découvrira l'écart au premier client.

**Seconde partie, les actions.** Chaque ligne porte une date et un nom. Vérifier
en séance que chaque personne nommée accepte sa ligne. Une action sans titulaire
présent est une action qui ne se fera pas.

Conclure par la phrase du support : **la prochaine preuve d'adoption n'est pas
un discours, c'est une première demande de fusion relue.**

---

## Questions qui vont être posées

Les préparer, parce qu'elles arriveront.

| Question | Réponse à donner |
|---|---|
| « Tout ça pour cinq personnes, ce n'est pas trop ? » | C'est écrit une fois et réutilisé à chaque mission. Le coût est aujourd'hui, le gain est à chaque client. |
| « On va vraiment tout relire ? » | Oui. Un rapport faux coûte un client ; une relecture coûte une heure. |
| « Et si un client refuse de signer l'autorisation ? » | On ne teste pas. Il n'y a pas de version dégradée de cette règle. |
| « Qui décide en cas de désaccord ? » | Le titulaire du domaine. S'il n'y en a pas, on en nomme un aujourd'hui. |
| « C'est fini quand ? » | Jamais, et c'est normal : la doctrine se corrige après chaque mission. Le RETEX sert à ça. |
| « Pourquoi Git et pas un dossier partagé ? » | Parce qu'un dossier partagé ne dit pas qui a changé quoi, ni quand, ni pourquoi. En cas de litige, c'est cette trace qui nous défend. |

---

## Ce qu'il ne faut pas faire

- **Dérouler l'arborescence dossier par dossier.** Personne ne retient.
- **Présenter la doctrine comme achevée.** L'écart se découvrira, et il coûtera
  la confiance.
- **Passer plus de trois minutes sur un outil.** Le sujet est la méthode.
- **Laisser la diapositive 10 pour la fin, à court de temps.** C'est la seule
  qui demande une décision. Si le temps manque, sauter 08 et 09.
- **Répondre à une objection par « c'est écrit dans le dépôt ».** Si c'est écrit
  et que personne ne le sait, c'est que la réunion n'a pas eu lieu.
