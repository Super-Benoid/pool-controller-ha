# CONVENTIONS.md

Pool Controller Home Assistant (PCHA)

Version : V1.0
Statut : Figé

---

# 1. Objet

Ce document définit les conventions de développement applicables à l'ensemble du projet Pool Controller Home Assistant (PCHA).

Ces conventions garantissent la cohérence, la maintenabilité et l'évolutivité du projet.

Elles sont obligatoires pour tous les développements.

---

# 2. Documents de référence

Le projet repose sur trois niveaux de documentation.

## SPEC

Les SPEC décrivent le comportement fonctionnel du contrôleur.

Elles répondent à la question :

> **Que doit faire le contrôleur ?**

---

## ARCHITECTURE.md

Décrit l'organisation du projet.

Il répond à la question :

> **Comment le projet est-il organisé ?**

---

## CONVENTIONS.md

Décrit les règles de développement.

Il répond à la question :

> **Comment le code doit-il être écrit ?**

---

# 3. Hiérarchie documentaire

En cas de contradiction :

1. Les SPEC prévalent.
2. ARCHITECTURE.md définit l'organisation du projet.
3. CONVENTIONS.md définit les règles de développement.
4. Le code implémente ces documents.

---

# 4. Source unique de vérité

Chaque information possède une seule source.

Une règle métier ne doit jamais être dupliquée.

Une décision ne doit jamais être implémentée dans plusieurs fichiers.

Une SPEC ne peut référencer qu'une seule SPEC comme source d'une information.

Elle ne doit jamais recopier cette information.

---

# 5. Une information = une SPEC

Une information fonctionnelle est décrite dans une seule SPEC.

Cette SPEC devient la référence unique (Single Source of Truth).

Les autres SPEC ne doivent jamais recopier cette information.

Elles doivent uniquement y faire référence.

Exemple :

- les modes de fonctionnement sont définis uniquement dans la SPEC-006 ;
- la machine à états est définie uniquement dans la SPEC-005 ;
- l'algorithme de filtration est défini uniquement dans la SPEC-003 ;
- la couche d'abstraction est définie uniquement dans la SPEC-004.

Toute duplication d'une règle fonctionnelle est interdite.

En cas de modification, une seule SPEC est mise à jour.
Les autres documents continuent de faire référence à cette SPEC.

---

# 6. Une SPEC = un domaine

Chaque SPEC décrit un seul domaine fonctionnel.

Le code respecte strictement cette séparation.

---

# 7. Une responsabilité = un fichier

Chaque fichier possède une responsabilité unique.

Un fichier ne doit jamais mélanger plusieurs domaines fonctionnels.

---

# 8. Développement par couches

Le projet est développé dans l'ordre suivant :

1. Helpers
2. Templates
3. Machine à états
4. Scripts
5. Automatisations
6. Diagnostics

Une couche est entièrement validée avant de commencer la suivante.

---

# 9. Couche d'abstraction

Les équipements physiques ne sont jamais utilisés directement par la logique métier.

Les scripts, automatisations, diagnostics et machines à états utilisent exclusivement des entités PCHA.

Exemple :

```text
Équipement physique
        │
        ▼
Template d'abstraction
        │
        ▼
sensor.pcha_*
        │
        ▼
Logique métier
```

---

# 10. Organisation des Templates

Les Templates sont organisés en deux niveaux.

## Niveau 1 : Abstraction

Transformation des équipements physiques en entités PCHA.

Aucune logique métier.

## Niveau 2 : Métier

Création des états logiques utilisés par le contrôleur.

---

# 11. Contrat d'interface

Chaque fichier commence par un contrat d'interface.

Il décrit uniquement :

* les Entrées ;
* les Sorties.

Exemple :

```text
Entrées

sensor.pcha_debit

Sorties

binary_sensor.pcha_debit_nominal
```

---

# 12. Convention de nommage

Toutes les entités créées par le projet utilisent le préfixe :

```text
pcha_
```

Les équipements physiques conservent leur nom d'origine.

Les préfixes suivants sont utilisés lorsque nécessaire :

| Préfixe   | Signification             |
| --------- | ------------------------- |
| consigne_ | Valeur cible configurable |
| seuil_    | Valeur de décision        |
| tempo_    | Temporisation             |
| etat_     | État interne              |

---

# 13. Helpers

Les Helpers représentent uniquement des paramètres configurables.

Ils ne doivent jamais contenir :

* une mesure ;
* un état calculé ;
* une information déductible.

Leur nombre doit rester minimal.

---

# 14. Développement d'un module

Chaque nouveau module suit obligatoirement les étapes suivantes :

1. Validation de la SPEC.
2. Définition du contrat d'interface.
3. Création du squelette.
4. Implémentation.
5. Tests.
6. Validation.
7. Intégration.
8. Module figé.

---

# 15. Gestion des évolutions

Toute évolution fonctionnelle commence par la modification de la SPEC concernée.

Le code n'introduit jamais un comportement qui n'est pas décrit dans une SPEC.

Une décision prise pendant le développement doit être immédiatement reportée dans le document de référence approprié :

* SPEC ;
* ARCHITECTURE.md ;
* CONVENTIONS.md.

Aucun développement ne doit se poursuivre tant que cette mise à jour documentaire n'a pas été réalisée.

---

# 16. Philosophie

Le projet privilégie :

* la simplicité ;
* la lisibilité ;
* la modularité ;
* la robustesse ;
* la réutilisabilité.

Une solution simple et claire est toujours préférée à une solution complexe.

---

# 17. Versionnement

La version V1 est considérée comme figée.

Toute nouvelle fonctionnalité ou amélioration non indispensable au fonctionnement de la V1 est reportée à une version ultérieure.

La stabilité de la V1 est prioritaire sur l'ajout de nouvelles fonctionnalités.
