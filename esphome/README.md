# ESPHome — PCHA V1.1

## D1 mini

`d1-mini-esp8266-luminosite-pisc.yaml` est un fichier complet pour la carte proche du BH1750.

Ajouter dans son `secrets.yaml` :

```yaml
packet_transport_key: "cle-longue-identique-sur-les-deux-cartes"
d1_mini_esp8266_luminosite_pisc__fallback_password: "mot-de-passe-a-remplacer"
```

## ESP32 Jardin

`esp32-jardin-packet-transport.yaml` est un fragment à fusionner dans le fichier existant. Il ne contient ni les relais, ni les débitmètres, ni la sonde de température bassin.

Après compilation, Home Assistant doit disposer exactement de :

```text
sensor.jardin_esp32_jardin_luminosite
binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite
binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok
```

Si Home Assistant crée un autre identifiant, renommer l'entité avant d'activer PCHA V1.1 ou adapter uniquement la couche d'abstraction `templates/capteurs.yaml`.
