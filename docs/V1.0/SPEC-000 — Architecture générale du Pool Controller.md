# SPEC-000 — Principes généraux

Version : 1.1
Statut : Figée

---

# 1. Objet

Le Pool Controller Home Assistant (PCHA) est un contrôleur logiciel destiné à automatiser le fonctionnement d'une piscine équipée d'un chauffage solaire passif.

Cette SPEC définit les principes généraux du projet.

Les comportements détaillés sont décrits dans les SPEC suivantes.

---

# 2. Philosophie

Le contrôleur est conçu selon les principes suivants :

* simplicité de fonctionnement ;
* robustesse ;
* sécurité des personnes ;
* protection de l'installation ;
* modularité ;
* évolutivité.

Les SPEC constituent la référence fonctionnelle du projet.

Le code est uniquement une implémentation des SPEC.

---

# 3. Priorités

Les priorités du contrôleur sont les suivantes :

1. Sécurité des personnes.
2. Protection de l'installation.
3. Chauffage de la piscine.
4. Optimisation énergétique.

La sécurité des personnes est toujours prioritaire sur la protection du matériel.

---

# 4. Installation hydraulique

Le contrôleur pilote une installation composée d'un **circuit hydraulique unique**.

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
Thermomètre
        │
        ▼
Serpentin solaire
        │
        ▼
Refoulement piscine
```

Il n'existe :

* qu'une seule pompe ;
* qu'un seul débit ;
* qu'un seul circuit hydraulique.

---

# 5. Principe de fonctionnement

Le chauffage solaire n'est **pas** un circuit indépendant.

Le serpentin solaire est un élément du circuit de filtration.

Par conséquent :

* toute période de chauffage est une période de filtration ;
* une période de filtration n'est pas obligatoirement une période de chauffage.

Le chauffage solaire consiste simplement à faire fonctionner la filtration lorsque les conditions d'ensoleillement sont favorables.

Le contrôleur ne distingue donc jamais un « circuit de chauffage » et un « circuit de filtration ».

Il pilote toujours un unique circuit hydraulique.

---

# 6. Modes de fonctionnement

Les différents modes sont définis dans la SPEC-006.

Leur philosophie est la suivante :

| Mode         | Description                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| OFF          | Arrêt absolu. Aucun démarrage automatique n'est autorisé.                                                   |
| SÉCURISATION | Le fonctionnement normal est arrêté. Seules les protections automatiques de l'installation restent actives. |
| AUTO         | Fonctionnement automatique complet conformément aux SPEC.                                                   |
| MANUEL       | Fonctionnement commandé par l'utilisateur.                                                                  |

---

# 7. Règles générales

Le contrôleur applique les principes suivants :

* une seule information possède une seule source de vérité ;
* aucune décision n'est dupliquée ;
* les comportements sont déterministes ;
* toute fonction est documentée dans une SPEC dédiée.

---

# 8. Découpage fonctionnel

Le projet est organisé selon les domaines suivants :

| SPEC     | Domaine                 |
| -------- | ----------------------- |
| SPEC-001 | Matériel                |
| SPEC-002 | Interfaces              |
| SPEC-003 | Filtration              |
| SPEC-004 | Configuration           |
| SPEC-005 | Machine à états         |
| SPEC-006 | Modes de fonctionnement |
| SPEC-007 | Diagnostics             |
| SPEC-008 | Chauffage solaire       |
| SPEC-009 | Journalisation          |

Chaque SPEC possède une responsabilité unique.

---

# 9. Évolutions

La version V1 est considérée comme figée.

Toute évolution fonctionnelle doit faire l'objet :

* d'une nouvelle SPEC ;
* ou d'une nouvelle version d'une SPEC existante.

Aucune modification du code ne doit introduire un comportement non décrit dans les SPEC.

---

# 10. Références

Les documents de référence du projet sont :

* ARCHITECTURE.md
* SPEC-000 à SPEC-009

En cas de contradiction :

1. Les SPEC prévalent sur le code.
2. ARCHITECTURE.md définit les règles d'organisation et d'implémentation.
