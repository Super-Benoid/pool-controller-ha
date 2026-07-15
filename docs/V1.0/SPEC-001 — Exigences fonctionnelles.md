# SPEC-001 — Exigences fonctionnelles

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit les exigences fonctionnelles du Pool Controller.

Elle décrit les fonctions que le système doit assurer, indépendamment de leur implémentation.

L'architecture générale est définie dans la **SPEC-000**.

---

# 2. Domaine d'application

Le Pool Controller pilote automatiquement une installation de filtration et de chauffage solaire de piscine.

Il assure :

* la filtration de l'eau ;
* le chauffage solaire ;
* la protection des équipements ;
* la gestion des modes utilisateur ;
* la supervision de l'installation.

---

# 3. Exigences fonctionnelles

## EXI-001 — Fonctionnement autonome

Le système doit fonctionner automatiquement sans intervention de l'utilisateur.

---

## EXI-002 — Filtration

Le système doit assurer la durée quotidienne de filtration définie par les règles de la **SPEC-003**.

---

## EXI-003 — Chauffage solaire

Le système doit exploiter l'énergie solaire disponible pour chauffer l'eau lorsque les conditions le permettent.

Les règles de fonctionnement sont définies dans la **SPEC-008**.

---

## EXI-004 — Protection du serpentin

Le système doit protéger le serpentin solaire contre les risques liés à une stagnation de l'eau.

Les stratégies de protection sont définies dans la **SPEC-008**.

---

## EXI-005 — Modes utilisateur

Le système doit permettre à l'utilisateur de sélectionner un mode de fonctionnement.

Les modes disponibles sont définis dans la **SPEC-006**.

---

## EXI-006 — Gestion des états

Le fonctionnement global doit être piloté exclusivement par la machine à états définie dans la **SPEC-005**.

---

## EXI-007 — Gestion des défauts

Le système doit détecter les anomalies de fonctionnement et appliquer la stratégie adaptée.

Les diagnostics et leurs conséquences sont définis dans la **SPEC-007**.

---

## EXI-008 — Sécurité

Le système doit garantir la protection du matériel avant toute autre considération.

Les principes de sécurité sont définis dans la **SPEC-000**.

---

## EXI-009 — Journalisation

Toute décision importante doit être enregistrée.

Le format et les règles de journalisation sont définis dans la **SPEC-009**.

---

## EXI-010 — Paramétrage

Tous les paramètres métier doivent être configurables depuis Home Assistant.

Le modèle de configuration est défini dans la **SPEC-004**.

---

# 4. Exigences non fonctionnelles

Le système doit :

* être déterministe ;
* être maintenable ;
* être modulaire ;
* être entièrement configurable ;
* être traçable ;
* être robuste face aux défauts de capteurs.

Les principes d'architecture associés sont définis dans la **SPEC-000**.

---

# 5. Critères d'acceptation

La version V1 est considérée conforme lorsque :

* la filtration est assurée conformément à la SPEC-003 ;
* le chauffage solaire fonctionne conformément à la SPEC-008 ;
* les modes utilisateur sont conformes à la SPEC-006 ;
* la machine à états est conforme à la SPEC-005 ;
* les diagnostics sont conformes à la SPEC-007 ;
* les événements sont journalisés conformément à la SPEC-009 ;
* la configuration est conforme à la SPEC-004.

---

# 6. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
