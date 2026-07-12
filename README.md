# Pool Controller HA

Contrôleur intelligent de filtration et de chauffage solaire pour Home Assistant.

## Objectifs

- Filtration automatique basée sur la température de l'eau.
- Chauffage solaire intelligent avec serpentin.
- Protection du serpentin contre la surchauffe.
- Surveillance du débit de filtration.
- Surveillance de la consommation électrique de la pompe.
- Tableau de bord Home Assistant.
- Notifications en cas d'anomalie.

## Fonctionnement

Le contrôleur prend ses décisions toutes les 5 minutes.

Il utilise les informations suivantes :

- Température de l'eau
- Température extérieure
- Luminosité
- Débit de filtration
- Consommation électrique de la pompe

Le système choisit automatiquement le meilleur mode de fonctionnement.

## Modes

- Arrêt
- Validation température
- Filtration
- Chauffage solaire
- Protection serpentin
- Défaut

## Matériel utilisé

- Home Assistant
- Pompe pilotée par prise Zigbee
- ESP32
- Sonde de température piscine
- Débitmètre
- Sonde de température extérieure Zigbee
- Capteur de luminosité