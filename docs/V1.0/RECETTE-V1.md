# Recette de mise en service — PCHA V1

**Version :** 1.0  
**Statut :** À exécuter sur l'installation réelle

---

# 1. Règles de sécurité

* Commencer avec le mode `OFF`.
* Ne jamais simuler un défaut hydraulique en obstruant volontairement le circuit.
* Garder l'accès à la prise de la pompe pendant les essais.
* Arrêter les essais si le débit ou le bruit de la pompe devient anormal.

# 2. Chargement

| Test | Résultat attendu |
|---|---|
| Vérification de configuration | Aucune erreur |
| Redémarrage Home Assistant | Démarrage normal |
| Tableau de bord Piscine | Accessible dans la barre latérale |
| Entités PCHA | Aucune entité essentielle `unknown` ou `unavailable` après stabilisation |

# 3. Abstraction matérielle

Vérifier que les valeurs PCHA suivent les équipements réels :

* `sensor.pcha_temperature_piscine_brute` ;
* `sensor.pcha_temperature_piscine` ;
* `sensor.pcha_temperature_exterieure` ;
* `sensor.pcha_luminosite` ;
* `sensor.pcha_debit_filtration` ;
* `sensor.pcha_puissance_pompe_filtration` ;
* `switch.pcha_commande_pompe_filtration`.

# 4. Mode OFF

1. Sélectionner `OFF`.
2. Vérifier que `binary_sensor.pcha_demande_fonctionnement` est `off`.
3. Vérifier que la machine revient à `ATTENTE`.
4. Vérifier que la pompe est arrêtée.

**Critère :** aucune demande automatique ne peut démarrer la pompe en mode `OFF`.

# 5. Marche forcée

1. Vérifier que le niveau n'est pas `CRITIQUE`.
2. Sélectionner `MARCHE_FORCEE`.
3. Vérifier le passage immédiat à `FILTRATION` et le démarrage de la pompe.
4. Revenir à `OFF` et vérifier l'arrêt selon les règles de la machine.

# 6. Débit et puissance

Pompe en fonctionnement stabilisé :

* débit attendu proche de `3 800 L/h` ;
* débit suffisant à partir de `3 000 L/h` ;
* puissance attendue entre `300 et 350 W`.

Vérifier que `PRO-001`, `PRO-002` et `COH-001` restent inactifs en fonctionnement normal.

# 7. Température

1. Pompe arrêtée, vérifier que `sensor.pcha_temperature_piscine` conserve la dernière valeur validée même si la sonde brute chauffe.
2. Mettre la pompe en circulation et attendre le délai de stabilisation.
3. Vérifier que la température validée devient la température brute moins la correction configurée.
4. Vérifier les attributs `source_coherent`, `corrected_value_coherent` et `measurement_valid`. Ils doivent être vrais lors d'une mesure stabilisée cohérente.
5. Vérifier que les minimum et maximum journaliers évoluent uniquement lors d'une nouvelle mesure validée après circulation.

Vérifier que la température de piscine reste dans l'intervalle strict :

```text
10 °C < température < 50 °C
```

Une valeur numérique hors plage doit laisser inchangés `sensor.pcha_temperature_piscine`, le minimum et le maximum du jour. `COH-002` doit devenir actif si cette valeur persiste pendant le délai de validation, puis se réarmer après le retour durable d'une mesure cohérente. Une ancienne statistique restaurée hors plage doit être remplacée à la prochaine mesure valide.

# 8. Planification de l'objectif quotidien

1. Relever l'heure du prochain coucher du soleil dans `sun.sun`.
2. Soustraire deux heures pour obtenir l'heure cible de fin de l'objectif quotidien.
3. Relever `sensor.pcha_temps_filtration_restant`.
4. Vérifier que `binary_sensor.pcha_filtration_requise` devient actif au plus tard à :

```text
coucher du soleil - 2 heures - temps de filtration restant
```

5. Vérifier qu'une filtration réalisée par une autre demande réduit le temps restant et repousse d'autant le dernier départ nécessaire.

**Critère :** en l'absence d'une autre contrainte, l'objectif quotidien est achevé deux heures avant le coucher du soleil.

# 9. Mode TRAITEMENT

1. Régler une courte durée d'essai adaptée au test.
2. Sélectionner `TRAITEMENT`.
3. Vérifier le démarrage du timer et de la demande de fonctionnement.
4. Quitter le mode avant la fin et vérifier l'annulation du timer.
5. Refaire le test jusqu'à expiration et vérifier le retour automatique à `AUTO`.
6. Remettre la durée nominale après le test.

# 10. Chauffage solaire

Lorsque la luminosité dépasse le seuil et que la température est sous la consigne :

* `binary_sensor.pcha_chauffage_solaire_requis` devient `on` ;
* en mode `AUTO`, cette demande peut démarrer la filtration même si l'objectif quotidien est atteint ;
* `binary_sensor.pcha_chauffage_solaire_actif` devient `on` lorsque la machine est en `FILTRATION`.

# 11. Protection du serpentin

En mode `SECURISATION` ou `AUTO`, avec une luminosité supérieure au seuil et sans circulation :

* la demande apparaît après 25 minutes ;
* la circulation est maintenue pendant au moins 5 minutes ;
* aucune protection automatique ne démarre la pompe en mode `OFF`.

# 12. Diagnostics et arrêt critique

Vérifier sans provoquer de défaut physique dangereux :

* la disparition contrôlée d'une source de mesure fait apparaître son diagnostic après le délai prévu ;
* un diagnostic `DEGRADE` ne coupe pas la filtration à lui seul ;
* un diagnostic `CRITIQUE` fait passer le niveau à `CRITIQUE` et arrête la pompe immédiatement ;
* la disparition de la condition réarme le diagnostic selon son mode prévu.

# 13. Notifications et journal

Vérifier :

* l'apparition d'une notification persistante pour un diagnostic `DEGRADE` ou `CRITIQUE` ;
* la réception sur `notify.mobile_app_oppo_ben` ;
* la notification de résolution ;
* l'acquittement des notifications persistantes ;
* les entrées PCHA dans le journal d'activité.

# 14. Validation finale

La V1 peut être considérée comme mise en service lorsque :

* tous les tests applicables sont conformes ;
* aucune erreur PCHA n'apparaît dans les journaux Home Assistant ;
* les valeurs normales de débit et de puissance sont confirmées ;
* l'arrêt `OFF` et l'arrêt `CRITIQUE` sont validés ;
* le tableau de bord et les notifications sont opérationnels.


# Contrôles des compteurs quotidiens

* Vérifier que `sensor.pcha_energie_pompe_quotidienne` augmente lorsque la pompe consomme et revient à zéro au changement de jour.
* Vérifier que `sensor.pcha_temps_luminosite_superieure_seuil_jour` augmente d’une minute par minute au-dessus du seuil.
* Vérifier que `sensor.pcha_luminosite_moyenne_superieure_seuil_jour` reflète uniquement les échantillons pris au-dessus du seuil.
* Vérifier l’affichage `03H56` des trois durées de filtration dans le tableau de bord.
* Vérifier l’affichage `Atteint à : HHhMM` et sa mise à jour : échéance planifiée en attente, puis heure actuelle + temps restant pendant la filtration.
