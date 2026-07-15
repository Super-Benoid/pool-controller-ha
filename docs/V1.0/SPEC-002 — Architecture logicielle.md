# SPEC-002 — Architecture logicielle

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit l'architecture logicielle du Pool Controller.

Elle décrit les modules logiciels, leurs responsabilités et leurs interactions.

Les principes généraux de conception sont définis dans la **SPEC-000**.

---

# 2. Principes d'architecture

L'architecture est modulaire.

Chaque module possède une responsabilité unique.

Les modules communiquent uniquement par l'intermédiaire des entités Home Assistant.

Aucun module ne doit contenir de logique appartenant à un autre module.

---

# 3. Architecture générale

Le Pool Controller est composé des modules suivants :

```text
Capteurs
     │
     ▼
Acquisition des données
     │
     ▼
Diagnostics
     │
     ▼
Machine à états
     │
     ▼
Gestion des modes
     │
     ▼
Fonctions métier
     │
     ▼
Scripts d'action
```

Chaque module ne dépend que du module situé immédiatement au-dessus.

---

# 4. Modules logiciels

## MOD-001 — Acquisition

Responsabilités :

* lire les capteurs ;
* lire les Helpers ;
* rendre les informations disponibles au reste du système.

Le détail des entités est défini dans la **SPEC-004**.

---

## MOD-002 — Diagnostics

Responsabilités :

* analyser les mesures ;
* détecter les anomalies ;
* produire les diagnostics.

Les règles sont définies dans la **SPEC-007**.

---

## MOD-003 — Machine à états

Responsabilités :

* déterminer l'état courant ;
* autoriser les transitions ;
* appliquer les priorités.

Les états sont définis dans la **SPEC-005**.

---

## MOD-004 — Gestion des modes

Responsabilités :

* interpréter le mode choisi par l'utilisateur ;
* transmettre la demande à la machine à états.

Les modes sont définis dans la **SPEC-006**.

---

## MOD-005 — Gestion de la filtration

Responsabilités :

* calculer le temps quotidien de filtration ;
* déterminer si la filtration doit être active.

Les règles sont définies dans la **SPEC-003**.

---

## MOD-006 — Gestion du chauffage solaire

Responsabilités :

* évaluer le potentiel solaire ;
* autoriser le chauffage ;
* protéger le serpentin.

Les règles sont définies dans la **SPEC-008**.

---

## MOD-007 — Scripts d'action

Responsabilités :

* piloter les relais ;
* démarrer ou arrêter la pompe ;
* commander les équipements.

Les scripts ne prennent aucune décision métier.

Ils exécutent uniquement les ordres transmis par la machine à états.

---

## MOD-008 — Journalisation

Responsabilités :

* enregistrer les événements ;
* tracer les décisions ;
* générer les notifications.

Les règles sont définies dans la **SPEC-009**.

---

# 5. Flux de fonctionnement

Chaque cycle de décision suit l'ordre suivant :

1. Acquisition des données.
2. Exécution des diagnostics.
3. Évaluation de la machine à états.
4. Détermination des fonctions autorisées.
5. Exécution des scripts.
6. Journalisation.

Cet ordre est invariant.

---

# 6. Dépendances

Les dépendances autorisées sont :

```text
Acquisition
      │
      ▼
Diagnostics
      │
      ▼
Machine à états
      │
      ▼
Gestion des modes
      │
      ▼
Fonctions métier
      │
      ▼
Scripts
      │
      ▼
Journalisation
```

Un module ne doit jamais accéder directement à un module situé plus bas dans la chaîne.

---

# 7. Contraintes d'implémentation

L'architecture doit respecter les contraintes suivantes :

* un seul contrôleur logique ;
* une seule machine à états ;
* aucun script décisionnel ;
* aucune logique dupliquée ;
* aucun accès direct aux actionneurs sans validation préalable de la machine à états.

---

# 8. Interfaces

Les échanges entre modules utilisent exclusivement :

* les entités Home Assistant ;
* les Helpers ;
* les scripts ;
* les timers.

Le modèle des entités est défini dans la **SPEC-004**.

---

# 9. Évolutivité

Chaque module doit pouvoir évoluer indépendamment, sous réserve de respecter :

* son interface publique ;
* les principes définis dans la **SPEC-000** ;
* les responsabilités définies dans cette spécification.

Toute nouvelle fonctionnalité doit être intégrée à un module existant ou faire l'objet d'un nouveau module clairement identifié.

---

# 10. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
