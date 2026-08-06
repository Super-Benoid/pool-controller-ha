# Installation — PCHA V1.1

**Version :** 1.1  
**Statut :** Figée

---

# 1. Préparation

La structure cible est :

```text
/config/
├── configuration.yaml
├── packages/
│   ├── piscine.yaml
│   └── piscine_diagnostics.yaml
└── pool-controller-ha/
```

Copier le dossier `pool-controller-ha` dans `/config/`.

# 2. Prérequis matériels V1.1

Vérifier la présence de ces entités avant de charger PCHA :

```text
sensor.jardin_esp32_jardin_temperature_bassin
sensor.jardin_esp32_jardin_luminosite
binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite
binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok
sensor.temperature_exterieure_temperature
```

Le bus I²C de l’ESP32 Jardin doit rester actif pour la sonde immergée du bassin. Les fichiers de référence ESPHome pour la chaîne de luminosité distante sont fournis dans `esphome/`.

# 3. Packages

Copier :

```text
installation/packages/piscine.yaml
installation/packages/piscine_diagnostics.yaml
```

vers `/config/packages/`, puis vérifier :

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Après une mise à jour Git du projet, resynchroniser les deux fichiers installés avant de vérifier la configuration :

```bash
cp /config/pool-controller-ha/installation/packages/piscine.yaml /config/packages/piscine.yaml
cp /config/pool-controller-ha/installation/packages/piscine_diagnostics.yaml /config/packages/piscine_diagnostics.yaml
```

Cette étape est indispensable lorsqu'une nouvelle famille d'entités est ajoutée. Le calcul des cycles nécessite notamment le chargement de `helpers/sensor.yaml` par la ligne `sensor:` de `/config/packages/piscine.yaml`.

# 4. Thème et tableau de bord

Fusionner les blocs `frontend:` et `lovelace:` de `installation/configuration_extrait.yaml` dans `/config/configuration.yaml`. Le dossier `themes/` contient le thème sombre **PCHA Concept D** et ses variantes cyan, violette et alerte.

Après redémarrage, le dashboard sélectionne automatiquement le thème au niveau de chaque vue. Pour l’appliquer aussi à la barre latérale et à l’en-tête Home Assistant, sélectionner **PCHA Concept D** dans le profil utilisateur.

# 5. Migration du calibrage

L'identifiant `input_number.pcha_correction_temperature_piscine` est conservé, mais son sens change :

```text
V1.0 : température = brute − correction
V1.1 : température = brute + calibrage
```

Il faut donc inverser le signe de l'ancienne valeur. Exemple :

```text
ancienne correction : +2,0 °C
nouveau calibrage   : −2,0 °C
```

Cette étape doit être réalisée immédiatement après le premier redémarrage V1.1.

# 6. Valeurs recommandées de mise en service

| Paramètre | Valeur initiale |
|---|---:|
| Température de consigne | `28 °C` |
| Seuil de luminosité chauffage | `15 000 lx` |
| Calibrage température bassin | `0,0 °C`, puis étalonnage réel |
| Durée du traitement | `60 min` |
| Temps minimum de marche | `5 min` |
| Temps minimum d'arrêt | `25 min` |
| Validation température bassin | `30 s` |
| Validation débit | `30 s` |
| Validation luminosité distante | `60 s` |

Le mode initial doit rester `OFF` pendant les contrôles.

# 7. Validation

1. Mettre PCHA en `OFF`.
2. Vérifier la configuration Home Assistant.
3. Redémarrer Home Assistant.
4. Vérifier les entités `pcha_*`, notamment `sensor.pcha_progression_objectif_quotidien`.
5. Vérifier que `sensor.pcha_volume_filtre_total`, `sensor.pcha_volume_filtre_quotidien` et `sensor.pcha_renouvellements_bassin_du_jour` sont numériques et augmentent pendant la filtration.
6. Contrôler le calibrage signé.
7. Vérifier que les deux états de luminosité distante sont `on`.
8. Exécuter `RECETTE-V1.1.md`.

# 8. Retour arrière

Sauvegarder avant installation :

```text
/config/configuration.yaml
/config/packages/
/config/pool-controller-ha/
```

En cas d'échec, remettre le mode sur `OFF`, restaurer les fichiers sauvegardés, puis vérifier la configuration avant de redémarrer.
