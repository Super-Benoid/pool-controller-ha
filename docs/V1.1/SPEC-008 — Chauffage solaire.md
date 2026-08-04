# SPEC-008 — Chauffage solaire

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit la demande de chauffage solaire et la protection du serpentin. Le circuit solaire est passif : toute circulation traverse le serpentin.

# 2. Fonctionnement normal par luminosité

Lorsque MES-004 est inactif :

```text
température bassin < consigne
ET luminosité > seuil de chauffage
→ chauffage solaire requis
```

La source affichée est `LUMINOSITE`.

# 3. Fonctionnement dégradé par température extérieure

Lorsque MES-004 est actif, le système utilise :

```text
sensor.pcha_temperature_exterieure
sensor.pcha_temperature_piscine
```

La demande s'active lorsque :

```text
température bassin < consigne
ET température extérieure − température bassin ≥ 2,0 °C
```

Une hystérésis évite les cycles rapides :

```text
activation : écart ≥ 2,0 °C
maintien   : écart > 1,0 °C
arrêt      : écart ≤ 1,0 °C
```

La source affichée est `TEMPERATURE_EXTERIEURE_SECOURS`.

Si la température extérieure ou la température bassin est indisponible, la source devient `INDISPONIBLE` et aucune demande de chauffage de confort n'est créée.

# 4. Entités de supervision

```text
sensor.pcha_source_chauffage_solaire
sensor.pcha_ecart_temperature_exterieure_bassin
binary_sensor.pcha_chauffage_solaire_requis
binary_sensor.pcha_chauffage_solaire_actif
```

# 5. Protection du serpentin

La protection reste distincte du chauffage de confort.

* En fonctionnement normal, elle utilise la luminosité au-dessus du seuil.
* Pendant MES-004, elle utilise `sun.sun` et reste autorisée lorsque le soleil est au-dessus de l'horizon.
* Elle devient requise après 25 minutes sans filtration et reste maintenue 5 minutes après le démarrage.
* Le mode `OFF` conserve son comportement d'arrêt absolu.

# 6. Bilan solaire

Les compteurs de durée au-dessus du seuil et de luminosité moyenne :

* sont échantillonnés une fois par minute ;
* sont remis à zéro au changement de jour ou de seuil ;
* sont suspendus pendant MES-004 ;
* n'interviennent dans aucune décision de commande.

# 7. Critères d'acceptation

* La luminosité pilote le mode normal.
* MES-004 provoque un basculement automatique sur l'écart extérieur/bassin.
* L'activation de secours se fait à `+2,0 °C` et l'arrêt à `+1,0 °C`.
* La protection du serpentin reste disponible pendant MES-004.
* L'objectif quotidien atteint n'annule pas une demande solaire valide.
