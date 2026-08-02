# Pool Controller Home Assistant

Contrôleur de filtration, de chauffage solaire et de surveillance hydraulique pour Home Assistant.

## Fonctions V1

- filtration quotidienne calculée selon la température de l'eau ;
- planification visant une fin de filtration avant le coucher du soleil ;
- chauffage solaire lorsque la luminosité est suffisante et que la consigne n'est pas atteinte ;
- protection périodique du serpentin ;
- modes `OFF`, `SECURISATION`, `AUTO`, `TRAITEMENT` et `MARCHE_FORCEE` ;
- diagnostics de mesure, de cohérence et de procédé ;
- arrêt de la filtration au niveau `CRITIQUE` ;
- journalisation et notifications ;
- tableau de bord Home Assistant natif, sans carte personnalisée.

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
