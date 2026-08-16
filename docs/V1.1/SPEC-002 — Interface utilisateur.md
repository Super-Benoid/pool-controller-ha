# SPEC-002 — Interface utilisateur

**Version :** 1.1  
**Statut :** Figée

---

# 1. Objet

Cette SPEC définit les informations, commandes et paramètres accessibles à l'utilisateur, ainsi que l'organisation générale du dashboard.

# 2. Principes

* L'utilisateur ne commande jamais directement le matériel.
* Une information affichée provient de son entité PCHA de référence.
* Une commande utilisateur agit uniquement sur un helper prévu à cet effet.

# 3. Informations affichées

| Vue | Informations principales |
|---|---|
| Accueil | État général, mesures en direct, objectif quotidien, réglages rapides et activité sur 24 h |
| Pilotage | Filtration, performances hydrauliques, énergie, temporisations AUTO et mode traitement |
| Solaire | Températures, chaîne solaire, luminosité distante, bilan solaire du jour et historique solaire |
| Diagnostics | Niveau global, diagnostics MES/COH/PRO, délais de validation et historique des défauts |
| Historique | Vue actuelle sur 24 heures et consultation des journées complètes J-1 à J-3 |

# 4. Affichage de l'objectif quotidien

Les durées sont présentées au format `03H56`. La carte affiche :

* l'objectif ;
* la température de référence ;
* le statut `Provisoire` ou `Figée` ;
* le temps réalisé ;
* le temps restant ;
* `Atteint à : HHhMM`.

# 5. Design du dashboard

Le dashboard V1.1 adopte une présentation plus moderne :

* vues courtes et lisibles ;
* priorité aux cartes `tile` ;
* regroupement par usage plutôt que par type technique ;
* indicateurs essentiels visibles dès la page d'accueil ;
* graphes de tendance directement intégrés dans les tuiles.

# 6. Graphes de tendance

Les graphes numériques principaux utilisent la carte native `tile` avec la fonctionnalité `trend-graph`, une période de `24` heures et le détail activé.

| Mesure | Entité PCHA | Emplacement |
|---|---|---|
| Luminosité | `sensor.pcha_luminosite` | Supervision |
| Température du bassin | `sensor.pcha_temperature_piscine` | Piscine et solaire |
| Puissance de la pompe | `sensor.pcha_puissance_pompe_filtration` | Filtration |

Les graphes multi-états et les historiques de diagnostics restent sur des cartes `history-graph`.

La vue Historique conserve sa période glissante de 24 heures pour `J`. Un
sélecteur placé dans le bandeau supérieur donne accès à `J-1`, `J-2` et `J-3`.
Pour ces journées passées, tous les graphes de mesures, états de fonctionnement
et diagnostics couvrent la même période calendaire de `00:00` à `23:59`.

Les synthèses journalières sont regroupées dans les en-têtes des graphes afin
d'éviter une rangée de cartes redondante : moyenne et amplitude max/min du
bassin pour les températures, moyenne lumineuse et durée d'ensoleillement,
temps de filtration et cycles du bassin, puis consommation totale de la pompe.
Le graphe de progression complète sa courbe avec la durée de l'objectif de la
journée et la température de référence utilisée pour son calcul.
L'activité du système est organisée en quatre couloirs indépendants : mode de
fonctionnement, état de la machine, commandes pompe/solaire et niveau de
fonctionnement. Chaque couloir possède une échelle d'états explicitement
libellée sur son axe vertical. Cette représentation reste lisible sans survol et
évite tout chevauchement lors de transitions rapprochées.

# 7. Paramètres modifiables

Les paramètres sont exclusivement ceux déclarés dans la SPEC-004, notamment :

* calibrage de température bassin de `−3,0 °C` à `+3,0 °C`, par pas de `0,1 °C` ;
* consigne de température ;
* seuil de luminosité ;
* délais de validation.

# 8. Références

* SPEC-003
* SPEC-004
* SPEC-007
* SPEC-008


# 9. Référence visuelle Concept D

Le dashboard V1.1 utilise le thème sombre `PCHA Concept D`, avec des accents cyan et violet. La vue Accueil présente :

* quatre états système sous forme de tuiles ;
* quatre cartes `sensor` détaillées avec valeur courante, axes et historique 24 h ;
* les minimums et maximums glissants sur 24 h ;
* une jauge de progression de l’objectif quotidien ;
* les réglages rapides et l’activité récente.

Le visuel de référence approuvé est archivé dans `docs/V1.1/assets/concept-d-reference.png`.
