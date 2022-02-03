# pi-estimator
Calcul de l'approximation de pi avec les méthodes spark et numpy et calcul du temps d'exécution des deux méthodes

## Exécution du programme depuis le terminal (sous Windows)
  1) Téléchargez le zip de la branche pi-estimator.
  2) Dézippez le dossier là où vous souhaitez placer le projet.
  3) Ouvrez votre terminal et placez-vous dans le dossier où se trouve le projet.
  4) Exécutez la commande suivante : spark-submit .\src\pi_estimator.py

## Résulats obtenus
Si vous souhaitez modifier le nombre de points, ouvrez le fichier pi_estimator.py dans un éditeur python et modifiez la valeur n à la ligne 40 du script.

### n = 100 000

![alt text](https://github.com/AxelleT/pi-estimator/blob/pi-estimator/results/results_100_000.png?raw=true)

![alt text](https://github.com/AxelleT/pi-estimator/blob/pi-estimator/results/tableau_100_000.png?raw=true)

### n = 1 000 000

![alt text](https://github.com/AxelleT/pi-estimator/blob/pi-estimator/results/results_1_000_000.png?raw=true)

![alt text](https://github.com/AxelleT/pi-estimator/blob/pi-estimator/results/tableau_1_000_000.png?raw=true)

## Comparaison entre Spark et Numpy
D'après les résulats précédents, on peut observer que Spark met plus de temps que Numpy mais aura cependant une meilleure approximation de pi que Numpy à mesure qu'on augmente le nombre de points n.
Numpy sera donc plus efficace sur des petits volumes et Spark sera plus précis sur de grands volumes, malgré sa lenteur par rapport à Numpy.
