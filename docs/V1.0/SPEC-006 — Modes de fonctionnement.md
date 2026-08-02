# SPEC-006 — Modes de fonctionnement

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit les modes sélectionnables et la demande de fonctionnement produite par chacun d'eux.

Un seul mode est actif à un instant donné.

# 2. Interface

**Entrées**

```text
input_select.pcha_mode_de_fonctionnement
binary_sensor.pcha_filtration_requise
binary_sensor.pcha_chauffage_solaire_requis
binary_sensor.pcha_protection_serpentin_requise
```

**Sortie**

```text
binary_sensor.pcha_demande_fonctionnement
```

# 3. Modes

| Mode | Demande de fonctionnement |
|---|---|
| `OFF` | Toujours inactive |
| `SECURISATION` | Active uniquement lorsque la protection du serpentin demande une circulation |
| `AUTO` | Active si la filtration automatique, le chauffage solaire ou la protection du serpentin demande une circulation |
| `TRAITEMENT` | Active pendant la durée du traitement |
| `MARCHE_FORCEE` | Active tant que le mode reste sélectionné |

# 4. Mode OFF

Aucun démarrage automatique n'est autorisé. La consultation des informations, le réglage des paramètres et le changement de mode restent possibles.

# 5. Mode SECURISATION

La filtration normale et la demande de chauffage de confort sont ignorées. Seule `binary_sensor.pcha_protection_serpentin_requise`, définie par SPEC-008, peut produire une demande de fonctionnement.

# 6. Mode AUTO

La demande consolidée est active lorsque :

```text
binary_sensor.pcha_filtration_requise
OU
binary_sensor.pcha_chauffage_solaire_requis
OU
binary_sensor.pcha_protection_serpentin_requise
```

Les règles internes de ces demandes restent définies uniquement dans les SPEC-003 et SPEC-008.

# 7. Mode TRAITEMENT

L'entrée dans ce mode initialise `timer.pcha_traitement` avec la durée configurée en minutes. La durée est réglable de 5 à 1 440 minutes par pas de 5 minutes.

Le démarrage demandé par ce mode n'est pas soumis aux temporisations anti-cycles du mode `AUTO`.

Le temps de traitement correspond exclusivement au temps réel pendant lequel la machine est en `FILTRATION`. Le timer est mis en pause pendant `ATTENTE` et reprend lorsque la machine revient en `FILTRATION`.

Une modification de `input_number.pcha_duree_traitement` pendant le traitement conserve le temps déjà réalisé. Le nouveau temps restant est égal à la nouvelle durée configurée moins le temps de traitement déjà écoulé. Si la nouvelle durée est déjà atteinte, le traitement se termine.

À l'expiration du timer, le mode revient à `AUTO`. Quitter le mode avant l'expiration annule le traitement en cours.

# 8. Mode MARCHE_FORCEE

La demande reste active jusqu'à la sélection d'un autre mode.

# 9. Diagnostics

Les diagnostics ne modifient jamais le mode. Le niveau de fonctionnement est appliqué par la machine à états conformément à la SPEC-005.

# 10. Critères d'acceptation

* Un seul mode est actif.
* La demande consolidée suit exclusivement le tableau de cette SPEC.
* En `AUTO`, une demande solaire peut rester active après l'atteinte de l'objectif quotidien de filtration.
* La protection du serpentin est prise en compte en modes `AUTO` et `SECURISATION`.
* La fin du traitement provoque le retour à `AUTO`.
* Un diagnostic ne change pas le mode sélectionné.

# 11. Références

* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
