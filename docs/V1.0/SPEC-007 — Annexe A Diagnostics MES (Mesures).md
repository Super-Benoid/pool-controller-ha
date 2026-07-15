# SPEC-007 — Annexe A

# Diagnostics MES (Mesures)

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette annexe définit les diagnostics de la famille **MES**.

Les diagnostics MES vérifient exclusivement que les mesures nécessaires au fonctionnement du Pool Controller sont disponibles et exploitables.

Ils ne vérifient ni leur cohérence ni le fonctionnement de l'installation.

---

# 2. Principes

Les diagnostics MES sont évalués en premier.

Ils constituent le premier niveau de validation de la chaîne de diagnostic définie dans la **SPEC-007**.

Un diagnostic MES devient actif lorsqu'une mesure :

* est indisponible ;
* est invalide ;
* n'est plus actualisée ;
* ne peut plus être utilisée de manière fiable.

Lorsqu'un diagnostic MES est actif, les diagnostics COH et PRO dépendant de cette mesure ne sont plus évalués.

---

# 3. Mesures surveillées

Seules les mesures indispensables au fonctionnement automatique sont surveillées.

| Identifiant | Mesure                           | Classe        |
| ----------- | -------------------------------- | ------------- |
| MES-001     | Température d'eau                | Critique      |
| MES-002     | Débit hydraulique                | Critique      |
| MES-003     | Puissance électrique de la pompe | Fonctionnelle |
| MES-004     | Luminosité                       | Fonctionnelle |

Les autres mesures ne génèrent aucun diagnostic MES.

---

# 4. Mesures non surveillées

Les mesures suivantes sont considérées comme des mesures de supervision :

* température extérieure ;
* énergie électrique consommée ;
* statistiques de fonctionnement ;
* données destinées uniquement aux tableaux de bord.

Leur absence ne modifie pas le comportement du Pool Controller.

---

# 5. Diagnostics

---

## MES-001 — Température d'eau indisponible

### Objet

Détecter l'absence d'une mesure exploitable de la température d'eau.

### Condition d'activation

La température d'eau est absente, invalide ou indisponible.

### Classe

MES

### Niveau

**DÉGRADÉ**

### Réarmement

Automatique.

### Conséquences

Le calcul normal de la filtration n'est plus possible.

Le contrôleur applique le comportement dégradé défini dans la **SPEC-003**.

---

## MES-002 — Débit hydraulique indisponible

### Objet

Détecter l'absence d'une mesure fiable du débit.

### Condition d'activation

La mesure de débit est absente, invalide ou indisponible.

### Classe

MES

### Niveau

**CRITIQUE**

### Réarmement

Temporisé.

Le temps de validation est configurable.

### Conséquences

Le contrôleur ne peut plus garantir la sécurité hydraulique.

La machine à états applique les règles définies dans la **SPEC-005**.

Les fonctions de protection sont définies dans la **SPEC-008**.

---

## MES-003 — Puissance électrique de la pompe indisponible

### Objet

Détecter l'absence de la mesure de puissance instantanée.

### Condition d'activation

La mesure de puissance est absente, invalide ou indisponible.

### Classe

MES

### Niveau

**DÉGRADÉ**

### Réarmement

Temporisé.

Le temps de validation est configurable.

### Conséquences

Les diagnostics utilisant cette mesure ne sont plus évalués.

Le contrôleur applique les règles de fonctionnement dégradé définies dans les annexes COH et PRO.

---

## MES-004 — Luminosité indisponible

### Objet

Détecter l'absence du capteur de luminosité.

### Condition d'activation

La mesure de luminosité est absente, invalide ou indisponible.

### Classe

MES

### Niveau

**DÉGRADÉ**

### Réarmement

Automatique.

### Conséquences

Le chauffage solaire applique la stratégie de repli définie dans la **SPEC-008**.

La filtration automatique reste assurée.

---

# 6. Critères d'acceptation

La famille MES est conforme lorsque :

* seules les mesures indispensables sont surveillées ;
* chaque diagnostic possède un identifiant unique ;
* chaque diagnostic possède un niveau unique ;
* chaque diagnostic possède un mode de réarmement unique ;
* les conséquences sont définies par les spécifications fonctionnelles concernées.

---

# 7. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
