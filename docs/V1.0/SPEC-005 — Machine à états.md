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

La machine à états décrit uniquement le fonctionnement interne du contrôleur.

Elle ne prend aucune décision métier.

Elle exécute les demandes de transition provenant des diagnostics définis dans la SPEC-007.

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

## DÉFAUT BLOQUANT

État atteint lorsqu'un défaut critique interdit tout fonctionnement.

Actions :

* arrêt de la pompe ;
* journalisation ;
* attente de disparition du défaut.

Le retour s'effectue par INITIALISATION.

L'état DÉFAUT BLOQUANT est exclusivement déclenché par la SPEC-007.

Le mode de fonctionnement n'est jamais modifié.

Lorsque le défaut disparaît, la machine retourne à INITIALISATION.

Le contrôleur reprend ensuite son fonctionnement en conservant le mode de fonctionnement sélectionné.

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
                        │
                        ▼
                    ATTENTE

Tous les états
      │
      ▼
 DÉFAUT BLOQUANT
      │
      ▼
 INITIALISATION
 ```

---

# 6. Transitions

| État courant           | Condition                         | État suivant           |
| ---------------------- | --------------------------------- | ---------------------- |
| INITIALISATION         | Contrôleur prêt                   | ATTENTE                |
| ATTENTE                | Filtration demmandée              | FILTRATION             |
| FILTRATION             | Plus aucune demande de filtration | ATTENTE                |
| Tous les états         | Défaut bloquant                   | DÉFAUT BLOQUANT        |
| DÉFAUT BLOQUANT        | Défaut disparu                    | INITIALISATION         |

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

# 8. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
