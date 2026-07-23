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
config/
└── pool-controller-ha/
    │
    ├── docs/
    │   ├── SPEC-000 — Principes généraux.md
    │   ├── SPEC-001 — Inventaire matériel.md
    │   ├── SPEC-002 — Interface utilisateur.md
    │   ├── SPEC-003 — Gestion de la filtration.md
    │   ├── SPEC-004 — Couche d'abstraction et configuration.md
    │   ├── SPEC-005 — Machine à états.md
    │   ├── SPEC-006 — Modes de fonctionnement.md
    │   ├── SPEC-007 — Diagnostics et sécurités Partie 1 — Architecture des diagnostics.md
    │   ├── SPEC-007 — Diagnostics et sécurités Partie 2 — Gestion des diagnostics.md
    │   ├── SPEC-007 — Annexe A Diagnostics MES (Mesures).md
    │   ├── SPEC-007 — Annexe B Diagnostics COH (Cohérence).md
    │   ├── SPEC-007 — Annexe C Diagnostics PRO (Procédé).md
    │   ├── SPEC-008 — Chauffage solaire.md
    │   └── SPEC-009 — Journalisation et notifications.md
    │
    └── packages/
        └── piscine/
            │
            ├── automations/
            │   ├── chauffage_solaire.yaml
            │   ├── filtration.yaml
            │   └── machine_etats.yaml
            │
            ├── diagnostics/
            │   ├── coh.yaml
            │   ├── mes.yaml
            │   └── pro.yaml
            │
            ├── helpers/
            │   ├── chauffage_solaire.yaml
            │   ├── filtration.yaml
            │   ├── hydraulique.yaml
            │   └── utilisateur.yaml
            │
            ├── scripts/
            │   ├── chauffage_solaire.yaml
            │   ├── filtration.yaml
            │   └── machine_etats.yaml
            │
            ├── templates/
            │   ├── chauffage_solaire.yaml
            │   ├── diagnostics.yaml
            │   ├── filtration.yaml
            │   ├── hydraulique.yaml
            │   └── machine_etats.yaml
            │
            ├── timers/
            │   └── timers.yaml
            │
            ├── ARCHITECTURE.md
            └── CONVENTIONS.md

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
sensor.pcha_debit
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
sensor.pcha_temperature_piscine
```
Elle est réalisé uniquement dans la SPEC-004.

---

## Niveau 2 — Métier

Création des états logiques utilisés par le contrôleur.

Exemple :

```text
sensor.pcha_debit
        │
        ▼
binary_sensor.pcha_debit_ok

binary_sensor.pcha_filtration_active
```

Les scripts et automatisations utilisent exclusivement ces états.

---

# 6. Contrat d'interface

Chaque fichier commence par un contrat d'interface.

Exemple :

```text
Entrées

    sensor.pcha_debit

Sorties

    binary_sensor.pcha_debit_nominal
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
sensor.pcha_debit

sensor.pcha_puissance_filtration

sensor.pcha_energie_filtration

binary_sensor.pcha_filtration_active

script.pcha_demarrer_filtration
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
