# Pool Controller Home Assistant — PCHA V1.1

Contrôleur de filtration, de chauffage solaire et de surveillance hydraulique pour Home Assistant.

## Évolutions V1.1

* sonde de température directement immergée dans le bassin ;
* suppression du délai de circulation nécessaire à la température ;
* calibrage signé de `−3,0 à +3,0 °C` par pas de `0,1 °C` ;
* objectif quotidien basé sur le maximum brut entre minuit et lever du soleil + 30 minutes, puis figé ;
* planification visant une fin deux heures avant le coucher du soleil ;
* BH1750 déporté sur D1 mini et transmis à l'ESP32 Jardin par Packet Transport UDP ;
* MES-004 étendu à la liaison distante et à l'état du BH1750 ;
* chauffage solaire de secours lorsque la température extérieure dépasse celle du bassin de `2 °C`, avec arrêt à `1 °C` ;
* dashboard modernisé : page d'accueil synthétique, vues dédiées Pilotage / Solaire / Diagnostics et cartes de tendance natives `tile` sur 24 heures.

## Installation

Consulter :

```text
docs/V1.1/INSTALLATION.md
docs/V1.1/MIGRATION-V1.0-V1.1.md
docs/V1.1/RECETTE-V1.1.md
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
