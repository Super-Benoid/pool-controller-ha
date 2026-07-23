# SPEC-003 — Gestion de la filtration

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette spécification définit les règles de gestion de la filtration de la piscine.

Elle décrit :

* le calcul de l'objectif quotidien de filtration ;
* les règles permettant d'autoriser la filtration ;
* les interactions avec les autres fonctions du contrôleur.

Elle ne décrit ni les modes de fonctionnement, ni la machine à états, ni les diagnostics.

---

# 2. Philosophie

Le contrôleur pilote un unique circuit hydraulique.

La filtration constitue la fonction principale du système.

Le chauffage solaire n'est pas une fonction indépendante.

Une période de chauffage est toujours une période de filtration réalisée lorsque les conditions d'ensoleillement sont favorables.

---

# 3. Objectifs

La filtration doit :

* maintenir la qualité de l'eau ;
* assurer un renouvellement hydraulique suffisant ;
* permettre le chauffage solaire lorsque les conditions le permettent ;
* respecter les contraintes définies par les autres SPEC.

Les demandes de filtration peuvent être refusées par la machine à états (SPEC-005) en cas de DÉFAUT BLOQUANT.

---

# 4. Calcul de l'objectif quotidien

Chaque jour, le contrôleur calcule un objectif quotidien de filtration.

Cet objectif représente la durée minimale de filtration à réaliser.

Le calcul est basé sur la température de l'eau.

---

# 5. Calcul du temps de filtration

Le temps quotidien de filtration est déterminé selon les paliers suivants :

| Température de l'eau |                     Temps quotidien |
| -------------------- | ----------------------------------: |
| < 20 °C              |                                 4 h |
| 20 °C à < 24 °C      |                                 6 h |
| 24 °C à < 27 °C      |                                 8 h |
| ≥ 27 °C              | 10 h + 2 h par degré supplémentaire |

Cette règle constitue la référence de la V1.

---

# 6. Mode dégradé

Si la température de la piscine est indisponible, le calcul du temps de filtration est réalisé à partir de la température de consigne définie par l'utilisateur.

Ce fonctionnement garantit la continuité du service.

---

# 7. Objectif quotidien

Le contrôleur maintient en permanence :

* le temps de filtration réalisé ;
* l'objectif quotidien.

Lorsque l'objectif est atteint, la filtration quotidienne est considérée comme terminée.

---

# 8. Répartition de la filtration

Le contrôleur répartit automatiquement les périodes de filtration sur la journée.

La stratégie de répartition est laissée à l'implémentation.

Elle doit cependant respecter les objectifs suivants :

* réaliser l'objectif quotidien de filtration une heure avant le couché du soleil ;
* limiter les démarrages inutiles ;
* favoriser les périodes propices au chauffage solaire.

---

# 9. Chauffage solaire

Le chauffage solaire ne modifie jamais le principe de fonctionnement de la filtration.

Le contrôleur continue de piloter un unique circuit hydraulique.

Lorsque les conditions d'ensoleillement sont réunies conformément à la SPEC-008, une période de filtration peut être prolongée afin d'exploiter l'énergie solaire disponible.

Le chauffage solaire est donc une conséquence du fonctionnement de la filtration.

---

# 10. Interaction avec les modes

Le comportement de la filtration dépend du mode de fonctionnement actif.

Les règles sont définies exclusivement dans la SPEC-006.

---

# 11. Interaction avec les diagnostics

Les diagnostics peuvent autoriser ou interdire la filtration.

Les règles associées sont définies dans la SPEC-007.

Cette SPEC ne définit aucun comportement en cas de défaut.

---

# 12. Paramètres configurables

Les paramètres suivants sont configurables :

* température de consigne ;
* seuil de luminosité ;
* paramètres éventuels de filtration définis par la SPEC-004.

Les valeurs sont fournies exclusivement par les entités PCHA.

---

# 13. Journalisation

Les événements significatifs liés à la filtration sont enregistrés conformément à la SPEC-009.

---

# 14. Critères d'acceptation

La gestion de la filtration est conforme lorsque :

* l'objectif quotidien est correctement calculé ;
* le mode dégradé fonctionne ;
* le temps de filtration est correctement comptabilisé ;
* la répartition respecte les objectifs définis ;
* le chauffage solaire est considéré comme une prolongation de la filtration ;
* les interactions avec les autres SPEC sont respectées.

---

# 15. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
