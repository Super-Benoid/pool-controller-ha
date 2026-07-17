# SPEC-008 — Chauffage solaire

**Projet :** Pool Controller HA

**Version :** V1.0.0

**Statut :** GELÉE (Frozen Specification)

---

# 1. Objet

Cette spécification définit le fonctionnement du chauffage solaire.

Elle décrit :

* les conditions d'autorisation du chauffage ;
* la protection du serpentin ;
* le comportement dans les différents modes utilisateur ;
* les stratégies de fonctionnement dégradé.

Les diagnostics associés sont définis dans la **SPEC-007**.

---

# 2. Principes

Le chauffage solaire utilise exclusivement l'énergie solaire disponible.

Le contrôleur :

* optimise le chauffage de l'eau ;
* protège le serpentin contre la surchauffe ;
* respecte les priorités de sécurité définies par la machine à états.

---

# 3. Conditions d'autorisation

Le chauffage solaire est autorisé uniquement lorsque toutes les conditions suivantes sont satisfaites :

* le mode utilisateur autorise le chauffage ;
* la machine à états n'est pas en **DEFAUT** ;
* le débit est suffisant ;
* la mesure de luminosité ou de température extérieur est disponible ;
* les conditions de chauffage sont satisfaites.

Les seuils de débit, de luminosité et de température sont configurables via les Helpers définis dans la **SPEC-004**.

---

# 4. Conditions d'arrêt

Le chauffage solaire est arrêté lorsque l'une des conditions d'autorisation disparaît.

L'arrêt est immédiat.

Les protections du serpentin restent actives si nécessaire.

---

# 5. Protection du serpentin

## Objectif

Empêcher une montée excessive en température du serpentin lorsque celui-ci est exposé au rayonnement solaire.

La protection du serpentin fait partie du fonctionnement normal du chauffage solaire.

Elle ne constitue pas un diagnostic.

---

## Déclenchement

La protection est activée lorsque les conditions définies pour le risque de surchauffe sont réunies.

Les critères exacts (température, luminosité, durée, etc.) sont configurables.

---

## Fonctionnement

Lorsque la protection est active :

* la circulation d'eau est autorisée afin de refroidir le serpentin ;
* le fonctionnement est maintenu jusqu'à disparition du risque.

Les algorithmes de pilotage sont définis par l'implémentation.

---

## Cas du mode OFF

Par défaut :

* la protection du serpentin reste active.

Si le Helper :

```text
input_boolean.desactiver_securites_off
```

est activé :

* aucun démarrage automatique de la pompe n'est autorisé ;
* la protection du serpentin est volontairement inhibée.

Ce Helper est automatiquement réinitialisé lors du retour en mode **AUTO**.

---

## Protection impossible

Lorsque la protection est nécessaire mais ne peut pas être assurée, le diagnostic **PRO-003** est activé conformément à la **SPEC-007**.

---

# 6. Fonctionnement dégradé

En cas de fonctionnement dégradé :

* le chauffage solaire applique les stratégies de repli définies pour chaque diagnostic ;
* seules les fonctions compatibles avec la sécurité restent autorisées.

Les diagnostics correspondants sont définis dans la **SPEC-007**.

---

# 7. Compatibilité avec les modes utilisateur

| Mode                          | Chauffage solaire | Protection serpentin |
| ----------------------------- | ----------------- | -------------------- |
| AUTO                          | Oui               | Oui                  |
| OFF                           | Non               | Oui (par défaut)     |
| OFF + désactivation sécurités | Non               | Non                  |
| TRAITEMENT                    | Oui               | Oui                  |
| MARCHE FORCÉE                 | Oui               | Oui                  |

Les transitions entre modes sont définies dans la **SPEC-005**.

---

# 8. Journalisation

Les événements suivants sont journalisés conformément à la **SPEC-009** :

* démarrage du chauffage solaire ;
* arrêt du chauffage solaire ;
* activation de la protection du serpentin ;
* fin de la protection du serpentin ;
* impossibilité d'assurer la protection.

---

# 9. Critères d'acceptation

Le chauffage solaire est conforme lorsque :

* il respecte les autorisations définies par la machine à états ;
* la protection du serpentin est assurée dès qu'un risque est détecté ;
* le mode OFF conserve les protections par défaut ;
* la désactivation temporaire des sécurités en mode OFF inhibe uniquement les protections automatiques ;
* toute impossibilité d'assurer la protection déclenche le diagnostic **PRO-003** ;
* tous les événements sont journalisés.

---

# 10. Références

* SPEC-000 — Architecture générale
* SPEC-003 — Gestion de la filtration
* SPEC-004 — Modèle Home Assistant
* SPEC-005 — Machine à états
* SPEC-006 — Modes utilisateur
* SPEC-007 — Diagnostics et sécurités
* SPEC-009 — Journalisation
