# SPEC-007 — Diagnostics et sécurités

## Partie 1 — Architecture des diagnostics

**Projet :** Pool Controller HA

**Version :** V1.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit l'architecture du système de diagnostic du Pool Controller.

Elle décrit :

* l'organisation des diagnostics ;
* la classification des mesures ;
* les niveaux de gravité ;
* la chaîne de décision.

Le détail des diagnostics est défini dans les annexes de cette spécification.

---

# 2. Principes

Le système de diagnostic a pour objectifs de :

* détecter les anomalies de fonctionnement ;
* protéger les équipements ;
* maintenir le fonctionnement lorsque cela reste compatible avec la sécurité ;
* garantir un comportement déterministe ;
* assurer la traçabilité des événements.

Les diagnostics sont évalués en permanence pendant le fonctionnement du contrôleur.

---

# 3. Classification des mesures

Toutes les mesures utilisées par le Pool Controller sont classées selon leur importance fonctionnelle.

Cette classification détermine si une mesure fait l'objet d'un diagnostic MES.

| Classe            | Description                                                                              | Diagnostic MES |
| ----------------- | ---------------------------------------------------------------------------------------- | -------------- |
| **Critique**      | Mesure indispensable à la sécurité ou au fonctionnement automatique.                     | Oui            |
| **Fonctionnelle** | Mesure nécessaire à une fonction du système sans impact direct sur la sécurité.          | Oui            |
| **Supervision**   | Mesure utilisée uniquement pour l'information, les statistiques ou les tableaux de bord. | Non            |

Seules les mesures des classes **Critique** et **Fonctionnelle** sont surveillées par le système de diagnostic.

Les mesures de **Supervision** ne génèrent jamais de diagnostic.

---

# 4. Architecture des diagnostics

Les diagnostics sont organisés en trois familles.

| Famille | Rôle                               |
| ------- | ---------------------------------- |
| **MES** | Validation des mesures             |
| **COH** | Vérification de cohérence          |
| **PRO** | Détection des anomalies de procédé |

Chaque diagnostic appartient à une seule famille.

Les familles sont évaluées dans un ordre fixe.

---

# 5. Chaîne de décision

Les diagnostics sont évalués selon la séquence suivante :

```text
Mesures
    │
    ▼
MES
    │
    ▼
COH
    │
    ▼
PRO
    │
    ▼
Niveau de gravité
    │
    ▼
Machine à états
```

Une famille n'est évaluée que si les familles précédentes sont validées.

Ainsi :

* un diagnostic COH n'est évalué que si les mesures nécessaires sont valides ;
* un diagnostic PRO n'est évalué que si les diagnostics MES et COH ne bloquent pas son analyse.

Cette organisation garantit un comportement déterministe.

---

# 6. Niveaux de gravité

Chaque diagnostic possède un niveau unique.

| Niveau         | Conséquence                                                  |
| -------------- | ------------------------------------------------------------ |
| **INFORMATIF** | Journalisation uniquement.                                   |
| **DÉGRADÉ**    | Passage au niveau de fonctionnement **DÉGRADÉ**.             |
| **CRITIQUE**   | Demande de transition vers **DÉFAUT BLOQUANT** (SPEC-005)    |

Les transitions d'état sont réalisées conformément à la **SPEC-005**.

---

# 7. Principes de fonctionnement

Le système de diagnostic applique les règles suivantes :

* un diagnostic ne peut appartenir qu'à une seule famille ;
* un diagnostic ne possède qu'un seul niveau de gravité ;
* un diagnostic ne possède qu'une seule stratégie de réarmement ;
* plusieurs diagnostics peuvent être actifs simultanément ;
* la machine à états applique toujours la conséquence correspondant au niveau de gravité le plus élevé.

Les diagnostics ne modifient jamais le mode de fonctionnement.

Ils déterminent uniquement :

- le niveau de fonctionnement ;

ou

- une demande de transition vers DÉFAUT BLOQUANT.

---

# 8. Organisation documentaire

Les diagnostics détaillés sont définis dans les annexes suivantes :

* **Annexe A** — Diagnostics MES ;
* **Annexe B** — Diagnostics COH ;
* **Annexe C** — Diagnostics PRO.

La présente spécification décrit uniquement leur architecture commune.

---

# 9. Références

* SPEC-000 — Architecture générale
* SPEC-005 — Machine à états
* SPEC-009 — Journalisation
