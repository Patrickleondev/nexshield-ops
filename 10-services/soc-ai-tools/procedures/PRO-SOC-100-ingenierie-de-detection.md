# PRO-SOC-100 - Ingénierie de détection

**Version** : v0.1 · **Service** : `soc-ai-tools` · **Phase** : exécution
**Responsable** : ingénieur détection · **Sortant** : règles éprouvées + couverture mesurée

**Préalable bloquant** : `PRO-SOC-001` close, sources vérifiées, techniques priorisées.

---

## Principe

**Une règle qui n'a jamais été déclenchée volontairement n'est pas une règle,
c'est une hypothèse.**

Le cycle est le même pour chaque technique retenue, et aucune étape ne se saute :

```
1. Comprendre la technique      -> ATT&CK
2. Identifier la trace          -> quelle source, quel champ
3. Vérifier que la trace existe -> dans les journaux du client
4. Écrire la règle              -> format SIGMA
5. Déclencher l'attaque         -> autorisation écrite obligatoire
6. Mesurer                      -> détectée, partielle, absente
7. Régler le bruit              -> avant mise en service
8. Écrire la conduite à tenir   -> une alerte sans procédure est du bruit
```

Une règle livrée sans l'étape 8 sera ignorée par l'équipe qui la reçoit.

---

## 1. Écrire en SIGMA

Format retenu : [SIGMA](https://github.com/SigmaHQ/sigma), Sigma HQ.

Raison : la règle est écrite une fois et se convertit vers la plateforme du
client. Si le client change de SIEM, notre travail ne se perd pas - c'est un
argument commercial, à dire au cadrage.

Contenu obligatoire de chaque règle :

| Champ | Contenu |
|---|---|
| `title` | Ce qui est détecté, en clair |
| `id` | Identifiant unique et stable |
| `status` | `experimental` jusqu'à l'épreuve réussie |
| `description` | Ce que la règle détecte, et ce qu'elle ne détecte pas |
| `references` | Page ATT&CK, source publique |
| `logsource` | Source précise, vérifiée présente |
| `detection` | La logique |
| `falsepositives` | **Renseigné.** Un champ vide signifie « non étudié » |
| `level` | Sévérité, selon l'échelle unique de `NOMENCLATURE.md` §4 |
| `tags` | `attack.tNNNN`, tactique |

## 2. Éprouver la règle

Autorisation écrite obligatoire, distincte du RoE principal.

- Déclencher la technique dans un environnement convenu
- Vérifier que l'alerte se lève, avec les bons champs
- Vérifier le délai entre l'action et l'alerte
- **Vérifier une variante** : une règle qui ne détecte qu'une seule commande
  précise est une règle « partielle », pas une règle « détectée »

Notation, en trois états :

| État | Condition |
|---|---|
| Détectée | La règle se déclenche sur la technique **et** sur au moins une variante |
| Partielle | Se déclenche sur un cas précis seulement, ou n'a pas été éprouvée |
| Absente | Aucune règle, ou trace inexistante dans les journaux |

## 3. Régler le bruit

**Avant mise en service, jamais après.**

- Mesurer le volume d'alertes sur sept jours d'historique
- Une règle produisant plus de cinq alertes par jour sur un parc normal est à
  affiner, pas à livrer
- Exclusions écrites et justifiées, jamais silencieuses
- Chaque exclusion est datée et porte un motif : une exclusion sans motif devient
  un angle mort permanent

> Le bruit ne dégrade pas seulement une règle, il dégrade toutes les autres.
> Une équipe qui reçoit trop d'alertes cesse de les lire.

## 4. Écrire la conduite à tenir

Une règle se livre avec sa fiche de réponse. Sans elle, l'alerte ne sert à rien.

| Section | Contenu |
|---|---|
| Ce qui s'est passé | En une phrase, compréhensible à 3 h du matin |
| Vérifier | Trois contrôles concrets, dans l'ordre |
| Faux positif probable si | Les cas légitimes connus |
| Si confirmé | Les actions, dans l'ordre, avec qui prévenir |
| Ne pas faire | Ce qui détruirait la preuve |

Référentiel de réponse :
[NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

## 5. Mesurer la couverture

Sortant du service, et seul chiffre qui compte :

| Indicateur | Ce qu'il dit |
|---|---|
| Techniques détectées / techniques priorisées | Le progrès réel |
| Techniques partielles | La dette, à traiter au prochain cycle |
| Techniques absentes faute de source | **La priorité de collecte**, pas de détection |

La dernière ligne est celle qui oriente le budget suivant : elle démontre qu'il
faut collecter avant d'écrire.

Représentation : matrice ATT&CK colorée avec l'échelle unique de la société.
La couleur n'est jamais seule porteuse d'information.

## 6. Défense

Pour les recommandations de durcissement associées à chaque technique :
[MITRE D3FEND](https://d3fend.mitre.org/). Une règle de détection se double
toujours d'une proposition de réduction de surface - détecter est un pis-aller
quand on peut empêcher.

---

## Règles d'exécution

- Aucune simulation d'attaque sans autorisation écrite et fenêtre convenue.
- Aucun extrait de journal client hors du coffre chiffré.
- Les journaux contiennent des données personnelles : la loi togolaise
  n° 2019-014 s'applique, minimisation comprise.
- Journal des opérations horodaté, y compris pour les actions passant par un
  outil automatique ou un serveur MCP.

---

## Critères de sortie

- [ ] Chaque technique priorisée a été traitée par le cycle complet
- [ ] Chaque règle est écrite en SIGMA, avec `falsepositives` renseigné
- [ ] Chaque règle a été déclenchée volontairement, et sur une variante
- [ ] Bruit mesuré sur sept jours, exclusions datées et motivées
- [ ] Chaque règle est livrée avec sa fiche de conduite à tenir
- [ ] Couverture mesurée en trois états, jamais en deux
- [ ] Techniques absentes faute de source listées comme priorité de collecte
- [ ] Recommandations de durcissement rattachées à D3FEND
- [ ] Extraits de journaux détruits, certificat produit
