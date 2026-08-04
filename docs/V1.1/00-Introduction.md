# Pool Controller Home Assistant — Introduction

**Version :** V1.1  
**Statut :** Figée

---

PCHA automatise la filtration, le chauffage solaire passif et la surveillance d'une piscine depuis Home Assistant.

La V1.1 introduit quatre évolutions principales :

1. une sonde immergée directement dans le bassin remplace la mesure sur la sortie de pompe ;
2. la température devient immédiatement disponible et reçoit un calibrage signé de `−3 à +3 °C` ;
3. la luminosité est acquise par une D1 mini proche du BH1750 puis transmise à l'ESP32 Jardin ;
4. en cas de perte de luminosité, le chauffage solaire utilise l'écart entre la température extérieure et celle du bassin.

L'objectif quotidien est calculé à partir du maximum thermique observé entre minuit et trente minutes après le lever du soleil, puis figé jusqu'au lendemain. Sa planification vise toujours une fin deux heures avant le coucher du soleil.

La documentation V1.0 reste conservée comme historique. Le dossier `docs/V1.1/` constitue la référence applicable au code courant.
