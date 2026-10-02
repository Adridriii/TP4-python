import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
"""
Classe représentant un nœud dans un arbre d'expression.
"""
class Noeud :
    def __init__ (self, x):
        self.x = x
        self.enfants = []
        

    def ajouter_noeud(self, noeud_enfant):
        
        self.enfants.append(noeud_enfant)
        

    def afficher(self):
        print(self.x, end=" ")

        for enfant in self.enfants:
            enfant.afficher()
    #calculer la valeur du noeud en fonction de ses enfants
    def evaluer(self, x=None):
        
        if x is None:
            x = {}

        if isinstance(self.x, (int, float)):
                return float(self.x)

        val = str(self.x)

        if val not in ("+", "-", "*", "/", "exp", "log", "sin", "cos"):
            if val in x:
                return float(x[val])
            else:
                raise ValueError(
                    f"La variable '{val}' n'a pas de valeur associée dans le dictionnaire."
                )
        valeurs_enfants = [e.evaluer(x) for e in self.enfants]
        if val == "+":
            return valeurs_enfants[0] + valeurs_enfants[1]
        elif val == "-":
            return valeurs_enfants[0] - valeurs_enfants[1]
        elif val == "*":
            return valeurs_enfants[0] * valeurs_enfants[1]
        elif val == "/":
            return valeurs_enfants[0] / valeurs_enfants[1]

        # Fonctions unaires (exp, log, sin, cos)
        elif val == "exp":
            return math.exp(valeurs_enfants[0])
        elif val == "log":
            return math.log(valeurs_enfants[0])
        elif val == "sin":
            return math.sin(valeurs_enfants[0])
        elif val == "cos":
            return math.cos(valeurs_enfants[0])




        # Méthode pour tracer le graphe à partir de la chaine de caractère correspondant à la variable qu'on veut tracer
    def tracer(self, nom_variable, valeurs_variables):
            


        if valeurs_variables is None:
            valeurs_variables = np.linspace(-5, 2, 400)
        y_values = []

        for val in valeurs_variables:
            # Évaluer l'expression pour chaque valeur de x
            y = self.evaluer({nom_variable: val})
            y_values.append(y)

        # Tracer le graphe
        plt.plot(valeurs_variables, y_values)
        plt.title(f"Graphe de l'expression avec {nom_variable}")
        plt.xlabel(nom_variable)
        plt.ylabel("f(x)")
        plt.grid()
        plt.savefig("graphe.png")
        print("Graphique sauvegardé sous 'graphe.png'")
        