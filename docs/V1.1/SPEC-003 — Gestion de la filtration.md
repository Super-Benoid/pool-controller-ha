# SPEC-003 — Gestion de la filtration

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit l'objectif quotidien de filtration et la demande automatique nécessaire pour l'atteindre.

# 2. Entrées et sorties

**Entrées**

* température brute cohérente du bassin ;
* calibrage signé de la température ;
* temps de filtration réalisé ;
* lever et coucher du soleil fournis par Home Assistant.

**Sorties**

```text
sensor.pcha_objectif_filtration_quotidien
sensor.pcha_heure_atteinte_objectif
sensor.pcha_temperature_reference_objectif_quotidien
binary_sensor.pcha_objectif_filtration_fige
binary_sensor.pcha_filtration_requise
```

# 3. Construction de la référence quotidienne

Une mesure unique prise à minuit n'est pas suffisante, notamment près des seuils de 20, 24 et 27 °C. La V1.1 applique la séquence suivante :

```text
À minuit
→ démarrage d'une nouvelle candidate
→ mémorisation de la température brute maximale valide
→ observation jusqu'à 30 minutes après le lever du soleil
→ ajout du calibrage signé
→ calcul et figement de l'objectif jusqu'au lendemain
```

Avant le figement, l'objectif est **provisoire** et suit uniquement la candidate maximale de la fenêtre. Après le figement, une hausse de température dans l'après-midi ne modifie plus l'objectif.

La référence est calculée ainsi :

```text
température de référence = maximum brut observé + calibrage
```

En cas de redémarrage après la fin de la fenêtre, le système reconstitue la décision avec les données restaurées. Si aucune mesure valide n'est disponible, le dernier objectif connu est conservé temporairement ; le figement du jour est effectué dès qu'une mesure cohérente devient disponible.

## 3.1 Exemples

| Mesures brutes de la fenêtre | Calibrage | Référence | Objectif |
|---|---:|---:|---:|
| 23,1 ; 23,4 ; 23,2 °C | +0,1 °C | 23,5 °C | 6 h |
| 24,7 ; 24,4 ; 23,8 °C | −0,2 °C | 24,5 °C | 8 h |
| 27,1 ; 27,4 ; 27,2 °C | 0,0 °C | 27,4 °C | 10 h 48 |

# 4. Tableau de calcul

| Température de référence | Objectif quotidien |
|---|---:|
| < 20 °C | 4 h |
| 20 °C à < 24 °C | 6 h |
| 24 °C à < 27 °C | 8 h |
| ≥ 27 °C | 10 h + 2 h par degré au-dessus de 27 °C |

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

* L'objectif est provisoire pendant la fenêtre nocturne puis figé.
* La référence utilise le maximum brut valide et le calibrage en vigueur au figement.
* L'objectif ne varie plus après le figement.
* Les statistiques journalières ne dépendent pas du fonctionnement de la pompe.
* La planification vise une fin deux heures avant le coucher du soleil.
