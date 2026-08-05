# Architecture — Pool Controller Home Assistant

**Version :** V1.1  
**Statut :** Figée

---

# 1. Principes

PCHA est organisé comme un logiciel industriel :

* une SPEC par domaine fonctionnel ;
* une responsabilité par fichier ;
* une source unique de vérité ;
* aucune lecture directe du matériel par les fonctions métier ;
* aucune commande physique hors de la couche d'actionnement.

# 2. Arborescence

```text
pool-controller-ha/
├── automations/
├── dashboard/
├── diagnostics/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONVENTIONS.md
│   ├── V1.0/              # archive
│   └── V1.1/              # référence courante
├── esphome/
├── helpers/
├── installation/
├── scripts/
└── templates/
```

Les fichiers d'un même dossier sont classés par ordre alphabétique.

# 3. Couches

```text
Équipements physiques / ESPHome
        │
        ▼
Abstraction PCHA — SPEC-004
        │
        ▼
Calculs et états métier — SPEC-003 / 005 / 006 / 008
        │
        ▼
Scripts d'actionnement
        │
        ▼
Automatisations d'orchestration
        │
        ▼
Dashboard, diagnostics, notifications
```

# 4. Température bassin V1.1

```text
Sonde immergée — I²C local — ESP32 Jardin
        │
        ▼
sensor.jardin_esp32_jardin_temperature_bassin
        │
        ├── disponibilité
        ├── cohérence stricte 10–50 °C
        ▼
sensor.pcha_temperature_piscine_brute
        │
        ├── calibrage signé −3 à +3 °C
        ├── aucune attente de circulation
        ▼
sensor.pcha_temperature_piscine
```

Les identifiants historiques `temperature_piscine` sont conservés comme contrats d'interface, mais les libellés utilisateur indiquent désormais **bassin**.

# 5. Référence de l'objectif quotidien

```text
Température calibrée cohérente
        │
        ├── échantillonnage chaque minute
        ├── moyenne de la journée terminée
        ▼
sensor.pcha_temperature_reference_objectif_quotidien
        │
        ├── figement au changement de jour
        └── calcul de durée selon la référence
        ▼
sensor.pcha_objectif_filtration_quotidien
```

Le capteur trigger-based conserve son état et ses attributs après redémarrage.

# 6. Luminosité distante

```text
BH1750
  │ I²C court
  ▼
D1 mini ESP8266
  │ Packet Transport UDP chiffré
  ▼
ESP32 Jardin
  ├── luminosité
  ├── état du fournisseur
  └── état du BH1750
        │
        ▼
Abstractions PCHA
  ├── sensor.pcha_luminosite
  ├── binary_sensor.pcha_liaison_luminosite_distante
  └── binary_sensor.pcha_capteur_luminosite_distant_ok
```

`MES-004` consomme uniquement ces abstractions.

# 7. Chauffage solaire

```text
MES-004 inactif
→ pilotage par luminosité

MES-004 actif
→ pilotage de secours par écart température extérieure / bassin
→ activation à +2 °C
→ arrêt à +1 °C
```

La protection du serpentin reste indépendante du chauffage de confort. Pendant MES-004, elle utilise la position du soleil comme secours.

# 8. Contrats de fichiers

Chaque fichier YAML commence par :

* ses entrées ;
* ses sorties ;
* la SPEC propriétaire.

Les diagnostics et automatisations ne doivent pas contourner les entités `pcha_*`.

# 9. Persistance

Les états quotidiens nécessitant une restauration utilisent des capteurs template déclenchés :

* objectif quotidien et référence ;
* temps de filtration réalisé ;
* minimum et maximum de température ;
* compteurs solaires.

# 10. Versions

* `docs/V1.0/` est conservé comme historique figé.
* `docs/V1.1/` décrit le code courant.
* toute évolution ultérieure crée une nouvelle version documentaire sans réécrire l'historique.
