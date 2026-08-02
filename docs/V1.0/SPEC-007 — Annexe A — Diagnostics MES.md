# SPEC-007 — Annexe A

## Diagnostics MES — Mesures

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Les diagnostics MES vérifient uniquement la disponibilité des mesures nécessaires. Ils utilisent les entités PCHA et leur attribut `source_available` défini dans la SPEC-004.

# 2. Mesures surveillées

| Identifiant | Mesure PCHA | Gravité | Réarmement |
|---|---|---|---|
| `MES-001` | Température piscine | `DEGRADE` | `TEMPORISE` |
| `MES-002` | Débit filtration | `CRITIQUE` | `TEMPORISE` |
| `MES-003` | Puissance pompe | `DEGRADE` | `AUTOMATIQUE` |
| `MES-004` | Luminosité | `DEGRADE` | `TEMPORISE` |

La température extérieure et l'énergie consommée sont des mesures de supervision ; leur absence ne modifie pas le fonctionnement.

# 3. Conditions et conséquences

## MES-001 — Température piscine indisponible

Actif lorsque la source de `sensor.pcha_temperature_piscine` reste indisponible pendant le délai configuré. Le calcul d'un nouvel objectif quotidien n'est plus possible ; SPEC-003 applique son comportement dégradé.

## MES-002 — Débit filtration indisponible

Actif lorsque la source de `sensor.pcha_debit_filtration` reste indisponible pendant le délai configuré. La sécurité hydraulique n'est plus garantie ; le niveau devient `CRITIQUE`.

## MES-003 — Puissance pompe indisponible

Actif lorsque la source de `sensor.pcha_puissance_pompe_filtration` est indisponible. Les diagnostics dépendant de cette mesure ne sont plus évalués.

## MES-004 — Luminosité indisponible

Actif lorsque la source de `sensor.pcha_luminosite` reste indisponible pendant le délai configuré. La demande de chauffage solaire est désactivée conformément à la SPEC-008 ; la filtration automatique reste disponible.

# 4. Critères d'acceptation

* Aucun diagnostic MES ne lit directement une entité physique.
* Une mesure invalide bloque uniquement les diagnostics qui en dépendent.
* Chaque diagnostic possède une gravité et un réarmement uniques.

# 5. Références

* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-007 — Partie 1 et Partie 2
* SPEC-008 — Chauffage solaire
