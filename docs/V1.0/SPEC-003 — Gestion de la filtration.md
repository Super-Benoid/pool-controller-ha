# SPEC-003 — Gestion de la filtration

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit les règles de gestion de la filtration de la piscine.

Elle décrit les objectifs de filtration, le calcul du temps de filtration et les règles de fonctionnement.

L'architecture générale est définie dans la **SPEC-000**.

---

# 2. Objectifs

La filtration doit :

* maintenir la qualité de l'eau ;
* assurer un renouvellement hydraulique suffisant ;
* participer au chauffage solaire lorsque celui-ci est disponible ;
* contribuer à la protection du serpentin.

Les modes de fonctionnement sont définis dans la **SPEC-006**.

Les états du contrôleur sont définis dans la **SPEC-005**.

---

# 3. Principe général

Chaque jour, le contrôleur calcule un **objectif quotidien de filtration**.

Cet objectif représente la durée minimale de fonctionnement de la pompe.

Le calcul est réalisé automatiquement à partir de la température de l'eau.

---

# 4. Calcul du temps de filtration

Le temps quotidien de filtration est déterminé selon les paliers suivants :

| Température de l'eau |                 Temps de filtration |
| -------------------- | ----------------------------------: |
| < 20 °C              |                                 4 h |
| 20 °C à < 24 °C      |                                 6 h |
| 24 °C à < 27 °C      |                                 8 h |
| ≥ 27 °C              | 10 h + 2 h par degré supplémentaire |

Cette règle constitue la référence de la V1.

---

# 5. Objectif quotidien

Le contrôleur maintient un compteur du temps de filtration réalisé.

À tout instant, il compare :

* le temps de filtration effectué ;
* l'objectif quotidien calculé.

La filtration est considérée comme terminée lorsque l'objectif est atteint.

---

# 6. Répartition de la filtration

Le contrôleur répartit automatiquement les périodes de filtration au cours de la journée.

La stratégie de répartition est optimisée afin de :

* améliorer la qualité de l'eau ;
* favoriser le chauffage solaire lorsque celui-ci est disponible ;
* limiter les cycles inutiles.

L'algorithme de répartition relève de l'implémentation.

---

# 7. Interaction avec le chauffage solaire

Lorsque le chauffage solaire est autorisé, la filtration peut être prolongée afin d'exploiter l'énergie disponible.

Les règles de chauffage solaire sont définies dans la **SPEC-008**.

---

# 8. Interaction avec les modes utilisateur

Le comportement de la filtration dépend du mode actif.

Les règles associées sont définies dans la **SPEC-006**.

---

# 9. Interaction avec les diagnostics

En présence d'un diagnostic de sécurité, le fonctionnement de la filtration est déterminé conformément à la **SPEC-007**.

La présente spécification ne définit aucun comportement en cas de défaut.

---

# 10. Paramètres configurables

Les paramètres utilisés par la gestion de la filtration sont configurables depuis Home Assistant.

Le modèle des Helpers est défini dans la **SPEC-004**.

---

# 11. Journalisation

Les événements significatifs liés à la filtration sont enregistrés conformément à la **SPEC-009**.

---

# 12. Critères d'acceptation

La gestion de la filtration est conforme lorsque :

* le temps quotidien est calculé selon les paliers définis ;
* l'objectif quotidien est respecté ;
* les interactions avec les autres fonctions respectent les spécifications de référence ;
* les paramètres sont configurables ;
* les événements sont correctement journalisés.

---

# 13. Références

* SPEC-000 — Architecture générale
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
