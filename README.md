# Pool Controller Home Assistant — PCHA V2.0

Contrôleur de filtration, de chauffage solaire et de surveillance hydraulique pour Home Assistant.

## Évolutions V2.0

* dashboard Concept D finalisé avec supervision temps réel ;
* objectif quotidien enrichi avec heure prévisionnelle d’atteinte ;
* graphiques modernisés, températures bassin/extérieur et delta thermique ;
* mode TRAITEMENT avec durée réglable de 5 minutes à 24 heures et affichage du temps restant.

Les documents `docs/V1.1/` restent la référence fonctionnelle détaillée du moteur de filtration.

## Base fonctionnelle V1.1

* sonde de température directement immergée dans le bassin ;
* suppression du délai de circulation nécessaire à la température ;
* calibrage signé de `−3,0 à +3,0 °C` par pas de `0,1 °C` ;
* objectif quotidien basé sur la température calibrée moyenne de la veille, figée au changement de jour après au moins 18 heures de mesures valides ;
* planification visant une fin deux heures avant le coucher du soleil ;
* BH1750 déporté sur D1 mini et transmis à l'ESP32 Jardin par Packet Transport UDP ;
* MES-004 étendu à la liaison distante et à l'état du BH1750 ;
* chauffage solaire de secours lorsque la température extérieure dépasse celle du bassin de `2 °C`, avec arrêt à `1 °C` ;
* dashboard Concept D sombre cyan/violet, avec quatre graphiques détaillés sur 24 heures, statistiques min/max, jauge de progression et vues Pilotage / Solaire / Diagnostics.

## Installation

Consulter :

```text
docs/V1.1/INSTALLATION.md
docs/V1.1/MIGRATION-V1.0-V1.1.md
docs/V1.1/RECETTE-V1.1.md
```

Après chaque mise à jour de la branche, resynchroniser les packages installés :

```bash
cp /config/pool-controller-ha/installation/packages/piscine.yaml /config/packages/piscine.yaml
cp /config/pool-controller-ha/installation/packages/piscine_diagnostics.yaml /config/packages/piscine_diagnostics.yaml
```

## Avertissement de migration du calibrage

L'identifiant historique du helper est conservé, mais sa formule change :

```text
V1.0 : brute − correction
V1.1 : brute + calibrage
```

Une ancienne correction `+2,0 °C` doit donc devenir un calibrage `−2,0 °C`.

## Documentation

* architecture : `docs/ARCHITECTURE.md` ;
* conventions : `docs/CONVENTIONS.md` ;
* documentation courante : `docs/V1.1/` ;
* historique : `docs/V1.0/` ;
* exemples ESPHome : `esphome/`.

## Entités physiques nouvelles

```text
sensor.jardin_esp32_jardin_temperature_bassin
binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite
binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok
```

Le mode doit être placé sur `OFF` pendant la migration et la vérification de configuration.
