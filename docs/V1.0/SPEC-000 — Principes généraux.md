# SPEC-000 — Principes généraux

Version : 1.0
Statut : Figée

---

# 1. Objet

Le Pool Controller Home Assistant (PCHA) est un contrôleur logiciel destiné à automatiser le fonctionnement d'une piscine équipée d'un chauffage solaire passif.

Cette SPEC définit les principes fondamentaux du projet.

Les comportements détaillés sont décrits dans les SPEC suivantes.

# 2. Périmètre

Le PCHA assure exclusivement :

la filtration de la piscine ;
l'optimisation du chauffage solaire ;
la protection de l'installation ;
la journalisation des événements.

Toute autre fonctionnalité est hors du périmètre de la V1.

# 3. Priorités

Le contrôleur applique les priorités suivantes :

1. Sécurité des personnes.
2. Protection de l'installation.
3. Filtration de la piscine.
4. Chauffage solaire.
5. Optimisation énergétique.

La sécurité des personnes est toujours prioritaire sur la protection du matériel.

---

# 4. Installation hydraulique

Le contrôleur pilote un unique circuit hydraulique.

Schéma de principe :

```text
Aspiration piscine
        │
        ▼
Pompe de filtration
        │
        ▼
Débitmètre
        │
        ▼
Thermomètre piscine
        │
        ▼
Serpentin solaire
        │
        ▼
Refoulement piscine
```

Le circuit hydraulique est unique.

Il n'existe :

* qu'une seule pompe ;
* qu'un seul débit ;
* qu'un seul circuit hydraulique.

Le serpentin solaire fait partie intégrante du circuit de filtration.

De part l'implantation du thermomètre piscine, il est nécessaire que la pompe fonctionne pendant un certain temps avant que la valeur mesurée corresponde réellement à la température du bassin.

---

# 5. Principe de fonctionnement

Les règles de fonctionnement de la filtration et du chauffage solaire sont définies dans les SPEC spécialisées :

SPEC-003 — Filtration
SPEC-008 — Chauffage solaire

---

# 6. Modes de fonctionnement

Le contrôleur possède plusieurs modes de fonctionnement sélectionnable par l'utilisateur.

La description complète de ces modes est définie exclusivement dans la SPEC-006.

---

# 7. Principes de conception

Le contrôleur applique les principes suivants :

* une seule information possède une seule source de vérité ;
* les comportements sont déterministes ;

---

# 8. Découpage fonctionnel

Ce reporter a ARCHITECTURE.md

---

# 9. Évolutions

La version V1 constitue une base stable.

Toute évolution fonctionnelle doit être documentée dans la SPEC concernée avant toute implémentation.

Tant que la V1 n'est pas figée, les SPEC sont corrigées directement afin de garantir leur cohérence.

Aucun comportement ne doit être ajouté dans le code sans être préalablement documenté.

---

# 10. Documents de référence

Le projet s'appuie sur les documents suivants :

* INTRODUCTION.md
* ARCHITECTURE.md
* CONVENTIONS.md
* SPEC-000 à SPEC-009

En cas de contradiction :

1. Les SPEC prévalent.
2. ARCHITECTURE.md définit l'organisation technique.
3. CONVENTIONS.md définit les règles de développement.

Le code implémente exclusivement ces documents.

---

# 11. Objectif

Le Pool Controller Home Assistant (PCHA) a pour objectif de fournir un contrôleur :

* fiable ;
* simple à utiliser ;
* indépendant du matériel ;
* facilement maintenable ;
* facilement évolutif.

Toutes les décisions de conception doivent contribuer à atteindre ces objectifs.
