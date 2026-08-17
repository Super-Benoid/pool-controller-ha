# Architecture — Pool Controller Home Assistant

**Version :** V3.0  
**Statut :** Courante — validation terrain

---

# 1. Principes

PCHA est organisé comme un logiciel industriel :

* une responsabilité par fichier ;
* une source unique de vérité ;
* aucune lecture directe du matériel par les fonctions métier ;
* aucune commande physique hors de la couche d'actionnement ;
* séparation entre **durée quotidienne à réaliser** et **planification de cette durée** ;
* optimisation météo toujours subordonnée aux diagnostics et aux sécurités.

# 2. Arborescence

```text
pool-controller-ha/
├── automations/
├── dashboard/
│   └── views/
├── diagnostics/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONVENTIONS.md
│   ├── V1.1/              # fondations historiques du moteur
│   └── V3.0/              # référence fonctionnelle courante
├── esphome/
├── helpers/
├── installation/
├── scripts/
└── templates/
```

Les fichiers d'un même dossier sont classés autant que possible par ordre alphabétique.

# 3. Couches

```text
Équipements physiques / ESPHome / intégrations
        │
        ▼
Abstractions PCHA des mesures et de la météo
        │
        ├── mesures bassin / débit / puissance / luminosité
        └── météo quotidienne et horaire
        │
        ▼
Calculs et états métier
        │
        ├── référence de température
        ├── objectif quotidien
        ├── potentiel thermique
        ├── cible météo-adaptative
        └── diagnostics MES / COH / PRO
        │
        ▼
Planification active V3
        │
        ├── filtration requise V3
        └── heure d'atteinte V3
        │
        ▼
Demande consolidée / machine à états
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

# 4. Température bassin

```text
Sonde immergée — ESP32 Jardin
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
        ▼
sensor.pcha_temperature_piscine
```

Les fonctions métier consomment uniquement les abstractions PCHA.

# 5. Référence et objectif quotidien

```text
Température calibrée cohérente
        │
        ├── échantillonnage régulier
        ├── moyenne de la veille acceptée après au moins 18 h de mesures valides
        ├── sinon conservation de la dernière référence fiable
        ▼
sensor.pcha_temperature_reference_objectif_quotidien
        │
        ├── figement au changement de jour
        └── loi de durée paramétrable
        ▼
sensor.pcha_objectif_filtration_quotidien
```

La loi V3 utilise :

```text
input_number.pcha_coefficient_filtration_base
input_number.pcha_temperature_seuil_acceleration_filtration
input_number.pcha_coefficient_filtration_acceleration
```

Le calcul de durée ne dépend pas directement de la météo.

# 6. Abstraction météo

La source météo physique ou l'intégration fournisseur est isolée dans `templates/meteo.yaml`.

Les autres fonctions consomment uniquement :

```text
sensor.pcha_meteo_aujourd_hui
sensor.pcha_meteo_demain
sensor.pcha_previsions_meteo_horaires
```

Cette règle évite de coupler la stratégie au fournisseur météo utilisé par Home Assistant.

# 7. Potentiel thermique

`templates/potentiel_thermique.yaml` évalue la fenêtre utile entre le moment courant, 10 h et le coucher du soleil.

Les sorties principales sont :

```text
sensor.pcha_score_potentiel_thermique_jour
sensor.pcha_potentiel_thermique_jour
```

Le niveau qualitatif est dérivé du score : `FAIBLE`, `MOYEN`, `BON` ou `EXCELLENT`.

# 8. Planification météo-adaptative V3

`templates/strategie.yaml` calcule :

```text
sensor.pcha_heure_cible_objectif
```

La cible standard est le coucher du soleil moins `input_number.pcha_marge_objectif_avant_coucher`.

La stratégie peut avancer ou retarder cette cible en fonction :

* de l'écart entre température du bassin et consigne ;
* du potentiel thermique du jour ;
* de la tendance J+1 lorsque le bassin est proche de la consigne.

Le décalage est borné à −120 / +90 minutes et la cible ne dépasse pas les 15 dernières minutes avant le coucher du soleil.

`templates/planification_v3.yaml` transforme cette cible en décision active :

```text
binary_sensor.pcha_filtration_requise_v3
sensor.pcha_heure_atteinte_objectif_v3
```

La demande consolidée du mode `AUTO` consomme `binary_sensor.pcha_filtration_requise_v3` en plus des demandes indépendantes de chauffage solaire et de protection du serpentin.

# 9. Compatibilité

Les interfaces historiques :

```text
binary_sensor.pcha_filtration_requise
sensor.pcha_heure_atteinte_objectif
```

restent présentes pour les dashboards et consommateurs existants. Elles reflètent la V3 avec repli sur la logique historique si les entités V3 sont indisponibles.

# 10. Luminosité distante et chauffage solaire

```text
BH1750
  │ I²C court
  ▼
D1 mini ESP8266
  │ Packet Transport UDP
  ▼
ESP32 Jardin
  │
  ▼
Abstractions PCHA
```

En fonctionnement normal, le chauffage solaire est piloté par la luminosité et la consigne. En cas d'indisponibilité de la luminosité, le secours thermique extérieur / bassin reste disponible selon les règles historiques.

La protection du serpentin reste indépendante de la stratégie météo V3.

# 11. Diagnostics et sécurité

Les diagnostics restent séparés en familles :

* `MES` — disponibilité des mesures ;
* `COH` — cohérence ;
* `PRO` — surveillance du procédé.

Le niveau de fonctionnement (`NORMAL`, `DÉGRADÉ`, `CRITIQUE`) reste une information d'état du système. Les conditions critiques peuvent interdire la transition vers `FILTRATION` selon les règles du moteur.

Les seuils de sécurité ne sont pas transformés en paramètres utilisateur courants par V3.0.

# 12. Dashboard

Le dashboard principal est `dashboard/piscine.yaml`.

La vue Paramètres V3 est externalisée dans :

```text
dashboard/views/parametres.yaml
```

Elle expose les réglages métier et présente les informations avancées de sécurité en lecture seule.

# 13. Persistance

Les états quotidiens nécessitant une restauration utilisent des capteurs template déclenchés lorsqu'une persistance est nécessaire, notamment :

* objectif quotidien et référence ;
* temps de filtration réalisé ;
* minimum et maximum de température ;
* compteurs solaires.

# 14. Versions

* V3.0 est la version courante du dépôt ;
* `docs/V3.0/` décrit les fonctions ajoutées par la planification météo-adaptative ;
* `docs/V1.1/` reste la référence historique détaillée des fondations du moteur ;
* les versions publiées antérieures, notamment `v2.0`, restent disponibles dans l'historique Git et les tags.
