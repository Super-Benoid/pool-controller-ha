# SPEC-008 — Chauffage solaire

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette SPEC définit le fonctionnement du chauffage solaire du Pool Controller Home Assistant (PCHA).

Le chauffage solaire est entièrement passif.

Il n'existe aucun circuit hydraulique dédié au chauffage.

---

# 2. Principe

Le chauffage solaire repose sur un principe simple :

> **Le chauffage solaire est une période de filtration réalisée lorsque les conditions d'ensoleillement sont favorables.**

Il n'existe :

* qu'une seule pompe ;
* qu'un seul circuit hydraulique ;
* qu'un seul débit.

Le serpentin solaire est intégré au circuit de filtration.

Toute circulation d'eau traverse donc naturellement le serpentin.

Aucune vanne n'est utilisée.

Aucun basculement hydraulique n'est réalisé.

---

# 4. Conditions d'autorisation

Le chauffage solaire est autorisé uniquement lorsque :

* le mode de fonctionnement l'autorise (SPEC-006) ;
* la filtration est autorisée (SPEC-003) ;
* le seuil minimal de luminosité est atteint ;
* la température de consigne de la piscine n'est pas atteinte ;
* aucun défaut bloquant n'est présent.

Si une seule de ces conditions n'est plus satisfaite, le chauffage solaire cesse.

En niveau DÉGRADÉ, le chauffage solaire peut être désactivé suivant les diagnostics définis dans la SPEC-007.

---

# 5. Détection de l'ensoleillement

Le chauffage solaire est piloté à partir de la luminosité mesurée.

Un helper permet de définir le seuil minimal d'ensoleillement.

Exemple :

```text
input_number.pcha_seuil_luminosite_chauffage
```

Le choix du seuil dépend des caractéristiques du capteur et est configurable par l'utilisateur.

---

# 6. Température de consigne

L'utilisateur définit la température souhaitée de la piscine.

Exemple :

```text
input_number.pcha_consigne_temperature
```

Lorsque cette température est atteinte :

* le chauffage solaire est arrêté ;
* la filtration continue selon les règles définies dans la SPEC-003.

---

# 7. Fin d'une période de chauffage

Une période de chauffage se termine lorsque :

* la température de consigne est atteinte ;
* la luminosité devient insuffisante ;
* la filtration n'est plus autorisée ;
* le mode de fonctionnement change ;
* un défaut bloquant est détecté.

# 9. Philosophie

Le chauffage solaire ne constitue pas une fonction indépendante.

Le contrôleur ne décide jamais de :

> « démarrer le chauffage ».

Il décide uniquement de :

> **prolonger ou démarrer une période de filtration lorsque les conditions permettent de récupérer de l'énergie solaire.**

Le chauffage est donc une conséquence du fonctionnement de la filtration.

---

# 10. Interaction avec les autres SPEC

Cette SPEC dépend :

* SPEC-000 — Principes généraux ;
* SPEC-003 — Filtration ;
* SPEC-006 — Modes de fonctionnement ;
* SPEC-007 — Diagnostics.

Elle ne définit aucun comportement de filtration.

La gestion de la durée de filtration reste exclusivement décrite dans la SPEC-003.

---

# 11. Évolutions futures

Les fonctionnalités suivantes sont exclues de la V1 :

* vanne trois voies motorisée ;
* mesure de température du serpentin ;
* température du local technique ;
* optimisation thermique avancée ;
* estimation du rendement solaire.

Elles pourront être intégrées dans une version ultérieure sans modifier le principe fondamental : **un seul circuit hydraulique, une seule filtration, dont certaines périodes sont exploitées pour le chauffage solaire.**
