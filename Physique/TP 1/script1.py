import numpy as np
import matplotlib.pyplot as plt

# Paramètres
valeurs = np.array([
    9.8, 10.2, 10.1, 9.9, 10.0,
    10.3, 9.7, 10.1, 9.8, 10.2,
    10.0, 9.9, 10.1, 10.2, 9.8,
    10.0, 9.7, 10.3, 10.1, 9.9
]) # Valeurs mesurées
n = 3 # Nombre de chiffres significatifs dans les résultats

# Calcul statistique
moyenne = np.mean(valeurs)
ecarttype = np.std(valeurs, ddof=1)
incertitudetype = ecarttype/np.sqrt(len(valeurs))

# Affichage
print(f"Statistiques sur les {len(valeurs)} valeurs :")
print(f"La moyenne est de {moyenne:.{n-1}e}.")
print(f"L'écart-type est de {ecarttype:.{n-1}e}.")
print(f"L'incertitude-type est de {incertitudetype:.{n-1}e}.")

# Plot
plt.hist(valeurs)
plt.xlabel("Valeur mesurée")
plt.ylabel("Nombre de mesures")
plt.title("Distribution des mesures")
plt.axvline(moyenne, color="red", label="Moyenne")
plt.text(
    0.05, 0.95,
    f"Moyenne = {moyenne:.{n-1}e}\n"
    f"Écart-type = {ecarttype:.{n-1}e}\n"
    f"Incertitude-type = {incertitudetype:.{n-1}e}",
    transform=plt.gca().transAxes,
    verticalalignment="top"
)
plt.show()



