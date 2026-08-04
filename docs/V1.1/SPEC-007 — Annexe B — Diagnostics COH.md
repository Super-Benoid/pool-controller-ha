# SPEC-007 — Annexe B — Diagnostics COH

**Version :** 1.1  
**Statut :** Figée

---

# 1. COH-001 — Cohérence hydraulique et électrique

Les seuils restent :

* débit critique inférieur à `500 L/h` ;
* débit insuffisant de `500` à moins de `3 000 L/h` ;
* débit normal à partir de `3 000 L/h` ;
* puissance normale de `300 à 350 W` ;
* puissance d'arrêt inférieure à `1 W`.

# 2. COH-002 — Température bassin incohérente

La plage physique stricte s'applique à la mesure brute et à la valeur calibrée :

```text
10 °C < température < 50 °C
```

COH-002 devient actif si la source est numérique mais que :

* la mesure brute est hors plage ;
* ou la valeur obtenue après ajout du calibrage est hors plage.

La temporisation est `input_number.pcha_temps_validation_temperature_piscine`.

Le calibrage ne peut jamais rendre valide une mesure brute physiquement incohérente. Une valeur incohérente n'écrase ni la dernière température métier cohérente, ni les minimums et maximums quotidiens.
