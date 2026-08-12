# Prompt - présentation du dépôt à l'équipe

À utiliser avec un agent capable de lire le dépôt (Manus, ou tout autre outil
branché sur GitHub). Objectif : produire un support qui fait **comprendre et
adopter** le dépôt par les quatre autres associés, dont certains ne sont pas
techniques.

Copier tout ce qui suit la ligne de séparation.

---

Tu as accès au dépôt privé `Patrickleondev/nexshield-ops`. C'est le dépôt
d'exploitation de NexShield, société de cybersécurité en création au Togo,
fondée par cinq associés.

Produis une **présentation (PPTX ou Google Slides) de 16 à 20 diapositives, en
français**, destinée à être projetée devant les quatre autres co-fondateurs qui
découvrent ce dépôt.

## Ce que la présentation doit obtenir

Ce n'est pas une visite guidée de l'arborescence. À la fin, chaque associé doit :

1. comprendre **pourquoi** ce dépôt existe et ce qu'il évite comme problèmes ;
2. savoir **où aller** pour son propre rôle ;
3. savoir **quoi faire concrètement** dans les deux semaines qui suivent ;
4. avoir accepté trois règles non négociables (voir plus bas).

## Ton public

- **Patrick-Léon** - sécurité IA et API, pentest, DevSecOps. Technique.
- **Winero** - ingénierie systèmes, pentest, vie privée. Technique.
- **Laurent** - backend, pentest, forensique. Technique.
- **Herbert** - stratégie. Non technique : évite le jargon d'outillage pour lui.
- **Dora** - responsable GRC. À l'aise avec les normes et le juridique, moins
  avec Git.

Règle de rédaction : **une diapositive qui n'est comprise que par les trois
profils techniques est une diapositive ratée.**

## Plan attendu

1. **Le problème** - ce qui arrive à une société de sécurité sans doctrine
   écrite : cinq façons de faire, un livrable différent par consultant, un
   litige impossible à défendre. Concret, pas théorique.
2. **La réponse en une image** - l'architecture de référentiels : ISO 27001
   comme colonne vertébrale, MITRE ATT&CK comme langage commun, un référentiel
   d'exécution par métier. Source : `00-societe/smsi/REFERENTIELS.md`.
3. **Pourquoi ces référentiels et pas d'autres** - reprendre les arguments
   commerciaux du document, pas seulement les noms.
4. **Le dépôt en un coup d'œil** - les dossiers racine et à quoi ils servent.
   Insister sur la structure identique des huit services : cadrage, exécution,
   checklist, outillage. Qui connaît un service sait naviguer dans les sept
   autres.
5. **Une diapositive par rôle** - « si tu es Dora, tu vis dans ces dossiers ».
   Cinq diapositives, une par associé, avec ses trois premiers documents à lire.
6. **Le cycle d'une mission** - les dix étapes, en insistant sur les deux
   bloquantes (NDA, autorisation de test). Source : `CONTRIBUTING.md` §4.
7. **Le cadre légal** - la loi togolaise n° 2018-026 pénalise l'accès frauduleux
   à un système d'information ; l'autorisation écrite est ce qui rend nos tests
   licites. Source : `00-societe/juridique/CADRE-LEGAL.md`.
8. **Les documents qu'on produit** - pack juridique DOCX, rapports par service,
   classeurs XLSX, supports PPTX, tous générés à partir d'une charte unique.
9. **Comment on travaille ensemble** - branches, revue, qui approuve quoi.
   Source : `CONTRIBUTING.md` §3.
10. **Comment on pilote** - tâches, estimation, délais, la règle des 85 % de
    charge. Source : `00-societe/PILOTAGE-PROJET.md`.
11. **Les trois règles non négociables** (voir plus bas), une diapositive entière.
12. **Ce qui reste à faire** - état d'avancement honnête, et qui prend quoi.
13. **Les deux prochaines semaines** - actions datées, avec un nom en face.

## Les trois règles à faire accepter explicitement

Elles doivent apparaître sur une diapositive dédiée, formulées simplement :

1. **Aucune action technique sans autorisation écrite signée.** Y compris un
   simple `whois` avant-vente. C'est ce qui sépare le métier d'un délit.
2. **Aucune preuve brute ni secret dans le dépôt.** Les preuves vivent au coffre
   chiffré et sont détruites à J+90.
3. **Personne ne publie son propre travail sans relecture.** Ni un rapport, ni un
   article, y compris le fondateur.

## Contraintes de forme

- Français. Vouvoiement inutile entre associés, mais registre professionnel.
- **Aucun emoji.**
- Palette : bleu nuit `#0B1220`, ardoise `#1E293B`, cyan `#06B6D4` en accent,
  fond clair. Sévérités : critique `#991B1B`, élevée `#C2410C`, moyenne
  `#A16207`, faible `#0369A1`.
- Police sans empattement, titres en demi-gras.
- Six lignes maximum par diapositive. Ce qui ne tient pas va dans les notes.
- **Notes de présentateur obligatoires** sur chaque diapositive : ce qu'il faut
  dire, pas ce qui est affiché.
- Schémas plutôt que listes à puces quand c'est possible. Pas d'images de
  banque d'images.

## Ce qu'il ne faut pas faire

- Ne pas inventer de contenu absent du dépôt. Si une information manque, écris
  « à compléter » plutôt que de la produire.
- Ne pas présenter la doctrine comme achevée. État réel, à reprendre tel quel :
  **les huit services ont désormais leur socle écrit** - une procédure de
  cadrage, une procédure d'exécution, une checklist bâtie sur leur référentiel et
  un document d'outillage. Mais **tous sont en `v0.1`** : rien n'a encore été
  éprouvé sur une mission réelle. Le passage en `v1.0` suppose une première
  mission et la relecture juridique des gabarits.
  L'honnêteté sur cet écart est le but de la diapositive 12.
- Ne pas transformer ça en argumentaire commercial : le public, ce sont les
  associés, pas des clients.

---

# Complément - diapositives à ajouter au support existant

Le support `nexshield_presentation.pptx` compte 12 diapositives. Cinq sujets du
plan initial n'y figurent pas. Ce complément se donne au même agent, avec le
support existant en pièce jointe.

Copier tout ce qui suit la ligne de séparation.

---

Tu as accès au dépôt `Patrickleondev/nexshield-ops` et au support existant
`nexshield_presentation.pptx`, qui compte 12 diapositives numérotées de 01 à 11.

Produis **cinq diapositives supplémentaires**, dans **exactement la même charte
graphique** que le support fourni : mêmes couleurs, mêmes polices, même
disposition d'en-tête `NN · TITRE EN CAPITALES`, même bandeau de source interne
en bas. Elles doivent pouvoir être insérées sans que la rupture se voie.

**Notes de présentateur obligatoires** sur chacune, entre 400 et 800 caractères,
disant ce qu'il faut dire et non ce qui est affiché.

**Aucun emoji. Aucun tiret cadratin.** Trait d'union simple uniquement.

## Diapositive A, à insérer après la diapositive 04

**Titre** : `05 · CE QUE NOUS VENDONS`
**Renuméroter les diapositives suivantes en conséquence.**

Les huit services, sous forme de grille de huit cartes. Chaque carte porte le nom
du service, son référentiel d'exécution et une phrase disant à qui il s'adresse.

Source : `README.md`, tableau « Les huit services », et le `README.md` de chaque
service. Ne pas inventer de service ni de référentiel absent du dépôt.

Message de la diapositive : les huit ont désormais la **même structure interne** -
cadrage, exécution, checklist, outillage. Ce n'est pas huit offres bricolées,
c'est une seule méthode déclinée huit fois.

Bandeau bas : indiquer que les trois plus immédiatement vendables sont
`pentest-audit`, `ai-redteaming` et `secu-applicative`, et que `ai-redteaming`
est le différenciateur : très peu d'acteurs de la sous-région sont structurés sur
ce métier.

## Diapositive B, à insérer juste après la diapositive du cycle de mission

**Titre** : `07 · UNE MISSION DANS GIT`

Schéma horizontal en cinq temps, reprenant le style du cycle de mission :

1. **Ouvrir** - `mission/<client>-<service>`, à partir d'une `main` à jour
2. **Verrouiller** - RoE et autorisation versés, avant la première commande
3. **Travailler** - un commit par jour, jamais de preuve ni de secret
4. **Livrer** - demande de fusion, deux approbations, puis tag
5. **Clôturer** - RETEX, preuves détruites, branche supprimée

Encadré à part, à mettre en évidence : **le code du service figure dans le nom de
la branche parce qu'il détermine la procédure à appliquer.** Donner les huit
codes : `pentest`, `airt`, `app`, `devsecops`, `soc`, `privacy`, `sensib`,
`infra`.

Second encadré : **un message de commit ne contient jamais de détail technique
exploitable.** Écrire `mission(acme): consigne 3 constatations`, jamais
`mission(acme): trouve une injection SQL sur /login`. Un historique Git peut
fuiter.

Source : `00-societe/procedures/PRO-GEN-001-procedure-git-de-mission.md`.

## Diapositive C, à insérer après la diapositive du mode de collaboration

**Titre** : `10 · NOMMER ET VERSIONNER`

Sujet volontairement mis en avant : c'est ce qui rend le dépôt lisible dans deux
ans, et c'est ce qu'une équipe néglige toujours.

Trois blocs :

1. **Un document** : `AAAAMMJJ-<CLIENT>-<TYPE>-<titre>-v<X.Y>.<ext>`, avec un
   exemple réel.
2. **Une vulnérabilité** : `<CLIENT>-<AAAA>-<NNN>`, numérotation continue par
   client et par année, **tous services confondus**, pour suivre une faille du
   rapport jusqu'à sa contre-vérification.
3. **Une version** : `v0.x` ne sort jamais de la société ; `v1.0` est la première
   version livrée ; **une version livrée ne se modifie plus**, une correction
   produit une `v1.1`.

Encadré : **le numéro de version vit à trois endroits qui doivent concorder** -
nom du fichier, page de garde, tableau d'historique.

Encadré : **on renomme toujours avec `git mv`**, jamais en supprimant puis
recréant, sinon l'historique est perdu. Ne se renomment jamais : un document
livré, un dossier de mission close, un identifiant de vulnérabilité.

Source : `NOMENCLATURE.md` et `CONVENTIONS.md`.

## Diapositive D, à insérer avant la diapositive des trois règles

**Titre** : `11 · COMMENT NOUS PILOTONS`

Trois idées, pas plus :

1. **Une tâche sans titulaire nommé et sans date n'existe pas.** Reprendre la
   formule telle quelle, elle est dans le dépôt.
2. **Les règles d'estimation** : coefficient 1,5 sur une technologie inconnue,
   20 % de marge pour la rédaction, **quatre jours facturables par semaine au
   maximum**. Le cinquième jour part en avant-vente, en veille et en imprévu.
3. **La règle des 85 %** : au-delà de 85 % de charge, on refuse une mission ou on
   décale une échéance. On ne prend pas en espérant que ça passe.

Encadré : **trois jours ouvrés minimum entre la fin des tests et la remise du
rapport.** Ce délai sert à la double relecture, il se prévoit au planning et se
vend au client comme une garantie de qualité.

Source : `00-societe/PILOTAGE-PROJET.md`.

## Diapositive E, à insérer avant la diapositive finale

**Titre** : `13 · COMMENT NOUS ABORDONS UN CLIENT`

Destinée surtout à Herbert, mais utile à tous : un consultant technique en
rendez-vous commercial fait souvent l'inverse de ce qui marche.

Quatre points :

1. **Trente minutes d'écoute sur soixante.** Le premier rendez-vous sert à
   comprendre, pas à démontrer.
2. **Aucun devis au premier rendez-vous.** Un prix donné avant le périmètre est
   un prix qu'on regrettera.
3. **Adapter à l'interlocuteur** : une direction générale entend le risque
   métier, une direction technique entend la méthode. Le même discours pour les
   deux échoue avec les deux.
4. **Ce qu'on refuse fait vendre.** Dire « nous ne testerons pas sans
   autorisation écrite » rassure davantage qu'une liste d'outils.

Encadré : **ne jamais tester avant la signature pour « montrer qu'on est bon ».**
C'est un délit, et c'est le meilleur moyen de perdre le client et la société.

Source : `00-societe/commercial/POSTURE.md`.

## Après insertion

Le support comptera 17 diapositives. Vérifier que la numérotation des en-têtes
est continue de 01 à 16, sans doublon ni saut. La couverture ne porte pas de
numéro.
