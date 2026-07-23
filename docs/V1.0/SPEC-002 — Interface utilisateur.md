# SPEC-002 — Interface utilisateur

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette SPEC définit l'ensemble des interactions entre l'utilisateur et le Pool Controller Home Assistant (PCHA).

Elle décrit exclusivement :

* les informations visibles ;
* les commandes disponibles ;
* les paramètres configurables.

Elle ne décrit aucun comportement interne du contrôleur.

---

# 2. Philosophie

L'utilisateur pilote le contrôleur au travers de fonctions métier.

Il ne manipule jamais directement les équipements physiques.

Le tableau de bord présente uniquement des informations utiles à l'exploitation de la piscine.

---

# 3. Tableau de bord

Le tableau de bord est organisé en zones.

| Zone du tableau de bord   | Paramètre                         | Modifiable | 
| ------------------------- | --------------------------------- | ---------- |
| État général              | Mode de fonctionnement            | OUI        |
|                           | État du contrôleur                | NON        |
|                           | Présence d'un défaut              | NON        |
|                           | Chauffage solaire actif / inactif | NON        |
|                           | Filtration active / inactive      | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Filtration                | Filtration active                 | NON        |
|                           | Débit instantané                  | NON        |
|                           | Temps de filtration réalisé       | NON        |
|                           | Temps de filtration restant       | NON        |
|                           | Puissance instantanée             | NON        |
|                           | Énergie consommée                 | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Piscine                   | Température actuel de l'eau       | NON        |
|                           | Température de consigne de l'eau  | OUI        |
|                           | Température minimale de l'eau     | NON        |
|                           | Température maximale de l'eau     | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Chauffage solaire         | Chauffage solaire actif           | NON        |
|                           | Seuil de luminosité               | OUI        |
|                           | Temps de chauffage solaire        | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Environnement             | Température extérieure            | NON        |
|                           | Luminosité                        | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Paramètres                | Temps marche pompe minimal        | OUI        |
|                           | Temps arrêt pompe minimal         | OUI        |
|                           | Temps validation temp piscine     | OUI        |
|                           | Durée du traitement               | OUI        |
| ------------------------- | --------------------------------- | ---------- |
| Diagnostics               | Alarmes actives                   | NON        |
|                           | Défauts actifs                    | NON        |
|                           | État des sécurités                | NON        |
| ------------------------- | --------------------------------- | ---------- |
| Historique                | Journal des événements            | NON        |
|                           | Historique des alarmes            | NON        |
| ------------------------- | --------------------------------- | ---------- |


# 5. Actions utilisateur

L'utilisateur peut :

* modifier le mode de fonctionnement ;
* modifier les consignes autorisées ;
* acquitter une alarme (si applicable) ;
* consulter l'historique.

Aucune commande ne permet de piloter directement les équipements physiques.

---

# 9. Références

* SPEC-000 — Principes généraux
* SPEC-003 — Filtration
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics
* SPEC-008 — Chauffage solaire
* ARCHITECTURE.md
* CONVENTIONS.md
