# SPEC-003 — Gestion de la filtration

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit l'objectif quotidien de filtration et la demande automatique nécessaire pour l'atteindre.

# 2. Entrées et sorties

**Entrées**

* température calibrée cohérente du bassin ;
* temps de filtration réalisé ;
* coucher du soleil fourni par Home Assistant.

**Sorties**

```text
sensor.pcha_objectif_filtration_quotidien
sensor.pcha_heure_atteinte_objectif
sensor.pcha_temperature_reference_objectif_quotidien
binary_sensor.pcha_objectif_filtration_fige
binary_sensor.pcha_filtration_requise
```

# 3. Construction de la référence quotidienne

Une mesure unique prise à minuit n'est pas représentative de la température du bassin. La référence quotidienne est donc construite à partir de la moyenne de toutes les températures calibrées cohérentes échantillonnées chaque minute pendant la journée terminée.

```text
Pendant la journée J−1
→ échantillonnage chaque minute de la température calibrée cohérente
→ cumul de la somme et du nombre d'échantillons
→ à minuit, calcul de la moyenne de J−1
→ la moyenne devient la référence figée de J
→ remise à zéro des accumulateurs pour la journée J
```

La référence est calculée ainsi au changement de jour :

```text
température de référence du jour J
= somme des températures calibrées valides de J−1
  / nombre d'échantillons valides de J−1
```

Le capteur restaure ses accumulateurs après un redémarrage. Si aucune moyenne valide de la veille n'est disponible, la dernière référence connue est conservée en secours afin de ne pas supprimer l'objectif quotidien.

## 3.1 Exemples

| Moyenne calibrée de la veille | Calcul | Objectif |
|---:|---|---:|
| 20 °C | 20 / 5 | 4 h |
| 25 °C | 25 / 5 | 5 h |
| 27 °C | 27 / 5 + 2 | 7 h 24 |
| 30 °C | 30 / 5 + 5 | 11 h |

# 4. Tableau de calcul

| Température de référence | Objectif quotidien |
|---|---:|
| ≤ 25 °C | température / 5 |
| > 25 °C | température / 5 + 1 h par degré au-dessus de 25 °C |

Toute minute pendant laquelle la machine est en `FILTRATION` compte dans le temps réalisé.

# 5. Minimum et maximum quotidiens

La sonde étant directement dans le bassin, les minimums et maximums sont actualisés toute la journée dès que `measurement_valid` est vrai, sans condition sur la pompe.

# 6. Planification

L'objectif doit être terminé deux heures avant le coucher du soleil :

```text
heure de départ au plus tard
= coucher du soleil − 2 heures − temps restant
```

Avant cette heure, une filtration provenant d'une autre demande compte dans le temps réalisé. À partir de cette heure, la demande reste active jusqu'à l'atteinte de l'objectif.

# 7. Critères d'acceptation

* La température calibrée cohérente est échantillonnée chaque minute.
* À minuit, la moyenne de la journée terminée devient la nouvelle référence.
* La référence et l'objectif restent figés pendant toute la nouvelle journée.
* En l'absence de moyenne valide de la veille, la dernière référence connue est conservée en secours.
* Les statistiques journalières ne dépendent pas du fonctionnement de la pompe.
* La planification vise une fin deux heures avant le coucher du soleil.
