# SPEC-001 — Inventaire matériel

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC inventorie les équipements physiques de la V1. Elle ne définit aucun comportement fonctionnel.

# 2. Circuit hydraulique

```text
Aspiration → Pompe → Débitmètre → Thermomètre piscine → Serpentin → Refoulement
```

# 3. Équipements présents

| Équipement | Fonction | Unité |
|---|---|---|
| Pompe de filtration commandée | Assurer la circulation d'eau | Marche / arrêt |
| Débitmètre | Mesurer le débit du circuit | L/h |
| Thermomètre piscine | Mesurer la température de l'eau en sortie de pompe | °C |
| Capteur de luminosité | Mesurer l'ensoleillement disponible | lx |
| Thermomètre extérieur | Mesurer la température de l'air | °C |
| Mesure de puissance | Mesurer la puissance instantanée de la pompe | W |
| Compteur d'énergie | Mesurer l'énergie consommée par la pompe | kWh |

Les identifiants Home Assistant et leur correspondance PCHA sont définis uniquement dans la SPEC-004.

# 4. Équipements absents de la V1

* vanne motorisée ;
* sonde de température du serpentin ;
* sonde de température du local technique.

# 5. Contraintes

Les équipements physiques fournissent des mesures ou exécutent des commandes. Ils ne contiennent aucune logique métier et ne sont utilisés directement que par la couche d'abstraction définie dans la SPEC-004.

# 6. Références

* SPEC-000 — Principes généraux
* SPEC-004 — Couche d'abstraction et configuration
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
