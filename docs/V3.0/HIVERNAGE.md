# HIVERNAGE — piscine démontée

Sélectionner HIVERNAGE dans le mode de fonctionnement PCHA lorsque la piscine
est démontée. Le mode est persistant : il reste sélectionné après redémarrage HA.
Le matériel débranché n'empêche pas son activation.

## Comportement

- Arrêt de la pompe si elle est accessible ; état machine HIVERNAGE même si
  l'actionneur est indisponible. Le logiciel ne peut pas arrêter un matériel
  inaccessible : conserver l'alimentation physique de la pompe coupée pour le démontage.
- Aucun démarrage via les scripts ou la commande abstraite PCHA, y compris
  solaire et protection serpentin. Une commande physique ON détectée provoque
  une nouvelle tentative d'arrêt tant que le mode est HIVERNAGE.
- Timers traitement, vidange et simulations annulés.
- Tous les diagnostics MES/COH/PRO publiés passent à OFF sans délai de retour
  et exposent `suspendu: true`. Le dashboard affiche SUSPENDU.
  Cela signifie surveillance suspendue, pas matériel déclaré sain.
- Le niveau global reste NORMAL en hiver pour la compatibilité ; le mode,
  l'état machine et les en-têtes indiquent explicitement HIVERNAGE.
- Le verrou manuel PRO-001 n'est pas effacé. Un ancien défaut non réarmé
  redevient visible à la remise en service.
- Notifications persistantes PCHA effacées, nouvelles notifications PCHA suspendues.
- Demandes de fonctionnement, filtration et protection désactivées.
  Objectif et temps restant affichés à zéro ; calcul et échantillonnage de la
  référence quotidienne suspendus. Référence courante et accumulateurs sont remis
  à vide pour ne pas réutiliser une température d'automne au printemps.
- Paramètres et historique HA conservés. Les historiques glissants J à J-7
  continuent naturellement de tourner ; la rétention Recorder existante s'applique.
- Une sortie directe vers AUTO ou un autre mode actif est ramenée à OFF.
  Reconnecter le matériel, attendre la stabilisation des diagnostics puis
  sélectionner explicitement AUTO. La référence repart de la température valide
  disponible, puis de la moyenne de la veille selon les règles habituelles.

## AWTRIX du salon

`integrations/awtrix_salon.yaml` reprend la dernière configuration retrouvée
du 30 août 2026, avec les icônes météo actualisées et les pages maison/Tesla.
Le topic existant est `awtrix_salon`.

En HIVERNAGE :
- suppression de `custom/piscine` par payload vide ;
- aucune republication de page piscine, même sur le cycle de cinq minutes ;
- suppression de la notification affichée avec `notify/dismiss` à l'entrée
  et après démarrage HA en hiver ;
- arrêt des alertes PCHA dédiées et filtrage des notifications persistantes PCHA
  dans le relais des alertes Home Assistant ;
- météo, température salon, énergie, Tesla et alertes hors PCHA continuent.

AWTRIX 3 ne propose pas d'identifiant pour effacer une seule notification :
`notify/dismiss` ferme la notification courante. L'opération de nettoyage à
l'entrée/au redémarrage peut donc fermer une autre notification qui l'aurait
remplacée. Elle n'est pas répétée périodiquement, afin de préserver les nouvelles
alertes hors PCHA. Source :
[API officielle AWTRIX 3](https://github.com/Blueforcer/awtrix3/blob/main/docs/api.md).

Au retour en saison, le changement de mode relance la publication de la page
piscine. Le firmware AWTRIX et ESPHome n'ont pas besoin d'être modifiés.

## Déploiement depuis GitHub, dans Studio Code Server

Après fusion de la PR, garder PCHA en OFF et la pompe débranchée :

```bash
cd /config/pool-controller-ha
git pull --ff-only origin main
bash installation/installer-awtrix.sh
ha core check
```

Si le dossier HA est `/homeassistant`, utiliser
`cd /homeassistant/pool-controller-ha` à la place.

Le script suppose l'inclusion existante :

```yaml
automation awtrix_salon: !include awtrix_salon.yaml
```

Il remplace uniquement le fichier connu `awtrix_salon.yaml` par un lien vers le
dépôt, après sauvegarde. Les prochaines modifications AWTRIX suivent donc
`git pull`. Il refuse un fichier personnalisé différent ou une inclusion
différente, sans rien modifier : dans ce cas transmettre le fichier actuel
pour l'intégrer dans GitHub. Ne pas remplacer manuellement une version inconnue
et ne pas ajouter une deuxième inclusion des mêmes automatisations.

Uniquement si le script et la vérification HA réussissent :

```bash
ha core restart
```

Actualiser PCHA, sélectionner HIVERNAGE, puis vérifier :
- machine HIVERNAGE, demande inactive, objectif suspendu ;
- diagnostics SUSPENDU, niveau global NORMAL ;
- page piscine retirée de l'AWTRIX, ancienne alerte PCHA fermée ;
- rotation des pages hors piscine active.

Si un ancien automatisme AWTRIX a été dupliqué dans l'interface HA, il peut
continuer à publier. Transmettre alors ses identifiants/configuration pour
corriger la source GitHub au lieu d'accumuler des automatismes concurrents.

## Validation

Tests locaux : `python -m unittest discover -s tests -v` avec PyYAML/Jinja2.
Ils couvrent les expressions réellement chargées depuis le YAML, la conservation
du verrou PRO-001, l'absence de matériel, les commandes de pompe et la sortie
via OFF, les fins de vidange tardives, ainsi que le nettoyage/filtrage AWTRIX.

La configuration complète HA et l'affichage physique AWTRIX doivent encore
être vérifiés sur l'installation. Aucun appareil n'a été commandé pendant
ces tests.
