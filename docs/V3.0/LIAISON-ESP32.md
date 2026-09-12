# MES-005 — Liaison ESP32 Jardin indisponible

MES-005 surveille la connexion native API entre Home Assistant et l'ESP32 Jardin.
Il ne déduit pas une déconnexion du RSSI, d'un débit nul, d'une mesure constante
ou d'une panne de la D1 mini distante.

## Comportement

- Source physique : `binary_sensor.jardin_esp32_jardin_statut_connexion`.
- Abstraction : `binary_sensor.pcha_liaison_esp32` ; seul l'état `on` confirme la liaison.
- Diagnostic : `binary_sensor.pcha_diagnostic_mes_005_liaison_esp32_indisponible`.
- `off`, `unknown`, `unavailable` ou entité absente : perte de liaison.
- Activation CRITIQUE après 60 secondes continues de perte détectée par HA.
  Le délai de détection ESPHome/HA s'ajoute à cette temporisation.
- Retour automatique après 60 secondes continues de liaison disponible.
  Une nouvelle coupure pendant ce délai maintient le défaut.
- Pendant la fenêtre de stabilisation au démarrage HA, aucune nouvelle activation.
  Les temporisations template ne sont pas persistées à travers un redémarrage HA.
- Défaut surveillé aussi en OFF. Le niveau CRITIQUE interdit FILTRATION et
  reste bloquant en VIDANGE, comme les critiques non hydrauliques.
- La reprise dépend toujours des demandes, autres défauts et temporisations PCHA.
  MES-005 ne réarme jamais le verrou manuel PRO-001.
- Si la protection solaire est requise, la liaison perdue validée contribue
  également à PRO-003 (circulation de protection impossible).
- Les MES de capteurs restent indépendants ; plusieurs notifications sont possibles.

Ce diagnostic localise une perte de communication. Il ne distingue pas à lui
seul Wi-Fi, alimentation, plantage ou redémarrage. Utiliser la durée de
fonctionnement et la cause du dernier redémarrage déjà ajoutées à l'ESP32.

## Installation, dans cet ordre

1. Passer PCHA en OFF et attendre l'arrêt de la pompe.
2. Dans ESPHome Builder, ajouter l'entrée de
   `esphome/esp32-jardin-statut.yaml` à la section `binary_sensor:` existante.
   C'est un fragment : ne pas remplacer le YAML complet, ni créer deux sections.
3. Valider, installer sans fil et attendre la reconnexion de l'ESP32.
4. Dans Home Assistant, vérifier le nouvel état « Statut connexion ».
   Son identifiant généré dépend du registre existant : le renommer exactement
   `binary_sensor.jardin_esp32_jardin_statut_connexion` ou adapter uniquement
   l'identifiant physique dans `templates/capteurs.yaml`.
   L'entité doit être activée et à `on` avant le déploiement PCHA.
5. Après fusion de la PR, mettre à jour le dépôt Home Assistant avec
   `git pull --ff-only origin main` depuis le dossier du dépôt.
6. Vérifier la configuration Home Assistant puis redémarrer HA.
7. Recharger le dashboard ; s'il est copié dans l'éditeur de configuration brute,
   le remplacer par le contenu actualisé de `dashboard/piscine.yaml`.
8. Vérifier MES-005 NORMAL puis reprendre AUTO si les autres diagnostics
   sont normaux. Vérifier la circulation lors du démarrage.

Une source absente ou mal nommée provoque volontairement MES-005 après les délais.
Cette modification n'est pas une correction prouvée de l'incident PRO-001 du 11/09.

## Vérification sur installation

Pompe en OFF, interrompre la liaison de façon contrôlée : vérifier l'activation
après 60 s de perte détectée, la notification et l'historique. Rétablir la liaison :
vérifier 60 s de stabilité avant résolution. Ne pas effectuer cet essai pendant
une filtration ou un arrosage. Vérifier ensuite le retour normal des capteurs.

## Vérifications locales

Exécuter `python -m unittest discover -s tests` (PyYAML et Jinja2 nécessaires).
Ces tests vérifient les expressions réellement chargées depuis le YAML, les délais
configurés et les intégrations. La compilation du firmware complet et le
comportement sur Home Assistant doivent être validés sur l'installation.

Source : [ESPHome Status Binary Sensor](https://esphome.io/components/binary_sensor/status/).
