# Installation — PCHA V1

**Version :** 1.0  
**Statut :** Figée

---

# 1. Préparation

La structure cible est :

```text
/config/
├── configuration.yaml
├── packages/
│   ├── piscine.yaml
│   └── piscine_diagnostics.yaml
└── pool-controller-ha/
```

Copier le dossier `pool-controller-ha` dans `/config/`.

# 2. Packages

Copier :

```text
installation/packages/piscine.yaml
installation/packages/piscine_diagnostics.yaml
```

vers :

```text
/config/packages/
```

Le fichier `configuration.yaml` doit charger ce dossier :

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Si la clé `homeassistant:` existe déjà, ajouter uniquement la ligne `packages:` sous cette clé.

# 3. Tableau de bord

Fusionner le bloc `lovelace:` de `installation/configuration_extrait.yaml` dans `/config/configuration.yaml`.

# 4. Paramètres de mise en service

Après le premier chargement, régler les helpers suivants :

| Paramètre | Valeur V1 de mise en service |
|---|---:|
| Température de consigne | `28 °C` |
| Seuil de luminosité chauffage | `15 000 lx` |
| Durée du traitement | `12 h` |
| Temps minimum de marche | `5 min` |
| Temps minimum d'arrêt | `25 min` |
| Validation température piscine | `30 s` |
| Validation débit | `30 s` |
| Validation luminosité | `30 s` |

Le mode initial doit rester `OFF` pendant les contrôles de mise en service.

# 5. Validation de la configuration

Exécuter **Vérifier la configuration** dans Home Assistant avant tout redémarrage.

Après validation :

1. redémarrer Home Assistant ;
2. vérifier la présence des entités `pcha_*` ;
3. ouvrir le tableau de bord **Piscine** ;
4. suivre la recette `RECETTE-V1.md`.

# 6. Retour arrière

Avant l'installation, sauvegarder :

```text
/config/configuration.yaml
/config/packages/
/config/pool-controller-ha/
```

En cas d'échec, remettre le mode sur `OFF`, restaurer les fichiers sauvegardés, puis vérifier la configuration avant de redémarrer.
