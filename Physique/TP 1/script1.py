import numpy as np
import matplotlib.pyplot as plt

# Paramètres
valeurs = np.array([
   14.97, 14.91, 15.00, 14.94, 14.93, 14.94, 14.91, 14.94, 14.88, 14.84
]) # Valeurs mesurées
n = 5 # Nombre de chiffres significatifs dans les résultats

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
plt.hist(valeurs, bins=5) # Histogramme
plt.xlabel("Valeur mesurée")
plt.ylabel("Nombre de mesures")
plt.title("Distribution des mesures")
plt.axvline(moyenne, color="red", label="Moyenne") # Ligne verticale de la moyenne
plt.text(
    0.05, 0.95, # Position dans le cadre (entre 0 et 1)
    f"Moyenne = {moyenne:.{n-1}e}\n"
    f"Écart-type = {ecarttype:.{n-1}e}\n"
    f"Incertitude-type = {incertitudetype:.{n-1}e}",
    transform=plt.gca().transAxes, # Transformer les coordonnées en coordonnées entre 0 et 1
    verticalalignment="top"
)
plt.legend() # Afficher la légende
plt.show() # Afficher le plot



