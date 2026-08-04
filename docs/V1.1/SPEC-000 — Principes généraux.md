# SPEC-000 — Principes généraux

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Le Pool Controller Home Assistant (PCHA) automatise une piscine équipée d'un circuit unique de filtration et d'un chauffage solaire passif.

Cette SPEC définit les principes communs de la V1.1. Les comportements détaillés appartiennent aux SPEC spécialisées.

# 2. Périmètre V1.1

Le PCHA assure :

* la filtration de la piscine ;
* l'exploitation du chauffage solaire ;
* la protection de l'installation ;
* la supervision, la journalisation et les notifications ;
* la mesure permanente de la température directement dans le bassin ;
* le fonctionnement dégradé du chauffage solaire lorsque la luminosité distante est indisponible.

# 3. Priorités

Les priorités sont, dans l'ordre :

1. sécurité des personnes ;
2. protection de l'installation ;
3. filtration de la piscine ;
4. chauffage solaire ;
5. optimisation énergétique.

# 4. Installation

Le contrôleur pilote un seul circuit hydraulique :

```text
Aspiration piscine → Pompe → Débitmètre → Serpentin solaire → Refoulement
```

La température est mesurée par une sonde immergée directement dans le bassin. Elle est représentative de l'eau sans démarrage préalable de la pompe.

La luminosité est mesurée par un BH1750 raccordé localement à une D1 mini. La D1 mini transmet la mesure à l'ESP32 Jardin par Wi-Fi et Packet Transport UDP.

```text
BH1750 → D1 mini → Wi-Fi / UDP → ESP32 Jardin → Home Assistant → PCHA
```

# 5. Répartition des responsabilités

| Domaine | Référence |
|---|---|
| Filtration et objectif quotidien | SPEC-003 |
| Abstraction et configuration | SPEC-004 |
| Machine à états | SPEC-005 |
| Modes de fonctionnement | SPEC-006 |
| Diagnostics et sécurités | SPEC-007 |
| Chauffage solaire | SPEC-008 |
| Journalisation et notifications | SPEC-009 |

# 6. Règles générales

* Une information possède une seule source de vérité.
* Une règle métier n'est jamais recopiée dans une autre SPEC.
* Le code n'introduit aucun comportement absent des SPEC.
* Le matériel n'est jamais utilisé directement par la logique métier : il passe par la couche d'abstraction PCHA.
* Les identifiants métier historiques sont conservés lorsque cela évite de casser les automatismes existants.
* Les valeurs aberrantes ne remplacent jamais la dernière valeur cohérente.

# 7. Références

* `00-Introduction.md`
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
* SPEC-001 à SPEC-009
