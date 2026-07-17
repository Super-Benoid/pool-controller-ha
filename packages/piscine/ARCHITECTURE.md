# Pool Controller Home Assistant (PCHA)

# Philosophie du projet

Le Pool Controller Home Assistant est conçu comme un logiciel industriel.

Les **spécifications (SPEC)** constituent la référence fonctionnelle.

Le **code est une implémentation des SPEC**, jamais l'inverse.

---

# Architecture du projet

Le projet est organisé selon les principes suivants :

* une SPEC = un domaine fonctionnel ;
* un domaine fonctionnel = un ensemble de fichiers ;
* un fichier = une responsabilité unique.

```text
config/
└── pool-controller-ha/
    │
    ├── docs/
    │   ├── SPEC-000
    │   ├── SPEC-001
    │   ├── SPEC-002
    │   ├── SPEC-003
    │   ├── SPEC-004
    │   ├── SPEC-005
    │   ├── SPEC-006
    │   ├── SPEC-007
    │   ├── SPEC-008
    │   └── SPEC-009
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
            └── ARCHITECTURE.md
```

---

# Conventions de développement

## Préfixe des entités

Toutes les entités créées par le contrôleur utilisent le préfixe :

`pcha_`

Les entités provenant d'intégrations externes (ESPHome, Shelly, MQTT, etc.) conservent leur nom d'origine.

---

# Convention de nommage

Le nom d'une entité doit permettre d'identifier immédiatement sa fonction.

| Type                  | Préfixe               | Exemple                                       |
| --------------------- | --------------------- | --------------------------------------------- |
| Mesure                | `sensor.pcha_`        | `sensor.pcha_debit`                           |
| Consigne              | `pcha_consigne_`      | `input_number.pcha_consigne_temperature`      |
| Seuil                 | `pcha_seuil_`         | `input_number.pcha_seuil_debit_critique`      |
| Temporisation         | `pcha_tempo_`         | `input_number.pcha_tempo_validation_debit`    |
| État logique          | `binary_sensor.pcha_` | `binary_sensor.pcha_filtration_active`        |
| Paramètre utilisateur | `input_boolean.pcha_` | `input_boolean.pcha_desactiver_securites_off` |
| Sélection utilisateur | `input_select.pcha_`  | `input_select.pcha_mode`                      |

---

# Couche d'abstraction

Le contrôleur ne manipule jamais directement les entités physiques.

Les capteurs physiques sont convertis en entités métier via les Templates.

Architecture logique :

```text
Capteurs physiques
        │
        ▼
Templates
        │
        ▼
Scripts
        │
        ▼
Automatisations
```

Règles :

* les Scripts n'accèdent jamais aux capteurs physiques ;
* les Automatisations n'accèdent jamais aux capteurs physiques ;
* les Diagnostics n'accèdent jamais aux capteurs physiques.

Toute la logique métier utilise exclusivement des entités `pcha_*`.

---

# Organisation des fichiers

Chaque fichier possède une responsabilité unique.

Un fichier n'est créé que s'il contient une logique propre.

Aucun fichier vide n'est conservé dans le projet.

---

# Correspondance avec les SPEC

| Domaine           | SPEC     |
| ----------------- | -------- |
| Helpers           | SPEC-004 |
| Machine à états   | SPEC-005 |
| Modes utilisateur | SPEC-006 |
| Diagnostics       | SPEC-007 |
| Filtration        | SPEC-003 |
| Chauffage solaire | SPEC-008 |
| Journalisation    | SPEC-009 |

Toute évolution fonctionnelle doit être réalisée dans la SPEC concernée avant toute modification du code.

---

# Cycle de développement

Chaque module suit systématiquement le cycle suivant :

1. Validation de la SPEC.
2. Implémentation.
3. Tests unitaires.
4. Validation fonctionnelle.
5. Gel du module.

Une fois un module validé, seules des corrections de bugs sont autorisées.

Les évolutions fonctionnelles sont intégrées dans une nouvelle version des SPEC.

---

# Principes d'architecture

Le projet applique les règles suivantes :

* une SPEC = un domaine fonctionnel ;
* un domaine fonctionnel = un ensemble de fichiers ;
* un fichier = une responsabilité unique ;
* une entité = une fonction ;
* une information = une source unique de vérité ;
* aucune duplication de logique ;
* aucune dépendance directe entre la logique métier et les équipements physiques.
