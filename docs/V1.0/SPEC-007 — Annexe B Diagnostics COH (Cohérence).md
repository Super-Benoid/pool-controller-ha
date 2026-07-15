# SPEC-007 — Annexe B

# Diagnostics COH (Cohérence)

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette annexe définit les diagnostics de la famille **COH**.

Les diagnostics COH vérifient la cohérence des mesures entre elles.

Ils permettent de détecter un capteur probablement défaillant ou une information incohérente avant d'analyser le fonctionnement réel de l'installation.

---

# 2. Principes

Les diagnostics COH sont évalués uniquement lorsque tous les diagnostics MES nécessaires sont validés.

Ils ne concluent jamais à un défaut de procédé.

Ils détectent uniquement une incohérence entre plusieurs informations disponibles.

---

# 3. Diagnostics

| Identifiant | Diagnostic                                                   | Niveau  |
| ----------- | ------------------------------------------------------------ | ------- |
| COH-001     | Débit incohérent avec la puissance de la pompe               | DÉGRADÉ |
| COH-002     | Débit anormalement faible malgré une pompe en fonctionnement | DÉGRADÉ |
| COH-003     | Température d'eau incohérente                                | DÉGRADÉ |

---

# 4. Diagnostics détaillés

---

## COH-001 — Débit incohérent avec la puissance de la pompe

### Objet

Détecter une incohérence entre le débit hydraulique mesuré et la consommation électrique de la pompe.

### Condition d'activation

La puissance électrique indique une pompe en fonctionnement alors que le débit mesuré est incompatible avec ce fonctionnement.

Le seuil de cohérence est défini dans les paramètres de configuration.

### Classe

COH

### Niveau

**DÉGRADÉ**

### Réarmement

Temporisé.

Le délai est configurable.

### Conséquences

Le contrôleur considère qu'au moins une des deux mesures est probablement erronée.

Les fonctions dépendantes utilisent le comportement dégradé défini dans les spécifications concernées.

---

## COH-002 — Débit anormalement faible malgré une pompe en fonctionnement

### Objet

Détecter une perte importante de débit sans conclure immédiatement à une panne de la pompe.

### Condition d'activation

La pompe est détectée en fonctionnement.

Le débit reste inférieur au seuil minimal configuré pendant une durée supérieure au délai de validation.

Cette situation peut notamment correspondre :

* à un filtre fortement encrassé ;
* à une prise d'air ;
* à un début de désamorçage ;
* à un tuyau partiellement obstrué.

### Classe

COH

### Niveau

**DÉGRADÉ**

### Réarmement

Temporisé.

### Conséquences

Le contrôleur demande un fonctionnement dégradé.

Les protections hydrauliques restent assurées conformément à la **SPEC-008**.

---

## COH-003 — Température d'eau incohérente

### Objet

Détecter une mesure de température probablement erronée.

### Condition d'activation

La température d'eau évolue d'une manière physiquement incompatible avec le fonctionnement normal de l'installation.

Les critères de validation sont définis par l'algorithme d'implémentation.

### Classe

COH

### Niveau

**DÉGRADÉ**

### Réarmement

Automatique.

### Conséquences

La température est considérée comme non fiable.

Le contrôleur applique le comportement dégradé défini dans la **SPEC-003** et la **SPEC-008**.

---

# 5. Critères d'acceptation

La famille COH est conforme lorsque :

* tous les diagnostics utilisent uniquement des mesures validées par la famille MES ;
* aucun diagnostic COH ne conclut à une panne matérielle ;
* chaque diagnostic possède un identifiant unique ;
* chaque diagnostic possède un niveau unique ;
* les comportements associés sont définis dans les spécifications fonctionnelles.

---

# 6. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
