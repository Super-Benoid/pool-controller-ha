# SPEC-000 — Principes généraux

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Le Pool Controller Home Assistant (PCHA) automatise une piscine équipée d'un circuit unique de filtration et d'un chauffage solaire passif.

Cette SPEC définit uniquement les principes communs du projet. Les comportements détaillés appartiennent aux SPEC spécialisées.

# 2. Périmètre V1

Le PCHA assure :

* la filtration de la piscine ;
* l'exploitation du chauffage solaire ;
* la protection de l'installation ;
* la supervision, la journalisation et les notifications.

Toute autre fonction est hors du périmètre de la V1.

# 3. Priorités

Les priorités sont, dans l'ordre :

1. sécurité des personnes ;
2. protection de l'installation ;
3. filtration de la piscine ;
4. chauffage solaire ;
5. optimisation énergétique.

# 4. Installation hydraulique

Le contrôleur pilote un seul circuit :

```text
Aspiration piscine
        │
        ▼
Pompe de filtration
        │
        ▼
Débitmètre
        │
        ▼
Thermomètre piscine
        │
        ▼
Serpentin solaire
        │
        ▼
Refoulement piscine
```

Il existe une seule pompe, un seul débit et aucun circuit solaire séparé. La mesure de température d'eau devient représentative du bassin après une circulation suffisante.

# 5. Répartition des responsabilités

Chaque domaine possède une source unique :

| Domaine | Référence |
|---|---|
| Filtration | SPEC-003 |
| Abstraction et configuration | SPEC-004 |
| Machine à états | SPEC-005 |
| Modes de fonctionnement | SPEC-006 |
| Diagnostics et sécurités | SPEC-007 |
| Chauffage solaire | SPEC-008 |
| Journalisation et notifications | SPEC-009 |

L'organisation technique et les règles de développement sont définies respectivement dans `ARCHITECTURE.md` et `CONVENTIONS.md`.

# 6. Règles générales

* Une information possède une seule source de vérité.
* Une règle métier n'est jamais recopiée dans une autre SPEC.
* Le code n'introduit aucun comportement absent des SPEC.
* Le matériel n'est jamais utilisé directement par la logique métier.
* Toute correction nécessaire à la V1 est portée par la SPEC propriétaire.

# 7. Références

* `00-Introduction.md`
* `ARCHITECTURE.md`
* `CONVENTIONS.md`
* SPEC-001 à SPEC-009
