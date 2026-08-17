# Changelog

## Maintenance après V2.0

* affichage explicite de `Pool Controller Home Assistant V2.0` dans le titre de la page d'accueil et alignement des documents actifs sur la version V2.0 ;
* ajout de la sélection J à J-7 dans l'onglet Historique, avec synchronisation de toute la page sur la journée choisie ;
* regroupement des synthèses journalières dans les en-têtes des graphes Historique : moyenne et amplitude de température, moyenne lumineuse et ensoleillement, filtration et cycles, consommation électrique ;
* correction des synthèses J-1 à J-7 : statistiques Recorder agrégées par journée, détails de température et luminosité sur 5 minutes, rafraîchissement au changement de date et unités d'affichage cohérentes ;
* suppression de la rangée d'indicateurs journaliers redondante de l'onglet Historique ;
* simplification du bandeau Historique et ajout de l'objectif de filtration ainsi que de sa température de référence dans le graphe de progression ;
* remplacement de la chronologie d'activité par quatre couloirs indépendants dont les états sont lisibles directement sur les axes, y compris lors de transitions rapprochées ;
* ajout du mode VIDANGE temporisé de 1 à 10 minutes, sans comptabilisation comme filtration et avec retour obligatoire sur OFF ;
* réarmement automatique de MES-002 après 60 secondes de retour stable du débitmètre ;
* mémorisation de PRO-001 jusqu'à un réarmement manuel effectué pompe arrêtée et en mode OFF ;
* séparation entre l'effacement des notifications et le réarmement fonctionnel ;
* ajout d'un onglet Maintenance avec simulation temporaire des quatre mesures principales ;
* suppression des anciens dashboards remplacés par le Concept D V2.0 ;
* suppression d'une image dupliquée et d'un helper vide ;
* retrait de la documentation V1.0 de la branche principale, toujours disponible dans l'historique Git ;
* mise à jour de l'exemple de configuration vers le dashboard actif.

## V2.0 — 2026-08-05

### Dashboard Concept D

* maintien du numéro V2.0 pour les corrections mineures du dashboard ;
* affichage conditionnel du temps de traitement restant, avec format heures/minutes et indication de pause ;
* remplacement des boutons répétitifs de durée par un curseur de 5 à 1 440 minutes ;
* saisie exacte toujours accessible en ouvrant la carte de durée ;
* fiabilisation du temps restant par arrondi à la minute supérieure.
* correction des libellés tronqués dans l’en-tête du graphique des températures ;
* centrage du pourcentage de progression et suppression de l’icône centrale de l’objectif quotidien de filtration ;
* affichage de la luminosité moyenne diurne dans l’en-tête, incluant les passages nuageux sans courbe supplémentaire ;
* affichage de la consommation électrique quotidienne dans l’en-tête de la puissance, sans courbe supplémentaire.
* affichage du nombre de cycles de filtration avec une décimale et signalement explicite d'une source de volume indisponible ;
* restructuration des en-têtes ApexCharts pour contenir valeurs, unités et libellés dans leurs colonnes sans débordement ;
* suppression de la dernière icône décorative de l’objectif et alignement du titre à gauche.
* filtrage des microcoupures de puissance : MES-003 s'active après 60 secondes d'indisponibilité et se réarme après 10 secondes stables.
* correction du compteur de cycles : chargement explicite de l'intégrateur de débit et suppression du faux `0` lorsque sa source n'est pas disponible.
* ajout de l'onglet Pilotage Concept D : chaîne de décision, commandes de mode et traitement, mesures de fonctionnement, temporisations et historique responsive.
* rééquilibrage de l'accueil : graphes élargis, objectif quotidien compact et durée d'ensoleillement ajoutée entre la valeur actuelle et la moyenne de luminosité.
* ajout de l'onglet Solaire Concept D : décision de chauffe, courbes température/luminosité, bilan du jour, réglages et historique responsive.
* ajout de l'onglet Diagnostics Concept D : synthèse globale, comptage des défauts actifs, familles MES/COH/PRO, gravités, cause MES-004, temporisations et historique 24 heures.
* harmonisation de la hauteur des cartes de synthèse Diagnostics et reformulation des libellés MES au repos pour éviter toute fausse impression de défaut.
* ajout de l'onglet Historique Concept D : indicateurs quotidiens, courbes séparées des températures, de la luminosité, du débit, de la puissance et de l'objectif, puis chronologies du fonctionnement et des diagnostics sur 24 heures.

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
* suppression de la légende redondante sous le graphique des températures et affichage centré du delta bassin − extérieur par une entité dédiée, sans inversion de la logique solaire ;
* ajout des minimums et maximums glissants sur 24 h ;
* ajout de `sensor.pcha_progression_objectif_quotidien` et d’une jauge de progression ;
* modernisation de l’anneau de progression avec dégradé cyan, bleu, violet et fuchsia ;
* réorganisation des vues Accueil, Pilotage, Solaire et Diagnostics.
