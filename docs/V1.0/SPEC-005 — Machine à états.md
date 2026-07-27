# SPEC-005 — Machine à états

Version : 1.0
Statut : Figée

# 1. Objet

Cette SPEC définit la machine à états du Pool Controller Home Assistant (PCHA).

Elle décrit :

* les états de fonctionnement ;
* les transitions entre états ;
* les conditions d'entrée ;
* les conditions de sortie.

Les règles métier restent définies dans les autres SPEC.

La présente SPEC décrit uniquement les états internes du contrôleur.

Elle ne décrit ni les modes de fonctionnement (SPEC-006), ni les diagnostics (SPEC-007).

---

# 2. Philosophie

La machine à états décrit exclusivement
le fonctionnement interne du contrôleur.

Elle ne prend jamais en compte
le niveau de diagnostic.

Les défauts sont exclusivement
gérés par la SPEC-007.

---

# 3. États de fonctionnement

Le contrôleur possède les états suivants.

## INITIALISATION

Premier état après le démarrage de Home Assistant.

Actions :

* lecture des Helpers ;
* lecture des entités PCHA ;
* vérification de cohérence ;
* calcul de l'objectif quotidien.

Sortie :

→ ATTENTE

---

## ATTENTE

État de repos.

La pompe est arrêtée.

Le contrôleur attend une demande de fonctionnement.

---

## FILTRATION

La Pompe est en fonctionnement.

L'état FILTRATION peut être demandé par plusieurs mécanismes indépendants :

- mode AUTO (SPEC-003) ;
- mode TRAITEMENT (SPEC-006) ;
- mode MARCHE FORCÉE (SPEC-006) ;
- décisions des diagnostics (SPEC-007).

La machine à états ne distingue pas l'origine de la demande.

Elle ne fait qu'exécuter la transition vers l'état FILTRATION.

---

# 4. Niveau de fonctionnement

Le niveau de fonctionnement n'est pas un état de la machine.

Il est déterminé exclusivement par la SPEC-007.

---

# 5. Diagramme de principe

```text
                 INITIALISATION
                        │
                        ▼
                    ATTENTE
                        │
                        ▼
                   FILTRATION
 ```

---

# 6. Transitions

| État courant           | Condition                         | État suivant           |
| ---------------------- | --------------------------------- | ---------------------- |
| INITIALISATION         | Contrôleur prêt                   | ATTENTE                |
| ATTENTE                | Filtration demmandée              | FILTRATION             |
| FILTRATION             | Plus aucune demande de filtration | ATTENTE                |

Les transitions peuvent être provoquées :

- par les règles fonctionnelles (SPEC-003) ;
- par le mode de fonctionnement (SPEC-006) ;
- par les diagnostics (SPEC-007).

---

# 7. Contraintes

Un seul état est actif à un instant donné.

Le mode dégradé peut coexister avec n'importe quel état de fonctionnement.

Les modes de fonctionnement (OFF, SÉCURISATION, AUTO, TRAITEMENT, MARCHE FORCÉE) ne font pas partie de la machine à états.

Ils autorisent ou interdisent certaines transitions conformément à la SPEC-006.

---

# 8. Script

| Événement                                         | Origine        | Script appelé              |
| ------------------------------------------------- | -------------- | -------------------------- |
| Démarrage HA                                      | Home Assistant | `pcha_machine_initialiser` |
| Changement de mode                                | input_select   | `pcha_machine_reevaluer`   |
| Fin du traitement                                 | timer          | `pcha_machine_reevaluer`   |
| Diagnostic modifié                                | SPEC-007       | `pcha_machine_reevaluer`   |
| **binary_sensor.pcha_filtration_requise modifié** | **SPEC-003**   | **pcha_machine_reevaluer** |

La machine est composée des scripts suivants :

- pcha_machine_initialiser

- pcha_machine_reevaluer

- pcha_machine_attente

- pcha_machine_filtration

pcha_machine_reevaluer
est l'unique script autorisé à décider
des transitions de la machine.

Les autres scripts appliquent uniquement
le changement d'état demandé.

---

# 9. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire

# MACH-001

La machine à états décrit uniquement
ce que fait le contrôleur.

Le niveau de fonctionnement décrit
uniquement ce qu'il est autorisé
à faire.

Ces deux informations sont indépendantes
et ne doivent jamais être fusionnées
dans une même variable d'état.