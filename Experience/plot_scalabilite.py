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
    ax.set_title('Scalabilité forte : Speed-up')
    ax.grid(True)

def faible_speedup(ax, df):
    df_filtered = df[df['Scenario'] == "2"]
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
    ax.set_title('Scalabilité faible : Speed-up')
    ax.grid(True)

def forte(ax, df):
    df_filtered = df[df['Scenario'] == "1"]

    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    ax.plot(df_mean['NumProc'], df_mean['ExecutionTime'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Temps d\'exécution moyen (ms)')
    ax.set_title('Scalabilité forte : Temps d\'exécution')
    ax.grid(True)

def faible(ax, df):
    df_filtered = df[df['Scenario'] == "2"]

    df_filtered['ExecutionTime'] = pd.to_numeric(df_filtered['ExecutionTime'], errors='coerce')
    df_filtered['NumProc'] = pd.to_numeric(df_filtered['NumProc'], errors='coerce')

    df_mean = df_filtered.groupby('NumProc')['ExecutionTime'].mean().reset_index()

    ax.plot(df_mean['NumProc'], df_mean['ExecutionTime'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Nombre de processus (NumProc)')
    ax.set_ylabel('Temps d\'exécution moyen (ms)')
    ax.set_title('Scalabilité faible : Temps d\'exécution')
    ax.grid(True)


# Création de la figure et des sous-graphiques
fig, axs = plt.subplots(4, 2, figsize=(15, 20))

# Chargement et tracé pour file_path1
df = pd.read_csv(file_path1, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])

# Supposons que la première ligne est l'entête si header=None
forte(axs[0, 0], df)
forte_speedup(axs[1, 0], df)

df = pd.read_csv(file_path1, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
faible(axs[2, 0], df)
faible_speedup(axs[3, 0], df)


# Chargement et tracé pour file_path2
df = pd.read_csv(file_path2, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
forte(axs[0, 1], df)
forte_speedup(axs[1, 1], df)

df = pd.read_csv(file_path2, sep=';', header=None, names=['Scenario', 'NumProc', 'NumIterations', 'ExecutionTime'])
faible(axs[2, 1], df)
faible_speedup(axs[3, 1], df)


# Ajustement de l'espacement
plt.tight_layout()
plt.show()
