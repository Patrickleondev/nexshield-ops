# Posture : comment nous abordons une entreprise

**Version** : v0.1 - **Statut** : à valider par les 5 associés

Ce document se lit **avant** le premier rendez-vous, par tout le monde. Il ne
décrit pas des techniques de vente : il décrit une posture. La technique varie,
la posture ne change jamais.

---

## 1. L'état d'esprit

### On vend une relation, pas une mission

Une entreprise qui nous appelle a un problème qu'elle ne sait pas encore nommer.
Notre travail commence par l'aider à le nommer - même si la conclusion est
qu'elle n'a pas besoin de nous tout de suite.

### On ne vend jamais par la peur

C'est la tentation du métier, et c'est une erreur de fond. Un client qui achète
par peur achète une fois, découvre qu'il a payé pour de l'angoisse, et ne
revient pas. Un client qui achète parce qu'il a **compris** son risque revient
chaque année.

Concrètement : pas de « vous allez vous faire pirater », pas de statistiques
mondiales anxiogènes, pas de démonstration d'intrusion sur ses systèmes pour
impressionner - c'est en plus illégal sans autorisation.

### On dit ce qu'on ne sait pas faire

Refuser une mission hors de notre compétence nous fait gagner le client suivant.
Accepter et échouer nous coûte le métier. « Ce n'est pas notre domaine, mais je
peux vous orienter » est une phrase qui rapporte, à terme, plus qu'un devis signé
à l'aveugle.

### On n'est jamais le plus intelligent de la pièce

Le client connaît son métier, ses contraintes, son historique et sa politique
interne infiniment mieux que nous. Nous connaissons les attaques. La valeur naît
du croisement, pas de la démonstration de supériorité technique.

Le signe qu'un rendez-vous s'est mal passé : nous avons plus parlé qu'écouté.

---

## 2. Le déroulé d'un premier rendez-vous

**Objectif : comprendre, pas vendre.** On ne sort pas de devis au premier
rendez-vous. Jamais.

| Temps | Ce qu'on fait |
|---|---|
| 5 min | Qui nous sommes, en trois phrases. Pas la plaquette complète. |
| **30 min** | **Questions. On écoute.** |
| 10 min | On reformule ce qu'on a compris de leur besoin. On se fait corriger. |
| 10 min | On explique comment on travaillerait - méthode, cadre, garanties |
| 5 min | Prochaine étape et délai de réponse |

### Les questions qui comptent

1. **Qu'est-ce qui vous inquiète le plus aujourd'hui ?** (la vraie question)
2. Qu'est-ce qui déclenche cette démarche : un incident, un client, un auditeur,
   une réglementation ? - *la réponse détermine tout le reste*
3. Qui, chez vous, porte le sujet sécurité ? À qui rend-il compte ?
4. Avez-vous déjà fait un audit ? Qu'en avez-vous fait ?
5. Que se passe-t-il si votre <application / service> est indisponible 48 h ?
6. Quelles données traitez-vous ? Personnelles, bancaires, de santé ?
7. Qui héberge quoi ?
8. **Quel est votre budget et votre échéance ?** - posée simplement, sans gêne

La question 4 est la plus révélatrice. « Nous avons fait un audit et le rapport
est dans un tiroir » vous dit que le problème n'est pas technique : c'est que le
rapport précédent était inexploitable. C'est exactement là que vous vous
différenciez.

### Ce qu'on ne fait pas

- Aucune reconnaissance, même passive, même « juste un `whois` », avant
  autorisation écrite (`SECURITY.md` §6). Arriver au rendez-vous avec une liste
  de leurs sous-domaines exposés impressionne, et c'est illégal.
- Pas de dénigrement d'un confrère ou d'un prestataire en place.
- Pas de chiffre annoncé à la volée. Un prix se donne par écrit, après cadrage.

---

## 3. Selon l'interlocuteur

Le même service se présente différemment. Ce n'est pas de la manipulation :
c'est parler la langue de celui qui écoute.

| Interlocuteur | Ce qui le préoccupe | Comment on lui parle |
|---|---|---|
| **Dirigeant** | Continuité, réputation, responsabilité personnelle | Impact métier, chiffré en jours d'arrêt et en clients perdus. Aucun jargon. |
| **DSI / RSSI** | Priorisation, moyens, arbitrages | Méthode, couverture, plan de remédiation réaliste. Il sait déjà qu'il a des failles ; il veut savoir lesquelles traiter d'abord. |
| **Responsable technique** | Ne pas être pris en défaut | Le respecter. Ce n'est pas lui l'accusé. Lui donner de quoi défendre son budget. |
| **Juridique / conformité** | Preuve, traçabilité, réglementation | Référentiels, attestations, rétention et destruction des données. |
| **Achats** | Comparabilité, prix | Périmètre écrit, unités claires, ce qui est inclus et ce qui ne l'est pas. |

**Le responsable technique est votre meilleur allié ou votre pire adversaire.**
S'il perçoit l'audit comme un examen de son travail, il freinera tout. Dites-lui,
dès la première minute : « Notre rapport sert à vous donner les arguments que
vous n'arrivez pas à faire passer. » C'est vrai, et ça change tout.

---

## 4. Par domaine

### Pentest et audit

Le piège : le client demande « un pentest » sans savoir ce qu'il veut prouver.
La question à poser : **« Qu'est-ce que vous ferez du rapport ? »** Selon la
réponse - rassurer un client, satisfaire un auditeur, prioriser un budget - le
périmètre et le format du livrable changent complètement.

### AI RedTeaming

Marché immature : la moitié des prospects ne sait pas que c'est testable. La
posture est **pédagogique avant d'être commerciale**. Expliquer l'injection de
prompt indirecte avec un exemple concret tiré de leur propre usage vaut mieux que
n'importe quelle plaquette.

Attention à ne pas surpromettre : on teste **leur** application et **leur**
configuration, pas le modèle de fondation du fournisseur.

### Sécurité applicative

Le client parle en fonctionnalités, nous parlons en exigences. ASVS fait le pont.
« Quel niveau d'assurance visez-vous ? » est une question qu'il n'a jamais
entendue et qui le place immédiatement en position de décideur plutôt que de
patient.

### DevSecOps

L'interlocuteur est une **équipe de développement**, pas une direction sécurité.
Elle craint qu'on lui impose des outils qui cassent sa chaîne et la ralentissent.
Poser d'abord : « Combien de temps prend votre chaîne aujourd'hui ? » Toute
recommandation qui l'allonge de plus de 10 % sera contournée dans les six mois -
autant le savoir et faire autrement.

### SOC et outillage défensif

La question qui ouvre tout : **« Si ça arrivait ce soir, vous le sauriez
comment ? »** Souvent le silence qui suit fait plus que tout un argumentaire.
Enchaîner sur la couverture ATT&CK : montrer les angles morts, pas les failles.

### X-Privacy

Interlocuteur souvent juridique. Ne jamais empiéter sur le terrain de l'avocat :
nous produisons des constats techniques et organisationnels, le conseil juridique
est renvoyé à un partenaire. Le dire explicitement crédibilise le reste.

### Sensibilisation

Le piège : le client veut « piéger ses employés ». Refuser cette formulation dès
le premier rendez-vous. Une campagne utilisée pour sanctionner détruit la
confiance et l'efficacité du programme - et se retourne contre le client.
Reformuler : mesurer collectivement, anonymement, pour progresser.

### Infrastructure, VPN, Cloudflare

Le plus technique, le plus rapide à chiffrer, le plus facile à démontrer : un
score CIS avant / après est immédiatement lisible. Bonne porte d'entrée chez un
prospect qui hésite sur un engagement plus lourd.

---

## 5. Après le rendez-vous

| Délai | Action |
|---|---|
| **Sous 24 h** | Courriel de synthèse : ce qu'on a compris de leur besoin, en cinq lignes. Rien d'autre. |
| Sous 5 jours | Proposition écrite, périmètre cadré, prix ferme |
| Sous 10 jours | Relance unique. Pas deux. |

Le courriel de synthèse à 24 h est l'action au meilleur rendement de tout le
processus commercial. Il prouve qu'on a écouté, il fait remonter les
malentendus tant qu'ils sont gratuits, et il laisse une trace écrite du besoin.

**Si on ne signe pas** : demander pourquoi, une fois, sans insister, et le
consigner. Trois refus pour la même raison signalent un problème d'offre, pas
trois mauvais prospects.
