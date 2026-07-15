# SPEC-000 — Architecture générale du Pool Controller

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

La présente spécification définit l'architecture générale du Pool Controller.

Elle constitue le document de référence de l'ensemble du projet.

Toutes les autres spécifications (SPEC-001 à SPEC-009) doivent respecter les principes définis dans ce document.

---

# 2. Objectifs

Le Pool Controller a pour objectif d'automatiser la gestion d'une piscine en garantissant :

* la sécurité du matériel ;
* la continuité de service ;
* une filtration optimisée ;
* un chauffage solaire autonome ;
* une architecture simple, robuste et maintenable.

Le système est entièrement supervisé par Home Assistant.

---

# 3. Périmètre

La V1 comprend :

* gestion automatique de la filtration ;
* chauffage solaire ;
* protection du serpentin ;
* gestion des modes utilisateur ;
* machine à états ;
* diagnostics ;
* journalisation.

La V1 est figée.

Toute évolution fonctionnelle relève d'une nouvelle version.

---

# 4. Principes fondamentaux

Le développement repose sur les principes suivants.

## 4.1 Sécurité

La protection du matériel est toujours prioritaire.

---

## 4.2 Continuité de service

Le fonctionnement est maintenu aussi longtemps que la sécurité peut être garantie.

---

## 4.3 Déterminisme

À un instant donné :

* une seule décision ;
* une seule transition d'état.

Le comportement doit être parfaitement reproductible.

---

## 4.4 Centralisation

Toutes les décisions passent par la machine à états.

Aucune automatisation parallèle ne doit prendre une décision métier.

---

## 4.5 Paramétrage

Toutes les constantes métier sont configurables via des Helpers Home Assistant.

Aucune valeur métier ne doit être codée en dur.

---

# 5. Architecture générale

Le contrôleur est organisé en couches.

```text
Capteurs

↓

Validation des mesures

↓

Diagnostics

↓

Machine à états

↓

Décision

↓

Scripts / Actionneurs
```

Chaque couche possède une responsabilité unique.

---

# 6. Machine à états

Le système est piloté exclusivement par la machine à états définie dans la **SPEC-005**.

Les états officiels sont :

* OFF
* AUTO
* TRAITEMENT
* MARCHE_FORCÉE
* SECURISATION
* DEFAUT

Aucun autre état n'est autorisé.

---

# 7. Architecture des diagnostics

Les diagnostics sont définis dans la **SPEC-007**.

Ils sont organisés en trois familles :

* MES : mesure ;
* COH : cohérence ;
* PRO : procédé.

Chaque diagnostic possède un niveau :

* INFORMATIF ;
* DÉGRADÉ ;
* CRITIQUE.

---

# 8. Journalisation

Toutes les décisions importantes sont journalisées.

Le format officiel est défini dans la **SPEC-009**.

---

# 9. Configuration

Toutes les valeurs métier sont configurables.

Les Helpers Home Assistant sont définis dans la **SPEC-004**.

---

# 10. Règles d'architecture

Le développement doit respecter les règles suivantes :

* une seule machine à états ;
* une seule source de décision ;
* aucune logique dupliquée ;
* aucune automatisation parallèle ;
* toutes les décisions sont journalisées ;
* tous les scripts sont idempotents.

---

# 11. Principe de responsabilité unique

Chaque spécification possède une responsabilité unique.

Une SPEC ne traite qu'un seul domaine fonctionnel.

Si une information appartient à une autre spécification, celle-ci est uniquement référencée.

Aucune duplication de contenu n'est autorisée.

---

# 12. Principe de source unique

Chaque règle métier est définie une seule fois dans l'ensemble de la documentation.

Cela concerne notamment :

* les constantes ;
* les seuils ;
* les algorithmes ;
* les diagnostics ;
* les états ;
* les conventions ;
* les règles de priorité.

Les autres spécifications ne doivent jamais recopier cette information.

Elles doivent uniquement faire référence à la spécification qui en est propriétaire.

Ce principe garantit la cohérence de la documentation et simplifie sa maintenance.

---

# 13. Organisation des spécifications

| Document | Responsabilité           |
| -------- | ------------------------ |
| SPEC-000 | Architecture générale    |
| SPEC-001 | Exigences fonctionnelles |
| SPEC-002 | Architecture logicielle  |
| SPEC-003 | Gestion de la filtration |
| SPEC-004 | Modèle Home Assistant    |
| SPEC-005 | Machine à états          |
| SPEC-006 | Modes utilisateur        |
| SPEC-007 | Diagnostics              |
| SPEC-008 | Chauffage solaire        |
| SPEC-009 | Journalisation           |

---

# 14. Évolutions

La version V1 est figée.

Toute modification de comportement doit obligatoirement :

* modifier la spécification concernée ;
* conserver la cohérence avec la présente SPEC-000 ;
* être documentée avant toute implémentation.

Le code est une implémentation des spécifications et ne constitue jamais la référence du projet.
