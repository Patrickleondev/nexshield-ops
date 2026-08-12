# Prompt — présentation du dépôt à l'équipe

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

- **Patrick-Léon** — sécurité IA et API, pentest, DevSecOps. Technique.
- **Winero** — ingénierie systèmes, pentest, vie privée. Technique.
- **Laurent** — backend, pentest, forensique. Technique.
- **Herbert** — stratégie. Non technique : évite le jargon d'outillage pour lui.
- **Dora** — responsable GRC. À l'aise avec les normes et le juridique, moins
  avec Git.

Règle de rédaction : **une diapositive qui n'est comprise que par les trois
profils techniques est une diapositive ratée.**

## Plan attendu

1. **Le problème** — ce qui arrive à une société de sécurité sans doctrine
   écrite : cinq façons de faire, un livrable différent par consultant, un
   litige impossible à défendre. Concret, pas théorique.
2. **La réponse en une image** — l'architecture de référentiels : ISO 27001
   comme colonne vertébrale, MITRE ATT&CK comme langage commun, un référentiel
   d'exécution par métier. Source : `00-societe/smsi/REFERENTIELS.md`.
3. **Pourquoi ces référentiels et pas d'autres** — reprendre les arguments
   commerciaux du document, pas seulement les noms.
4. **Le dépôt en un coup d'œil** — les six dossiers racine et à quoi ils servent.
5. **Une diapositive par rôle** — « si tu es Dora, tu vis dans ces dossiers ».
   Cinq diapositives, une par associé, avec ses trois premiers documents à lire.
6. **Le cycle d'une mission** — les dix étapes, en insistant sur les deux
   bloquantes (NDA, autorisation de test). Source : `CONTRIBUTING.md` §4.
7. **Le cadre légal** — la loi togolaise n° 2018-026 pénalise l'accès frauduleux
   à un système d'information ; l'autorisation écrite est ce qui rend nos tests
   licites. Source : `00-societe/juridique/CADRE-LEGAL.md`.
8. **Les documents qu'on produit** — pack juridique DOCX, rapports par service,
   classeurs XLSX, supports PPTX, tous générés à partir d'une charte unique.
9. **Comment on travaille ensemble** — branches, revue, qui approuve quoi.
   Source : `CONTRIBUTING.md` §3.
10. **Comment on pilote** — tâches, estimation, délais, la règle des 85 % de
    charge. Source : `00-societe/PILOTAGE-PROJET.md`.
11. **Les trois règles non négociables** (voir plus bas), une diapositive entière.
12. **Ce qui reste à faire** — état d'avancement honnête, et qui prend quoi.
13. **Les deux prochaines semaines** — actions datées, avec un nom en face.

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
- Ne pas présenter la doctrine comme achevée : la plupart des services sont en
  `v0.1`, seul `pentest-audit` a une méthodologie et deux procédures rédigées.
  L'honnêteté sur l'état d'avancement est le but de la diapositive 12.
- Ne pas transformer ça en argumentaire commercial : le public, ce sont les
  associés, pas des clients.
