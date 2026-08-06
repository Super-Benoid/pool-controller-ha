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
| `VIDANGE` | Pompe commandée pour évacuer l'eau hors du circuit de filtration |

Un diagnostic ou un défaut n'est jamais un état de la machine.

# 4. Transitions

| État courant | Condition | État suivant |
|---|---|---|
| `INITIALISATION` | Initialisation terminée | `ATTENTE` |
| `ATTENTE` | Demande active et niveau différent de `CRITIQUE` | `FILTRATION` |
| `FILTRATION` | Plus aucune demande ou niveau `CRITIQUE` | `ATTENTE` |
| `ATTENTE` | Mode `VIDANGE`, timer actif et absence de critique non hydraulique | `VIDANGE` |
| `VIDANGE` | Timer expiré, changement de mode ou critique non hydraulique | `ATTENTE` |

Les temps minimums de marche et d'arrêt sont des protections anti-cycles appliquées uniquement lorsqu'un changement de `binary_sensor.pcha_demande_fonctionnement` provoque une transition en mode `AUTO`. Ils évitent les changements d'état rapprochés, notamment lors des passages nuageux.

Ils ne s'appliquent pas aux changements de mode, à l'initialisation, aux rechargements, ni aux modes `OFF`, `SECURISATION`, `TRAITEMENT`, `MARCHE_FORCEE` et `VIDANGE`. Une entrée en `TRAITEMENT`, `MARCHE_FORCEE` ou `VIDANGE` peut donc démarrer immédiatement. Une sélection de `OFF` arrête immédiatement.

Le niveau CRITIQUE est prioritaire sur toutes les temporisations. Il provoque
un arrêt immédiat, même si le temps minimum de marche n'est pas terminé. En
`VIDANGE`, les seuls critiques hydrauliques `MES-002` et `PRO-001` sont ignorés,
car le débitmètre est volontairement hors du circuit. Toute autre criticité,
notamment `PRO-003`, reste bloquante.

Le mode `VIDANGE` ne peut être engagé qu'après un passage explicite par `OFF`,
pompe effectivement arrêtée. Il est limité par `timer.pcha_vidange` et retourne
obligatoirement sur `OFF` à l'expiration ou après un redémarrage de Home Assistant.

# 5. Commande de la pompe

La machine applique ses états par les scripts de pompe. Elle n'accède jamais à l'actionneur physique.

```text
ATTENTE    → demande d'arrêt
FILTRATION → demande de marche
VIDANGE    → demande de marche sans créditer l'objectif de filtration
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
* Seuls les quatre états définis existent.
* `CRITIQUE` interdit l'entrée et le maintien en `FILTRATION`.
* `VIDANGE` est limité à dix minutes, n'est jamais repris après redémarrage et
  n'alimente pas le compteur quotidien de filtration.
* Les changements de mode ou de demande provoquent une réévaluation.
* La pompe est commandée uniquement par les scripts prévus.

# 8. Références

* SPEC-004 — Couche d'abstraction et configuration
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
