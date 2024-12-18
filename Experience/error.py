import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le CSV
data = pd.read_csv("XP_piJava.txt", delimiter=";")

# Remplacer la virgule par un point pour que les erreurs puissent être lues comme des float
data["Error"] = data["Error"].str.replace(",", ".").astype(float)

# Filtrer les données pour ne garder que celles avec NumProc == 4
data_filtered = data[data['NumProc'] == 4]

# Calculer la médiane de l'erreur pour chaque groupe Npoint
medians = data_filtered.groupby('Npoint')['Error'].median().reset_index()

# Créer un nuage de points (scatter plot) pour les données filtrées
plt.figure(figsize=(10, 6))
plt.scatter(data_filtered['Npoint'], data_filtered['Error'], color='k', marker='o', label="Données")

# Ajouter les médianes sous forme de points rouges
plt.scatter(medians['Npoint'], medians['Error'], color='r', marker='o', label="Médiane de l'erreur")

# Tracer une ligne passant par les médianes
plt.plot(medians['Npoint'], medians['Error'], color='r', linestyle='-', linewidth=1.5, label="Ligne des médianes")


# Ajouter un titre et des labels
plt.title("Erreur en fonction du nombre de points (Npoint) pour NumProc = 4 avec Médiane")
plt.xlabel("Nombre de points (Npoint)")
plt.ylabel("Erreur")

# Mettre les axes en échelle logarithmique
plt.xscale('log')
plt.yscale('log')

# Ajouter une légende pour identifier les points de données et les médianes
plt.legend()

# Afficher le graphique
plt.show()
