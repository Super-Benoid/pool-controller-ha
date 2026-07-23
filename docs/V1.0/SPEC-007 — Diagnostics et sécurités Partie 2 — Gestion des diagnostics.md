# SPEC-007 — Diagnostics et sécurités

## Partie 2 — Gestion des diagnostics

**Projet :** Pool Controller HA

**Version :** V1.0

**Statut :** GELÉE (Frozen Specification)

---

# 10. Activation d'un diagnostic

Un diagnostic devient actif lorsque les conditions définies dans son annexe sont satisfaites.

Chaque diagnostic est évalué indépendamment.

Plusieurs diagnostics peuvent être actifs simultanément.

L'ensemble des diagnostics actifs représente l'état sanitaire de l'installation.

---

# 11. Désactivation d'un diagnostic

Un diagnostic disparaît uniquement lorsque sa condition d'activation n'est plus présente et que son mode de réarmement est satisfait.

La disparition d'un diagnostic ne provoque pas automatiquement un changement d'état.

La machine à états réévalue systématiquement la situation conformément à la **SPEC-005**.

---

# 12. Réarmement

Chaque diagnostic possède un mode de réarmement unique.

Les modes autorisés sont :

| Mode            | Description                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------ |
| **Automatique** | Le diagnostic disparaît immédiatement lorsque la condition n'est plus présente.                  |
| **Temporisé**   | La condition doit rester absente pendant une durée configurable avant disparition du diagnostic. |
| **MARCHE FORCÉE**      | Une action volontaire de l'utilisateur est nécessaire.                                           |

Le mode de réarmement est défini individuellement dans chaque diagnostic.

Les temporisations sont configurables depuis Home Assistant conformément à la **SPEC-004**.

---

# 13. Conséquences

Un diagnostic peut uniquement provoquer les actions suivantes :

* génération d'un événement de diagnostic ;
* passage du niveau NORMAL à DÉGRADÉ ;
* demande de transition vers **DÉFAUT BLOQUANT** ;
* génération d'une notification ;
* journalisation.

Les décisions opérationnelles restent exclusivement du ressort :

* de la machine à états (**SPEC-005**) ;
* des fonctions métier (**SPEC-003** et **SPEC-008**).

---

# 14. Priorité des diagnostics

Lorsque plusieurs diagnostics sont actifs simultanément :

* le niveau **CRITIQUE** est prioritaire sur le niveau **DÉGRADÉ** ;
* le niveau **DÉGRADÉ** est prioritaire sur le niveau **INFORMATIF**.

Les priorités entre états sont définies dans la **SPEC-005**.

---

# 15. Journalisation

Chaque changement d'état d'un diagnostic est enregistré.

Les informations minimales sont :

* identifiant du diagnostic ;
* famille (MES, COH ou PRO) ;
* niveau ;
* état (activation ou disparition) ;
* date et heure ;
* motif du changement.

Le format des journaux est défini dans la **SPEC-009**.

---

# 16. Notifications

Les notifications utilisateur sont générées selon le niveau du diagnostic.

| Niveau     | Notification |
| ---------- | ------------ |
| INFORMATIF | Optionnelle  |
| DÉGRADÉ    | Recommandée  |
| CRITIQUE   | Obligatoire  |

Le contenu et le canal de notification sont définis dans la **SPEC-009**.

---

# 17. Niveau de fonctionnement

* NORMAL, les diagnostiques n'ont révélé aucun defaut
* DEGRADE, les diagnostiques ont révélé un defaut non critique
* BLOQUE, les diagnostiques ont révélé un defaut critique

---

# 17. Critères d'acceptation

Le système de diagnostic est conforme lorsque :

* chaque diagnostic appartient à une seule famille ;
* chaque diagnostic possède un seul niveau de gravité ;
* chaque diagnostic possède un seul mode de réarmement ;
* les transitions demandées respectent la **SPEC-005** ;
* tous les changements de diagnostic sont journalisés ;
* les notifications sont générées conformément à leur niveau de gravité.

---

# 18. Références

* SPEC-000 — Architecture générale
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation
