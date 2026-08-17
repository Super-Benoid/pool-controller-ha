# Pool Controller Home Assistant — PCHA V3.0

Contrôleur de filtration, de chauffage solaire et de surveillance hydraulique pour Home Assistant.

**Version courante : V3.0 — planification météo-adaptative active.**

## Évolutions V3.0

* loi de durée de filtration rendue paramétrable tout en conservant les valeurs historiques par défaut ;
* marge avant coucher du soleil configurable ;
* abstraction météo quotidienne et horaire derrière des entités `pcha_*` ;
* calcul d'un score et d'un niveau de potentiel thermique journalier ;
* cible de filtration météo-adaptative selon le potentiel thermique, la température du bassin, la consigne et la tendance J+1 ;
* activation de cette cible dans la demande de filtration du mode `AUTO` ;
* compatibilité conservée avec les anciennes entités de filtration requise et d'heure d'atteinte ;
* accueil enrichi avec météo J/J+1, potentiel thermique, stratégie et cible utilisée ;
* nouvelle vue **Paramètres PCHA V3.0** séparant réglages métier et informations avancées de sécurité.

La référence fonctionnelle V3.0 est :

```text
docs/V3.0/README.md
```

Le dashboard actif est :

```text
dashboard/piscine.yaml
```

La vue Paramètres est isolée dans :

```text
dashboard/views/parametres.yaml
```

## Principes fonctionnels

### Objectif quotidien

La température de référence est construite à partir de la température calibrée cohérente du bassin et figée au changement de jour à partir de la moyenne fiable de la veille.

La durée est calculée avec les paramètres :

```text
input_number.pcha_coefficient_filtration_base
input_number.pcha_temperature_seuil_acceleration_filtration
input_number.pcha_coefficient_filtration_acceleration
```

### Planification V3

La durée demandée et l'heure à laquelle elle doit être terminée restent deux notions distinctes.

La météo influence la **planification** via :

```text
sensor.pcha_meteo_aujourd_hui
sensor.pcha_meteo_demain
sensor.pcha_previsions_meteo_horaires
sensor.pcha_score_potentiel_thermique_jour
sensor.pcha_potentiel_thermique_jour
sensor.pcha_heure_cible_objectif
```

La décision active de filtration est exposée par :

```text
binary_sensor.pcha_filtration_requise_v3
sensor.pcha_heure_atteinte_objectif_v3
```

### Sécurité et solaire

Les diagnostics MES / COH / PRO, la machine à états, les sécurités hydrauliques et la protection du serpentin restent indépendants de l'optimisation météo. Les seuils de sécurité ne sont pas exposés comme paramètres utilisateur courants.

## Base historique V1.1

La documentation `docs/V1.1/` reste la référence technique détaillée des fondations du moteur : abstraction des mesures, température bassin, diagnostics, modes, chauffage solaire et protections.

Les anciennes versions restent consultables dans l'historique Git et les tags de version, notamment `v2.0`.

## Installation / mise à jour

Après mise à jour de la branche locale :

```bash
cd /config/pool-controller-ha
git pull --ff-only origin main
```

Les fichiers installés sous `/config/packages/` peuvent être resynchronisés si l'installation utilise les copies fournies par le dépôt :

```bash
cp /config/pool-controller-ha/installation/packages/piscine.yaml /config/packages/piscine.yaml
cp /config/pool-controller-ha/installation/packages/piscine_diagnostics.yaml /config/packages/piscine_diagnostics.yaml
```

Pour une modification touchant les templates, automatisations, scripts, helpers ou packages, valider la configuration avant application :

```bash
ha core check
```

Un simple changement de dashboard ne nécessite normalement ni `ha core check` ni redémarrage de Home Assistant Core.

## Documentation

* architecture : `docs/ARCHITECTURE.md` ;
* conventions : `docs/CONVENTIONS.md` ;
* référence V3.0 : `docs/V3.0/README.md` ;
* référence historique du moteur : `docs/V1.1/` ;
* maintenance et tests : `docs/MAINTENANCE.md` ;
* exemples ESPHome : `esphome/`.

## Entités physiques principales

```text
sensor.jardin_esp32_jardin_temperature_bassin
sensor.jardin_esp32_jardin_debit_filtration_piscine
sensor.prises_exterieur_power
sensor.jardin_esp32_jardin_luminosite
binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite
binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok
```

Aucune fonction métier PCHA ne doit contourner les abstractions `pcha_*` pour lire directement ces entités physiques.
