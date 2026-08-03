# SPEC-002 — Interface utilisateur

**Version :** 1.0  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit les informations, commandes et paramètres accessibles à l'utilisateur. Elle ne décrit aucun comportement interne.

# 2. Principes

* L'utilisateur ne commande jamais directement le matériel.
* Une information affichée provient de son entité PCHA de référence.
* Une commande utilisateur agit uniquement sur un helper prévu à cet effet.

# 3. Informations affichées

| Zone | Informations principales |
|---|---|
| État général | Mode, état de la machine, niveau de fonctionnement, diagnostics actifs |
| Filtration | État de filtration, débit, objectif quotidien, temps réalisé, temps restant, puissance, énergie quotidienne |
| Piscine | Température brute, température validée après circulation, correction, consigne, minimum et maximum du jour |
| Chauffage solaire | Demande solaire, chauffage actif, luminosité, seuil, protection du serpentin, temps quotidien au-dessus du seuil et luminosité moyenne associée |
| Environnement | Température extérieure, luminosité |
| Traitement | Mode actif, durée configurée, temps restant |
| Historique | Événements et notifications |

Les durées de l’objectif quotidien, du temps réalisé et du temps restant sont présentées dans le tableau de bord au format `03H56`. La carte affiche également `Atteint à : HHhMM`, correspondant à l’heure prévisionnelle d’achèvement de l’objectif selon l’état courant et la planification définie par la SPEC-003.

# 4. Commandes utilisateur

L'utilisateur peut :

* sélectionner le mode défini dans la SPEC-006 ;
* modifier les paramètres déclarés dans la SPEC-004 ;
* acquitter les alarmes ;
* consulter l'historique.

# 5. Paramètres modifiables

Les paramètres modifiables sont exclusivement les helpers configurables déclarés dans la SPEC-004.

# 6. Références

* SPEC-003 — Gestion de la filtration
* SPEC-004 — Couche d'abstraction et configuration
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
* SPEC-009 — Journalisation et notifications
