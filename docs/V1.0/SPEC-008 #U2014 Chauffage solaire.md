# SPEC-008 — Chauffage solaire

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit la demande de chauffage solaire et la protection thermique du serpentin.

Le chauffage est passif : toute circulation d'eau traverse le serpentin intégré au circuit de filtration.

# 2. Interface

**Entrées**

```text
sensor.pcha_temperature_piscine
sensor.pcha_luminosite
input_number.pcha_temperature_de_consigne
input_number.pcha_seuil_luminosite_chauffage
input_select.pcha_etat_machine
```

**Sorties fonctionnelles**

```text
binary_sensor.pcha_chauffage_solaire_requis
binary_sensor.pcha_chauffage_solaire_actif
binary_sensor.pcha_protection_serpentin_requise
```

La demande de protection est consommée par le mode `SECURISATION` et par le fonctionnement normal.

# 3. Demande de chauffage solaire

`binary_sensor.pcha_chauffage_solaire_requis` est actif lorsque les deux conditions sont vraies :

```text
température piscine < température de consigne
ET
luminosité > seuil de chauffage
```

Il devient inactif dès qu'une de ces conditions n'est plus satisfaite.

Cette demande est indépendante de l'objectif quotidien de filtration. Elle peut donc rester active lorsque cet objectif est atteint.

Le mode qui utilise cette demande est défini dans la SPEC-006.

# 4. Chauffage solaire actif

`binary_sensor.pcha_chauffage_solaire_actif` est actif lorsque la demande solaire est active et que la machine est en `FILTRATION`.

Cette information décrit un fonctionnement réel ; elle ne commande pas la pompe.

# 5. Protection du serpentin

`binary_sensor.pcha_protection_serpentin_requise` devient actif lorsque la luminosité dépasse le seuil et qu'aucune circulation n'a eu lieu pendant 25 minutes.

Lorsque la circulation commence, la demande reste active pendant 5 minutes.

La durée de 5 minutes correspond à la durée minimale de la demande de
protection.

Une autre demande de fonctionnement peut maintenir la circulation au-delà
de cette durée.

La disparition de la demande de protection ne constitue jamais, à elle
seule, un ordre direct d'arrêt de la pompe. La décision reste appliquée par
la machine à états conformément à SPEC-005.

Cette protection :

* reste autorisée en mode `SECURISATION` ;
* n'est jamais exécutée en mode `OFF` ;
* reste soumise au niveau de fonctionnement appliqué par la SPEC-005.

L'impossibilité d'assurer une protection requise relève du diagnostic `PRO-003` défini dans la SPEC-007.

# 6. Mesures indisponibles

Si la température piscine ou la luminosité n'est pas exploitable, la demande de chauffage solaire est inactive. Les diagnostics correspondants sont définis dans la SPEC-007.

# 7. Responsabilités

SPEC-008 ne commande jamais la pompe, ne calcule pas l'objectif de filtration, ne change pas le mode et ne décide pas des transitions.

# 8. Critères d'acceptation

* La demande solaire suit uniquement la température, la consigne, la luminosité et le seuil.
* L'objectif quotidien atteint n'annule pas une demande solaire valide.
* Le chauffage actif nécessite une circulation réelle.
* `binary_sensor.pcha_protection_serpentin_requise` respecte le cycle 25 minutes / 5 minutes.
* Aucune commande physique n'est réalisée par cette fonction.

# 9. Références

* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* SPEC-009 — Journalisation et notifications
