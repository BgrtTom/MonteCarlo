#!/bin/bash

# Initialiser le nombre de répétition
numRepetition=5

# Création ou réinitialisation du fichier de résultats
echo "Scenario;NumWorkers;NumIterations;ExecutionTime(ms)"


# Pour Pi.java
# Compilation de Pi.java
echo "Compiling Pi.java..."
javac Pi.java
if [ $? -ne 0 ]; then
    echo "Compilation failed. Exiting."
    exit 1
fi

# Scénario 1 : Scalabilité forte
echo "Running Scenario 1: Strong Scalability"
fixed_iterations=160000000
for workers in 1 2 4 6 8 12 16; do
    echo "Workers: $workers, Iterations: $fixed_iterations"
    java Pi "$workers" "$fixed_iterations" strong "$numRepetition"
done

# Scénario 2 : Scalabilité faible
echo "Running Scenario 2: Weak Scalability"
for workers in 1 2 4 6 8 12 16; do
    for iterations_base in 10000000; do
        iterations=$((iterations_base * workers))
        echo "Workers: $workers, Iterations: $iterations"
        java Pi "$workers" "$iterations" weak "$numRepetition"
    done
done



# Pour Assignment102
# Compilation de Assignement102.java
echo "Compiling Assignement102.java..."
javac Assignment102.java
if [ $? -ne 0 ]; then
    echo "Compilation failed. Exiting."
    exit 1
fi

# Scénario 1 : Scalabilité forte
echo "Running Scenario 1: Strong Scalability"
fixed_iterations=160000000
for proc in 1 2 4 6 8 12 16; do
    echo "Proc: $proc, Iterations: $fixed_iterations"
    java Assignment102 "$proc" "$fixed_iterations" strong "$numRepetition"
done

# Scénario 2 : Scalabilité faible
echo "Running Scenario 2: Weak Scalability"
for proc in 1 2 4 6 8 12 16; do
    for iterations_base in 10000000; do
        iterations=$((iterations_base * proc))
        echo "proc: $proc, Iterations: $iterations"
        java Assignment102 "$proc" "$iterations" weak "$numRepetition"
    done
done

echo "Experiments completed."

# Exécution du script Python pour générer les graphiques
echo "Running plot_scalabilite.py to generate plots..."

python3 plot_scalabilite.py

echo "Plot completed."

