# SPEC-005 — Machine à états

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit les états internes du contrôleur et leurs transitions.

Elle ne définit ni l'origine des demandes, ni les modes, ni les diagnostics.

# 2. Interface

**Entrées**

```text
binary_sensor.pcha_demande_fonctionnement
input_select.pcha_niveau_fonctionnement
input_select.pcha_mode_de_fonctionnement
input_number.pcha_temps_marche_pompe_min
input_number.pcha_temps_arret_pompe_min
```

**Sortie**

```text
input_select.pcha_etat_machine
```

# 3. États

| État | Définition |
|---|---|
| `INITIALISATION` | État temporaire au démarrage du contrôleur |
| `ATTENTE` | Aucune circulation en cours |
| `FILTRATION` | Pompe de filtration commandée en marche |

Un diagnostic ou un défaut n'est jamais un état de la machine.

# 4. Transitions

| État courant | Condition | État suivant |
|---|---|---|
| `INITIALISATION` | Initialisation terminée | `ATTENTE` |
| `ATTENTE` | Demande active et niveau différent de `CRITIQUE` | `FILTRATION` |
| `FILTRATION` | Plus aucune demande ou niveau `CRITIQUE` | `ATTENTE` |

Les temps minimums de marche et d'arrêt sont des protections anti-cycles appliquées uniquement lorsqu'un changement de `binary_sensor.pcha_demande_fonctionnement` provoque une transition en mode `AUTO`. Ils évitent les changements d'état rapprochés, notamment lors des passages nuageux.

Ils ne s'appliquent pas aux changements de mode, à l'initialisation, aux rechargements, ni aux modes `OFF`, `SECURISATION`, `TRAITEMENT` et `MARCHE_FORCEE`. Une entrée en `TRAITEMENT` ou `MARCHE_FORCEE` peut donc démarrer immédiatement. Une sélection de `OFF` arrête immédiatement.

Le niveau CRITIQUE est prioritaire sur toutes les temporisations. Il
provoque un arrêt immédiat, même si le temps minimum de marche n'est pas
terminé.

# 5. Commande de la pompe

La machine applique ses états par les scripts de pompe. Elle n'accède jamais à l'actionneur physique.

```text
ATTENTE    → demande d'arrêt
FILTRATION → demande de marche
```

# 6. Responsabilités

La machine :

* ne calcule pas les demandes ;
* ne modifie pas le mode ;
* ne produit pas de diagnostic ;
* ne connaît pas l'origine de la demande consolidée.

Le script `pcha_machine_reevaluer` est l'unique point de décision des transitions.

# 7. Critères d'acceptation

* Un seul état est actif.
* Seuls les trois états définis existent.
* `CRITIQUE` interdit l'entrée et le maintien en `FILTRATION`.
* Les changements de mode ou de demande provoquent une réévaluation.
* La pompe est commandée uniquement par les scripts prévus.

# 8. Références

* SPEC-004 — Couche d'abstraction et configuration
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
