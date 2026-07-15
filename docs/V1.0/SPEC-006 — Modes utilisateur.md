# SPEC-006 — Modes utilisateur

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit les modes de fonctionnement accessibles à l'utilisateur.

Elle décrit le comportement attendu de chaque mode.

Les transitions entre états sont définies dans la **SPEC-005**.

---

# 2. Principes

Le mode utilisateur représente le fonctionnement souhaité par l'utilisateur.

Le mode sélectionné ne peut jamais contourner les règles de sécurité.

En présence d'un diagnostic de niveau supérieur, la machine à états applique les priorités définies dans la **SPEC-005**.

---

# 3. Modes disponibles

La V1 comporte quatre modes utilisateur :

| Mode          | Description                                        |
| ------------- | -------------------------------------------------- |
| OFF           | Arrêt volontaire de l'installation.                |
| AUTO          | Fonctionnement entièrement automatique.            |
| TRAITEMENT    | Fonctionnement imposé pour un traitement de l'eau. |
| MARCHE_FORCÉE | Fonctionnement manuel imposé par l'utilisateur.    |

---

# 4. Mode OFF

## Objectif

Permettre l'arrêt volontaire de l'installation.

## Comportement

Le contrôleur ne réalise aucune fonction automatique.

Par défaut, les fonctions de sécurité restent actives.

Lorsque l'option Désactiver les sécurités en mode OFF est activée, aucun démarrage automatique de la pompe n'est autorisé.

Cette option est temporaire et est automatiquement réinitialisée lors du passage en mode AUTO.

---

# 5. Mode AUTO

## Objectif

Assurer le fonctionnement normal de la piscine.

## Comportement

Le contrôleur pilote automatiquement :

* la filtration ;
* le chauffage solaire ;
* la protection du serpentin.

Les règles de fonctionnement sont définies dans :

* **SPEC-003** (filtration) ;
* **SPEC-008** (chauffage solaire).

---

# 6. Mode TRAITEMENT

## Objectif

Permettre un traitement de l'eau nécessitant une filtration continue.

## Comportement

Le contrôleur maintient la filtration pendant la durée demandée.

Les fonctions de sécurité restent actives.

Le chauffage solaire continue de fonctionner si ses conditions de fonctionnement sont satisfaites.

---

# 7. Mode MARCHE_FORCÉE

## Objectif

Permettre à l'utilisateur d'imposer le fonctionnement de la pompe.

## Comportement

La filtration est maintenue tant que le mode est actif.

Le chauffage solaire reste autorisé lorsque ses conditions sont satisfaites.

Les diagnostics de sécurité restent prioritaires.

---

# 8. Priorité des modes

Lorsque plusieurs demandes sont simultanément présentes, les priorités sont définies par la machine à états (SPEC-005).

Un mode utilisateur ne peut jamais empêcher :

* une mise en SECURISATION ;
* un passage en DEFAUT.

---

# 9. Sélection du mode

Le mode actif est sélectionné par l'utilisateur via Home Assistant.

Le modèle des entités est défini dans la **SPEC-004**.

Le changement de mode est pris en compte par la machine à états conformément à la **SPEC-005**.

---

# 10. Journalisation

Tout changement de mode est enregistré conformément à la **SPEC-009**.

Les informations minimales enregistrées sont :

* mode précédent ;
* nouveau mode ;
* date et heure ;
* origine de la demande (utilisateur ou système).

---

# 11. Critères d'acceptation

La gestion des modes est conforme lorsque :

* un seul mode utilisateur est actif à tout instant ;
* le changement de mode est pris en compte par la machine à états ;
* les fonctions de sécurité restent prioritaires ;
* tous les changements sont journalisés.

---

# 12. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
