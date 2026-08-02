# SPEC-004 — Couche d'abstraction et configuration

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit l'interface stable entre les équipements physiques et le reste du PCHA, ainsi que les helpers configurables.

Elle ne contient aucune règle métier.

# 2. Principes HAL

* Seule la couche d'abstraction connaît les identifiants physiques.
* Les autres composants utilisent exclusivement les entités `pcha_*`.
* Le remplacement d'un équipement ne modifie pas les SPEC fonctionnelles.
* Une entité PCHA possède une seule définition.
* Une mesure abstraite conserve la dernière valeur valide et expose un attribut booléen `source_available` indiquant la disponibilité de sa source.
* L'indisponibilité est interprétée uniquement par la SPEC-007.

# 3. Capteurs d'abstraction

Fichier responsable :

```text
templates/capteurs.yaml
```

| Entité physique | Entité PCHA |
|---|---|
| `sensor.jardin_esp32_jardin_temperature_piscine` | `sensor.pcha_temperature_piscine_brute` puis `sensor.pcha_temperature_piscine` validée après circulation |
| `sensor.temperature_exterieure_temperature` | `sensor.pcha_temperature_exterieure` |
| `sensor.jardin_esp32_jardin_luminosite` | `sensor.pcha_luminosite` |
| `sensor.jardin_esp32_jardin_debit_filtration_piscine` | `sensor.pcha_debit_filtration` |
| `sensor.prises_exterieur_power` | `sensor.pcha_puissance_pompe_filtration` |
| `sensor.prises_exterieur_energy` | `sensor.pcha_energie_pompe_filtration` |

# 4. Actionneur d'abstraction

Fichier responsable :

```text
templates/actionneurs.yaml
```

| Entité physique | Entité PCHA |
|---|---|
| `switch.jardin_prises_exterieur_pompe_de_filtration` | `switch.pcha_commande_pompe_filtration` |

La couche d'abstraction transmet l'état et les commandes. Elle ne décide jamais quand la pompe doit fonctionner.

# 5. Helpers configurables

## 5.1 Commandes utilisateur

```text
input_boolean.pcha_acquitter_alarmes
```

## 5.2 Paramètres numériques

```text
input_number.pcha_temperature_de_consigne
input_number.pcha_correction_temperature_piscine
input_number.pcha_seuil_luminosite_chauffage
input_number.pcha_duree_traitement
input_number.pcha_temps_marche_pompe_min
input_number.pcha_temps_arret_pompe_min
input_number.pcha_temps_validation_temperature_piscine
input_number.pcha_temps_validation_debit
input_number.pcha_temps_validation_luminosite
```

Les bornes de configuration sont définies dans
helpers/input_number.yaml.

La correction est soustraite à la mesure brute. Une valeur de `2 °C` corrige une sonde qui affiche environ 2 °C de trop. La température métier est actualisée uniquement après une circulation continue d'au moins `input_number.pcha_temps_validation_temperature_piscine`.

Les valeurs sélectionnées sont conservées par Home Assistant.
Le comportement fonctionnel de chaque paramètre appartient à sa SPEC
propriétaire.

## 5.3 Sélections persistantes

```text
input_select.pcha_mode_de_fonctionnement
input_select.pcha_etat_machine
input_select.pcha_niveau_fonctionnement
```

Leurs valeurs et leurs comportements sont définis uniquement dans les SPEC-006, SPEC-005 et SPEC-007.

## 5.4 Timer fonctionnel

```text
timer.pcha_traitement
```

Il est réservé au mode `TRAITEMENT` défini dans la SPEC-006.

Aucun `input_text` n'est utilisé en V1.

## 5.5 Compteur quotidien d’énergie

```text
sensor.pcha_energie_pompe_quotidienne
```

Ce compteur est produit par `helpers/utility_meter.yaml` à partir de `sensor.pcha_energie_pompe_filtration` et est réinitialisé chaque jour. La mesure totale reste l’interface d’abstraction de la source physique.

# 6. Templates métier

Les templates métier consomment uniquement les entités PCHA. Chaque entité métier est définie par la SPEC fonctionnelle qui en est propriétaire.

SPEC-004 ne redéfinit ni leurs règles ni leurs résultats.

# 7. Contraintes

SPEC-004 ne doit jamais :

* calculer une demande de filtration ou de chauffage ;
* décider d'une transition ;
* déterminer un mode ou un niveau de fonctionnement ;
* produire un diagnostic ;
* commander directement le matériel depuis une logique métier.

# 8. Critères d'acceptation

* Les identifiants physiques sont confinés aux templates d'abstraction.
* Toutes les couches supérieures utilisent des entités PCHA.
* Chaque mesure expose sa disponibilité sans créer de diagnostic.
* Les helpers sont limités aux commandes et paramètres nécessaires.
* Les valeurs des modes, états et niveaux sont conformes à leurs SPEC propriétaires.

# 9. Références

* SPEC-001 — Inventaire matériel
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
