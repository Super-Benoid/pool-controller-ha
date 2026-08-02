# ARCHITECTURE.md

# Pool Controller Home Assistant (PCHA)

Version : V1.0
Statut : Figée

---

# 1. Philosophie du projet

Le Pool Controller Home Assistant (PCHA) est conçu comme un logiciel industriel.

Les **SPEC** définissent le comportement fonctionnel.

Le code est uniquement une implémentation de ces SPEC.

Les règles suivantes sont immuables :

* une SPEC = un domaine fonctionnel ;
* une responsabilité = un fichier ;
* une information = une source unique de vérité ;
* aucun accès direct aux équipements physiques par la logique métier.

---

# 2. Architecture générale

```text
/config/
├── configuration.yaml
├── packages/
│   ├── piscine.yaml
│   └── piscine_diagnostics.yaml
└── pool-controller-ha/
    ├── automations/
    │   ├── chauffage.yaml
    │   ├── filtration.yaml
    │   ├── journalisation.yaml
    │   ├── machine.yaml
    │   ├── notifications.yaml
    │   └── traitement.yaml
    ├── dashboard/
    │   └── piscine.yaml
    ├── diagnostics/
    │   └── diagnostics.yaml
    ├── docs/
    │   ├── ARCHITECTURE.md
    │   ├── CONVENTIONS.md
    │   └── V1.0/
    │       ├── 00-Introduction.md
    │       ├── INSTALLATION.md
    │       ├── RECETTE-V1.md
    │       └── SPEC-000 à SPEC-009
    ├── helpers/
    │   ├── input_boolean.yaml
    │   ├── input_number.yaml
    │   ├── input_select.yaml
    │   ├── input_text.yaml
    │   └── timer.yaml
    ├── installation/
    │   ├── configuration_extrait.yaml
    │   └── packages/
    │       ├── piscine.yaml
    │       └── piscine_diagnostics.yaml
    ├── scripts/
    │   ├── machine.yaml
    │   ├── pompe.yaml
    │   └── traitement.yaml
    └── templates/
        ├── actionneurs.yaml
        ├── calculs.yaml
        ├── capteurs.yaml
        ├── chauffage.yaml
        └── systeme.yaml
```

Les dossiers et les fichiers sont classés par ordre alphabétique.

Un fichier n'est créé que s'il possède une responsabilité réelle.

---

# 3. Architecture logique

Le contrôleur est construit par couches.

```text
Équipements physiques
        │
        ▼
Templates (abstraction)
        │
        ▼
Entités métier PCHA
        │
        ▼
Machine à états
        │
        ▼
Scripts
        │
        ▼
Automatisations
```

Chaque couche dépend uniquement de la couche située immédiatement en dessous.

Aucune dépendance directe n'est autorisée entre une couche haute et les équipements physiques.

---

# 4. Couche d'abstraction

Les équipements physiques ne sont jamais utilisés directement par la logique métier.

Exemple :

```text
sensor.jardin_esp32_jardin_debit_filtration_piscine
                │
                ▼
sensor.pcha_debit_filtration
```

Toutes les couches supérieures utilisent exclusivement :

* `sensor.pcha_*`
* `binary_sensor.pcha_*`

Les équipements physiques peuvent être remplacés sans modifier la logique métier.


# 5. Architecture

La couche d'abstraction est composée de deux niveaux.

## Niveau 1 — Abstraction

Transformation des équipements physiques en entités PCHA.

Aucune logique métier.

Exemple :

```text
sensor.jardin_esp32_jardin_temperature_piscine
        │
        ▼
sensor.pcha_temperature_piscine_brute
        │
        ▼
sensor.pcha_temperature_piscine
```
Elle est réalisée uniquement dans la SPEC-004.

---

## Niveau 2 — Métier

Création des états logiques utilisés par le contrôleur.

Exemple :

```text
sensor.pcha_debit_filtration
        │
        ▼
binary_sensor.pcha_filtration_requise

binary_sensor.pcha_chauffage_solaire_actif
```

Les scripts et automatisations utilisent exclusivement ces états.

---

# 6. Contrat d'interface

Chaque fichier commence par un contrat d'interface.

Exemple :

```text
Entrées

    sensor.pcha_debit_filtration

Sorties

    binary_sensor.pcha_filtration_requise
```

Le contrat décrit uniquement :

* les entités consommées ;
* les entités produites.

---

# 7. Convention de nommage

Toutes les entités créées par le projet utilisent le préfixe :

```text
pcha_
```

Exemples :

```text
sensor.pcha_debit_filtration

sensor.pcha_puissance_pompe_filtration

sensor.pcha_energie_pompe_filtration

binary_sensor.pcha_chauffage_solaire_actif

script.pcha_pompe_demarrer
```

Les équipements physiques conservent leur nom d'origine.

---

# 8. Helpers

Les Helpers représentent uniquement les paramètres configurables par l'utilisateur.

Ils ne contiennent jamais :

* une mesure ;
* un état calculé ;
* une information déductible.

Le nombre de Helpers est volontairement limité au strict nécessaire.

---

# 9. Scripts

Les Scripts réalisent des actions.

Ils :

* utilisent exclusivement des entités PCHA ;
* n'accèdent jamais directement aux équipements physiques.

Les commandes des équipements passent toujours par les Scripts.

---

# 10. Automatisations

Les Automatisations orchestrent le fonctionnement global.

Elles :

* utilisent uniquement des entités PCHA ;
* ne réalisent aucun calcul complexe ;
* ne pilotent jamais directement les équipements physiques.

---

# 11. Diagnostics

Les Diagnostics utilisent uniquement :

* les entités PCHA ;
* les états métier.

Ils ne lisent jamais directement les équipements physiques.

Ils surveillent uniquement les informations indispensables au fonctionnement.

---

# 12. Développement

Chaque nouveau module suit obligatoirement le cycle suivant :

1. Validation de la SPEC.
2. Définition du contrat d'interface.
3. Création du squelette.
4. Implémentation.
5. Tests.
6. Validation.
7. Module figé.

---

# 13. Source unique de vérité

Chaque information possède une seule source.

Une règle métier ne doit jamais être dupliquée.

Une même décision ne doit jamais être implémentée à plusieurs endroits.

---

# 14. Évolutions

Une fois une SPEC validée :

* elle est considérée comme figée pour la V1 ;
* toute évolution devient une proposition pour une version ultérieure.

L'architecture suit le même principe.

Elle n'évolue que si un besoin réel apparaît pendant l'implémentation.

---

# 15. Objectif

Cette architecture garantit :

* indépendance vis-à-vis du matériel ;
* forte modularité ;
* maintenance facilitée ;
* testabilité ;
* évolutivité ;
* lisibilité du projet.

Toute implémentation doit respecter intégralement ce document.

---

# 16. HAL

La couche d'abstraction (SPEC-004) constitue le HAL du projet.

---

17. Architecture d'implémentation
Home Assistant
│
├── helpers
│
├── templates
│
├── scripts
│
├── automations
│
└── diagnostics

# 17.1 Dépendances

Matériel

↓

HAL (SPEC-004)

↓

Machine à états (SPEC-005)

↓

Modes (SPEC-006)

↓

Fonctions
(SPEC-003 / SPEC-008)

↓

Diagnostics (SPEC-007)

# 17.2 Règles d'implémentation

Les templates d'abstraction implémentent exclusivement la SPEC-004.
Les templates métier implémentent la SPEC fonctionnelle indiquée dans leur contrat d'interface.
Les scripts ne prennent aucune décision.
Les automatisations ne contiennent aucune logique métier.
Les diagnostics appliquent exclusivement la SPEC-007.
Les calculs fonctionnels sont réalisés uniquement par les composants définis dans les SPEC concernées.
Les entités pcha_* constituent l'unique interface entre le matériel et les couches fonctionnelles.

# 17.3 Dépendances

Scripts
        │
        ├──► Templates
        ✖
Diagnostics
        │
        ├──► Scripts
        ✖
Fonctions
        │
        ├──► Capteurs physiques
        ✖