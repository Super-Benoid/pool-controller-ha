# INTRODUCTION.md

# Pool Controller Home Assistant (PCHA)

Version : V1.0
Statut : Figée

---

# Présentation

Le projet **Pool Controller Home Assistant (PCHA)** est un contrôleur logiciel destiné à automatiser la gestion d'une piscine équipée d'un système de chauffage solaire passif.

Son objectif est de piloter l'installation de manière simple, fiable et évolutive, tout en restant indépendant du matériel utilisé.

Le projet est entièrement intégré à **Home Assistant** et repose sur des composants standards (ESPHome, Shelly, etc.).

---

# Philosophie

Le contrôleur a été conçu autour de quelques principes fondamentaux :

* simplicité avant complexité ;
* sécurité avant performance ;
* modularité avant optimisation ;
* une seule source de vérité pour chaque information.

L'installation hydraulique est volontairement modélisée de façon fidèle à la réalité.

Il n'existe qu'un seul circuit hydraulique.

Le chauffage solaire n'est pas un circuit indépendant.

Il s'agit simplement d'une période de filtration réalisée lorsque les conditions d'ensoleillement permettent de récupérer de l'énergie solaire.

---

# Objectifs

Le projet poursuit plusieurs objectifs :

* automatiser complètement la filtration ;
* exploiter gratuitement l'énergie solaire disponible ;
* protéger l'installation ;
* limiter la consommation électrique ;
* proposer une architecture simple à maintenir ;
* permettre des évolutions futures sans remettre en cause les fondations du projet.

---

# Principes de développement

Le projet est construit selon une séparation stricte entre :

* les besoins fonctionnels ;
* l'architecture logicielle ;
* l'implémentation.

Cette séparation garantit la cohérence du projet et facilite sa maintenance.

---

# Organisation documentaire

Le projet repose sur quatre documents de référence.

## INTRODUCTION.md

Présente le projet, ses objectifs et sa philosophie.

---

## SPEC-000 à SPEC-009

Décrivent le comportement fonctionnel attendu.

Elles répondent à la question :

> **Que doit faire le contrôleur ?**

---

## ARCHITECTURE.md

Décrit l'organisation technique du projet.

Il répond à la question :

> **Comment le projet est-il organisé ?**

---

## CONVENTIONS.md

Décrit les règles de développement.

Il répond à la question :

> **Comment le projet est-il développé ?**

---

# Organisation générale

Le développement suit une architecture par couches.

```text
Équipements physiques
        │
        ▼
Templates d'abstraction
        │
        ▼
Entités métier PCHA
        │
        ▼
Machine à états
        │
        ▼
Scripts
        │
        ▼
Automatisations
        │
        ▼
Diagnostics
```

Cette architecture permet de remplacer un équipement physique sans modifier la logique métier.

---

# Versions

La version **V1** constitue une base stable et opérationnelle.

Son objectif est de couvrir les besoins essentiels de l'installation.

Les évolutions futures (V2, V3, …) pourront enrichir les fonctionnalités sans remettre en cause l'architecture générale.

---

# Conclusion

Le Pool Controller Home Assistant (PCHA) est conçu comme un projet logiciel structuré, documenté et évolutif.

Chaque fonctionnalité est décrite par une SPEC.

Chaque choix technique est documenté dans l'architecture.

Chaque règle de développement est définie dans les conventions.

Cette organisation garantit un projet cohérent, maintenable et pérenne.
