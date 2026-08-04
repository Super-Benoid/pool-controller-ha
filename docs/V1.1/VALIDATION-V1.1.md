# Validation statique — PCHA V1.1

**Version :** 1.1  
**Date :** 2026-08-04  
**Statut :** Validation statique réussie ; recette réelle à exécuter

---

# 1. Contrôles réalisés

* chargement syntaxique de tous les fichiers YAML avec prise en charge des balises Home Assistant et ESPHome ;
* analyse syntaxique de toutes les expressions Jinja détectées ;
* contrôle des `unique_id` dupliqués ;
* inventaire des entités PCHA, helpers et scripts produits ;
* contrôle des références internes `pcha_*` ;
* recherche des anciennes références à la sonde de sortie de pompe dans le code courant ;
* recherche de secrets ou mots de passe recopiés dans les fichiers fournis ;
* contrôle de l'intégrité de l'archive finale.

# 2. Résultats

```text
27 fichiers YAML chargés
218 expressions Jinja analysées
60 interfaces PCHA / helpers / scripts recensées
0 référence interne PCHA manquante
0 unique_id dupliqué
0 ancienne source sensor.jardin_esp32_jardin_temperature_piscine dans le code V1.1
```

# 3. Limites de cette validation

L'environnement de construction ne contient ni une instance Home Assistant complète, ni le compilateur ESPHome. Les contrôles suivants restent donc à effectuer sur l'installation réelle :

1. **Vérifier la configuration** dans Home Assistant avant redémarrage.
2. Compiler séparément les deux configurations ESPHome après fusion du fragment ESP32 avec le fichier réel.
3. Exécuter `RECETTE-V1.1.md` en commençant en mode `OFF`.
4. Contrôler les identifiants d'entités réellement créés par ESPHome.

# 4. Critère de mise en service

La V1.1 ne doit être replacée en `AUTO` qu'après réussite de la vérification Home Assistant, confirmation des trois nouvelles entités physiques et contrôle du calibrage signé.
