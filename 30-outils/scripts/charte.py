"""Charte graphique partagée par tous les générateurs de documents.

Source unique de vérité pour les couleurs, les polices et les libellés.
Modifier ici change DOCX, XLSX et PPTX d'un coup.
Voir 90-templates/design/charte.md pour la justification.
"""

# --- Palette -----------------------------------------------------------------
PRIMAIRE      = "0B1220"   # bleu nuit : titres 1, bandeaux, couverture
SECONDAIRE    = "1E293B"   # ardoise : titres 2 et 3, filets
ACCENT        = "06B6D4"   # cyan : liens, mises en avant
TEXTE         = "0F172A"
TEXTE_FAIBLE  = "475569"   # légendes, notes
FOND_ALTERNE  = "F1F5F9"   # lignes paires de tableau
BLANC         = "FFFFFF"
BORDURE       = "CBD5E1"

# --- Sévérités : couleurs figées, jamais modifiées ---------------------------
SEVERITES = {
    "Critique":    {"fond": "991B1B", "texte": BLANC},
    "Élevée":      {"fond": "C2410C", "texte": BLANC},
    "Moyenne":     {"fond": "A16207", "texte": BLANC},
    "Faible":      {"fond": "0369A1", "texte": BLANC},
    "Information": {"fond": "475569", "texte": BLANC},
    "Corrigée":    {"fond": "15803D", "texte": BLANC},
}
ORDRE_SEVERITES = list(SEVERITES)

STATUTS_VULN = ["Ouverte", "En cours", "Corrigée", "Acceptée", "Faux positif"]

# --- Typographie -------------------------------------------------------------
POLICE_TITRE = "Inter"
POLICE_CORPS = "Inter"
POLICE_MONO  = "JetBrains Mono"
# Replis : le poste du client n'aura pas Inter installé.
REPLI_SANS   = "Calibri"
REPLI_MONO   = "Consolas"

TAILLES = {"t1": 20, "t2": 16, "t3": 13, "corps": 10.5, "petit": 9, "mono": 9.5}

SOCIETE = "NexShield"
BASELINE = "Next Threat. Next Shield."
CLASSIFICATION = "CONFIDENTIEL - DIFFUSION RESTREINTE"


def rgb(hexa: str) -> tuple[int, int, int]:
    """'0B1220' -> (11, 18, 32)"""
    return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4))
