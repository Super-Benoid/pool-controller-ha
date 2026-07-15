# SPEC-007 — Annexe C

# Diagnostics PRO (Procédé)

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette annexe définit les diagnostics de la famille **PRO**.

Les diagnostics PRO détectent un dysfonctionnement réel du procédé de filtration ou du chauffage solaire.

Ils sont évalués uniquement lorsque les mesures sont valides (MES) et cohérentes (COH).

---

# 2. Principes

Les diagnostics PRO :

* caractérisent une anomalie réelle de fonctionnement ;
* peuvent entraîner un passage en **SECURISATION** ou **DEFAUT** ;
* utilisent uniquement des mesures validées ;
* ne concluent jamais à une défaillance de capteur.

Les conditions normales de fonctionnement du chauffage solaire sont définies dans la **SPEC-008**.

---

# 3. Diagnostics

| Identifiant | Diagnostic                         | Niveau   |
| ----------- | ---------------------------------- | -------- |
| PRO-001     | Débit critique                     | CRITIQUE |
| PRO-002     | Débit insuffisant prolongé         | DÉGRADÉ  |
| PRO-003     | Protection du serpentin impossible | CRITIQUE |

---

# 4. Diagnostics détaillés

---

## PRO-001 — Débit critique

### Objet

Détecter une circulation d'eau insuffisante pour garantir la sécurité hydraulique.

### Condition d'activation

Le débit est inférieur au débit critique configuré pendant une durée supérieure au délai de validation.

### Classe

PRO

### Niveau

**CRITIQUE**

### Réarmement

Temporisé.

### Conséquences

Le contrôleur demande un passage en **DEFAUT** conformément à la **SPEC-005**.

---

## PRO-002 — Débit insuffisant prolongé

### Objet

Détecter une perte durable de performance hydraulique.

### Condition d'activation

Le débit reste inférieur au débit nominal configuré tout en restant supérieur au débit critique, pendant une durée supérieure au délai de validation.

### Classe

PRO

### Niveau

**DÉGRADÉ**

### Réarmement

Temporisé.

### Conséquences

Le contrôleur demande un passage en **SECURISATION**.

Le fonctionnement dégradé est défini dans la **SPEC-003**.

---

## PRO-003 — Protection du serpentin impossible

### Objet

Détecter l'impossibilité d'assurer la protection thermique du serpentin lorsqu'elle est requise.

### Condition d'activation

Les conditions de protection définies dans la **SPEC-008** nécessitent une circulation d'eau mais celle-ci ne peut pas être assurée.

Exemples :

* débit critique ;
* impossibilité de démarrer la pompe ;
* protections volontairement désactivées en mode OFF.

### Classe

PRO

### Niveau

**CRITIQUE**

### Réarmement

Automatique lorsque les conditions permettant la protection redeviennent satisfaisantes.

### Conséquences

Le contrôleur demande un passage en **DEFAUT**.

Une notification utilisateur est obligatoire.

---

# 5. Critères d'acceptation

La famille PRO est conforme lorsque :

* tous les diagnostics utilisent uniquement des mesures validées par MES et COH ;
* chaque diagnostic décrit une anomalie réelle du procédé ;
* chaque diagnostic possède un identifiant unique ;
* chaque diagnostic possède un niveau unique ;
* les conséquences sont appliquées par la machine à états conformément à la **SPEC-005**.

---

# 6. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
