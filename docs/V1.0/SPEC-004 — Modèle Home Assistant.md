# SPEC-004 — Modèle Home Assistant

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit l'organisation des entités Home Assistant utilisées par le Pool Controller.

Elle décrit :

* les familles d'entités ;
* les conventions de nommage ;
* les responsabilités de chaque type d'entité.

Elle ne définit aucune logique métier.

Les règles de fonctionnement sont décrites dans les autres spécifications.

---

# 2. Principes

Toutes les interactions entre le contrôleur et Home Assistant utilisent des entités standard.

Les valeurs métier sont stockées exclusivement dans des Helpers.

Les scripts exécutent uniquement des actions.

Les automatisations déclenchent les traitements mais ne prennent jamais de décision métier.

---

# 3. Familles d'entités

Le modèle repose sur les familles suivantes :

| Famille         | Rôle                          |
| --------------- | ----------------------------- |
| Sensors         | Mesures physiques             |
| Binary Sensors  | États booléens                |
| Helpers         | Paramètres configurables      |
| Scripts         | Exécution d'actions           |
| Automatisations | Déclenchement des traitements |
| Timers          | Temporisations                |
| Notifications   | Information utilisateur       |

---

# 4. Sensors

Les capteurs représentent exclusivement des mesures physiques.

Ils ne doivent contenir aucune logique métier.

Exemples :

* température d'eau ;
* température extérieure ;
* luminosité ;
* débit ;
* puissance électrique ;
* énergie consommée.

---

# 5. Helpers

Les Helpers contiennent toutes les valeurs configurables.

Exemples :

* température de consigne ;
* seuil débit critique ;
* seuil débit nominal ;
* durée de validation des défauts ;
* paramètres de protection ;
* paramètres de filtration.

Aucune constante métier ne doit être codée dans les scripts.

---

# 6. Scripts

Les scripts exécutent les actions demandées par le contrôleur.

Ils ne prennent aucune décision.

Exemples :

* démarrer la filtration ;
* arrêter la filtration ;
* lancer un traitement.

Les décisions sont exclusivement prises par la machine à états (SPEC-005).

---

# 7. Automatisations

Les automatisations ont uniquement pour rôle :

* déclencher les traitements ;
* réagir à un événement Home Assistant ;
* appeler un script ou le contrôleur.

Elles ne doivent contenir aucune logique métier.

---

# 8. Timers

Les temporisations utilisent exclusivement les entités `timer`.

Exemples :

* validation d'un défaut ;
* durée minimale de fonctionnement ;
* protection du serpentin ;
* temporisations de sécurité.

---

# 9. Conventions de nommage

Toutes les entités respectent les conventions suivantes :

| Type             | Préfixe          |
| ---------------- | ---------------- |
| Sensor           | `sensor.`        |
| Binary Sensor    | `binary_sensor.` |
| Helper numérique | `input_number.`  |
| Helper booléen   | `input_boolean.` |
| Helper sélection | `input_select.`  |
| Timer            | `timer.`         |
| Script           | `script.`        |

Les noms doivent être :

* explicites ;
* stables ;
* en minuscules ;
* séparés par des underscores.

---

# 10. Organisation

Les entités sont regroupées par domaine fonctionnel.

Exemples :

* filtration ;
* chauffage solaire ;
* diagnostics ;
* configuration ;
* supervision.

Cette organisation facilite la maintenance et l'évolution du projet.

---

# 11. Traçabilité

Toute action importante doit être identifiable.

Les scripts, automatisations et événements enregistrés dans les journaux utilisent les identifiants définis dans la **SPEC-009**.

---

# 12. Évolutions

L'ajout d'une nouvelle entité doit respecter :

* les conventions de nommage ;
* les principes de la **SPEC-000** ;
* la responsabilité de cette spécification.

Aucune nouvelle logique métier ne doit être introduite dans les entités Home Assistant.

---

# 13. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
