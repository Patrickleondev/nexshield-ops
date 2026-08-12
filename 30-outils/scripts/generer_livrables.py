#!/usr/bin/env python3
"""Génère un gabarit de rapport DOCX par service.

Usage : python3 30-outils/scripts/generer_livrables.py [--out 90-templates/build/livrables]

Un rapport de test d'intrusion et un audit de maturité DevSecOps n'ont ni la
même structure, ni le même lecteur, ni les mêmes annexes. Chaque service a donc
son gabarit - construit sur un socle commun pour que l'ensemble reste cohérent.

Socle commun (toutes missions) : couverture, sommaire, synthèse exécutive,
cadre de la mission, limites, constatations, plan d'action, annexes de
couverture, d'outillage, de preuves, de diffusion.
"""
from __future__ import annotations
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import charte as C
from docx_outils import (consigne, couverture, nouveau_document, pied_de_page,
                         sommaire, tableau)

CONFIDENTIEL = "CONFIDENTIEL - DIFFUSION RESTREINTE"

# --- Définition des services -------------------------------------------------
# champs_constatation : lignes de la fiche de vulnérabilité propre au métier
# sections_metier     : (titre, [sous-titres]) insérées après le cadre
# annexes_metier      : annexes supplémentaires
SERVICES = {
 "pentest-audit": dict(
   titre="Rapport de test d'intrusion",
   code="RAPPORT", lecteur="Direction et équipe technique",
   refs=[("PTES", "-", "Structuration des phases"),
         ("OWASP WSTG", "<v4.2>", "Catalogue de tests, preuve de couverture"),
         ("NIST SP 800-115", "-", "Cadre technique"),
         ("MITRE ATT&CK", "<v15>", "Qualification des techniques"),
         ("CVSS", "v4.0", "Scoring")],
   champs=[("OWASP WSTG", "WSTG-<CAT>-<NN>"), ("MITRE ATT&CK", "T<NNNN>")],
   sections=[("Renseignement", ["Reconnaissance passive", "Reconnaissance active",
                                "Surface d'attaque identifiée"]),
             ("Modélisation de menaces", ["Profils d'attaquant retenus",
                                          "Actifs critiques identifiés"])],
   annexes=[("Couverture des tests OWASP WSTG",
             ["Identifiant", "Intitulé", "Statut", "Motif si non exécuté"]),
            ("Chemin d'attaque détaillé", None)],
   phases=["Pré-engagement", "Renseignement", "Modélisation de menaces",
           "Analyse de vulnérabilités", "Exploitation", "Post-exploitation",
           "Restitution"]),

 "ai-redteaming": dict(
   titre="Rapport d'évaluation offensive de système à base d'IA",
   code="RAPPORT", lecteur="Équipe produit, data science et direction",
   refs=[("OWASP Top 10 for LLM Applications", "2025", "Taxonomie des risques"),
         ("MITRE ATLAS", "<version>", "TTP adverses IA"),
         ("NIST AI RMF", "1.0", "Gouvernance du risque"),
         ("NIST AI 600-1", "-", "Profil IA générative"),
         ("CVSS", "v4.0", "Scoring, adapté au contexte IA")],
   champs=[("OWASP LLM", "LLM<NN>:2025"), ("MITRE ATLAS", "AML.T<NNNN>"),
           ("Taux de réussite", "<n/N tentatives>"),
           ("Reproductibilité", "<déterministe / stochastique>")],
   sections=[("Description du système évalué",
              ["Modèle et fournisseur", "Architecture (RAG, agents, outils)",
               "Garde-fous en place", "Données d'ancrage et sources",
               "Périmètre d'action des agents"]),
             ("Modélisation des menaces IA",
              ["Surfaces d'entrée (directe, indirecte, documents ingérés)",
               "Capacités accessibles au modèle", "Impact d'un détournement d'outil"])],
   annexes=[("Couverture OWASP Top 10 LLM",
             ["Identifiant", "Risque", "Statut", "Motif si non exécuté"]),
            ("Jeu de cas de test rejouable",
             ["Identifiant", "Objectif", "Entrée", "Résultat attendu", "Statut"]),
            ("Coûts d'inférence engendrés", ["Phase", "Requêtes", "Coût estimé"])],
   phases=["Cadrage", "Analyse du système", "Modélisation des menaces",
           "Tests adverses", "Évaluation des garde-fous", "Restitution"]),

 "secu-applicative": dict(
   titre="Rapport d'évaluation de sécurité applicative",
   code="RAPPORT", lecteur="Équipe de développement et direction technique",
   refs=[("OWASP ASVS", "<v4.0.3>", "Niveau d'assurance visé"),
         ("OWASP MASVS/MASTG", "<version>", "Applications mobiles"),
         ("OWASP API Security Top 10", "<2023>", "API"),
         ("CWE", "<v4.14>", "Classification"), ("CVSS", "v4.0", "Scoring")],
   champs=[("OWASP ASVS", "V<x.y.z>"), ("OWASP WSTG", "WSTG-<CAT>-<NN>"),
           ("Composant", "<module, endpoint, écran>")],
   sections=[("Niveau d'assurance",
              ["Niveau visé et justification", "Taux de conformité par chapitre ASVS",
               "Écart au niveau visé"])],
   annexes=[("Matrice de conformité ASVS",
             ["Exigence", "Intitulé", "Niveau", "Statut", "Commentaire"]),
            ("Inventaire des dépendances et vulnérabilités connues",
             ["Composant", "Version", "CVE", "Sévérité", "Correctif disponible"])],
   phases=["Cadrage", "Analyse de l'architecture", "Revue des exigences ASVS",
           "Tests dynamiques", "Revue de code", "Restitution"]),

 "devsecops": dict(
   titre="Rapport d'audit de maturité DevSecOps",
   code="RAPPORT", lecteur="Direction technique et équipes de développement",
   refs=[("OWASP SAMM", "2.0", "Modèle de maturité"),
         ("NIST SSDF (SP 800-218)", "1.1", "Pratiques de développement sécurisé"),
         ("SLSA", "<v1.0>", "Chaîne d'approvisionnement"),
         ("CIS Benchmarks", "<version>", "Durcissement des composants")],
   champs=[("Domaine SAMM", "<Gouvernance / Conception / …>"),
           ("Pratique SSDF", "<PO/PS/PW/RV>.<n>"),
           ("Niveau actuel", "<0-3>"), ("Niveau cible", "<0-3>")],
   sections=[("Scores de maturité",
              ["Score global", "Score par domaine SAMM",
               "Comparaison avec le niveau cible", "Évolution depuis l'audit précédent"]),
             ("Chaîne de livraison",
              ["Cartographie de la chaîne actuelle", "Contrôles en place",
               "Temps de traversée et impact des contrôles proposés"])],
   annexes=[("Grille SAMM détaillée",
             ["Domaine", "Pratique", "Niveau actuel", "Niveau cible", "Écart", "Action"]),
            ("Couverture SSDF",
             ["Pratique", "Intitulé", "Statut", "Preuve"]),
            ("Feuille de route",
             ["Horizon", "Action", "Domaine", "Effort", "Gain de maturité"])],
   phases=["Cadrage", "Entretiens", "Analyse de la chaîne", "Revue des dépôts",
           "Notation", "Restitution"]),

 "soc-ai-tools": dict(
   titre="Rapport d'évaluation de la capacité de détection",
   code="RAPPORT", lecteur="Équipe SOC et direction sécurité",
   refs=[("MITRE ATT&CK", "<v15>", "Référentiel de couverture"),
         ("MITRE D3FEND", "<version>", "Contre-mesures"),
         ("SIGMA", "-", "Format des règles produites"),
         ("NIST SP 800-61", "r3", "Réponse à incident")],
   champs=[("Technique ATT&CK", "T<NNNN>.<NNN>"),
           ("Tactique", "<TA…>"), ("Source de journal requise", "<…>"),
           ("Statut de détection", "<absente / partielle / effective>")],
   sections=[("Couverture de détection",
              ["Matrice ATT&CK avant intervention", "Angles morts identifiés",
               "Sources de télémétrie disponibles et manquantes"]),
             ("Qualité opérationnelle",
              ["Taux de faux positifs constaté", "Délai moyen de détection",
               "Charge de triage estimée"])],
   annexes=[("Matrice de couverture ATT&CK",
             ["Tactique", "Technique", "Détection", "Source", "Règle proposée"]),
            ("Règles SIGMA livrées",
             ["Identifiant", "Intitulé", "Technique", "Source", "Statut"]),
            ("Playbooks de réponse", None)],
   phases=["Cadrage", "Inventaire de la télémétrie", "Évaluation de la couverture",
           "Simulation d'adversaire", "Ingénierie de détection", "Restitution"]),

 "x-privacy": dict(
   titre="Rapport d'audit de conformité en protection des données",
   code="RAPPORT", lecteur="Direction, juridique et DPO",
   refs=[("RGPD - Règlement (UE) 2016/679", "-", "Référence"),
         ("Loi togolaise n° 2019-014", "-", "Droit local"),
         ("ISO/IEC 27701", "2019", "Management de la vie privée"),
         ("NIST Privacy Framework", "1.0", "Grille d'analyse")],
   champs=[("Article RGPD", "Art. <n>"), ("Loi n° 2019-014", "Art. <n>"),
           ("ISO 27701", "<mesure>"), ("Traitement concerné", "<…>"),
           ("Niveau de risque pour les personnes", "<faible / moyen / élevé>")],
   sections=[("Cartographie des traitements",
              ["Inventaire", "Bases légales", "Durées de conservation",
               "Destinataires et sous-traitants", "Transferts hors territoire"]),
             ("Droits des personnes",
              ["Information", "Accès, rectification, effacement",
               "Portabilité et opposition", "Délais de réponse constatés"])],
   annexes=[("Registre des traitements",
             ["Traitement", "Finalité", "Base légale", "Catégories de données",
              "Destinataires", "Durée", "Mesures de sécurité"]),
            ("Plan de mise en conformité",
             ["Écart", "Référence", "Action", "Responsable", "Échéance"])],
   phases=["Cadrage", "Entretiens", "Cartographie", "Analyse d'écart",
           "Analyse d'impact si requise", "Restitution"]),

 "sensibilisation": dict(
   titre="Rapport de campagne de sensibilisation",
   code="RAPPORT", lecteur="Direction et ressources humaines",
   refs=[("NIST SP 800-50", "r1", "Programme de sensibilisation"),
         ("ISO/IEC 27001", "2022", "Mesure A.6.3"),
         ("ENISA", "-", "Supports et bonnes pratiques")],
   champs=[("Population concernée", "<service, effectif>"),
           ("Type d'exercice", "<hameçonnage / atelier / module>"),
           ("Indicateur", "<taux de clic / de signalement / de saisie>")],
   sections=[("Résultats de la campagne",
              ["Taux de clic", "Taux de saisie d'identifiants",
               "Taux de signalement", "Délai moyen de signalement",
               "Comparaison avec la campagne précédente"]),
             ("Analyse par population",
              ["Résultats agrégés par service", "Facteurs explicatifs"])],
   annexes=[("Contenu des exercices", None),
            ("Programme de l'année suivante",
             ["Trimestre", "Action", "Population", "Objectif mesurable"])],
   phases=["Cadrage", "Conception des contenus", "Exercice",
           "Mesure", "Débriefing", "Restitution"]),

 "infra-vpn-cloudflare": dict(
   titre="Rapport d'audit de durcissement d'infrastructure",
   code="RAPPORT", lecteur="Équipe infrastructure et direction technique",
   refs=[("CIS Benchmarks", "<version par produit>", "Référentiel de durcissement"),
         ("Guides ANSSI", "-", "Recommandations complémentaires"),
         ("CIS Controls", "v8", "Grille de maturité"),
         ("NIST SP 800-207", "-", "Architecture zéro confiance")],
   champs=[("Mesure CIS", "<n.n.n>"), ("Niveau CIS", "<L1 / L2>"),
           ("Système concerné", "<hôte, rôle>"),
           ("Correctif automatisable", "<oui / non>")],
   sections=[("Scores de conformité",
              ["Score global par système", "Score par chapitre CIS",
               "Comparaison avant / après si remédiation réalisée"]),
             ("Architecture et segmentation",
              ["Schéma de l'existant", "Matrice des flux constatée",
               "Écarts à l'architecture cible"])],
   annexes=[("Grille CIS détaillée",
             ["Mesure", "Intitulé", "Niveau", "Système", "Statut", "Correctif"]),
            ("Matrice des flux",
             ["Source", "Destination", "Port", "Protocole", "Justification", "Statut"]),
            ("Playbooks de durcissement livrés", None)],
   phases=["Cadrage", "Collecte des configurations", "Analyse d'écart",
           "Remédiation si au contrat", "Contre-mesure", "Restitution"]),
}


def rapport(slug: str, d: dict, chemin: str) -> None:
    doc = nouveau_document()
    couverture(doc, d["titre"], "<Périmètre de la mission>",
               [["Client", "<Raison sociale>"],
                ["Référence", f"<AAAAMMJJ-CLIENT-{d['code']}-titre-v1.0>"],
                ["Version", "v1.0"],
                ["Date", "<AAAA-MM-JJ>"],
                ["Auteurs", "<Noms>"],
                ["Relecteurs", "<Noms>"],
                ["Service", slug],
                ["Doctrine appliquée", f"{slug} v<X.Y>"],
                ["Destinataires", d["lecteur"]],
                ["Classification", CONFIDENTIEL]],
               "Ce document contient des informations sur la sécurité des systèmes "
               "du Client. Sa diffusion est strictement limitée aux destinataires "
               "désignés en annexe.")
    doc.add_page_break()
    sommaire(doc)
    doc.add_page_break()

    # --- Synthèse exécutive
    doc.add_heading("Synthèse exécutive", level=1)
    consigne(doc, "Deux pages maximum, sans jargon, lisibles par un dirigeant qui "
                  "n'ouvrira pas le reste du document.")
    for t, aide in [("Contexte et objectif", "Pourquoi cette mission, à la demande "
                     "de qui, dans quel cadre."),
                    ("Verdict", "Une phrase, orientée impact métier."),
                    ("Appréciation globale", "Posture générale et points forts "
                     "constatés - il y en a toujours, et les citer crédibilise "
                     "les critiques.")]:
        doc.add_heading(t, level=2)
        doc.add_paragraph(f"<{aide}>")

    doc.add_heading("Constatations en un coup d'œil", level=2)
    tableau(doc, ["Sévérité", "Nombre", "Délai de correction recommandé"],
            [["Critique", "0", "Immédiat (< 72 h)"], ["Élevée", "0", "30 jours"],
             ["Moyenne", "0", "90 jours"], ["Faible", "0", "Prochain cycle"],
             ["Information", "0", "Aucune obligation"]],
            largeurs=[4, 3, 9])

    doc.add_heading("Les trois priorités", level=2)
    for i in range(1, 4):
        doc.add_paragraph(f"<Titre {i}> - <impact métier> → <action> - <effort>",
                          style="List Number")
    doc.add_page_break()

    # --- Cadre
    doc.add_heading("1. Cadre de la mission", level=1)
    doc.add_heading("1.1 Périmètre", level=2)
    tableau(doc, ["#", "Élément évalué", "Type", "Identifiant", "Environnement"],
            [["1", "<…>", "<…>", "<…>", "<…>"]],
            largeurs=[1.2, 4, 3.3, 4.5, 3])
    doc.add_heading("1.2 Périmètre exclu", level=2)
    doc.add_paragraph("<Ce qui n'a pas été évalué, et pourquoi.>")

    doc.add_heading("1.3 Cadre contractuel et légal", level=2)
    tableau(doc, ["Élément", "Référence"],
            [["Accord de confidentialité", "<référence, date>"],
             ["Contrat-cadre / énoncé des travaux", "<référence, date>"],
             ["Règles d'engagement", "<référence, version>"],
             ["Autorisation signée", "<signataire, fonction, date>"],
             ["Droit applicable", "<Togo - loi n° 2018-026 / autre>"]],
            largeurs=[6, 10])

    doc.add_heading("1.4 Référentiels appliqués", level=2)
    tableau(doc, ["Référentiel", "Version", "Usage dans la mission"],
            [[r, v, u] for r, v, u in d["refs"]], largeurs=[5.5, 3, 7.5])

    doc.add_heading("1.5 Phases réalisées", level=2)
    tableau(doc, ["Phase", "Période", "Contenu"],
            [[p, "<du … au …>", "<…>"] for p in d["phases"]],
            largeurs=[5, 3.5, 7.5])

    doc.add_heading("1.6 Équipe", level=2)
    tableau(doc, ["Nom", "Rôle", "Période"],
            [["<…>", "Chef de mission", "<…>"], ["<…>", "Intervenant", "<…>"],
             ["<…>", "Relecteur qualité", "<…>"]], largeurs=[5.5, 5, 5.5])

    doc.add_heading("1.7 Limites de l'évaluation", level=2)
    consigne(doc, "Section de protection - ne jamais la supprimer, même vide.")
    doc.add_paragraph("<Ce qui n'a pas pu être évalué et pourquoi.>")
    doc.add_paragraph(
        "Cette évaluation porte sur un périmètre délimité, à un instant donné. "
        "L'absence de constatation sur un élément ne garantit pas son absence de "
        "faiblesse.")

    doc.add_heading("1.8 Échelle de sévérité", level=2)
    tableau(doc, ["Sévérité", "CVSS v4.0", "Définition"],
            [["Critique", "9.0 - 10.0", "Compromission immédiate, impact majeur"],
             ["Élevée", "7.0 - 8.9", "Compromission avec un prérequis réaliste"],
             ["Moyenne", "4.0 - 6.9", "Impact limité ou exploitation conditionnée"],
             ["Faible", "0.1 - 3.9", "Impact marginal"],
             ["Information", "0.0", "Observation sans impact direct"]],
            largeurs=[3, 3, 10])
    doc.add_page_break()

    # --- Sections métier
    numero = 2
    for titre, sous in d["sections"]:
        doc.add_heading(f"{numero}. {titre}", level=1)
        for i, s in enumerate(sous, start=1):
            doc.add_heading(f"{numero}.{i} {s}", level=2)
            doc.add_paragraph("<…>")
        numero += 1
        doc.add_page_break()

    # --- Constatations
    doc.add_heading(f"{numero}. Constatations détaillées", level=1)
    consigne(doc, "Une sous-section par constatation, par sévérité décroissante. "
                  "Dupliquer le bloc ci-dessous autant que nécessaire.")
    doc.add_heading(f"{numero}.1 <CLIENT>-2026-001 - <titre orienté impact>", level=2)
    lignes = [["Identifiant", "<CLIENT>-2026-001"], ["Sévérité", "Critique"],
              ["Score CVSS v4.0", "<9.3>"], ["Vecteur CVSS", "<CVSS:4.0/…>"],
              ["Criticité métier", "<si différente : justifier>"],
              ["Élément affecté", "<…>"], ["CWE", "CWE-<000>"]]
    lignes += [[k, v] for k, v in d["champs"]]
    lignes += [["Statut", "Ouverte"], ["Constatée par", "<nom>"],
               ["Date", "<AAAA-MM-JJ>"]]
    tableau(doc, ["Champ", "Valeur"], lignes, largeurs=[5.5, 10.5])

    for t, aide in [("Description", "Le problème en clair, avant tout détail technique."),
                    ("Conditions d'exploitation", "Position de l'attaquant, "
                     "authentification requise, interaction utilisateur, complexité."),
                    ("Impact métier", "La section qui justifie la facture. Chiffrer."),
                    ("Preuve de concept", "Reproductible pas à pas. Aucune donnée "
                     "personnelle réelle. Les preuves brutes restent au coffre."),
                    ("Recommandation", "Distinguer la mesure d'urgence du correctif "
                     "de fond. Ne jamais présenter un contournement comme une correction."),
                    ("Détection", "Comment le client détecte cette attaque demain."),
                    ("Références externes", "CVE, avis éditeur, publication.")]:
        doc.add_heading(t, level=3)
        consigne(doc, aide)
        doc.add_paragraph("<…>")
    numero += 1
    doc.add_page_break()

    doc.add_heading(f"{numero}. Constatations hors référentiel", level=1)
    consigne(doc, "Ce que la checklist ne prévoyait pas. Une section vide sur "
                  "plusieurs missions d'affilée est un signal d'alerte interne.")
    doc.add_paragraph("<…>")
    numero += 1

    doc.add_heading(f"{numero}. Plan d'action", level=1)
    tableau(doc, ["#", "Constatation", "Sévérité", "Action", "Effort", "Délai",
                  "Responsable"],
            [["1", "<…>", "Critique", "<…>", "<…>", "< 72 h", "<…>"]],
            largeurs=[1, 3.4, 2.2, 3.4, 1.8, 2, 2.2])
    doc.add_paragraph(
        "Contre-vérification : <prévue le … / non prévue au contrat>. Elle porte "
        "uniquement sur les constatations du présent rapport.")
    doc.add_page_break()

    # --- Annexes
    lettres = "ABCDEFGHIJ"
    idx = 0
    for titre, entetes in d["annexes"]:
        doc.add_heading(f"Annexe {lettres[idx]} - {titre}", level=1)
        if entetes:
            largeur = 16 / len(entetes)
            tableau(doc, entetes, [["<…>"] * len(entetes)],
                    largeurs=[largeur] * len(entetes))
        else:
            doc.add_paragraph("<…>")
        idx += 1

    doc.add_heading(f"Annexe {lettres[idx]} - Conformité et rattachement réglementaire",
                    level=1)
    consigne(doc, "Transforme le rapport en pièce d'audit pour les clients soumis "
                  "à une obligation. Indicatif : ne constitue pas un audit de "
                  "conformité ni un avis juridique.")
    tableau(doc, ["Constatation", "ISO 27001", "Exigence locale", "RGPD", "Commentaire"],
            [["<…>", "A.<n>.<n>", "<Loi 2018-026 / règles ANCy>", "<Art. 32>", "<…>"]],
            largeurs=[3.2, 2.6, 4, 2.4, 3.8])
    idx += 1

    doc.add_heading(f"Annexe {lettres[idx]} - Outillage", level=1)
    tableau(doc, ["Outil", "Version", "Usage", "Phase"],
            [["<…>", "<…>", "<…>", "<…>"]], largeurs=[4, 3, 6, 3])
    idx += 1

    doc.add_heading(f"Annexe {lettres[idx]} - Manifeste des preuves", level=1)
    doc.add_paragraph(
        "Preuves conservées chiffrées, hors du présent document. Destruction "
        "prévue le <date de remise + 90 jours>, actée par certificat.")
    tableau(doc, ["Fichier", "Description", "SHA-256"],
            [["<…>", "<…>", "<…>"]], largeurs=[4.5, 5.5, 6])
    idx += 1

    doc.add_heading(f"Annexe {lettres[idx]} - Glossaire", level=1)
    tableau(doc, ["Terme", "Définition"], [["<…>", "<…>"]], largeurs=[4, 12])
    idx += 1

    doc.add_heading(f"Annexe {lettres[idx]} - Diffusion et confidentialité", level=1)
    tableau(doc, ["Destinataire", "Fonction", "Date de remise", "Format"],
            [["<…>", "<…>", "<…>", "PDF chiffré"]], largeurs=[4.5, 4.5, 3.5, 3.5])
    doc.add_paragraph(
        f"Document classé {CONFIDENTIEL}. Toute diffusion hors de la liste "
        "ci-dessus requiert l'accord écrit du Client.")

    pied_de_page(doc.sections[0], f"<CLIENT> - {d['titre']} - {CONFIDENTIEL}")
    doc.save(chemin); print("écrit", chemin)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="90-templates/build/livrables")
    ap.add_argument("--service", help="ne générer que ce service")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for slug, d in SERVICES.items():
        if a.service and a.service != slug:
            continue
        rapport(slug, d, os.path.join(a.out, f"Modele-rapport-{slug}.docx"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
