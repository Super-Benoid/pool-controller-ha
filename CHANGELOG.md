# Changelog

## V1.1 — 2026-08-04

### Température

* nouvelle source `sensor.jardin_esp32_jardin_temperature_bassin` ;
* suppression de la validation par circulation ;
* calibrage signé `−3 à +3 °C` ;
* minimum et maximum mis à jour pompe arrêtée ou en marche.

### Objectif quotidien

* candidate maximale de minuit à trente minutes après le lever du soleil ;
* référence calibrée et objectif figé jusqu'au lendemain ;
* affichage de la référence et de son statut dans le dashboard.
* centralisation de l'heure prévisionnelle dans `sensor.pcha_heure_atteinte_objectif` ;

### Luminosité et solaire

* chaîne D1 mini / Packet Transport / ESP32 supervisée ;
* MES-004 enrichi avec une cause ;
* secours thermique extérieur/bassin avec hystérésis `2 °C / 1 °C` ;
* compteurs solaires suspendus pendant MES-004 ;
* graphe de luminosité ajouté à Supervision.
### Dashboard

* refonte du dashboard avec une organisation plus moderne ;
* nouvelle page d'accueil de synthèse ;
* regroupement des cartes par usage : Pilotage, Solaire, Diagnostics ;
* conservation des cartes natives `tile` avec `trend-graph` sur 24 heures pour les mesures principales.


## V1.1 — Concept D

* ajout du thème sombre cyan/violet `PCHA Concept D` ;
* remplacement des simples tuiles de tendance par quatre cartes capteur détaillées avec axes et historique 24 h ;
* ajout d’un pictogramme coloré avant le titre de chaque graphique (température, luminosité, débit et puissance), avec trois vagues fléchées pour le débit de filtration ;
* ajout des minimums et maximums glissants sur 24 h ;
* ajout de `sensor.pcha_progression_objectif_quotidien` et d’une jauge de progression ;
* modernisation de l’anneau de progression avec dégradé cyan, bleu, violet et fuchsia ;
* réorganisation des vues Accueil, Pilotage, Solaire et Diagnostics.
