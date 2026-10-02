from noeud import Noeud
import matplotlib
import numpy as np

n_deux = Noeud(2)
n_y = Noeud("y")

# 2. Création de l'opération d'addition (2 + y)
n_add = Noeud("+")
n_add.ajouter_noeud(n_deux)
n_add.ajouter_noeud(n_y)

# 3. Création de la racine exp(...)
racine = Noeud("exp")
racine.ajouter_noeud(n_add)
racine.afficher()

y = {"y": 3.0}  # Dictionnaire avec la valeur de y
try:
    racine.evaluer(y)  # Dictionnaire vide
except ValueError as e:
    print(e)  # Affiche l'erreur si y n'a pas de valeur associée

print("Résultat :", racine.evaluer(y))


#appel de la méthode tracer
valeurs_y = np.linspace(-5, 2, 200)
racine.tracer("y", valeurs_y)