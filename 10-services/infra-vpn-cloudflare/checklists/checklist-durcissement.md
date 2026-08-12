# Checklist - durcissement d'infrastructure

**Version** : v0.1 · Se recopie dans l'annexe du rapport d'intervention.

**Référentiels** : [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) ·
[Guides de l'ANSSI](https://cyber.gouv.fr/publications) ·
[NIST SP 800-207 Zero Trust](https://csrc.nist.gov/pubs/sp/800/207/final) ·
[MITRE ATT&CK](https://attack.mitre.org/)

**Règle unique** : un changement, une fenêtre, un retour arrière.

---

## 0. Avant toute intervention

- [ ] Sauvegarde récente pour chaque système touché
- [ ] **Restauration déjà testée**, pas seulement sauvegarde effectuée
- [ ] Fenêtre, personne à joindre et critère d'arrêt écrits
- [ ] Retour arrière écrit avant le changement
- [ ] Niveau CIS visé arrêté, service par service

## 1. Exposition

- [ ] Inventaire réel établi par balayage, comparé au déclaré
- [ ] **Aucune interface d'administration joignable depuis Internet**
- [ ] Services exposés sans justification métier : fermés
- [ ] Environnements de test et de recette non exposés
- [ ] Certificats valides, couvrants, renouvellement automatique
- [ ] Enregistrements DNS obsolètes supprimés

## 2. Accès et identité

- [ ] Second facteur sur tous les accès distants
- [ ] Second facteur sur les comptes à privilèges
- [ ] **Aucune exception, direction comprise**
- [ ] Accès distant donné par application, pas au réseau entier
- [ ] Comptes de prestataires nominatifs et limités dans le temps
- [ ] Comptes de service sans interface interactive
- [ ] Secrets en coffre, pas dans des fichiers de configuration
- [ ] Comptes inactifs désactivés
- [ ] Journalisation des connexions envoyée hors du système

## 3. Segmentation

- [ ] Postes utilisateurs séparés des serveurs
- [ ] Serveurs séparés selon leur exposition
- [ ] Administration sur un chemin dédié
- [ ] Refus par défaut, flux autorisés listés explicitement
- [ ] Systèmes obsolètes isolés
- [ ] Phase d'observation tenue avant tout refus réel

## 4. Systèmes

- [ ] Écart CIS mesuré **avant** changement
- [ ] Recommandations triées : sans risque, à tester, cassantes
- [ ] Application par lots, une fenêtre par lot
- [ ] Vérification de service après chaque lot
- [ ] Écart CIS re-mesuré après
- [ ] Recommandations non appliquées consignées avec leur motif
- [ ] Correctifs de sécurité à jour, ou plan daté
- [ ] Services inutiles désactivés

## 5. Bordure et filtrage

- [ ] **Origine non joignable directement**
- [ ] TLS de bout en bout, mode strict
- [ ] Filtrage applicatif en observation avant blocage
- [ ] Limitation de débit sur authentification et réinitialisation
- [ ] Protection contre les robots réglée sans bloquer les usages légitimes
- [ ] En-têtes de sécurité posés
- [ ] SPF, DKIM et DMARC posés et vérifiés

## 6. Journalisation

- [ ] Journaux envoyés hors du système qui les produit
- [ ] Rétention conforme au besoin, coût connu
- [ ] Horloges synchronisées
- [ ] Sources exploitables par `soc-ai-tools`

## 7. Sauvegardes

- [ ] Fréquence adaptée à la perte de données acceptable
- [ ] Une copie hors ligne ou immuable
- [ ] Restauration testée, avec sa durée mesurée
- [ ] Sauvegardes non accessibles depuis les comptes d'administration courants

---

## Avant de clore

- [ ] Écart CIS avant et après, affiché par système
- [ ] Chaque écart assumé porte un motif écrit
- [ ] Configurations remises, documentées et modifiables par le client
- [ ] Journal des opérations complet : quoi, quand, par qui
- [ ] Aucune action menée hors fenêtre
- [ ] Double relecture effectuée
