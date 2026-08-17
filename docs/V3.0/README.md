# PCHA V3.0 — Référence fonctionnelle

**Statut :** version courante, en validation terrain.

PCHA V3.0 conserve le moteur de sécurité et les diagnostics issus des versions précédentes et ajoute une planification météo-adaptative de la filtration.

## 1. Objectif quotidien

La durée quotidienne reste calculée à partir de la température de référence du bassin, figée au changement de jour à partir de la moyenne fiable de la veille.

La loi est désormais paramétrable :

```text
Durée = T × coefficient de base
      + max(T − seuil d'accélération, 0) × coefficient d'accélération
```

Valeurs de référence V3.0 :

```text
coefficient de base          0,20 h/°C
seuil d'accélération        25,0 °C
coefficient d'accélération   1,00 h/°C
```

Les réglages sont exposés dans l'onglet **Paramètres PCHA V3.0**.

## 2. Météo et potentiel thermique

La météo est isolée derrière des abstractions PCHA :

```text
sensor.pcha_meteo_aujourd_hui
sensor.pcha_meteo_demain
sensor.pcha_previsions_meteo_horaires
```

Le potentiel thermique de la journée est synthétisé par :

```text
sensor.pcha_score_potentiel_thermique_jour
sensor.pcha_potentiel_thermique_jour
```

Le score combine principalement l'état du ciel et la température extérieure prévue sur la fenêtre utile avant le coucher du soleil.

## 3. Planification active

`sensor.pcha_heure_cible_objectif` calcule la cible météo-adaptative. La cible standard reste le coucher du soleil moins la marge configurée.

Selon la température du bassin, la consigne, le potentiel thermique du jour et, près de l'équilibre, la tendance J+1, la cible peut être avancée ou retardée. Le décalage est borné entre −120 et +90 minutes et la cible ne dépasse pas les 15 dernières minutes avant le coucher du soleil.

La planification active est consommée par :

```text
binary_sensor.pcha_filtration_requise_v3
sensor.pcha_heure_atteinte_objectif_v3
```

En mode `AUTO`, la demande consolidée utilise la décision de filtration V3, tout en conservant séparément les demandes de chauffage solaire et de protection du serpentin.

Les anciennes entités :

```text
binary_sensor.pcha_filtration_requise
sensor.pcha_heure_atteinte_objectif
```

restent disponibles comme interfaces de compatibilité et reflètent la V3 avec repli sur la logique historique si nécessaire.

## 4. Dashboard

L'accueil affiche désormais :

* la météo du jour et du lendemain ;
* le potentiel thermique et son score ;
* la stratégie retenue ;
* la cible réellement utilisée pour l'objectif quotidien.

La vue `dashboard/views/parametres.yaml` regroupe les paramètres métier modifiables. Les valeurs avancées liées aux diagnostics et à la sécurité y sont présentées en lecture seule.

## 5. Sécurité

V3.0 ne modifie pas les principes de sécurité :

* abstraction obligatoire des capteurs physiques ;
* diagnostics MES / COH / PRO ;
* interdiction de filtration au niveau CRITIQUE selon les règles du moteur ;
* protections solaires et hydrauliques indépendantes de l'optimisation météo ;
* seuils de sécurité non exposés comme réglages utilisateur courants.

La référence détaillée historique du moteur reste disponible dans `docs/V1.1/`.
