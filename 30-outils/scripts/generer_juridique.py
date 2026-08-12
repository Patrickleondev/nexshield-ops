#!/usr/bin/env python3
"""Génère le pack juridique en DOCX — documents destinés à être signés.

Usage : python3 30-outils/scripts/generer_juridique.py [--out 90-templates/build/juridique]

Un contrat ne se signe pas en Markdown. Ces documents sont produits en DOCX
parce qu'ils circulent, s'annotent et se signent.

Le RoE suit la structure du standard PTES (« Pre-engagement Interactions ») :
chronologie, lieux, données sensibles, gestion des preuves, réunions de suivi,
heures de test, protocole de blocage, autorisation écrite, approbations tierces.
Sources : 00-societe/smsi/REFERENCES.md

AVERTISSEMENT : bases de travail techniquement structurées, NON RELUES PAR UN
JURISTE. À faire valider avant tout usage réel.
"""
from __future__ import annotations
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import charte as C
from docx_outils import (bloc_signatures, consigne, couverture, historique_versions,
                         nouveau_document, pied_de_page, sommaire, tableau)

AVERTISSEMENT = ("Modèle interne. Toutes les mentions entre chevrons doivent être "
                 "renseignées avant signature. Ce document n'a pas été relu par un "
                 "conseil juridique : le faire valider avant tout usage contractuel.")

CONFIDENTIEL = "CONFIDENTIEL — DIFFUSION RESTREINTE"


def _art(doc, numero: str, titre: str) -> None:
    doc.add_heading(f"Article {numero} — {titre}", level=2)


def _p(doc, texte: str) -> None:
    doc.add_paragraph(texte, style="NS Clause")


# =============================================================== NDA
def nda(chemin: str) -> None:
    doc = nouveau_document()
    couverture(doc, "Accord de confidentialité", "Engagement bilatéral",
               [["Parties", "<Raison sociale du client> et " + C.SOCIETE],
                ["Référence", "<AAAAMMJJ-CLIENT-NDA-v1.0>"],
                ["Date d'effet", "<AAAA-MM-JJ>"],
                ["Durée de l'obligation", "<5> ans à compter de la divulgation"]],
               AVERTISSEMENT)
    doc.add_page_break()

    doc.add_heading("Accord de confidentialité", level=1)
    _p(doc, "Entre les soussignés :")
    tableau(doc, ["", "Partie 1", "Partie 2"],
            [["Raison sociale", "<Client>", C.SOCIETE],
             ["Forme et capital", "<…>", "<…>"],
             ["Immatriculation", "<…>", "<…>"],
             ["Siège social", "<…>", "<…>"],
             ["Représentée par", "<nom, fonction>", "<nom, fonction>"]],
            largeurs=[4, 6, 6])
    _p(doc, "Ci-après désignées individuellement « la Partie » et collectivement "
            "« les Parties ».")

    _art(doc, "1", "Objet")
    _p(doc, "Les Parties souhaitent échanger des informations confidentielles dans "
            "le cadre de l'évaluation, de la préparation et de l'exécution éventuelle "
            "de prestations de sécurité des systèmes d'information. Le présent accord "
            "définit les conditions de protection de ces informations.")

    _art(doc, "2", "Définition des informations confidentielles")
    _p(doc, "Constitue une information confidentielle toute information, quels qu'en "
            "soient la forme et le support, communiquée par une Partie à l'autre, et "
            "notamment : architectures et configurations techniques, adressage, code "
            "source, identifiants, résultats de tests, vulnérabilités identifiées, "
            "données commerciales, financières ou stratégiques, données à caractère "
            "personnel, ainsi que l'existence et le contenu des échanges entre les Parties.")
    _p(doc, "Les vulnérabilités identifiées et les rapports produits sont réputés "
            "confidentiels par nature, sans qu'une mention particulière soit nécessaire.")

    _art(doc, "3", "Exclusions")
    _p(doc, "Ne sont pas soumises au présent accord les informations qui : (a) étaient "
            "licitement connues de la Partie réceptrice avant leur communication ; "
            "(b) sont ou deviennent publiques sans manquement au présent accord ; "
            "(c) sont développées de manière indépendante sans usage des informations "
            "confidentielles ; (d) sont reçues licitement d'un tiers non tenu à une "
            "obligation de confidentialité.")

    _art(doc, "4", "Obligations")
    _p(doc, "Chaque Partie s'engage à : ne pas divulguer les informations "
            "confidentielles à des tiers ; ne les utiliser que pour l'objet défini à "
            "l'article 1 ; en restreindre l'accès aux seules personnes ayant besoin "
            "d'en connaître, elles-mêmes tenues à une obligation équivalente ; "
            "appliquer des mesures de protection au moins équivalentes à celles "
            "appliquées à ses propres informations confidentielles, et en tout état de "
            "cause raisonnables au regard de leur sensibilité.")

    _art(doc, "5", "Divulgation imposée par la loi")
    _p(doc, "La Partie contrainte de divulguer une information confidentielle en vertu "
            "d'une obligation légale ou d'une décision d'autorité en informe l'autre "
            "Partie sans délai, dans la mesure permise par la loi, et limite la "
            "divulgation au strict nécessaire.")

    _art(doc, "6", "Durée")
    _p(doc, "Le présent accord prend effet à sa signature et demeure applicable "
            "pendant toute la durée des échanges, puis pendant <cinq (5)> années à "
            "compter de la dernière communication d'information confidentielle.")

    _art(doc, "7", "Restitution et destruction")
    _p(doc, "À la demande de la Partie émettrice ou au terme des échanges, la Partie "
            "réceptrice restitue ou détruit les informations confidentielles en sa "
            "possession et en atteste par écrit, sous réserve des exemplaires dont la "
            "conservation est imposée par la loi ou par ses obligations d'archivage "
            "professionnel.")

    _art(doc, "8", "Absence de licence et de partenariat")
    _p(doc, "Le présent accord ne confère aucun droit de propriété intellectuelle, "
            "aucune licence, et ne constitue ni une obligation de contracter ni un "
            "engagement d'exclusivité.")

    _art(doc, "9", "Droit applicable et juridiction")
    _p(doc, "Le présent accord est régi par le droit <togolais>. Tout différend "
            "relatif à sa validité, son interprétation ou son exécution sera soumis "
            "aux tribunaux compétents de <…>, à défaut de résolution amiable dans un "
            "délai de trente (30) jours.")

    doc.add_paragraph()
    _p(doc, "Fait à <lieu>, le <date>, en deux exemplaires originaux.")
    bloc_signatures(doc, ["Pour le Client", f"Pour {C.SOCIETE}"])

    pied_de_page(doc.sections[0], f"Accord de confidentialité — {CONFIDENTIEL}")
    doc.save(chemin); print("écrit", chemin)


# =============================================================== RoE (PTES)
def roe(chemin: str) -> None:
    doc = nouveau_document()
    couverture(doc, "Règles d'engagement", "Rules of Engagement",
               [["Client", "<Raison sociale>"],
                ["Mission", "<Type de mission>"],
                ["Référence", "<AAAAMMJJ-CLIENT-ROE-titre-v1.0>"],
                ["Version", "v1.0"],
                ["Contrat de rattachement", "<référence SOW / MSA>"],
                ["Doctrine appliquée", "<service> v<X.Y>"],
                ["Classification", CONFIDENTIEL]],
               AVERTISSEMENT)
    doc.add_page_break()
    sommaire(doc)
    doc.add_page_break()

    consigne(doc, "Document structuré selon le standard PTES, section "
                  "« Pre-engagement Interactions ». Ne pas supprimer de section : "
                  "une section sans objet se remplit par « Sans objet », ce qui est "
                  "une information contractuelle en soi.")

    doc.add_heading("1. Parties et rattachement contractuel", level=1)
    tableau(doc, ["", "Client", "Prestataire"],
            [["Raison sociale", "<…>", C.SOCIETE],
             ["Représentant signataire", "<nom, fonction>", "<nom, fonction>"],
             ["Autorité sur les actifs testés", "<confirmée le …>", "—"]],
            largeurs=[5, 5.5, 5.5])
    tableau(doc, ["Document", "Référence", "Date"],
            [["Accord de confidentialité", "<…>", "<…>"],
             ["Contrat-cadre (MSA)", "<…>", "<…>"],
             ["Énoncé des travaux (SOW)", "<…>", "<…>"],
             ["Autorisation de test", "<…>", "<…>"]],
            largeurs=[6, 6, 4])
    _p(doc, "Le présent document est technique. Il précise les modalités "
            "d'exécution et ne se substitue pas aux stipulations contractuelles.")

    doc.add_heading("2. Objectifs de la mission", level=1)
    consigne(doc, "PTES distingue objectifs primaires (sécurité) et secondaires "
                  "(conformité, responsabilité). Les écrire séparément évite le "
                  "malentendu classique où le client attend une attestation de "
                  "conformité et reçoit un rapport technique.")
    doc.add_heading("2.1 Objectifs primaires — sécurité", level=2)
    _p(doc, "<Ce que le client cherche à établir sur sa sécurité réelle.>")
    doc.add_heading("2.2 Objectifs secondaires — conformité", level=2)
    _p(doc, "<Obligation réglementaire, exigence d'un client, appel d'offres.>")
    doc.add_heading("2.3 Ce que la mission ne permettra pas de conclure", level=2)
    _p(doc, "<Formulé explicitement. Une mission de test d'intrusion n'est pas un "
            "audit de conformité et ne délivre pas de certification.>")

    doc.add_heading("3. Périmètre", level=1)
    doc.add_heading("3.1 Actifs inclus", level=2)
    tableau(doc, ["#", "Actif", "Type", "Identifiant exact", "Environnement", "Propriétaire"],
            [["1", "<…>", "<web / API / IP / mobile / LLM>", "<URL, IP, plage CIDR, identifiant de compte>", "<prod / préprod>", "<…>"],
             ["2", "", "", "", "", ""]],
            largeurs=[0.9, 2.6, 2.8, 4.4, 2.4, 2.9])
    _p(doc, "Un actif non listé est hors périmètre, quelle que soit sa proximité "
            "technique avec un actif listé. Les sous-domaines ne sont pas inclus "
            "implicitement : ils figurent au tableau ou sont couverts par une mention "
            "explicite de type « *.exemple.tld ».")

    doc.add_heading("3.2 Actifs explicitement exclus", level=2)
    _p(doc, "<Production critique, systèmes tiers, filiales, environnements "
            "partagés, plages d'adresses voisines.>")

    doc.add_heading("3.3 Tiers et fournisseurs de service", level=2)
    consigne(doc, "PTES traite ce point séparément : un hébergeur ou un fournisseur "
                  "cloud impose ses propres conditions. C'est un blocage fréquent.")
    tableau(doc, ["Actif", "Fournisseur", "Autorisation requise", "Référence", "Statut"],
            [["<…>", "<Cloudflare / AWS / hébergeur>", "<oui / non>", "<…>", "<obtenue / en cours>"]],
            largeurs=[3.2, 3.6, 3, 3, 3.2])
    _p(doc, "Le Client se charge d'obtenir ces autorisations. Aucun test ne démarre "
            "sur un actif concerné tant que le statut n'est pas « obtenue ».")

    doc.add_heading("3.4 Maîtrise de la dérive de périmètre", level=2)
    _p(doc, "Toute extension du périmètre fait l'objet d'un avenant écrit au présent "
            "document, signé des deux Parties, précisant l'impact sur le calendrier "
            "et sur le prix. Aucune extension n'est réalisée à titre gracieux en "
            "cours de mission.")

    doc.add_heading("4. Nature et profondeur des tests", level=1)
    tableau(doc, ["Paramètre", "Choix retenu"],
            [["Approche", "<boîte noire / boîte grise / boîte blanche>"],
             ["Position", "<externe / interne / les deux>"],
             ["Connaissance des équipes du Client", "<informées / non informées>"],
             ["Comptes fournis", "<aucun / rôles : …>"],
             ["Élévation de privilèges", "<autorisée / interdite>"],
             ["Mouvement latéral", "<autorisé / interdit>"],
             ["Persistance", "<autorisée, à nettoyer et documenter / interdite>"],
             ["Profondeur d'exploitation", "<preuve d'accès seulement / exploitation complète>"],
             ["Référentiel appliqué", "<PTES + OWASP WSTG v… + ASVS L…>"]],
            largeurs=[7, 9])

    doc.add_heading("5. Techniques interdites", level=1)
    _p(doc, "Sauf mention écrite contraire, sont interdits :")
    for t in ["le déni de service, les tests de charge et l'épuisement de ressources ;",
              "l'ingénierie sociale visant les personnes (hameçonnage, vishing, prétexte) ;",
              "l'intrusion physique ;",
              "l'exfiltration réelle de données — la preuve d'accès se fait par un "
              "extrait minimal anonymisé ou par capture de métadonnées ;",
              "la modification ou la destruction de données de production ;",
              "le recours à des codes d'exploitation publics non maîtrisés en production ;",
              "toute action sur un actif hors périmètre."]:
        doc.add_paragraph(t, style="List Bullet")

    doc.add_heading("5.1 Prétextes d'ingénierie sociale autorisés", level=2)
    consigne(doc, "Section PTES. À remplir uniquement si l'ingénierie sociale est "
                  "au périmètre ; sinon écrire « Sans objet ».")
    _p(doc, "<Prétextes acceptés, cibles autorisées, mentions interdites "
            "(usurpation d'une autorité publique, d'un dirigeant nommé, urgence "
            "médicale). Accord des représentants du personnel : <référence>.>")

    doc.add_heading("5.2 Tests de déni de service", level=2)
    _p(doc, "<Interdits par défaut. Si autorisés : fenêtre dédiée, environnement "
            "de préproduction, critères d'arrêt et procédure de rétablissement.>")

    doc.add_heading("6. Calendrier et heures de test", level=1)
    tableau(doc, ["Phase", "Début", "Fin", "Fenêtre horaire autorisée"],
            [[p, "<…>", "<…>", "<…>"] for p in
             ["Pré-engagement", "Renseignement", "Analyse de vulnérabilités",
              "Exploitation", "Post-exploitation", "Rédaction", "Restitution"]],
            largeurs=[4.5, 3, 3, 5.5])
    _p(doc, "Toute intervention hors fenêtre requiert un accord écrit préalable des "
            "deux contacts techniques. Un courriel horodaté suffit.")

    doc.add_heading("6.1 Lieux d'intervention", level=2)
    _p(doc, "<À distance depuis <pays> / sur site à <adresse>. Préciser les "
            "contraintes régionales, les autorisations d'accès aux locaux et les "
            "personnes habilitées à accompagner les testeurs.>")

    doc.add_heading("7. Communication", level=1)
    doc.add_heading("7.1 Contacts", level=2)
    tableau(doc, ["Rôle", "Nom", "Téléphone (joignable 24/7)", "Courriel"],
            [[r, "<…>", "<…>", "<…>"] for r in
             ["Chef de mission (prestataire)", "Testeur principal",
              "Contact technique (client)", "Contact d'escalade (client)",
              "Astreinte client hors ouvrés"]],
            largeurs=[5, 3.5, 4, 3.5])

    doc.add_heading("7.2 Adresses source des tests", level=2)
    _p(doc, "Les tests seront émis depuis les adresses suivantes, communiquées "
            "avant le démarrage afin que le Client puisse distinguer nos tests d'une "
            "attaque réelle : <adresses IP>.")

    doc.add_heading("7.3 Réunions de suivi", level=2)
    _p(doc, "Point d'avancement <quotidien / hebdomadaire>, le <jour> à <heure>, "
            "d'une durée de <15> minutes, portant sur : ce qui a été fait, ce qui est "
            "prévu, ce qui bloque.")

    doc.add_heading("7.4 Protocole de blocage", level=2)
    consigne(doc, "Section PTES (« shunning »). Point souvent oublié qui fait perdre "
                  "des journées entières de test.")
    _p(doc, "<Le Client s'engage à ne pas bloquer les adresses source des testeurs "
            "pendant les fenêtres autorisées / Le Client bloque normalement, le test "
            "évaluant aussi la réaction défensive.> Tout blocage effectué est signalé "
            "au chef de mission dans l'heure.")

    doc.add_heading("8. Procédures d'exception", level=1)
    doc.add_heading("8.1 Découverte d'une vulnérabilité critique", level=2)
    _p(doc, "Arrêt immédiat de l'exploitation de cette voie ; notification du contact "
            "technique dans les deux (2) heures, par téléphone puis par écrit ; "
            "aucune poursuite sans accord écrit du Client.")
    doc.add_heading("8.2 Découverte d'une compromission préexistante", level=2)
    _p(doc, "Arrêt de la mission ; notification du contact d'escalade dans l'heure ; "
            "préservation en l'état, sans intervention ; bascule éventuelle sur une "
            "prestation de réponse à incident faisant l'objet d'un avenant.")
    _p(doc, "Le Prestataire rappelle au Client que celui-ci peut être soumis à une "
            "obligation de déclaration auprès de l'autorité compétente. Cette "
            "déclaration relève de la seule responsabilité du Client.")
    doc.add_heading("8.3 Arrêt d'urgence", level=2)
    _p(doc, "Chaque Partie peut demander l'arrêt immédiat des tests, par téléphone à "
            "un contact listé à l'article 7.1, sans avoir à se justifier. L'arrêt est "
            "effectif immédiatement et confirmé par écrit dans l'heure. La reprise "
            "n'intervient que sur accord écrit.")
    doc.add_heading("8.4 Incident causé par les tests", level=2)
    _p(doc, "Arrêt immédiat, notification sous trente (30) minutes, assistance au "
            "rétablissement, et fiche d'incident annexée au rapport.")

    doc.add_heading("9. Données sensibles et preuves", level=1)
    doc.add_heading("9.1 Données à caractère personnel", level=2)
    _p(doc, "Les testeurs s'abstiennent d'accéder aux données à caractère personnel "
            "au-delà de ce qui est strictement nécessaire à la démonstration d'une "
            "vulnérabilité. Toute donnée rencontrée est anonymisée dans le rapport et "
            "n'est pas conservée.")
    doc.add_heading("9.2 Conservation et destruction des preuves", level=2)
    tableau(doc, ["Élément", "Modalité"],
            [["Support de stockage", "<chiffré, dédié à la mission>"],
             ["Localisation", "<…>"],
             ["Chiffrement", "<algorithme, gestion des clés>"],
             ["Durée de conservation", "<90> jours après remise du rapport"],
             ["Destruction", "Certificat de destruction signé, remis au Client"],
             ["Conservation du rapport", "Durée du contrat + <3> ans"]],
            largeurs=[6, 10])
    _p(doc, "Aucune donnée du Client n'est stockée sur un service tiers non prévu au "
            "contrat. Les comptes de test fournis sont révoqués par le Client à la fin "
            "de la mission.")

    doc.add_heading("10. Livrables et calendrier de remise", level=1)
    tableau(doc, ["Livrable", "Format", "Échéance", "Destinataires"],
            [["Notification des vulnérabilités critiques", "Téléphone puis écrit", "Sous 2 h", "<…>"],
             ["Rapport technique", "<PDF chiffré>", "<date>", "<…>"],
             ["Synthèse exécutive", "<PDF chiffré>", "<date>", "<…>"],
             ["Restitution orale", "<visioconférence / sur site>", "<date>", "<…>"],
             ["Attestation de test", "<PDF>", "<date>", "<…>"],
             ["Certificat de destruction", "<PDF>", "<J+90>", "<…>"],
             ["Contre-vérification", "<PDF chiffré>", "<date ou « non prévue »>", "<…>"]],
            largeurs=[5, 3.2, 3.4, 4.4])

    doc.add_heading("11. Acceptation", level=1)
    _p(doc, "En signant, chaque Partie confirme avoir lu et accepté l'intégralité des "
            "présentes règles. Le Client confirme détenir l'autorité nécessaire pour "
            "autoriser les tests sur les actifs listés à l'article 3.1, et reconnaît "
            "que tout test comporte un risque résiduel d'indisponibilité ou de "
            "dégradation, malgré les précautions décrites.")
    bloc_signatures(doc, ["Pour le Client", f"Pour {C.SOCIETE}"])

    doc.add_page_break()
    historique_versions(doc)

    pied_de_page(doc.sections[0], f"Règles d'engagement — <CLIENT> — {CONFIDENTIEL}")
    doc.save(chemin); print("écrit", chemin)


# =============================================================== Autorisation
def autorisation(chemin: str) -> None:
    doc = nouveau_document(marge_cm=2.2)
    doc.add_heading("Autorisation de réalisation de tests de sécurité", level=1)
    consigne(doc, "Le document que chaque testeur garde sur lui, signé, pendant "
                  "toute la durée des tests. Il tient sur une page, délibérément : "
                  "il doit pouvoir être lu et compris en trente secondes par un "
                  "responsable qui s'inquiète d'une activité anormale. C'est la "
                  "pièce qui établit la licéité des tests au regard de la loi "
                  "n° 2018-026 (voir 00-societe/juridique/CADRE-LEGAL.md).")

    _p(doc, "Je soussigné(e) <Nom, Prénom>, exerçant les fonctions de <fonction> au "
            "sein de <Raison sociale>, immatriculée sous le numéro <…>, dont le siège "
            "est situé <adresse>,")
    _p(doc, "déclare détenir l'autorité nécessaire pour disposer des systèmes "
            "d'information listés ci-après, et autorise expressément la société "
            f"{C.SOCIETE}, ainsi que les personnes nommément désignées ci-dessous "
            "agissant en son nom, à réaliser des tests de sécurité informatique sur "
            "ces systèmes.")

    doc.add_heading("Systèmes autorisés", level=2)
    tableau(doc, ["Identifiant (IP, domaine, application)", "Type", "Environnement"],
            [["<…>", "<…>", "<…>"], ["", "", ""]],
            largeurs=[8, 4, 4])
    _p(doc, "Tout système non listé dans ce tableau est exclu de la présente autorisation.")

    doc.add_heading("Personnes autorisées", level=2)
    tableau(doc, ["Nom, Prénom", "Rôle", "Pièce d'identité"],
            [["<…>", "Chef de mission", "<type et numéro>"],
             ["<…>", "Testeur", "<type et numéro>"]],
            largeurs=[6, 4, 6])

    doc.add_heading("Période d'autorisation", level=2)
    _p(doc, "Du <date, heure> au <date, heure> inclus. La présente autorisation est "
            "caduque de plein droit au terme de cette période.")

    doc.add_heading("Conditions", level=2)
    _p(doc, "Les tests sont réalisés conformément aux règles d'engagement référencées "
            "<AAAAMMJJ-CLIENT-ROE-…-v1.0>, qui font partie intégrante de la présente "
            "autorisation et en précisent les limites techniques.")
    _p(doc, "Sont notamment exclus : le déni de service, l'exfiltration réelle de "
            "données, la modification ou la destruction de données, et toute action "
            "sur un système non listé.")

    doc.add_heading("Contact de vérification", level=2)
    _p(doc, "En cas de doute sur l'authenticité du présent document ou sur la "
            "légitimité d'une activité observée, contacter immédiatement : "
            "<Nom> — <fonction> — <téléphone joignable 24/7>.")

    doc.add_paragraph()
    _p(doc, "Fait à <lieu>, le <date>.")
    bloc_signatures(doc, ["Pour le Client"])

    p = doc.add_paragraph(style="NS Legende")
    p.add_run("Document confidentiel. Toute reproduction ou usage hors du cadre "
              "défini ci-dessus est interdit. Ce document ne vaut pas autorisation "
              "pour des systèmes appartenant à des tiers (hébergeurs, fournisseurs "
              "de services) : celle-ci doit être obtenue séparément par le Client.")

    pied_de_page(doc.sections[0], "Autorisation de test — à conserver pendant les tests")
    doc.save(chemin); print("écrit", chemin)


# =============================================================== MSA
def msa(chemin: str) -> None:
    doc = nouveau_document()
    couverture(doc, "Contrat-cadre de services", "Master Services Agreement",
               [["Parties", "<Client> et " + C.SOCIETE],
                ["Référence", "<AAAAMMJJ-CLIENT-MSA-v1.0>"],
                ["Date d'effet", "<AAAA-MM-JJ>"],
                ["Durée", "<12> mois, reconductible"]],
               AVERTISSEMENT)
    doc.add_page_break()
    sommaire(doc)
    doc.add_page_break()

    consigne(doc, "Les articles 6 (responsabilité), 7 (propriété intellectuelle), "
                  "9 (assurance) et 12 (droit applicable) doivent impérativement "
                  "être relus par un juriste. Le plafond de responsabilité doit être "
                  "cohérent avec la couverture réelle de votre assurance.")

    articles = [
        ("1", "Objet", "Le présent contrat définit les conditions générales dans "
         "lesquelles le Prestataire réalise, pour le Client, des prestations de "
         "sécurité des systèmes d'information. Chaque prestation fait l'objet d'un "
         "énoncé des travaux (SOW) distinct qui, seul, engage les Parties sur un "
         "périmètre, un prix et un calendrier."),
        ("2", "Documents contractuels et hiérarchie", "En cas de contradiction, "
         "l'ordre de préséance est le suivant : (1) l'énoncé des travaux signé ; "
         "(2) les règles d'engagement signées ; (3) le présent contrat-cadre ; "
         "(4) l'accord de confidentialité ; (5) toute annexe technique."),
        ("3", "Obligations du Prestataire", "Le Prestataire s'engage à exécuter les "
         "prestations conformément aux règles de l'art et aux référentiels annoncés, "
         "à affecter du personnel qualifié, à respecter strictement le périmètre "
         "autorisé, et à signaler sans délai toute vulnérabilité critique. Le "
         "Prestataire est tenu d'une obligation de moyens : un test d'intrusion est "
         "une évaluation à un instant donné, sur un périmètre délimité, et ne "
         "garantit pas l'absence de vulnérabilité."),
        ("4", "Obligations du Client", "Le Client s'engage à fournir une autorisation "
         "de test signée par une personne ayant autorité sur les actifs, à obtenir "
         "les autorisations des tiers concernés, à mettre à disposition les accès et "
         "les interlocuteurs prévus, à disposer de sauvegardes vérifiées avant le "
         "démarrage, et à révoquer les comptes de test à la fin de la mission."),
        ("5", "Prix, facturation et délais de paiement", "Les prix sont fixés dans "
         "chaque énoncé des travaux. Sauf stipulation contraire : <30> % à la "
         "signature, solde à la remise du rapport. Paiement à <30> jours date de "
         "facture. Tout retard donne lieu à des pénalités au taux de <…>."),
        ("6", "Responsabilité", "La responsabilité du Prestataire est limitée aux "
         "dommages directs et prouvés, et plafonnée au montant total effectivement "
         "payé au titre de l'énoncé des travaux concerné. Sont exclus les dommages "
         "indirects, notamment la perte d'exploitation, de données, de chiffre "
         "d'affaires ou de clientèle. Le Client reconnaît que tout test comporte un "
         "risque résiduel d'indisponibilité, malgré les précautions contractuelles."),
        ("7", "Propriété intellectuelle", "Le Client devient propriétaire des "
         "rapports et livrables à leur paiement intégral. Le Prestataire conserve la "
         "pleine propriété de ses méthodologies, outils, scripts, gabarits, règles de "
         "détection et savoir-faire, y compris lorsqu'ils ont été employés ou "
         "améliorés à l'occasion de la mission, et conserve le droit de les "
         "réutiliser librement."),
        ("8", "Confidentialité", "Les stipulations de l'accord de confidentialité "
         "conclu entre les Parties s'appliquent au présent contrat et lui survivent "
         "dans les conditions qu'il prévoit."),
        ("9", "Assurance", "Le Prestataire déclare être titulaire d'une assurance de "
         "responsabilité civile professionnelle couvrant les conséquences pécuniaires "
         "de sa responsabilité, à hauteur de <montant>. Une attestation est fournie "
         "sur demande."),
        ("10", "Sous-traitance", "Le Prestataire ne peut sous-traiter tout ou partie "
         "des prestations sans l'accord écrit préalable du Client. Il demeure en tout "
         "état de cause responsable de l'exécution."),
        ("11", "Non-sollicitation de personnel", "Chaque Partie s'interdit de "
         "solliciter ou d'embaucher un collaborateur de l'autre ayant participé aux "
         "prestations, pendant la durée du contrat et <douze (12)> mois après son "
         "terme, sauf accord écrit."),
        ("12", "Droit applicable et règlement des différends", "Le présent contrat "
         "est régi par le droit <togolais>. Les Parties s'efforcent de résoudre tout "
         "différend à l'amiable dans un délai de trente (30) jours. À défaut, "
         "compétence est attribuée aux tribunaux de <…>."),
        ("13", "Résiliation", "Chaque Partie peut résilier le présent contrat-cadre "
         "moyennant un préavis écrit de <trente (30)> jours, sans que cette "
         "résiliation n'affecte les énoncés des travaux en cours d'exécution. En cas "
         "de manquement grave non réparé dans les quinze (15) jours d'une mise en "
         "demeure, la résiliation peut intervenir sans préavis."),
        ("14", "Durée", "Le présent contrat prend effet à sa signature pour une durée "
         "de <douze (12)> mois, reconductible tacitement par périodes équivalentes."),
    ]
    for num, titre, corps in articles:
        _art(doc, num, titre)
        _p(doc, corps)

    doc.add_paragraph()
    _p(doc, "Fait à <lieu>, le <date>, en deux exemplaires originaux.")
    bloc_signatures(doc, ["Pour le Client", f"Pour {C.SOCIETE}"])
    pied_de_page(doc.sections[0], f"Contrat-cadre de services — {CONFIDENTIEL}")
    doc.save(chemin); print("écrit", chemin)


# =============================================================== SOW
def sow(chemin: str) -> None:
    doc = nouveau_document()
    couverture(doc, "Énoncé des travaux", "Statement of Work",
               [["Client", "<Raison sociale>"],
                ["Référence", "<AAAAMMJJ-CLIENT-SOW-titre-v1.0>"],
                ["Contrat-cadre", "<référence MSA>"],
                ["Service", "<pentest-audit / ai-redteaming / …>"],
                ["Date", "<AAAA-MM-JJ>"]],
               AVERTISSEMENT)
    doc.add_page_break()

    doc.add_heading("1. Contexte et objectifs", level=1)
    _p(doc, "<Pourquoi cette mission, ce qu'elle doit permettre de décider.>")

    doc.add_heading("2. Périmètre", level=1)
    _p(doc, "<Résumé. Le détail technique est dans les règles d'engagement.>")

    doc.add_heading("3. Prestations réalisées", level=1)
    tableau(doc, ["#", "Prestation", "Description", "Jours"],
            [["1", "<…>", "<…>", "<…>"], ["2", "", "", ""]],
            largeurs=[1, 4, 8, 3])

    doc.add_heading("4. Ce qui n'est pas inclus", level=1)
    consigne(doc, "Section décisive pour éviter la dérive de périmètre. Reprendre "
                  "le « hors périmètre » du README du service concerné.")
    _p(doc, "<…>")

    doc.add_heading("5. Livrables", level=1)
    tableau(doc, ["Livrable", "Format", "Échéance"],
            [["Rapport technique", "PDF chiffré", "<…>"],
             ["Synthèse exécutive", "PDF chiffré", "<…>"],
             ["Restitution orale", "<…>", "<…>"],
             ["Attestation de test", "PDF", "<…>"]],
            largeurs=[6, 5, 5])

    doc.add_heading("6. Calendrier", level=1)
    tableau(doc, ["Jalon", "Date", "Responsable"],
            [["Signature", "<…>", "<…>"],
             ["Autorisation de test remise", "<…>", "Client"],
             ["Démarrage des tests", "<…>", "Prestataire"],
             ["Fin des tests", "<…>", "Prestataire"],
             ["Remise du rapport", "<…>", "Prestataire"],
             ["Restitution", "<…>", "Prestataire"],
             ["Destruction des preuves", "<J+90>", "Prestataire"]],
            largeurs=[7, 4, 5])

    doc.add_heading("7. Équipe affectée", level=1)
    tableau(doc, ["Nom", "Rôle", "Séniorité", "Jours"],
            [["<…>", "<…>", "<…>", "<…>"]],
            largeurs=[5, 4.5, 3, 3.5])

    doc.add_heading("8. Conditions financières", level=1)
    tableau(doc, ["Poste", "Quantité", "Prix unitaire", "Total"],
            [["<Prestation>", "<n> jours", "<…>", "<…>"],
             ["Total hors taxes", "", "", "<…>"]],
            largeurs=[7, 3, 3, 3])
    _p(doc, "Modalités : <30> % à la signature, solde à la remise du rapport. "
            "Paiement à <30> jours. Validité de la présente offre : <30> jours.")

    doc.add_heading("9. Conditions suspensives", level=1)
    _p(doc, "L'exécution est suspendue tant que les éléments suivants ne sont pas "
            "réunis : règles d'engagement signées ; autorisation de test signée par "
            "une personne ayant autorité ; autorisations des tiers concernés ; accès "
            "et comptes de test fournis ; sauvegardes vérifiées. Tout retard dans la "
            "fourniture de ces éléments décale le calendrier d'autant.")

    doc.add_paragraph()
    bloc_signatures(doc, ["Pour le Client", f"Pour {C.SOCIETE}"])
    pied_de_page(doc.sections[0], f"Énoncé des travaux — <CLIENT> — {CONFIDENTIEL}")
    doc.save(chemin); print("écrit", chemin)


# =============================================================== Attestations
def attestation(chemin: str) -> None:
    doc = nouveau_document()
    doc.add_heading("Attestation de réalisation de tests de sécurité", level=1)
    consigne(doc, "Document remis au Client pour ses propres besoins : appel "
                  "d'offres, auditeur, assureur, client final. Il atteste qu'une "
                  "mission a eu lieu et n'expose AUCUNE vulnérabilité. Il peut donc "
                  "circuler, contrairement au rapport.")
    _p(doc, f"La société {C.SOCIETE} atteste avoir réalisé, pour le compte de "
            "<Raison sociale du Client>, une prestation d'évaluation de la sécurité "
            "de ses systèmes d'information, dans les conditions suivantes :")
    tableau(doc, ["Élément", "Valeur"],
            [["Nature de la prestation", "<Test d'intrusion applicatif / …>"],
             ["Périmètre", "<Description générale, sans identifiant technique>"],
             ["Période de réalisation", "<du … au …>"],
             ["Méthodologie", "<PTES, OWASP WSTG v…, doctrine v…>"],
             ["Référence du rapport", "<AAAAMMJJ-CLIENT-RAPPORT-…-v1.0>"],
             ["Contre-vérification", "<réalisée le … / non prévue>"]],
            largeurs=[6, 10])
    _p(doc, "Les constatations détaillées figurent dans le rapport référencé "
            "ci-dessus, remis au Client et couvert par l'accord de confidentialité "
            "entre les Parties. La présente attestation n'expose aucune information "
            "susceptible de faciliter une attaque.")
    _p(doc, "Cette attestation ne constitue ni une certification, ni un avis de "
            "conformité à un référentiel ou à une réglementation. Une évaluation "
            "porte sur un périmètre délimité, à un instant donné.")
    doc.add_paragraph()
    _p(doc, "Fait à <lieu>, le <date>.")
    bloc_signatures(doc, [f"Pour {C.SOCIETE}"])
    pied_de_page(doc.sections[0], "Attestation de test")
    doc.save(chemin); print("écrit", chemin)


def certificat_destruction(chemin: str) -> None:
    doc = nouveau_document()
    doc.add_heading("Certificat de destruction des données de mission", level=1)
    _p(doc, f"La société {C.SOCIETE} certifie avoir procédé à la destruction "
            "définitive de l'ensemble des données collectées dans le cadre de la "
            "mission référencée ci-dessous, conformément à ses engagements "
            "contractuels.")
    tableau(doc, ["Élément", "Valeur"],
            [["Client", "<Raison sociale>"],
             ["Mission", "<référence>"],
             ["Règles d'engagement", "<référence>"],
             ["Date de remise du rapport", "<AAAA-MM-JJ>"],
             ["Date de destruction", "<AAAA-MM-JJ>"],
             ["Délai contractuel", "<90> jours"]],
            largeurs=[6, 10])

    doc.add_heading("Éléments détruits", level=2)
    tableau(doc, ["Nature", "Support", "Méthode de destruction", "Opérateur"],
            [["Preuves brutes (captures, sorties d'outils)", "<coffre chiffré>",
              "<effacement cryptographique / suppression de clé>", "<…>"],
             ["Identifiants de test fournis par le Client", "<…>", "<…>", "<…>"],
             ["Copies de travail locales", "<postes des testeurs>", "<…>", "<…>"],
             ["Sauvegardes intermédiaires", "<…>", "<…>", "<…>"]],
            largeurs=[5, 3.5, 4.5, 3])

    doc.add_heading("Éléments conservés", level=2)
    tableau(doc, ["Élément", "Motif", "Durée", "Protection"],
            [["Rapport final", "Obligation d'archivage professionnel",
              "<durée du contrat + 3 ans>", "Chiffré, accès restreint"],
             ["Documents contractuels", "Obligation légale", "<…>", "<…>"]],
            largeurs=[4.5, 4.5, 3.5, 3.5])

    _p(doc, "Le Prestataire confirme qu'aucune copie des éléments détruits ne subsiste "
            "en sa possession ni en celle de ses collaborateurs, sur quelque support "
            "que ce soit.")
    doc.add_paragraph()
    _p(doc, "Fait à <lieu>, le <date>.")
    bloc_signatures(doc, [f"Pour {C.SOCIETE}"])
    pied_de_page(doc.sections[0], "Certificat de destruction")
    doc.save(chemin); print("écrit", chemin)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="90-templates/build/juridique")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    j = lambda n: os.path.join(a.out, n)
    nda(j("Modele-NDA.docx"))
    msa(j("Modele-MSA-contrat-cadre.docx"))
    sow(j("Modele-SOW-enonce-des-travaux.docx"))
    roe(j("Modele-ROE-regles-engagement.docx"))
    autorisation(j("Modele-AUTH-autorisation-de-test.docx"))
    attestation(j("Modele-ATTEST-attestation-de-test.docx"))
    certificat_destruction(j("Modele-CERT-destruction-des-donnees.docx"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
