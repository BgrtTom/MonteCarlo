import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

class PiMonteCarlo {
    AtomicInteger nAtomSuccess;
    long nThrows; // Utilisation de long pour gérer des nombres plus grands
    double value;
    int nProcessors; // Nombre de processeurs pour la gestion des threads

    // Classe interne pour les tâches de calcul
    class MonteCarlo implements Runnable {
        @Override
        public void run() {
            double x = Math.random();
            double y = Math.random();
            if (x * x + y * y <= 1) {
                nAtomSuccess.incrementAndGet();
            }
        }
    }

    // Constructeur avec le nombre de lancers et le nombre de processus
    public PiMonteCarlo(long i, int p) {
        this.nAtomSuccess = new AtomicInteger(0);
        this.nThrows = i; // Nombre total de lancers
        this.value = 0;
        this.nProcessors = p;
    }

    // Méthode pour obtenir une estimation de Pi
    public double getPi() {
        ExecutorService executor = Executors.newFixedThreadPool(nProcessors); // Utilisation de nProcessors pour le pool de threads
        for (long i = 1; i <= nThrows; i++) {
            executor.execute(new MonteCarlo());
        }
        executor.shutdown();
        while (!executor.isTerminated()) {
            // Attente que toutes les tâches soient terminées
        }
        value = 4.0 * nAtomSuccess.get() / nThrows; // Calcul de Pi
        return value;
    }

    // Accesseurs
    public AtomicInteger getnAtomSuccess() {
        return nAtomSuccess;
    }

    public int getnProcessors() {
        return nProcessors;
    }
}

public class Assignment102 {
    public static void main(String[] args) {
        // Vérification des arguments
        if (args.length < 4) {
            System.out.println("Usage: java Assignment102 <numProc> <numIterations> <numRepetition>");
            System.out.println("<numProc>: Number of processes (1, 2, 4, 8, 16)");
            System.out.println("<numIterations>: Total number of iterations (e.g., 16000000, 160000000)");
	    System.out.println("<scalabilityType>: 'strong' or 'weak'");
            System.out.println("<numRepetition>: Number of runs to perform for each configuration");
            return;
        }

        // Lecture des arguments
        int numProc = Integer.parseInt(args[0]);
        long numIterations = Long.parseLong(args[1]);
	String scalabilityType = args[2];
        int numRepetition = Integer.parseInt(args[3]);


        // Exécution des expériences
        for (int i = 0; i < numRepetition; i++) {
            PiMonteCarlo piVal = new PiMonteCarlo(numIterations, numProc);
            long startTime = System.currentTimeMillis();
            double value = piVal.getPi();
            long stopTime = System.currentTimeMillis();

            // Écriture des résultats dans le fichier
            try (FileWriter fw = new FileWriter("XP_assignement102.txt", true)) {
                fw.write(String.format("%s;%d;%d;%d\n",
                        scalabilityType.equalsIgnoreCase("strong") ? "1" : "2", numProc, numIterations, stopTime - startTime));
            } catch (IOException ioe) {
                System.err.println("IOException: " + ioe.getMessage());
            }
        }
    }
}
