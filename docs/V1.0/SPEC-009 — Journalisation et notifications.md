# SPEC-009 — Journalisation et notifications

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit les règles de journalisation et de notification du Pool Controller.

Elle décrit :

* les événements à enregistrer ;
* les notifications utilisateur ;
* les informations minimales à conserver.

Elle ne définit pas le stockage physique des journaux.

---

# 2. Principes

La journalisation a pour objectifs de :

* faciliter le diagnostic ;
* assurer la traçabilité du fonctionnement ;
* permettre l'analyse des anomalies ;
* informer l'utilisateur des événements importants.

Chaque événement est enregistré une seule fois.

---

# 3. Événements journalisés

Les événements suivants sont obligatoirement enregistrés.

## 3.1 Machine à états

* changement d'état ;
* changement de mode utilisateur.

Références :

* **SPEC-005**
* **SPEC-006**

---

## 3.2 Diagnostics

* apparition d'un diagnostic ;
* disparition d'un diagnostic.

Référence :

* **SPEC-007**

---

## 3.3 Filtration

* démarrage automatique ;
* arrêt automatique.

Référence :

* **SPEC-003**

---

## 3.4 Chauffage solaire

* démarrage ;
* arrêt ;
* activation de la protection du serpentin ;
* fin de la protection du serpentin ;
* protection impossible.

Référence :

* **SPEC-008**

---

# 4. Informations enregistrées

Chaque événement contient au minimum :

| Champ         | Description                          |
| ------------- | ------------------------------------ |
| Date et heure | Horodatage                           |
| Type          | Nature de l'événement                |
| Source        | Fonction ayant généré l'événement    |
| Description   | Message lisible                      |
| Niveau        | Information, Avertissement ou Erreur |

Des informations complémentaires peuvent être ajoutées selon le type d'événement.

---

# 5. Niveaux de journalisation

Les événements sont classés selon trois niveaux.

| Niveau        | Description                         |
| ------------- | ----------------------------------- |
| Information   | Fonctionnement normal               |
| Avertissement | Fonctionnement dégradé              |
| Erreur        | Défaut nécessitant une intervention |

---

# 6. Notifications

Les notifications sont destinées à informer l'utilisateur des événements importants.

| Niveau        | Notification |
| ------------- | ------------ |
| Information   | Optionnelle  |
| Avertissement | Recommandée  |
| Erreur        | Obligatoire  |

Les notifications sont transmises par Home Assistant.

---

# 7. Contenu minimal d'une notification

Chaque notification contient au minimum :

* date et heure ;
* titre ;
* description ;
* niveau ;
* recommandation éventuelle.

---

# 8. Critères d'acceptation

Le système est conforme lorsque :

* tous les événements définis sont journalisés ;
* chaque événement est enregistré une seule fois ;
* les notifications respectent leur niveau de gravité ;
* les journaux permettent de reconstituer la chronologie des événements.

---

# 9. Références

* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
