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

# 3. Entité physique → Description → Fonction → couche d'abstraction

| Entité physique                                     | Description                                                          | Fonction                           | Entité PCHA                            |
| --------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------- | -------------------------------------- |
| sensor.jardin_esp32_jardin_debit_filtration_piscine | Mesure le débit instantané du circuit hydraulique                    | Débit de filtration                | sensor.pcha_debit_filtration           |
| sensor.jardin_esp32_jardin_temperature_piscine      | Mesure la température de l'eau circulant dans le circuit             | Température piscine                | sensor.pcha_temperature_piscine        |
| sensor.jardin_esp32_jardin_luminosite               | Mesure la luminosité au niveau du chauffage solaire.                 | Luminosité                         | sensor.pcha_luminosite                 |
| sensor.temperature_exterieure_temperature           | Mesure la température extérieure                                     | Température extérieure             | sensor.pcha_temperature_exterieure     |
| sensor.prises_exterieur_power                       | Mesure la puissance instantanée consommée par la pompe de filtration | Puissance pompe filtration         | sensor.pcha_puissance_pompe_filtration |
| sensor.prises_exterieur_energy                      | Mesure l'énergie consommée par la pompe de filtration                | Énergie pompe filtration           | sensor.pcha_energie_pompe_filtration   |
| switch.jardin_prises_exterieur_pompe_de_filtration  | Commande le fonctionnement de la pompe de filtration                 | Commande pompe filtration          | switch.pcha_Commande_pompe_filtration  |

Cette correspondance est réalisée exclusivement ici pour les entités physiques afin de garantir qu'une seule SPEC sera à modifier en cas de remplacement de capteur physique.
Aucun autre composant du projet n'accède directement aux équipements physiques.

# 4. Helpers

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

# 5. Entités d'abstraction

Les équipements physiques sont convertis en entités PCHA au chapitre 3.

---

# 6. Entités métier

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

# 7. Convention de nommage

Se Conformer à CONVENTIONS.md

---

# 8. Organisation des fichiers

Se Conformer à ARCHITECTURE.md

---

# 9. Contraintes

Se Conformer à CONVENTIONS.md

---

# 10. Critères d'acceptation

La couche d'abstraction est conforme lorsque :

* chaque équipement physique possède une entité PCHA ;
* tous les Helpers représentent uniquement des paramètres configurables ;
* aucun Template d'abstraction ne contient de logique métier ;
* les états métier sont créés exclusivement par les Templates métier ;
* aucun composant du projet n'utilise directement un équipement physique.

---

# 11. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-001 — Inventaire matériel
* SPEC-002 — Interface utilisateur
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
