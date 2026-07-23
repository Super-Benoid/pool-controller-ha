# SPEC-001 — Inventaire matériel

Version : 1.0
Statut : Figée

---

# 1. Objet

Cette SPEC décrit les équipements physiques utilisés par le Pool Controller Home Assistant (PCHA).

Elle constitue l'inventaire matériel de l'installation.

Elle définit :

* les capteurs ;
* les actionneurs ;
* le schéma hydraulique.

Elle ne décrit aucun comportement fonctionnel.

Les comportements sont définis dans les autres SPEC.

---

# 2. Philosophie

Le contrôleur est conçu pour être totalement indépendant du matériel.

Les équipements physiques :

* fournissent des mesures ;
* exécutent des commandes.

Ils ne contiennent aucune logique métier.

Le reste du projet ne doit jamais accéder directement aux équipements physiques.

Toutes les interactions passent obligatoirement par la couche d'abstraction définie dans la SPEC-004.

---

# 4. Liste du matériel

* Débitmètre en L/h, mesure le débit du circuit hydraulique.
* Thermomètre piscine en °C, mesure la température de l'eau en sortie pompe de filtration.
* Luminosité en Lux, mesure l'ensoleillement au niveau du serpentin solaire.
* Thermomètre extérieur en °C, mesure la température de l'air ambiant.
* Puissance pompe filtration en Watt, mesure la puissance active instantanée.
* Énergie pompe filtration en kWh, mesure la consommation total.

---

# 5. Équipements absents de la V1

Les équipements suivants ne sont pas présents dans cette version :

* vanne motorisée ;
* sonde de température du serpentin ;
* sonde de température du local technique.

Ces équipements pourront être ajoutés dans une version ultérieure sans remettre en cause l'architecture générale.

---

# 6. Contraintes

Les entités physiques ne sont jamais utilisés directement par le reste du projet.
Exemple :
- la machine à états ;
- les scripts ;
- les automatisations ;
- les diagnostics.

Elles sont accessibles exclusivement via la couche d'abstraction définie précédemment dans le chapitre 4.

---

# 9. Références

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 — Principes généraux
* SPEC-004 — Couche d'abstraction et configuration
