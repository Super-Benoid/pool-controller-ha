# SPEC-005 — Machine à états

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit la machine à états du Pool Controller.

Elle décrit :

* les états autorisés ;
* les transitions entre états ;
* les règles de priorité.

Les actions exécutées dans chaque état sont définies dans les spécifications fonctionnelles correspondantes.

---

# 2. Principes

Le Pool Controller est piloté par une unique machine à états.

À tout instant :

* un seul état est actif ;
* une seule transition est autorisée ;
* toutes les décisions transitent par cette machine.

Les principes généraux sont définis dans la **SPEC-000**.

---

# 3. États

La V1 comporte exclusivement les états suivants.

| État          | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| OFF           | Installation arrêtée à la demande de l'utilisateur.            |
| AUTO          | Fonctionnement automatique normal.                             |
| TRAITEMENT    | Fonctionnement imposé pour un traitement de l'eau.             |
| MARCHE_FORCÉE | Fonctionnement imposé par l'utilisateur.                       |
| SECURISATION  | Fonctionnement dégradé permettant de protéger les équipements. |
| DEFAUT        | Arrêt de sécurité de l'installation.                           |

Aucun autre état n'est autorisé.

---

# 4. Diagramme des transitions

```text
                    OFF
                     │
                     ▼
                    AUTO
                  ↙  │  ↘
                 ▼   ▼   ▼
       TRAITEMENT   MARCHE_FORCÉE
                 ↘   │   ↙
                     ▼
               SECURISATION
                     │
                     ▼
                  DEFAUT
```

Toutes les transitions ne sont pas nécessairement autorisées.

Les conditions sont définies ci-dessous.

---

# 5. Transitions autorisées

| Depuis        | Vers          | Condition                                        |
| ------------- | ------------- | ------------------------------------------------ |
| OFF           | AUTO          | Activation du fonctionnement automatique         |
| OFF           | SECURISATION  | Désactiver les sécurités en mode OFF = Faux      |
| AUTO          | OFF           | Arrêt demandé par l'utilisateur                  |
| AUTO          | TRAITEMENT    | Sélection du mode Traitement                     |
| AUTO          | MARCHE_FORCÉE | Sélection du mode Marche forcée                  |
| TRAITEMENT    | AUTO          | Fin ou annulation du traitement                  |
| MARCHE_FORCÉE | AUTO          | Fin ou annulation de la marche forcée            |
| AUTO          | SECURISATION  | Diagnostic de niveau DÉGRADÉ                     |
| TRAITEMENT    | SECURISATION  | Diagnostic de niveau DÉGRADÉ                     |
| MARCHE_FORCÉE | SECURISATION  | Diagnostic de niveau DÉGRADÉ                     |
| SECURISATION  | AUTO          | Disparition du diagnostic et réarmement autorisé |
| Tout état     | DEFAUT        | Diagnostic de niveau CRITIQUE                    |
| DEFAUT        | AUTO          | Réarmement conforme à la SPEC-007                |

Les règles de diagnostic sont définies dans la **SPEC-007**.

---

# 6. Priorités

Lorsque plusieurs événements sont simultanément présents, les priorités suivantes s'appliquent.

| Priorité | État          |
| -------: | ------------- |
|        1 | DEFAUT        |
|        2 | SECURISATION  |
|        3 | MARCHE_FORCÉE |
|        4 | TRAITEMENT    |
|        5 | AUTO          |
|        6 | OFF           |

L'état de priorité la plus élevée est toujours retenu.

---

# 7. Responsabilités

La machine à états :

* détermine l'état courant ;
* autorise ou refuse les transitions ;
* applique les priorités ;
* transmet les autorisations aux modules fonctionnels.

Elle ne pilote jamais directement les équipements.

Les scripts d'action sont définis dans la **SPEC-004**.

---

# 8. Comportement des états

Chaque état autorise un ensemble de fonctions.

Le détail de ces fonctions est défini dans les spécifications correspondantes :

* filtration : **SPEC-003** ;
* modes utilisateur : **SPEC-006** ;
* diagnostics : **SPEC-007** ;
* chauffage solaire : **SPEC-008**.

La présente spécification ne décrit que les transitions d'état.

---

# 9. Journalisation

Chaque transition d'état doit être enregistrée conformément à la **SPEC-009**.

Les informations minimales sont :

* état précédent ;
* état suivant ;
* date et heure ;
* motif de la transition ;
* identifiant du diagnostic ou de la commande utilisateur.

---

# 10. Critères d'acceptation

La machine à états est conforme lorsque :

* un seul état est actif à tout instant ;
* seules les transitions autorisées sont possibles ;
* les priorités sont toujours respectées ;
* toutes les transitions sont journalisées ;
* aucune décision métier ne contourne la machine à états.

---

# 11. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Modèle Home Assistant
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
