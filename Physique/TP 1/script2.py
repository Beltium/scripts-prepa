import numpy as np
import matplotlib.pyplot as plt

# Paramètres
l = 1
u_l = 0.005 # Incertitude

g = 9.81
u_g = 0.01 # Incertitude

n = 3 # Nombre chiffres significatifs
N = 10000 # Nombre de simulations

# Calcul aléatoire des valeurs
valeurs_l = np.random.uniform(l-u_l, l+u_l, N)
valeurs_g = np.random.uniform(g-u_g, g+u_g, N)

# Calcul de la période
T = 2 * np.pi * np.sqrt(valeurs_l/valeurs_g)

# Statistiques
moyenne = np.mean(T)
incertitudetype = np.std(T, ddof=1)

# Affichage
print(f"Nombre de simulations : {N}")
print(f"Valeur moyenne : {moyenne:.{n-1}e}")
print(f"Incertitude-type composée : {incertitudetype:.{n-1}e}")

# Histogramme
plt.hist(T, bins = 100) # Histogramme avec 100 intervalles
plt.axvline(moyenne, color="red", label="Moyenne")
plt.xlabel("Période T (s)")
plt.ylabel("Nombre de simulations")
plt.title("Simulation aléatoire de la période du pendule")
plt.text(
    0.05, 0.95, # Position dans le cadre (entre 0 et 1)
    f"Moyenne = {moyenne:.{n-1}e}\n"
    f"Incertitude-type = {incertitudetype:.{n-1}e}",
    transform=plt.gca().transAxes, # Transformer les coordonnées en coordonnées entre 0 et 1
    verticalalignment="top"
)
plt.legend() # Afficher la légende
plt.show() # Afficher le plot