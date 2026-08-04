# SPEC-004 — Couche d'abstraction et configuration

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit l'interface entre le matériel, les helpers et la logique métier PCHA.

# 2. Principes

* Les automatisations, scripts et diagnostics utilisent les entités PCHA.
* Une mesure incohérente ne remplace pas la dernière mesure cohérente.
* La plage physique stricte de la température bassin est `10 °C < T < 50 °C`.
* La température bassin est exploitable immédiatement, sans circulation préalable.

# 3. Correspondances matérielles

| Source physique Home Assistant | Entité PCHA |
|---|---|
| `sensor.jardin_esp32_jardin_temperature_bassin` | `sensor.pcha_temperature_piscine_brute`, puis `sensor.pcha_temperature_piscine` |
| `sensor.temperature_exterieure_temperature` | `sensor.pcha_temperature_exterieure` |
| `sensor.jardin_esp32_jardin_luminosite` | `sensor.pcha_luminosite` |
| `binary_sensor.jardin_esp32_jardin_liaison_capteur_luminosite` | `binary_sensor.pcha_liaison_luminosite_distante` |
| `binary_sensor.jardin_esp32_jardin_capteur_luminosite_ok` | `binary_sensor.pcha_capteur_luminosite_distant_ok` |
| `sensor.jardin_esp32_jardin_debit_filtration_piscine` | `sensor.pcha_debit_filtration` |
| `sensor.prises_exterieur_power` | `sensor.pcha_puissance_pompe_filtration` |
| `sensor.prises_exterieur_energy` | `sensor.pcha_energie_pompe_filtration` |

Les identifiants métier historiques contenant `temperature_piscine` sont conservés pour la compatibilité, même si leur libellé utilisateur devient **température bassin**.

# 4. Calibrage de température

Le helper historique est conservé :

```text
input_number.pcha_correction_temperature_piscine
```

En V1.1, il représente un calibrage signé :

```text
minimum : −3,0 °C
maximum : +3,0 °C
pas     : 0,1 °C
formule : température calibrée = température brute + calibrage
```

Exemples :

* une sonde qui affiche `0,6 °C` de moins reçoit un calibrage `+0,6 °C` ;
* une sonde qui affiche `0,8 °C` de trop reçoit un calibrage `−0,8 °C`.

Le helper `input_number.pcha_temps_validation_temperature_piscine` n'est plus un temps de stabilisation hydraulique. Il sert uniquement à temporiser `MES-001` et `COH-002`.

# 5. Attributs température

`sensor.pcha_temperature_piscine` expose notamment :

* `source_available` ;
* `source_coherent` ;
* `corrected_value_coherent` pour compatibilité ;
* `measurement_valid` ;
* `calibrage_applique` ;
* `temperature_brute` ;
* `temperature_calibree_candidate`.

# 6. Chaîne de luminosité

`sensor.pcha_luminosite` est disponible seulement lorsque les trois conditions sont vraies :

```text
liaison Packet Transport active
ET BH1750 distant déclaré OK
ET mesure numérique comprise entre 0 et 100 000 lx
```

La dernière valeur numérique cohérente peut rester affichée, mais les attributs `source_available` et `source_coherent` passent à faux dès que la chaîne n'est plus exploitable ou que la mesure sort de la plage `0 à 100 000 lx`.

# 7. Helpers configurables

| Helper | Fonction |
|---|---|
| `input_number.pcha_correction_temperature_piscine` | Calibrage signé bassin |
| `input_number.pcha_temperature_de_consigne` | Consigne bassin |
| `input_number.pcha_seuil_luminosite_chauffage` | Seuil normal de chauffage solaire |
| `input_number.pcha_temps_validation_temperature_piscine` | Validation diagnostics température |
| `input_number.pcha_temps_validation_luminosite` | Validation MES-004 |
| `input_number.pcha_temps_validation_debit` | Validation débit |
| `input_number.pcha_temps_marche_pompe_min` | Marche minimale |
| `input_number.pcha_temps_arret_pompe_min` | Arrêt minimal |
| `input_number.pcha_duree_traitement` | Durée traitement |
