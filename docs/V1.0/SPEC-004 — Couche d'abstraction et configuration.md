# SPEC-004 — Couche d'abstraction et configuration

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette SPEC définit la couche d'abstraction entre les équipements physiques et la logique métier.

Elle décrit :

* les entités PCHA ;
* les Helpers ;
* les Templates ;
* les conventions de nommage.

Cette couche constitue l'unique interface entre le matériel et le contrôleur.

---

# 2. Philosophie

Le matériel est interchangeable.

La logique métier ne connaît jamais les équipements physiques.

Elle manipule uniquement des entités PCHA.

Exemple :

```text
sensor.jardin_esp32_jardin_debit_filtration_piscine
        │
        ▼
sensor.pcha_debit_filtration
        │
        ▼
Machine à états
```

Ainsi, le remplacement d'un équipement ne modifie jamais les autres couches du projet.

---

# 3. Principes de la couche d'abstraction

La couche d'abstraction :

- ne contient aucune règle métier ;

- ne réalise aucun calcul fonctionnel ;

- ne prend aucune décision ;

- ne fait que présenter des entités PCHA indépendantes du matériel.

Une entité PCHA ne doit jamais exposer unknown, unavailable ou none.

Toute logique métier appartient exclusivement aux SPEC fonctionnelles.

---

# 3.1 Nomenclature

1. Capteurs (sensor)

| Entité	                     | Description	      | Source              |
| ---------------------------------- | ---------------------- | ------------------- |
| sensor.pcha_temperature_piscine    | Température de l'eau   | Température piscine |
| sensor.pcha_temperature_exterieure | Température extérieure | Sonde extérieure    |
| sensor.pcha_debit_filtration       | Débit instantané	      | Débitmètre          |
| sensor.pcha_puissance_pompe        | Puissance électrique   | Prise Zigbee        |
| sensor.pcha_energie_pompe          | Énergie consommée      | Prise Zigbee        |
| sensor.pcha_luminosite             | Luminosité extérieure  | Capteur ESP32       |

2. Actionneurs (switch)

| Entité	                     | Description	      |
| ---------------------------------- | ---------------------- | 
| switch.pcha_pompe_filtration	     | Pompe de filtration    | 

3. Modes (input_select)

Entité
input_select.pcha_mode

Valeurs :

OFF
SECURISATION
AUTO
TRAITEMENT
MARCHE_FORCEE

4. Réglages (input_number)

| Entité	                           | Description	         |
| ---------------------------------------- | --------------------------- | 
| input_number.pcha_temperature_consigne   | Température cible           |
| input_number.pcha_duree_traitement       | Durée du traitement (h)     |
| input_number.pcha_seuil_luminosite       | Seuil de chauffage solaire  |
| input_number.pcha_hysteresis_temperature | Hystérésis température      |
| input_number.pcha_debit_minimal          | Débit minimal autorisé      |
| input_number.pcha_delai_validation_debit | Validation défaut débit (s) |

5. États internes (input_select)

Entité
input_select.pcha_etat_machine

Valeurs possibles :

INITIALISATION
ATTENTE
FILTRATION
DEFAUT_BLOQUANT

6. Niveau de fonctionnement (input_select)

Entité
input_select.pcha_niveau_fonctionnement

Valeurs :

NORMAL
DEGRADE
BLOQUE

Définies exclusivement par la SPEC-007.

7. Informations calculées (binary_sensor)

Ces entités sont calculées par le projet et ne doivent jamais lire directement le matériel.

| Entité	                           | Description	         |
| ---------------------------------------- | --------------------------- | 
| binary_sensor.pcha_filtration_autorisee  | Filtration autorisée        |
| binary_sensor.pcha_chauffage_autorise    | Chauffage solaire autorisé  |
| binary_sensor.pcha_traitement_actif      | Traitement en cours         |
| binary_sensor.pcha_marche_forcee         | Marche forcée active        |
| binary_sensor.pcha_defaut_bloquant       | Défaut bloquant actif       |
| binary_sensor.pcha_filtration_requise    | Filtration requise          |

8. Capteurs calculés (sensor)

| Entité	                           | Description	           |
| ---------------------------------------- | ----------------------------- | 
| sensor.pcha_duree_filtration_cible       | Durée calculée                |
| sensor.pcha_duree_filtration_restante    | Temps restant                 |
| sensor.pcha_volume_filtre_jour           | Volume filtré quotidien       |
| sensor.pcha_energie_journaliere          | Énergie consommée aujourd'hui |

9. Scripts

script.pcha_demarrer_filtration

script.pcha_arreter_filtration

script.pcha_initialiser

script.pcha_reinitialiser_defauts

10. Automatisations

automation.pcha_machine_etats

automation.pcha_diagnostics

automation.pcha_filtration

automation.pcha_traitement

automation.pcha_chauffage

---

# 3.2 Principes de la couche d'abstraction

HAL-001 — Interface unique

La couche d'abstraction constitue l'unique interface entre le matériel et le reste du système.

Aucune SPEC fonctionnelle, aucun script, aucune automatisation et aucun calcul métier ne doit accéder directement aux entités physiques de Home Assistant.

Toutes les interactions avec le matériel s'effectuent exclusivement au travers des entités pcha_*.

---

HAL-002 — Neutralité fonctionnelle

La couche d'abstraction ne contient aucune logique métier.

Elle ne doit :

prendre aucune décision ;
réaliser aucun calcul fonctionnel ;
interpréter aucune mesure ;
appliquer aucune règle de gestion.

Son unique responsabilité est de présenter des entités normalisées indépendantes du matériel utilisé.

---

HAL-003 — Robustesse des entités

Les entités PCHA doivent toujours présenter une interface exploitable par les couches supérieures.

Elles ne doivent jamais exposer directement les états Home Assistant :

unknown
unavailable
none

Lorsqu'une donnée physique devient indisponible, la couche d'abstraction conserve la dernière valeur valide connue.

La perte de communication ou la défaillance d'un capteur est détectée exclusivement par les mécanismes définis dans la SPEC-007 – Diagnostics.

---

HAL-004 — Source unique des défauts

La couche d'abstraction ne génère aucun diagnostic.

Elle ne signale jamais :

un défaut,
une alarme,
un mode dégradé,
une indisponibilité fonctionnelle.

Ces décisions relèvent exclusivement de la SPEC-007.

---

HAL-005 — Indépendance matérielle

Le remplacement d'un équipement physique (ESPHome, Zigbee, Z-Wave, Wi-Fi, etc.) ne doit entraîner aucune modification des couches fonctionnelles du contrôleur.

Seule la couche d'abstraction est autorisée à connaître les identifiants matériels réels.

---

# 4. Entité physique → Description → Fonction → couche d'abstraction

Remarque : les entités pcha_* constituent une interface logique stable. Elles ne reflètent pas directement l'état brut des équipements physiques, mais fournissent une abstraction normalisée conforme aux principes HAL définis dans cette SPEC.

| Entité physique                                     | Description                                                          | Fonction                           | Entité PCHA                            |
| --------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------- | -------------------------------------- |
| sensor.jardin_esp32_jardin_debit_filtration_piscine | Mesure le débit instantané du circuit hydraulique                    | Débit de filtration                | sensor.pcha_debit_filtration           |
| sensor.jardin_esp32_jardin_temperature_piscine      | Mesure la température de l'eau circulant dans le circuit             | Température piscine                | sensor.pcha_temperature_piscine        |
| sensor.jardin_esp32_jardin_luminosite               | Mesure la luminosité au niveau du chauffage solaire.                 | Luminosité                         | sensor.pcha_luminosite                 |
| sensor.temperature_exterieure_temperature           | Mesure la température extérieure                                     | Température extérieure             | sensor.pcha_temperature_exterieure     |
| sensor.prises_exterieur_power                       | Mesure la puissance instantanée consommée par la pompe de filtration | Puissance pompe filtration         | sensor.pcha_puissance_pompe_filtration |
| sensor.prises_exterieur_energy                      | Mesure l'énergie consommée par la pompe de filtration                | Énergie pompe filtration           | sensor.pcha_energie_pompe_filtration   |
| switch.jardin_prises_exterieur_pompe_de_filtration  | Commande le fonctionnement de la pompe de filtration                 | Commande pompe filtration          | switch.pcha_commande_pompe_filtration  |

Cette correspondance est réalisée exclusivement ici pour les entités physiques afin de garantir qu'une seule SPEC sera à modifier en cas de remplacement de capteur physique.
Aucun autre composant du projet n'accède directement aux équipements physiques.

# 5. Helpers

Les Helpers représentent uniquement des paramètres configurables.

Ils ne doivent jamais contenir :

* une mesure physique ;
* un état calculé ;
* une décision métier.

---

## Helpers utilisateur

### Mode de fonctionnement

```text
input_select.pcha_mode_de_fonctionnement
```

Valeurs :

* OFF
* SÉCURISATION
* AUTO
* TRAITEMENT
* MARCHE FORCÉE

---

### Etat machine

```text
input_select.pcha_etat_machine
```
Valeurs :

* INITIALISATION
* ATTENTE
* FILTRATION

---

### Niveau fonctionnement

```text
input_select.pcha_niveau_fonctionnement
```
Valeurs :

* NORMAL
* DEGRADE
* BLOQUE

---

### Température de consigne

```text
input_number.pcha_temperature_de_consigne
```

---

### Seuil de luminosité

```text
input_number.pcha_seuil_luminosite_chauffage
```

---

### Temps Marche Pompe Minimal

```text
input_number.pcha_temps_marche_pompe_min
```
---

### Temps Arrêt Pompe Minimal

```text
input_number.pcha_temps_arret_pompe_min
```
---

### Temps validation température piscine

```text
input_number.pcha_temps_validation_temperature_piscine
```
---

### Durée du traitement

```text
input_number.pcha_duree_traitement
```
Description :
Durée du traitement exprimée en heures.

Cette durée est utilisée exclusivement lorsque le mode TRAITEMENT est actif.

---

Les futurs paramètres de configuration suivront la même convention.

---

# 6. Entités d'abstraction

Les équipements physiques sont convertis en entités PCHA au chapitre 3.

---

# 7. Entités métier

Les Templates métier créent les états utilisés par le contrôleur.

Exemples :

```text
binary_sensor.pcha_filtration_autorisee

binary_sensor.pcha_objectif_atteint

binary_sensor.pcha_chauffage_autorise

binary_sensor.pcha_debit_ok

binary_sensor.pcha_defaut
```

---

# 8. Convention de nommage

Se Conformer à CONVENTIONS.md

---

# 9. Organisation des fichiers

Se Conformer à ARCHITECTURE.md

---

# 10. Contraintes

Se Conformer à CONVENTIONS.md

---

# 11. Critères d'acceptation

La couche d'abstraction est conforme lorsque :

* chaque équipement physique possède une entité PCHA ;
* tous les Helpers représentent uniquement des paramètres configurables ;
* aucun Template d'abstraction ne contient de logique métier ;
* les états métier sont créés exclusivement par les Templates métier ;
* aucun composant du projet n'utilise directement un équipement physique.

---

# 12. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-001 — Inventaire matériel
* SPEC-002 — Interface utilisateur
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états

# TIM-001 — Les timers Home Assistant sont réservés aux temporisations fonctionnelles visibles par l'utilisateur. Les temporisations de validation, d'hystérésis ou de protection sont implémentées par la logique métier et ne doivent pas être représentées par des entités timer.

# Aucun helper de type input_text n'est utilisé dans le projet.

Les états internes du contrôleur sont persistés à l'aide de
input_select afin de garantir :

- une liste d'états contrôlée ;
- une persistance native Home Assistant ;
- une compatibilité avec la machine à états ;
- une impossibilité d'utiliser une valeur non définie par la SPEC.

# HAL-006

Les états persistants du contrôleur sont stockés exclusivement
dans des input_select.

Aucun état du contrôleur ne doit être stocké dans un input_text
ou calculé par un template.