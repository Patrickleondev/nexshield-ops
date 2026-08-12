#!/usr/bin/env bash
# Crée le squelette d'une mission. Usage : nouvelle-mission.sh CLIENT TYPE
set -euo pipefail

CLIENT="${1:?Usage: nouvelle-mission.sh CLIENT TYPE}"
TYPE="${2:?Usage: nouvelle-mission.sh CLIENT TYPE}"
ANNEE="$(date +%Y)"
RACINE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# Numéro d'ordre : première place libre pour ce client et ce type cette année
n=1
while [ -d "$RACINE/20-missions/$ANNEE/$CLIENT-$TYPE-$(printf '%02d' $n)" ]; do
  n=$((n+1))
done
NN="$(printf '%02d' $n)"
DIR="$RACINE/20-missions/$ANNEE/$CLIENT-$TYPE-$NN"

mkdir -p "$DIR"/{roe,rapport}

# Les gabarits sont des DOCX generes. On les regenere si besoin, puis on copie.
BUILD="$RACINE/90-templates/build"
if [ ! -f "$BUILD/juridique/Modele-ROE-regles-engagement.docx" ]; then
  ( cd "$RACINE" && make modeles >/dev/null )
fi
cp "$BUILD/juridique/Modele-ROE-regles-engagement.docx"   "$DIR/roe/"
cp "$BUILD/juridique/Modele-AUTH-autorisation-de-test.docx" "$DIR/roe/"
cp "$BUILD/juridique/Modele-SOW-enonce-des-travaux.docx"   "$DIR/roe/"
if [ -f "$BUILD/livrables/Modele-rapport-$TYPE.docx" ]; then
  cp "$BUILD/livrables/Modele-rapport-$TYPE.docx" "$DIR/rapport/"
else
  cp "$BUILD/livrables/Modele-rapport-pentest-audit.docx" "$DIR/rapport/"
  echo "Note : pas de gabarit propre au service '$TYPE', gabarit pentest copie."
fi
cp "$BUILD/Classeur-mission.xlsx"        "$DIR/"
cp "$BUILD/Modele-restitution.pptx"      "$DIR/rapport/"

cat > "$DIR/README.md" <<FICHE
# $CLIENT - $TYPE #$NN

| | |
|---|---|
| **Statut** | prospect |
| **Chef de mission** | <à définir> |
| **Équipe** | <à définir> |
| **Doctrine appliquée** | \`$TYPE v<X.Y>\` |
| **Ouverture** | $(date +%Y-%m-%d) |
| **Destruction des preuves** | <date de livraison + 90 j> |

## Périmètre

<résumé ; le détail contractuel est dans roe/>

## Préalables bloquants

- [ ] NDA signé
- [ ] MSA / SOW signé
- [ ] RoE validé par les deux parties
- [ ] **Autorisation de test signée** par une personne ayant autorité
- [ ] Autorisation / notification de l'hébergeur si actifs chez un tiers
- [ ] Contacts d'urgence 24/7 échangés
- [ ] Coffre à preuves provisionné

> Tant qu'une case est décochée, **aucune commande n'est lancée**.

## Journal

| Date | Événement |
|---|---|
FICHE

cat > "$DIR/retex.md" <<'RETEX'
# Retour d'expérience

Obligatoire à la clôture, **y compris quand la mission s'est bien passée**.
C'est la boucle de rétroaction qui maintient la doctrine vivante.

## Ce qui a bien marché

## Ce qui a manqué dans la méthodologie

> Chaque point ici doit devenir une PR sur `10-services/<service>/`.

## Écarts entre l'estimation et le temps réel

## Outils à ajouter ou à retirer

## Retour du client

## Actions

| # | Action | Responsable | Échéance |
|---|---|---|---|
RETEX

touch "$DIR/preuves.sha256"
echo "Mission créée : 20-missions/$ANNEE/$CLIENT-$TYPE-$NN"
echo "→ Commencez par les préalables bloquants du README."
