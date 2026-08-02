# SPEC-007 — Annexe B

## Diagnostics COH — Cohérence

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Les diagnostics COH recherchent une incohérence entre des informations PCHA disponibles et validées par la famille MES. Ils ne concluent pas à un défaut de procédé.

# 2. Diagnostics

| Identifiant | Diagnostic | Gravité | Réarmement |
|---|---|---|---|
| `COH-001` | Débit incohérent avec la puissance de la pompe | `DEGRADE` | `TEMPORISE` |
| `COH-002` | Température d'eau incohérente | `DEGRADE` | `TEMPORISE` |

# 3. Conditions et conséquences

## COH-001 — Débit incohérent avec la puissance

COH-001 est évalué uniquement lorsque :

- la mesure de débit est disponible et validée par MES ;
- la mesure de puissance est disponible et validée par MES.

Les références V1 sont :

- puissance inférieure à 1 W : pompe électriquement arrêtée ;
- puissance comprise entre 300 et 350 W inclus : puissance normale ;
- débit supérieur ou égal à 3 000 L/h : circulation normale ;
- débit inférieur à 500 L/h : absence de circulation exploitable.

Une incohérence existe notamment lorsque :

- un débit supérieur ou égal à 500 L/h est mesuré alors que la puissance
  reste inférieure à 1 W ;
- la pompe est commandée à l'arrêt alors qu'une puissance supérieure ou
  égale à 1 W persiste ;
- la pompe est commandée à l'arrêt alors qu'un débit supérieur ou égal à
  500 L/h persiste ;
- un débit normal est mesuré alors que la puissance reste durablement hors
  de la plage de 300 à 350 W.

La condition doit rester présente pendant la durée définie par :

input_number.pcha_temps_validation_debit

Cette durée ne peut pas être inférieure à 30 secondes en V1. Elle filtre notamment l'inertie hydraulique et électrique observée pendant les quelques secondes qui suivent l'arrêt ou le démarrage de la pompe.

COH-001 ne doit pas être activé uniquement parce que le débit est inférieur
à 3 000 L/h lorsque la pompe est commandée en marche. Cette situation
appartient à PRO-001 ou PRO-002.

La gravité de COH-001 reste DEGRADE.

Lorsqu'il est actif, les analyses qui nécessitent simultanément une mesure
de débit et une mesure de puissance cohérentes ne sont plus évaluées.

## COH-002 — Température piscine incohérente

COH-002 vérifie la cohérence physique de la mesure source et de la température corrigée de la piscine.

Il est évalué lorsque la source physique fournit une valeur numérique, donc lorsqu'elle n'est pas déclarée indisponible par MES-001. La couche d'abstraction conserve la dernière température cohérente pour les fonctions métier, mais expose simultanément :

* `source_coherent`, pour la valeur physique courante ;
* `corrected_value_coherent`, pour la valeur après application de la correction.

Ainsi, une mesure aberrante reste détectable sans contaminer la température métier ni les statistiques quotidiennes.

La plage de cohérence physique retenue pour la V1 est :

```text
10 °C < température piscine < 50 °C
```

COH-002 devient actif lorsque la mesure source ou la température corrigée vérifie :

```text
température piscine ≤ 10 °C
OU
température piscine ≥ 50 °C
```

Les valeurs exactement égales à `10 °C` ou `50 °C` sont considérées comme incohérentes.

La condition doit rester présente continuellement pendant la durée définie par :

```text
input_number.pcha_temps_validation_temperature_piscine
```

Lorsque COH-002 est actif, la mesure courante ne doit pas être utilisée comme une mesure fiable. Elle n'écrase jamais la dernière température métier cohérente.

Conformément aux règles de dégradation définies par SPEC-007, la valeur de température de consigne peut être utilisée comme valeur de remplacement fonctionnelle lorsque cela est nécessaire.

COH-002 ne commande jamais directement la pompe et ne modifie jamais directement l’état de la machine.

Son réarmement est `TEMPORISE`, conformément à la partie 2 de SPEC-007.


# 4. Critères d'acceptation

* Les mesures utilisées sont validées par MES.
* Une valeur numérique hors plage active COH-002 sans écraser la dernière température cohérente.
* Un diagnostic COH signale une incohérence sans identifier arbitrairement le capteur fautif.
* Aucun diagnostic COH ne commande le système.

# 5. Références

* SPEC-003 — Gestion de la filtration
* SPEC-007 — Partie 1 et Partie 2
* SPEC-008 — Chauffage solaire
