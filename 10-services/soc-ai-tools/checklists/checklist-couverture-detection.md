# Checklist - couverture de détection

**Version** : v0.1 · Se recopie dans l'annexe du rapport de couverture.

**Référentiels** : [MITRE ATT&CK](https://attack.mitre.org/) ·
[SIGMA](https://github.com/SigmaHQ/sigma) ·
[MITRE D3FEND](https://d3fend.mitre.org/) ·
[NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

**Notation en trois états**, jamais en deux : **Détectée**, **Partielle**,
**Absente**. Compter les partielles comme couvertes est la façon dont on obtient
des taux flatteurs et faux.

---

## 1. Sources de journaux

Aucune règle ne s'écrit avant que cette section soit entièrement cochée.

- [ ] Chaque source déclarée vérifiée par un événement réel retrouvé
- [ ] Rétention réelle mesurée, pas celle de la documentation
- [ ] Horloges synchronisées entre les sources
- [ ] Champs nécessaires présents et non tronqués
- [ ] Volume quotidien mesuré, coût connu du client
- [ ] Taux de déploiement réel de l'EDR sur le parc, vérifié

## 2. Couverture par tactique ATT&CK

| Tactique | Priorisées | Détectées | Partielles | Absentes |
|---|---|---|---|---|
| Reconnaissance | | | | |
| Développement de ressources | | | | |
| Accès initial | | | | |
| Exécution | | | | |
| Persistance | | | | |
| Élévation de privilèges | | | | |
| Contournement des défenses | | | | |
| Accès aux identifiants | | | | |
| Découverte | | | | |
| Déplacement latéral | | | | |
| Collecte | | | | |
| Commande et contrôle | | | | |
| Exfiltration | | | | |
| Impact | | | | |

## 3. Par règle produite

- [ ] Écrite en SIGMA, convertible vers la plateforme du client
- [ ] `logsource` correspond à une source vérifiée présente
- [ ] `falsepositives` renseigné - un champ vide signifie « non étudié »
- [ ] `tags` porte l'identifiant `attack.tNNNN`
- [ ] `level` selon l'échelle de sévérité unique (`NOMENCLATURE.md` §4)
- [ ] Déclenchée volontairement, avec autorisation écrite
- [ ] Éprouvée sur **au moins une variante** de la technique
- [ ] Délai entre action et alerte mesuré
- [ ] Bruit mesuré sur sept jours d'historique
- [ ] Moins de cinq alertes par jour sur un parc normal
- [ ] Exclusions écrites, datées, motivées
- [ ] Fiche de conduite à tenir rédigée
- [ ] Durcissement associé proposé, rattaché à D3FEND

## 4. Réponse à incident

- [ ] Une procédure de réponse écrite existe
- [ ] Qui reçoit l'alerte hors heures ouvrées est écrit, avec un nom
- [ ] Chaîne d'escalade définie, avec des délais
- [ ] Conduite de préservation des preuves écrite
- [ ] Obligations de notification identifiées : ANCy et CERT.tg pour le Togo,
      IPDCP en cas de données personnelles

## 5. Ce qui manque faute de collecte

À remplir explicitement. C'est ce qui oriente le budget de l'année suivante.

| Technique | Source manquante | Coût estimé de la collecte |
|---|---|---|
| | | |

---

## Avant de clore

- [ ] Couverture affichée en trois états, avec l'écart au périmètre priorisé
- [ ] Aucune technique partielle comptée comme détectée
- [ ] Toutes les règles remises dans un format que le client peut modifier
- [ ] Chaque règle accompagnée de sa fiche de réponse
- [ ] Priorités de collecte listées et chiffrées
- [ ] Extraits de journaux détruits, certificat produit
- [ ] Double relecture effectuée
