# Maintenance et tests PCHA

**Version :** V2.0
**Statut :** Courante

---

## Vidange

1. Sélectionner `OFF` et vérifier l'arrêt réel de la pompe.
2. Positionner manuellement la vanne du filtre à sable sur VIDANGE.
3. Régler une durée de 1 à 10 minutes.
4. Sélectionner `VIDANGE`.
5. À la fin, laisser le mode sur `OFF`, remettre la vanne sur FILTRATION puis sélectionner `AUTO`.

La vidange ne traverse pas le débitmètre. Elle ne crédite donc ni le temps de filtration quotidien, ni les renouvellements du bassin, ni le chauffage solaire. Elle ne reprend jamais après un redémarrage de Home Assistant.

## Défaut de débit critique

`PRO-001` reste mémorisé après l'arrêt de la pompe. Pour le réarmer :

1. sélectionner `OFF` ;
2. contrôler le niveau d'eau, les tuyaux, le filtre, l'aspiration et la pompe ;
3. vérifier que le débitmètre est disponible ;
4. utiliser **Réarmer PRO-001** dans l'onglet Maintenance ;
5. sélectionner volontairement le mode souhaité.

Le bouton **Effacer les notifications** ne réarme aucun diagnostic.

## Simulation des capteurs

L'onglet Maintenance peut simuler l'indisponibilité de la température du bassin, du débit, de la puissance ou de la luminosité. La simulation agit sur l'abstraction PCHA et laisse la valeur physique visible pour comparaison.

Toutes les simulations s'arrêtent automatiquement après cinq minutes et après chaque redémarrage de Home Assistant. Le bouton **Arrêter tous les tests** les annule immédiatement.

La simulation du débit provoque `MES-002`, arrête la filtration après 60 secondes et se réarme automatiquement 60 secondes après la fin du test. Un débit réellement mesuré sous 500 L/h provoque en revanche `PRO-001`, qui exige un réarmement manuel.
