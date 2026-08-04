# SPEC-001 — Inventaire matériel

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC inventorie les équipements physiques de la V1.1. Elle ne définit aucun comportement fonctionnel.

# 2. Circuit hydraulique

```text
Aspiration → Pompe → Débitmètre → Serpentin → Refoulement
```

La sonde de température bassin est immergée et ne fait plus partie de la tuyauterie de sortie de pompe. Elle est raccordée au bus I²C local de l’ESP32 Jardin ; ce bus doit donc être conservé.

# 3. Équipements présents

| Équipement | Fonction | Unité / état |
|---|---|---|
| Pompe de filtration commandée | Assurer la circulation d'eau | Marche / arrêt |
| Débitmètre | Mesurer le débit du circuit | L/h |
| Sonde température bassin | Mesurer directement la température de l'eau | °C |
| ESP32 Jardin | Acquisition de la sonde bassin sur son bus I²C local, actionneurs et réception de la luminosité distante | — |
| BH1750 | Mesurer l'ensoleillement disponible | lx |
| D1 mini ESP8266 | Lire le BH1750 et diffuser sa mesure | Wi-Fi / UDP |
| Thermomètre extérieur | Mesurer la température de l'air | °C |
| Mesure de puissance | Mesurer la puissance instantanée de la pompe | W |
| Compteur d'énergie | Mesurer l'énergie consommée par la pompe | kWh |

# 4. Chaîne de luminosité distante

```text
BH1750 — I²C court — D1 mini — Packet Transport UDP — ESP32 Jardin
```

La D1 mini transmet :

* `luminosite_jardin` ;
* `capteur_luminosite_ok`.

L'ESP32 publie vers Home Assistant :

* `sensor.jardin_esp32_jardin_luminosite` ;
* `binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite` ;
* `binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok`.

# 5. Équipements absents

* vanne motorisée ;
* sonde de température du serpentin ;
* sonde de température du local technique.

# 6. Références

* SPEC-000
* SPEC-004
* SPEC-007
* SPEC-008
