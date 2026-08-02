# SPEC-003 — Gestion de la filtration

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit l'objectif quotidien de filtration et la demande automatique nécessaire pour l'atteindre.

Elle ne définit ni les modes, ni les transitions de la machine, ni le chauffage solaire, ni les diagnostics.

# 2. Interface

**Entrées**

* température d'eau fournie par la SPEC-004 ;
* temps de filtration réalisé dans la journée ;
* heure du prochain coucher du soleil fournie par Home Assistant.

**Sortie**

```text
binary_sensor.pcha_filtration_requise
```

# 3. Objectif quotidien

L'objectif quotidien minimal dépend de la température de l'eau :

| Température de l'eau | Objectif quotidien |
|---|---:|
| < 20 °C | 4 h |
| 20 °C à < 24 °C | 6 h |
| 24 °C à < 27 °C | 8 h |
| ≥ 27 °C | 10 h + 2 h par degré au-dessus de 27 °C |

Toute période pendant laquelle la machine est en `FILTRATION` compte dans le temps réalisé.

# 4. Demande automatique

`binary_sensor.pcha_filtration_requise` est actif lorsque l'algorithme journalier demande une circulation pour atteindre l'objectif quotidien.

La répartition vise l'achèvement de l'objectif une heure avant le coucher du soleil.

L'heure de départ au plus tard est calculée ainsi :

```text
coucher du soleil - 1 heure - temps de filtration restant
```

Avant cette heure, la demande de filtration reste inactive. Une circulation produite par une autre demande compte néanmoins dans le temps réalisé et repousse automatiquement l'heure de départ calculée.

À partir de cette heure, la demande reste active jusqu'à l'atteinte de l'objectif. Si l'échéance est déjà dépassée ou si l'heure du coucher du soleil est indisponible, la demande devient immédiatement active afin de privilégier l'atteinte de l'objectif.

Cette stratégie limite les démarrages inutiles et favorise les périodes utiles au chauffage solaire.

Lorsque l'objectif quotidien est atteint, cette demande devient inactive.

L'atteinte de l'objectif n'interdit pas une demande distincte du chauffage solaire, définie uniquement dans la SPEC-008.

# 5. Niveau dégradé

Un niveau `DEGRADE` n'interdit pas à lui seul la filtration. Les restrictions éventuelles proviennent uniquement des diagnostics concernés dans la SPEC-007.

# 6. Responsabilités

SPEC-003 est l'unique producteur de `binary_sensor.pcha_filtration_requise`.

Elle ne commande pas la pompe, ne change pas l'état de la machine et ne consolide pas les demandes des autres fonctions.

# 7. Critères d'acceptation

* L'objectif quotidien respecte le tableau de calcul.
* Le temps réalisé est comptabilisé une seule fois.
* La demande automatique s'arrête lorsque l'objectif est atteint.
* Une demande solaire indépendante reste possible conformément à la SPEC-008.
* La pompe n'est jamais commandée directement par cette fonction.

# 8. Références

* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation et notifications
