# SPEC-009 — Journalisation et notifications

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit la journalisation des événements du contrôleur et les notifications utilisateur. Elle ne modifie jamais le comportement des fonctions qui produisent ces événements.

# 2. Principes

* Chaque changement fonctionnel produit au maximum un événement de journal PCHA.
* Le journal est une trace chronologique, jamais une source de décision.
* Une notification n'a aucun effet sur un diagnostic, un mode, un état ou une demande.
* La journalisation et les notifications utilisent exclusivement les interfaces PCHA.

# 3. Événements obligatoires

| Domaine | Événements |
|---|---|
| Machine | Changement d'état |
| Modes | Changement de mode, début et fin d'un traitement |
| Diagnostics | Activation et disparition d'un diagnostic, changement du niveau global |
| Filtration | Activation et disparition de la demande automatique, démarrage et arrêt réels de la pompe |
| Chauffage solaire | Demande activée ou désactivée, chauffage actif ou inactif, début et fin d'une protection, protection impossible |

La protection impossible est fournie par le diagnostic `PRO-003` défini dans SPEC-007.

# 4. Événement de journal

Chaque événement journalisé est publié sous le type :

```text
pcha_journal
```

Il contient au minimum :

* `horodatage` ;
* `type` ;
* `source` ;
* `description` ;
* `niveau`.

Pour un diagnostic, il contient également l'identifiant, la famille, la gravité et l'état d'activation.

L'événement est enregistré dans l'activité Home Assistant par `logbook.log`.

# 5. Niveaux de journalisation

| Niveau | Usage |
|---|---|
| `INFORMATION` | Fonctionnement normal ou diagnostic informatif |
| `AVERTISSEMENT` | Fonctionnement dégradé |
| `ERREUR` | Diagnostic critique ou intervention requise |

# 6. Notifications

| Gravité ou niveau | Notification |
|---|---|
| `INFORMATIF` / `INFORMATION` | Optionnelle |
| `DEGRADE` / `AVERTISSEMENT` | Recommandée |
| `CRITIQUE` / `ERREUR` | Obligatoire |

En V1.1 :

* les diagnostics `DEGRADE` et `CRITIQUE` créent une notification persistante Home Assistant ;
* ils sont également transmis à `notify.mobile_app_oppo_ben` ;
* la disparition du diagnostic ferme la notification persistante et produit une notification de résolution.

Une notification contient au minimum un titre, une description, la date et l'heure, le niveau et une recommandation.

# 7. Effacement des notifications

La commande :

```text
input_boolean.pcha_acquitter_alarmes
```

ferme les notifications persistantes PCHA visibles.

L'effacement :

* ne réarme aucun diagnostic ;
* ne modifie pas le niveau global ;
* ne modifie pas la machine ;
* ne modifie pas le mode ;
* ne supprime pas la trace du journal.

La commande revient automatiquement à `off` après traitement.

Cette commande est distincte de `input_button.pcha_rearmer_defaut_debit`. Le réarmement de PRO-001 agit sur un verrou fonctionnel et n'est accepté que dans les conditions de sécurité définies par la SPEC-007.

# 8. Fichiers responsables

```text
automations/journalisation.yaml
automations/notifications.yaml
```

Le premier fichier produit et enregistre les événements. Le second fichier gère exclusivement les notifications et leur effacement.

# 9. Critères d'acceptation

* Tous les événements obligatoires sont traçables chronologiquement.
* Aucun événement PCHA identique n'est produit plusieurs fois pour un même changement.
* Toute activation critique provoque une notification persistante et mobile.
* Toute activation dégradée provoque une notification persistante et mobile.
* La disparition d'un diagnostic ferme sa notification persistante.
* L'effacement des notifications ne modifie aucune information fonctionnelle.
* La journalisation et les notifications ne modifient aucune entité fonctionnelle, à l'exception du retour automatique de la commande d'effacement à `off`.

# 10. Références

* SPEC-003 — Gestion de la filtration
* SPEC-005 — Machine à états
* SPEC-006 — Modes de fonctionnement
* SPEC-007 — Diagnostics et sécurités
* SPEC-008 — Chauffage solaire
