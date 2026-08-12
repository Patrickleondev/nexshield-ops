#!/usr/bin/env python3
"""Classe un export de favoris de navigateur (Netscape HTML) dans 40-veille/.

Usage : python3 30-outils/scripts/classer-veille.py <export.html> [--out 40-veille]

Les dossiers de favoris sans rapport avec la sécurité (études, emploi, loisirs,
certifications personnelles) sont exclus : voir EXCLUS.
"""
from __future__ import annotations
import argparse, html, os, re, sys
from collections import defaultdict

# ─── Dossiers de favoris → fichier de veille ────────────────────────────────
MAPPING: dict[str, str] = {}


def _m(cible: str, *dossiers: str) -> None:
    for d in dossiers:
        MAPPING[d.lower()] = cible


_m("pentest-audit",
   "RedTeaming", "AD_Pentesting", "Pentesting", "Pentesting_reports_templates",
   "Windows Privesc", "Pwn", "Tools", "Tools and Cheat Sheet", "Mes_Outils",
   "Online_Tool", "X.Tools_Projects", "OSINT", "Stegano", "Malware_dev")
_m("ai-redteaming",
   "AI RedTeaming", "HTB_AI_RedTeaming", "AI AGENTS_4_BOUNTY", "Cyber AI",
   "Models", "Recherches FUTURE AI")
_m("secu-applicative",
   "PortSwigger", "bug hunting wp", "WriteUps", "Other Write up",
   "Intigriti_Bug_Bounty", "Web_CTF_challs", "Android Security", "Pentesting_web")
_m("soc-ai-tools",
   "SIEM Cours Ressources", "Wazuh", "Blue Teaming & Labs", "Threat Intelligence",
   "Forensics", "Reverse", "CVEs_PoCs", "Veilles")
_m("devsecops",
   "DevOps", "Kubernetes Traning", "Cloud", "Cloud SEC",
   "Automation - n8n - Cyber - projects", "MCP_Learning", "Microsoft MCP",
   "Systeme_Admin", "Linux", "Frappe", "Rust_Programming", "JAVA")
_m("outillage-ia",
   "BREAKING AI", "AI Tools and projects", "AI Tooling", "AI_Prompt_Engineering",
   "Analytics Vidhya", "AWS_AI_Learning")
_m("montee-competence",
   "My_Training", "TryHackme", "HTB", "HackTheBox", "VulnLabs", "rootme",
   "Challenges", "Wow All CTFs", "CTFs", "CTFs_Tools", "CTFs_Preps",
   "Réseau, simulations de Labs", "Sidequests&hard rooms", "Krauq&CTF",
   "ECOWAS_CTF_2026_Ressources", "Crypto_et_Maths", "SKILLS", "Cybersecurity_Courses",
   "Cyber Projects", "Projets_Stage_Cybersec", "Cisco Netacad", "Microsoft_Learning")
_m("references-et-blogs",
   "Cyber_Blogs", "Articles&Cyber", "X_Bookmarks", "Club_and_Resources", "ICDFA")
_m("societe", "StartingUp_Business")

# ─── Exclus : sans rapport avec l'activité (demande explicite) ──────────────
EXCLUS = {d.lower() for d in (
    "CY CERGY", "France", "PARIS_LIFE", "Lingua Sklills Prepa", "JOBS", "Films",
    "Livres", "Africa TechUp Tour", "GOOGLE", "Simplon", "GPA-ISC2",
    "Notes_Certifications", "CERTS", "Fortinet_Certs", "Certifications & Learning",
    "Master_Ressources", "PPE", "Stories_BLK", "Crypto", "Jekyll_theme",
    "Cyber Projects perso",
)}

# Racines de l'export : ne rien exclure ni classer ici, tout part au tri manuel.
_m("a-trier", "Barre des favoris", "Other Bookmarks", "Synced Bookmarks")

TITRES = {
    "pentest-audit": "Pentest & audit — outils et ressources",
    "ai-redteaming": "AI RedTeaming — outils et ressources",
    "secu-applicative": "Sécurité applicative — outils et ressources",
    "soc-ai-tools": "SOC & défensif — outils et ressources",
    "devsecops": "DevSecOps & infrastructure — outils et ressources",
    "outillage-ia": "Outillage IA généraliste",
    "montee-competence": "Montée en compétence — labs, CTF, entraînement",
    "references-et-blogs": "Références, blogs et veille",
    "societe": "Création et gestion de la société",
    "a-trier": "À trier",
}


# Un export de favoris contient des URL de session : jetons OAuth, JWT, clés de
# partage. Ils ne doivent pas entrer dans le dépôt — voir SECURITY.md §1.
SENSIBLES = re.compile(
    r"(?:^|[?&#])(?:id_token|access_token|refresh_token|token|auth|key|"
    r"api[_-]?key|secret|password|passwd|pwd|session|sig|signature|code)="
    r"[^&#]+", re.I)


def assainir(url: str) -> tuple[str, bool]:
    """Retire les paramètres porteurs de jetons. Rend (url, a_ete_nettoyee)."""
    propre = SENSIBLES.sub(lambda m: m.group(0)[0] if m.group(0)[0] in "?&#" else "", url)
    # Recolle proprement les séparateurs laissés par la substitution.
    propre = re.sub(r"[?&#]+$", "", re.sub(r"([?&#])[&#]+", r"\1", propre))
    return propre, propre != url


def parcourir(chemin: str):
    """Rend (dossiers, url, titre) pour chaque favori, en suivant l'imbrication."""
    with open(chemin, encoding="utf-8", errors="replace") as fh:
        brut = fh.read()
    motif = re.compile(
        r'<DT><H3[^>]*>(.*?)</H3>|<DT><A HREF="(.*?)"[^>]*>(.*?)</A>|(</DL>)',
        re.I | re.S)
    pile: list[str] = []
    for dossier, url, titre, fermeture in motif.findall(brut):
        if dossier:
            pile.append(html.unescape(re.sub(r"<[^>]+>", "", dossier)).strip())
        elif fermeture:
            if pile:
                pile.pop()
        elif url:
            propre = html.unescape(re.sub(r"<[^>]+>", "", titre)).strip()
            yield list(pile), html.unescape(url), propre or url


def cible(pile: list[str]) -> str | None:
    """Fichier de destination, ou None si le favori est exclu."""
    # Le dossier le plus profond gagne : c'est le plus spécifique.
    for nom in reversed(pile):
        bas = nom.lower()
        if bas in EXCLUS:
            return None
        if bas in MAPPING:
            return MAPPING[bas]
    return "a-trier"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--out", default="40-veille")
    args = ap.parse_args()

    if not os.path.isfile(args.export):
        print(f"Introuvable : {args.export}", file=sys.stderr)
        return 1

    groupes: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    vus: set[str] = set()
    exclus = doublons = nettoyes = 0

    for pile, url, titre in parcourir(args.export):
        if not url.startswith(("http://", "https://")):
            continue
        url, modifiee = assainir(url)
        nettoyes += modifiee
        dest = cible(pile)
        if dest is None:
            exclus += 1
            continue
        if url in vus:
            doublons += 1
            continue
        vus.add(url)
        origine = pile[-1] if pile else "(racine)"
        groupes[dest][origine].append((titre, url))

    os.makedirs(args.out, exist_ok=True)
    total = 0
    for dest, sections in sorted(groupes.items()):
        n = sum(len(v) for v in sections.values())
        total += n
        lignes = [
            f"# {TITRES.get(dest, dest)}",
            "",
            f"> {n} entrées, issues de l'export de favoris. Classement automatique",
            f"> (`30-outils/scripts/classer-veille.py`) — **à relire et élaguer à la main**.",
            "",
        ]
        for origine, items in sorted(sections.items()):
            lignes += [f"## {origine}", ""]
            for titre, url in sorted(items, key=lambda x: x[0].lower()):
                propre = titre.replace("|", "\\|").replace("[", "(").replace("]", ")")
                lignes.append(f"- [{propre}]({url})")
            lignes.append("")
        chemin = os.path.join(args.out, f"{dest}.md")
        with open(chemin, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lignes))
        print(f"{n:5d}  {chemin}")

    print(f"\n{total} conservés · {exclus} exclus (hors sécurité) · {doublons} doublons"
          f" · {nettoyes} URL expurgées de leurs jetons")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
