import numpy as np
import matplotlib.pyplot as plt

# Paramètres
l = 554e-3
u_l = 0.7e-3 # Incertitude

T = 1.493
u_T = 0.002 # Incertitude

n = 5 # Nombre chiffres significatifs
N = 1000 # Nombre de simulations

# Calcul aléatoire des valeurs
valeurs_l = np.random.uniform(l-u_l, l+u_l, N)
valeurs_T = np.random.uniform(T-u_T, T+u_T, N)

# Calcul de g
g = (4 * (np.pi)**2 * valeurs_l)/(valeurs_T**2)

# Statistiques
moyenne = np.mean(g)
incertitudetype = np.std(g, ddof=1)

# Affichage
print(f"Nombre de simulations : {N}")
print(f"Valeur moyenne : {moyenne:.{n-1}e}")
print(f"Incertitude-type composée : {incertitudetype:.{n-1}e}")

# Histogramme
plt.hist(g, bins = 100) # Histogramme avec 100 intervalles
plt.axvline(moyenne, color="red", label="Moyenne")
plt.xlabel("Valeurs de g (m.s^-2)")
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