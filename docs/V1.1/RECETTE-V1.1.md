# Recette de mise en service — PCHA V1.1

**Version :** 1.1  
**Statut :** À exécuter sur l'installation réelle

---

# 1. Sécurité

* Commencer en mode `OFF`.
* Ne jamais obstruer le circuit pour provoquer un défaut.
* Conserver un accès immédiat à l'alimentation de la pompe.

# 2. Chargement

| Test | Résultat attendu |
|---|---|
| Vérification de configuration | Aucune erreur |
| Redémarrage Home Assistant | Démarrage normal |
| Dashboard Piscine | Accessible |
| Entités essentielles | Ni `unknown` ni `unavailable` après validation |

# 3. Température bassin

1. Vérifier que `sensor.jardin_esp32_jardin_temperature_bassin` est numérique.
2. Vérifier que `sensor.pcha_temperature_piscine_brute` suit cette source, pompe arrêtée.
3. Régler temporairement le calibrage à `0,0 °C`.
4. Vérifier que `sensor.pcha_temperature_piscine` suit immédiatement la mesure brute.
5. Régler `+0,5 °C` et vérifier que la température PCHA augmente de `0,5 °C`.
6. Régler `−0,5 °C` et vérifier qu'elle diminue de `0,5 °C`.
7. Régler le calibrage réel dans la plage `−3,0 à +3,0 °C`.
8. Vérifier que les minimum et maximum du jour évoluent même pompe arrêtée.

Une valeur brute ou calibrée hors de l'intervalle strict `10–50 °C` doit activer `COH-002` après temporisation sans écraser la dernière valeur cohérente.

# 4. Référence et objectif quotidien

1. Vérifier l'affichage de `sensor.pcha_temperature_reference_objectif_quotidien`.
2. Vérifier que l'attribut `temperature_moyenne_jour_en_cours` évolue à partir des échantillons calibrés cohérents.
3. Simuler le changement de jour et vérifier que la moyenne de la journée terminée devient `temperature_reference`.
4. Vérifier que les accumulateurs journaliers repartent pour la nouvelle journée.
5. Vérifier qu'une variation de température après minuit ne modifie plus la référence ni l'objectif du jour.
6. Vérifier la formule : `T / 5` jusqu'à 25 °C, puis `T / 5 + (T − 25)` au-dessus de 25 °C.
7. Vérifier que `sensor.pcha_heure_atteinte_objectif` applique la planification et que la carte affiche la référence, le statut et `Atteint à`.

# 5. Planification

Vérifier :

```text
heure cible = coucher du soleil − 2 heures
heure de départ = heure cible − temps restant
```

Une filtration provenant d'une autre demande doit réduire le temps restant.

# 6. Chaîne de luminosité distante

En fonctionnement normal :

```text
binary_sensor.pcha_liaison_luminosite_distante = on
binary_sensor.pcha_capteur_luminosite_distant_ok = on
binary_sensor.pcha_diagnostic_mes_004_luminosite_indisponible = off
```

Vérifier que `sensor.pcha_luminosite` reçoit une valeur toutes les dix secondes environ et que le graphe de la vue **Supervision** se remplit.

# 7. MES-004 et secours thermique

1. Placer le système en situation sûre et conserver la pompe accessible.
2. Interrompre la D1 mini ou la transmission Packet Transport.
3. Vérifier que MES-004 devient actif après le délai configuré.
4. Vérifier que `sensor.pcha_source_chauffage_solaire` devient `TEMPERATURE_EXTERIEURE_SECOURS` si les deux températures sont valides.
5. Avec un écart inférieur à `2,0 °C`, vérifier que le chauffage de confort reste arrêté.
6. Avec un écart supérieur ou égal à `2,0 °C`, vérifier que la demande devient active si le bassin est sous la consigne.
7. Une fois active, réduire l'écart entre `1,0 et 2,0 °C` : la demande doit rester active.
8. À un écart inférieur ou égal à `1,0 °C`, la demande doit s'arrêter.
9. Vérifier que les compteurs de luminosité sont suspendus pendant MES-004.
10. Injecter, si possible en banc de test, une valeur hors plage et vérifier la cause `MESURE_HORS_LIMITES`.
11. Rétablir la D1 mini et vérifier le retour à la source `LUMINOSITE` après temporisation.

# 8. Protection du serpentin

* En mode normal, la protection utilise la luminosité.
* Pendant MES-004, elle utilise la position du soleil.
* La demande apparaît après 25 minutes sans filtration et reste maintenue 5 minutes après démarrage.
* Le mode `OFF` ne démarre pas la pompe.

# 9. Débit, puissance et modes

Reprendre les essais V1.0 :

* débit normal proche de `3 800 L/h` ;
* débit suffisant à partir de `3 000 L/h` ;
* puissance normale de `300 à 350 W` ;
* tests `OFF`, `AUTO`, `SECURISATION`, `TRAITEMENT`, `MARCHE_FORCEE` ;
* arrêt immédiat sur niveau `CRITIQUE`.

# 10. Validation finale

La V1.1 est validée lorsque :

* la température bassin est disponible sans circulation ;
* le calibrage signé est correct ;
* l'objectif quotidien est figé selon la fenêtre définie ;
* le graphe de luminosité est visible ;
* MES-004 distingue la liaison et le BH1750 ;
* le secours extérieur/bassin respecte les seuils `2,0 / 1,0 °C` ;
* aucune erreur PCHA n'apparaît dans les journaux.
