# Pool Controller Home Assistant

Contrôleur de filtration, de chauffage solaire et de surveillance hydraulique pour Home Assistant.

## Fonctions V1

- filtration quotidienne calculée selon la température de l'eau ;
- planification visant une fin de l'objectif quotidien deux heures avant le coucher du soleil ;
- chauffage solaire lorsque la luminosité est suffisante et que la consigne n'est pas atteinte ;
- protection périodique du serpentin ;
- modes `OFF`, `SECURISATION`, `AUTO`, `TRAITEMENT` et `MARCHE_FORCEE` ;
- diagnostics de mesure, de cohérence et de procédé ;
- arrêt de la filtration au niveau `CRITIQUE` ;
- journalisation et notifications ;
- énergie quotidienne de la pompe et bilan solaire quotidien ;
- tableau de bord Home Assistant natif, sans carte personnalisée, avec heure prévisionnelle d’atteinte de l’objectif quotidien.

## Installation

Les fichiers prêts à copier sont fournis dans :

```text
installation/
├── configuration_extrait.yaml
└── packages/
    ├── piscine.yaml
    └── piscine_diagnostics.yaml
```

La procédure détaillée se trouve dans :

```text
docs/V1.0/INSTALLATION.md
```

Après installation, exécuter la recette :

```text
docs/V1.0/RECETTE-V1.md
```

Le mode doit rester `OFF` jusqu'à la validation des contrôles de mise en service.

## Documentation

- règles fonctionnelles : `docs/V1.0/` ;
- organisation : `docs/ARCHITECTURE.md` ;
- conventions : `docs/CONVENTIONS.md`.


## Température piscine

La température utilisée par les calculs est corrigée en soustrayant `input_number.pcha_correction_temperature_piscine` et n'est actualisée qu'après une circulation stabilisée. Les valeurs hors de l'intervalle strict 10–50 °C sont signalées mais n'écrasent ni la dernière valeur cohérente ni les minimum/maximum quotidiens.
