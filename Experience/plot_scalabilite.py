import pandas as pd
import matplotlib.pyplot as plt

file_path1 = 'XP_piJava.txt'
file_path2 = 'XP_assignement102.txt'

def forte_speedup(ax, df):
    df_filtered = df[df['Scenario'] == "1"]

    # Convertir les colonnes nécessaires en entiers, en gérant les erreurs éventuelles
    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    sequential_time = df_mean['ExecutionTime'].iloc[0]
    df_mean['speedup'] = sequential_time / df_mean['ExecutionTime']

    ax.plot(df_mean['NumProc'], df_mean['speedup'], marker='o', linestyle='-', color='r')
    ax.plot([1, 12], [1, 12], '--b', label='Speedup idéal')
    ax.legend()
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Speed-up')
    ax.set_title('Scalabilité forte (pour 16*10^7 points) : Speed-up')
    ax.grid(True)

def faible_speedup(ax, df):
    df_filtered = df[df['Scenario'] == "2"]
    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    sequential_time = df_mean['ExecutionTime'].iloc[0]
    df_mean['speedup'] = sequential_time / df_mean['ExecutionTime']

    ax.plot(df_mean['NumProc'], df_mean['speedup'], marker='o', linestyle='-', color='r')
    ax.plot([1, 16], [1, 1], '--b', label='Speedup idéal')
    ax.legend()
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Speed-up')
    ax.set_title('Scalabilité faible (pour 10^7 points par Processus) : Speed-up')
    ax.grid(True)

def forte(ax, df):
    df_filtered = df[df['Scenario'] == "1"]

    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    ax.plot(df_mean['NumProc'], df_mean['ExecutionTime'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Temps d\'exécution moyen (ms)')
    ax.set_title('Scalabilité forte (pour 16*10^7 points) : Temps d\'exécution')
    ax.grid(True)

def faible(ax, df):
    df_filtered = df[df['Scenario'] == "2"]
    print(df_filtered)
    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    ax.plot(df_mean['NumProc'], df_mean['ExecutionTime'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Temps d\'exécution moyen (ms)')
    ax.set_title('Scalabilité faible (pour 10^7 points par Processus) : Temps d\'exécution')
    ax.grid(True)


# Création de la figure et des sous-graphiques
fig, axs = plt.subplots(2, 2, figsize=(10, 15))

# Chargement et tracé pour file_path1
df = pd.read_csv(file_path1, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
forte(axs[0, 0], df)
forte_speedup(axs[1, 0], df)

#df = pd.read_csv(file_path1, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
#faible(axs[0, 0], df)
#faible_speedup(axs[1, 0], df)


# Chargement et tracé pour file_path2
df = pd.read_csv(file_path2, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
forte(axs[0, 1], df)
forte_speedup(axs[1, 1], df)

#df = pd.read_csv(file_path2, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
#faible(axs[0, 1], df)
#faible_speedup(axs[1, 1], df)

for row in range(2):  # Pour chaque ligne de graphes
    ymin = min(axs[row, 0].get_ylim()[0], axs[row, 1].get_ylim()[0])
    ymax = max(axs[row, 0].get_ylim()[1], axs[row, 1].get_ylim()[1])

    # Appliquer la même échelle de l'axe y à chaque colonne de la ligne
    axs[row, 0].set_ylim(ymin, ymax)
    axs[row, 1].set_ylim(ymin, ymax)



fig.text(0.25, 0.92, "Pi.java", ha='center', va='center', fontsize=14)
fig.text(0.75, 0.92, "Assignemeent102", ha='center', va='center', fontsize=14)

# Ajustement de l'espacement
plt.subplots_adjust(hspace=0.3)

fig.suptitle("Analyse de Scalabilité : Forte, pour Pi.java et Assignemeent102", fontsize=16)

plt.show()