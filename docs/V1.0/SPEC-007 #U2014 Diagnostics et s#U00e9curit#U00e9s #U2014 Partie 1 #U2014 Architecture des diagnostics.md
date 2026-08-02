# SPEC-007 — Diagnostics et sécurités

## Partie 1 — Architecture des diagnostics

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette partie définit l'organisation commune des diagnostics. Les conditions propres à chaque diagnostic sont décrites dans les annexes.

# 2. Familles

| Famille | Responsabilité |
|---|---|
| `MES` | Vérifier la disponibilité et l'exploitabilité des mesures |
| `COH` | Vérifier la cohérence entre informations valides |
| `PRO` | Détecter une anomalie réelle du procédé |

La chaîne d'évaluation est :

```text
MES → COH → PRO
```

Un diagnostic dépendant d'une information invalide n'est pas évalué.

# 3. Gravités

| Gravité | Effet global |
|---|---|
| `INFORMATIF` | Information sans restriction fonctionnelle |
| `DEGRADE` | Fonctionnement maintenu avec les restrictions définies par le diagnostic concerné |
| `CRITIQUE` | Filtration interdite par la machine à états |

# 4. Niveau de fonctionnement

Le niveau global est publié dans :

```text
input_select.pcha_niveau_fonctionnement
```

Valeurs :

```text
NORMAL
INFORMATIF
DEGRADE
CRITIQUE
```

Il correspond à la gravité la plus élevée parmi les diagnostics actifs, ou à `NORMAL` si aucun diagnostic n'est actif.

Le niveau n'est ni un mode, ni un état de la machine.

# 5. Responsabilités

Les diagnostics :

* ne commandent pas la pompe ;
* ne modifient pas le mode ;
* ne modifient pas directement l'état de la machine ;
* publient leur état et le niveau global ;
* produisent les événements consommés par la SPEC-009.

# 6. Organisation documentaire

* Partie 2 — Gestion des diagnostics ;
* Annexe A — MES ;
* Annexe B — COH ;
* Annexe C — PRO.

# 7. Références

* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-009 — Journalisation et notifications
