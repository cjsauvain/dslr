# dslr

Prédiction de la maison de Poudlard à partir des notes des élèves, avec une régression logistique one-vs-all écrite à la main (sigmoïde, log-loss, descente de gradient). pandas, numpy et matplotlib servent au chargement des CSV, aux calculs et aux graphiques. Les statistiques et les métriques ne passent pas par scikit-learn.

## Installation

Python 3.10 ou plus.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Lancer

```bash
python describe.py datasets/dataset_train.csv
python histogram.py datasets/dataset_train.csv
python scatter_plot.py datasets/dataset_train.csv
python pair_plot.py datasets/dataset_train.csv

python logreg_train.py datasets/dataset_train.csv
python logreg_predict.py datasets/dataset_test.csv model.json
```

`histogram.py` et `scatter_plot.py` ouvrent une fenêtre. `pair_plot.py` écrit `pair_plots.pdf`. L'entraînement écrase `model.json`. La prédiction écrit `houses.csv`.

Pour mesurer le modèle sur un jeu qu'il n'a pas vu :

```bash
python logreg_train.py datasets/dataset_train.csv \
    --validation-ratio 0.2 --metrics --confusion-matrix
```

`--validation-ratio` est dans `[0, 1[`. `--learning-curve` trace la loss. Sur un split 80/20, l'accuracy est d'environ 0,97.

## Modèle

Les valeurs manquantes sont remplacées par la médiane du train, puis les notes sont standardisées. Arithmancy, Care of Magical Creatures et Defense Against the Dark Arts sont écartées : elles n'aident pas à séparer les maisons. Un classifieur est entraîné par maison. `model.json` conserve les moyennes, les écarts-types, les médianes et les poids, pour que la prédiction réapplique le même prétraitement.
