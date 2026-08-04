# Migration PCHA V1.0 → V1.1

# 1. Mettre le mode sur OFF

Avant tout remplacement de fichier :

```text
input_select.pcha_mode_de_fonctionnement = OFF
```

# 2. Vérifier les nouvelles sources

```text
sensor.jardin_esp32_jardin_temperature_bassin
binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite
binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok
```

# 3. Remplacer le projet complet

Remplacer `/config/pool-controller-ha/` par le dossier V1.1, sans modifier les deux packages d'inclusion déjà installés.

# 4. Inverser l'ancien réglage de température

L'ancien helper est restauré avec sa valeur V1.0. Son signe doit être inversé :

| Ancienne correction V1.0 | Nouveau calibrage V1.1 |
|---:|---:|
| `+2,0 °C` | `−2,0 °C` |
| `+0,7 °C` | `−0,7 °C` |
| `0,0 °C` | `0,0 °C` |

# 5. Vérifier puis redémarrer

Exécuter la vérification de configuration, redémarrer Home Assistant, puis suivre `RECETTE-V1.1.md`.
