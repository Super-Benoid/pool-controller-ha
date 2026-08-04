# SPEC-002 — Interface utilisateur

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit les informations, commandes et paramètres accessibles à l'utilisateur.

# 2. Principes

* L'utilisateur ne commande jamais directement le matériel.
* Une information affichée provient de son entité PCHA de référence.
* Une commande utilisateur agit uniquement sur un helper prévu à cet effet.

# 3. Informations affichées

| Zone | Informations principales |
|---|---|
| État général | Mode, état de la machine, niveau de fonctionnement, diagnostics actifs |
| Filtration | État, débit, objectif quotidien, référence thermique, objectif figé ou provisoire, temps réalisé, temps restant, heure `Atteint à`, puissance et énergie |
| Bassin | Température brute, température calibrée, calibrage signé, consigne, minimum et maximum du jour |
| Chauffage solaire | Demande, état actif, source de pilotage, écart extérieur/bassin, luminosité, état de la liaison distante et protection du serpentin |
| Supervision | Tuiles de tendance sur 24 heures pour la luminosité, la température du bassin et la puissance de la pompe |
| Traitement | Mode actif, durée configurée et temps restant |
| Diagnostics | MES, COH, PRO et états de la chaîne de luminosité distante |

# 4. Affichage de l'objectif quotidien

Les durées sont présentées au format `03H56`. La carte affiche :

* l'objectif ;
* la température de référence ;
* le statut `Provisoire` ou `Figée` ;
* le temps réalisé ;
* le temps restant ;
* `Atteint à : HHhMM`.

# 5. Graphes de tendance

Les graphes numériques principaux utilisent la carte native `tile` avec la fonctionnalité `trend-graph`, une période de `24` heures et le détail activé.

| Mesure | Entité PCHA | Emplacement |
|---|---|---|
| Luminosité | `sensor.pcha_luminosite` | Supervision |
| Température du bassin | `sensor.pcha_temperature_piscine` | Piscine et solaire |
| Puissance de la pompe | `sensor.pcha_puissance_pompe_filtration` | Filtration |

Les graphes multi-états et les historiques de diagnostics restent sur des cartes `history-graph`.

# 6. Paramètres modifiables

Les paramètres sont exclusivement ceux déclarés dans la SPEC-004, notamment :

* calibrage de température bassin de `−3,0 °C` à `+3,0 °C`, par pas de `0,1 °C` ;
* consigne de température ;
* seuil de luminosité ;
* délais de validation.

# 7. Références

* SPEC-003
* SPEC-004
* SPEC-007
* SPEC-008
