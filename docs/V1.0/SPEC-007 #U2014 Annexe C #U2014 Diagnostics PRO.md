# SPEC-007 — Annexe C

## Diagnostics PRO — Procédé

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Les diagnostics PRO détectent une anomalie réelle du procédé à partir de mesures validées par MES et COH.

# 2. Diagnostics

| Identifiant | Diagnostic | Gravité | Réarmement |
|---|---|---|---|
| `PRO-001` | Débit critique | `CRITIQUE` | `TEMPORISE` |
| `PRO-002` | Débit insuffisant prolongé | `DEGRADE` | `TEMPORISE` |
| `PRO-003` | Protection du serpentin impossible | `CRITIQUE` | `AUTOMATIQUE` |

# 3. Conditions et conséquences

## PRO-001 — Débit critique

PRO-001 est évalué uniquement lorsque :

- la machine est en FILTRATION ;
- la mesure de débit est disponible ;
- la mesure a été validée par la famille MES ;
- aucun diagnostic COH n'interdit son exploitation.

Sa condition d'activation est :

débit < 500 L/h

La condition doit rester présente continuellement pendant la durée définie
par :

input_number.pcha_temps_validation_debit

La valeur opérationnelle V1 de cette durée est de 30 secondes.

La gravité de PRO-001 est CRITIQUE.

Le niveau global devient CRITIQUE. SPEC-005 interdit alors le maintien de
la machine en FILTRATION et provoque l'arrêt immédiat de la pompe.

PRO-001 n'est pas évalué lorsque la pompe est normalement arrêtée.

Son réarmement est TEMPORISE conformément à la partie 2 de SPEC-007.

## PRO-002 — Débit insuffisant prolongé

PRO-002 est évalué uniquement lorsque :

- la machine est en FILTRATION ;
- la mesure de débit est disponible ;
- la mesure a été validée par la famille MES ;
- aucun diagnostic COH n'interdit son exploitation ;
- la condition de PRO-001 n'est pas active.

Sa condition d'activation est :

500 L/h ≤ débit < 3 000 L/h

La condition doit rester présente continuellement pendant la durée définie
par :

input_number.pcha_temps_validation_debit

La valeur opérationnelle V1 de cette durée est de 30 secondes.

La gravité de PRO-002 est DEGRADE.

Un débit supérieur ou égal à 3 000 L/h est considéré comme suffisant pour
la V1.

La valeur d'environ 3 800 L/h est une référence observée et non un seuil
de déclenchement.

PRO-002 n'est pas actif lorsque le débit est inférieur à 500 L/h. Cette
situation appartient exclusivement à PRO-001.

Son réarmement est TEMPORISE conformément à la partie 2 de SPEC-007.

## PRO-003 — Protection du serpentin impossible

PRO-003 est évalué lorsqu'une protection du serpentin est demandée par la SPEC-008.

Il devient actif lorsqu'au moins une des conditions observables suivantes est vraie :

* le mode de fonctionnement est `OFF` ;
* l'actionneur PCHA de la pompe est indisponible ;
* `MES-002` est actif et la sécurité hydraulique ne peut plus être vérifiée ;
* `PRO-001` est actif et le débit est critique.

Sa gravité est `CRITIQUE` et son réarmement est `AUTOMATIQUE`.

Il disparaît dès que la protection n'est plus demandée ou que la cause empêchant la circulation a disparu.

Le niveau devient `CRITIQUE` et l'événement doit être notifié conformément à la SPEC-009.

# 4. Critères d'acceptation

* Les diagnostics utilisent uniquement des informations validées.
* Chaque diagnostic décrit une anomalie réelle du procédé.
* La conséquence est portée par le niveau de fonctionnement, jamais par un changement direct de mode ou d'état.

# 5. Références

* SPEC-005 — Machine à états
* SPEC-007 — Partie 1 et Partie 2
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation et notifications
