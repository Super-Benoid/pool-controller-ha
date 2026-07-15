# 00 - Introduction

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

**Auteur :** Super-Benoid

---

# 1. Objet du document

Ce document constitue l'introduction officielle du projet **Pool Controller HA**.

Il décrit les objectifs du projet, sa philosophie de conception et les règles qui régissent son développement.

L'ensemble des documents de spécification (SPEC) constitue la référence unique du projet.

Aucune implémentation ne doit s'écarter des spécifications validées.

---

# 2. Présentation du projet

Pool Controller HA est un contrôleur logiciel destiné à Home Assistant permettant de piloter automatiquement la filtration et le chauffage solaire d'une piscine.

Le projet repose exclusivement sur les fonctionnalités natives de Home Assistant et des intégrations existantes.

L'objectif n'est pas de réaliser une simple automatisation mais de développer un véritable contrôleur capable de prendre des décisions cohérentes en fonction de nombreux paramètres.

---

# 3. Objectifs

Les objectifs principaux sont les suivants :

* garantir une excellente qualité d'eau ;
* optimiser le chauffage solaire ;
* limiter la consommation électrique ;
* protéger les équipements ;
* être totalement configurable ;
* être entièrement documenté ;
* rester simple à maintenir.

---

# 4. Philosophie du projet

Le contrôleur doit toujours privilégier :

1. La sécurité des personnes et du matériel.
2. La qualité sanitaire de l'eau.
3. L'utilisation de l'énergie solaire.
4. La réduction de la consommation électrique.
5. Le confort d'utilisation.

Lorsqu'un conflit apparaît entre plusieurs objectifs, cette hiérarchie est toujours respectée.

---

# 5. Principe général

Toutes les décisions sont prises à partir :

* des mesures physiques ;
* des paramètres configurés par l'utilisateur ;
* de l'état interne du contrôleur.

Le contrôleur ne réalise aucune action aléatoire.

Chaque décision doit être :

* explicable ;
* reproductible ;
* enregistrée dans le journal.

---

# 6. Architecture générale

Le contrôleur est organisé en cinq couches.

```
Capteurs
      │
      ▼
Acquisition
      │
      ▼
Calculs
      │
      ▼
Machine à états
      │
      ▼
Commande de la pompe
```

Chaque couche possède une responsabilité unique.

---

# 7. Cycle de fonctionnement

Le contrôleur fonctionne en continu.

Toutes les dix secondes :

1. lecture des capteurs ;
2. validation des données ;
3. mise à jour des calculs ;
4. détection des événements ;
5. éventuelle transition d'état ;
6. commande de la pompe ;
7. journalisation.

Le contrôleur utilise une architecture hybride :

* supervision cyclique toutes les dix secondes ;
* décisions déclenchées uniquement lorsqu'une transition est nécessaire.

---

# 8. Principes de conception

Le projet respecte les principes suivants :

* une responsabilité par fichier ;
* une responsabilité par script ;
* aucune duplication de logique ;
* paramètres configurables ;
* comportement déterministe ;
* priorité aux sécurités ;
* documentation avant implémentation.

---

# 9. Version V1

La version V1 est figée.

Les éléments suivants ne seront plus modifiés :

* architecture générale ;
* algorithmes ;
* hiérarchie des priorités ;
* organisation des packages ;
* noms des entités ;
* stratégie de décision.

Les évolutions futures seront intégrées dans une version V2.

---

# 10. Documentation

La documentation officielle est composée des documents suivants :

* 00 – Introduction
* SPEC-001 – Cahier des charges
* SPEC-002 – Architecture technique
* SPEC-003 – Algorithme
* SPEC-004 – Catalogue des entités
* SPEC-005 – Machine à états
* SPEC-006 – Variables internes
* SPEC-007 – Gestion des défauts
* SPEC-008 – Protection serpentin
* SPEC-009 – Packages
* SPEC-010 – Scripts
* SPEC-011 – Automatisations
* SPEC-012 – Dashboard
* SPEC-013 – Plan de tests
* SPEC-014 – Mise en service
* SPEC-015 – Maintenance

Cette documentation constitue la référence unique du projet.

---

# 11. Gestion des versions

Le développement suit le cycle suivant :

```
Spécifications
        ↓
Implémentation
        ↓
Tests
        ↓
Corrections
        ↓
Validation
        ↓
Publication
```

Toute modification fonctionnelle doit faire l'objet d'une nouvelle version des spécifications.

---

# 12. Objectif final

À l'issue de la V1, le projet devra permettre :

* une installation simple dans Home Assistant ;
* une configuration entièrement graphique ;
* un fonctionnement autonome ;
* une maintenance aisée ;
* une compréhension complète grâce à la documentation.

Le projet a vocation à devenir un contrôleur open source fiable, documenté et évolutif pour la gestion de la filtration et du chauffage solaire d'une piscine.
