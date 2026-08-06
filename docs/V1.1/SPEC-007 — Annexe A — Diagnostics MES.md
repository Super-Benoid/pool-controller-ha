# SPEC-007 — Annexe A — Diagnostics MES

**Version :** 1.1  
**Statut :** Figée

---

# 1. Tableau

| ID | Mesure | Gravité | Réarmement |
|---|---|---|---|
| `MES-001` | Température bassin | `DEGRADE` | `TEMPORISE` |
| `MES-002` | Débit | `CRITIQUE` | `TEMPORISE` |
| `MES-003` | Puissance | `DEGRADE` | `TEMPORISE` |
| `MES-004` | Luminosité distante | `DEGRADE` | `TEMPORISE` |

# 2. MES-001 — Température bassin indisponible

Actif lorsque `sensor.jardin_esp32_jardin_temperature_bassin` ne fournit plus de valeur numérique pendant le délai configuré. La mesure n'attend jamais le démarrage de la pompe.

# 3. MES-003 — Puissance pompe indisponible

MES-003 devient actif lorsque `sensor.prises_exterieur_power` ne fournit plus de valeur numérique pendant **60 secondes consécutives**. Une interruption plus courte est considérée comme une microcoupure de communication et ne déclenche pas le diagnostic.

Après le retour de la mesure, MES-003 se réarme automatiquement lorsque la puissance reste numérique pendant **10 secondes consécutives**. Sa gravité reste `DEGRADE` et n'interdit pas la filtration.

# 4. MES-004 — Luminosité distante indisponible

La chaîne surveillée est :

```text
BH1750 → D1 mini → Wi-Fi/UDP → ESP32 Jardin → PCHA
```

MES-004 devient actif, après `input_number.pcha_temps_validation_luminosite`, si l'une des conditions suivantes existe :

* liaison Packet Transport absente ;
* D1 mini joignable mais BH1750 sans mesure valide récente ;
* valeur reçue non numérique, indisponible ou hors de la plage `0 à 100 000 lx`.

L'attribut `cause` prend l'une des valeurs :

```text
LIAISON_PACKET_TRANSPORT
CAPTEUR_BH1750
MESURE_INDISPONIBLE
MESURE_HORS_LIMITES
AUCUNE
```

# 5. Effets de MES-004

MES-004 maintient le niveau `DEGRADE`, mais n'interdit plus systématiquement le chauffage solaire :

* la stratégie normale par luminosité est abandonnée ;
* la température extérieure devient la source de secours conformément à la SPEC-008 ;
* les compteurs de luminosité sont suspendus ;
* la filtration normale reste autorisée ;
* la protection du serpentin reste disponible par la position du soleil.
