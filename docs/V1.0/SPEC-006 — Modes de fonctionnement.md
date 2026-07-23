# SPEC-006 — Modes de fonctionnement

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette SPEC définit les différents modes de fonctionnement du Pool Controller Home Assistant (PCHA).

Un seul mode est actif à un instant donné.

Les modes définissent les autorisations de fonctionnement du contrôleur.

---

# 2. Modes disponibles

Le contrôleur possède 5 modes de fonctionnement commandé par l'utilisateur:

| Mode         | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| OFF          | Arrêt absolu du contrôleur.                                         |
| SÉCURISATION | Fonctionnement normal arrêté. Seules les sécurités restent actives. |
| AUTO         | Fonctionnement normal en continu.                                 |
| TRAITEMENT   | Fonctionnement forcé temporisé.
| MARCHE FORCÉE| Fonctionnement forcé en continu.                          |

---

# 3. Mode OFF

## Objectif

Garantir qu'aucun équipement ne puisse démarrer automatiquement.

Ce mode est destiné :

* aux opérations de maintenance ;
* aux interventions sur l'installation ;
* à toute situation nécessitant un arrêt total.

La sécurité des personnes est prioritaire sur la protection du matériel.

---

## Fonctionnement

Lorsque le mode OFF est sélectionné :

* aucune filtration automatique n'est autorisée ;
* aucun chauffage solaire n'est autorisé ;
* aucune temporisation ne peut provoquer un démarrage ;
* aucune sécurité ne peut provoquer un démarrage ;
* aucune reprise automatique n'est autorisée.

Le contrôleur ne réalise aucune action automatique.

---

## Autorisations

Sont uniquement autorisés :

* le changement de mode ;
* la consultation des informations ;
* la modification des paramètres.

---

# 4. Mode SÉCURISATION

## Objectif

Protéger l'installation sans assurer le fonctionnement normal de la piscine.

Ce mode est destiné :

* aux périodes d'hivernage partiel ;
* aux essais ;
* aux absences prolongées ;
* à toute situation où la filtration normale est volontairement arrêtée mais où les protections doivent rester actives.

---

## Fonctionnement

Dans ce mode :

* la filtration programmée est désactivée ;
* le chauffage solaire est désactivé ;
* les protections définies dans les SPEC restent autorisées.

Exemples :

* protection manque d'eau ;
* protection débit ;
* protection antigel (version future).

Les protections sont détaillées dans les SPEC correspondantes.

---

# 5. Mode AUTO

## Objectif

Assurer le fonctionnement normal de la piscine.

Dans ce mode :

* la filtration est entièrement automatique ;
* le chauffage solaire est géré automatiquement conformément à la SPEC-008 ;
* les diagnostics sont actifs ;
* les sécurités sont actives.

Toutes les décisions sont prises par la machine à états.

---

# 6. Mode TRAITEMMENT

## Objectif

Permettre à l'utilisateur de programmmer un temps de fonctionnement de la filtration en continue pour réaliser correctement un traitement de l'eau.

Dans ce mode :

* la filtration fonctionne de façon continue jusqu'à la fin de la temporisation;
* A la fin de la temporisation, le mode passe en AUTO;
* les diagnostics sont actifs ;
* les sécurités sont actives.

---

# 7. Mode MARCHE FORCÉE

## Objectif

Permettre à l'utilisateur de commander directement les fonctions principales.

Dans ce mode :

* les commandes utilisateur sont prioritaires ;
* les sécurités restent actives ;
* les diagnostics restent actifs.

Les automatismes de confort sont suspendus.

---

# 8. Changement de mode

Le changement de mode est immédiat.

Le contrôleur applique instantanément les règles du nouveau mode.

Les temporisations incompatibles avec le nouveau mode sont annulées.

---

# 9. Priorité des modes

Les modes sont exclusifs.

Un seul mode peut être actif.

Ordre de priorité :

1. OFF
2. SÉCURISATION
3. MARCHE FORCÉE
4. TRAITEMENT
5. AUTO

En cas de conflit, le mode ayant la priorité la plus élevée est appliqué.

---

# 10. Interaction avec la machine à états

La machine à états adapte son comportement en fonction du mode sélectionné.

* OFF : aucun état actif.
* SÉCURISATION : uniquement les états liés aux protections.
* AUTO : fonctionnement normal.
* TRAITEMENT : fonctionnement temporisé.
* MARCHE FORCÉE : fonctionnement en continu.

Les états sont définis dans la SPEC-005.

---

# 11. Interaction avec le chauffage solaire

Le chauffage solaire n'est jamais considéré comme une fonction indépendante.

Une période de chauffage est toujours une période de filtration. Elle est seulement réaliser lors de conditions climatiques favorable au réchauffement de l'eau. 

---

# 12. Influence des diagnostics

Les diagnostics ne modifient jamais le mode de fonctionnement.

Ils peuvent uniquement provoquer une transition de la machine vers l'état DÉFAUT BLOQUANT conformément à la SPEC-005.

Lorsque le défaut disparaît, le mode de fonctionnement reste inchangé.

---

# 13. Références

* SPEC-000 — Principes généraux
* SPEC-003 — Filtration
* SPEC-005 — Machine à états
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
