# SPEC-007 — Diagnostics et sécurités

## Partie 2 — Gestion des diagnostics

**Version :** 1.0  
**Statut :** Figée

---

# 1. Activation

Un diagnostic devient actif lorsque sa condition d'activation et son éventuelle durée de validation sont satisfaites.

Plusieurs diagnostics peuvent être actifs simultanément.

# 2. Réarmement

Chaque diagnostic utilise un seul mode de réarmement :

| Mode | Définition |
|---|---|
| `AUTOMATIQUE` | Disparition dès que la condition n'est plus présente |
| `TEMPORISE` | Disparition après une durée continue sans condition active |
| `MANUEL` | Disparition après disparition de la condition et demande utilisateur de réinitialisation |

# 3. Priorité

La priorité est :

```text
CRITIQUE > DEGRADE > INFORMATIF > NORMAL
```

Le niveau global est recalculé après chaque activation ou disparition.

# 4. Conséquences

Un diagnostic peut uniquement :

* modifier le niveau global par sa gravité ;
* rendre indisponibles les analyses qui dépendent d'une information invalide ;
* produire un événement de diagnostic.

Les décisions opérationnelles appartiennent aux SPEC fonctionnelles et à la machine à états.

# 5. Journalisation et notifications

Chaque activation et disparition produit un événement contenant l'identifiant, la famille, la gravité, l'état et le motif.

La conservation de cet événement et la notification utilisateur sont définies uniquement dans la SPEC-009.

# 6. Critères d'acceptation

* Chaque diagnostic possède une famille, une gravité et un mode de réarmement uniques.
* Le niveau global correspond au diagnostic actif le plus grave.
* Aucun diagnostic ne modifie directement le mode ou l'état de la machine.
* Chaque changement produit un seul événement.

# 7. Références

* SPEC-005 — Machine à états
* SPEC-007 — Partie 1
* SPEC-009 — Journalisation et notifications
