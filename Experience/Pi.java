import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Pi {
    public static void main(String[] args) throws Exception {
        if (args.length < 4) {
            System.out.println("Usage: java Pi <numWorkers> <numIterations> <scalabilityType> <numRepetition>");
            System.out.println("<scalabilityType>: 'strong' or 'weak'");
            return;
        }

        // Utiliser long au lieu de int pour gérer les grandes valeurs
        int numWorkers = Integer.parseInt(args[0]);
        long totalIterations = Long.parseLong(args[1]);  // Changer en long pour accepter des grandes valeurs
        String scalabilityType = args[2];
	int numRepetition = Integer.parseInt(args[3]);

        long iterationsPerWorker;
        if ("strong".equalsIgnoreCase(scalabilityType)) {
            iterationsPerWorker = totalIterations / numWorkers;
        } else if ("weak".equalsIgnoreCase(scalabilityType)) {
            iterationsPerWorker = totalIterations;
        } else {
            System.out.println("Invalid scalability type. Use 'strong' or 'weak'.");
            return;
        }
	
	for (int i = 0; i < numRepetition; ++i) {
            long executionTime = runExperiment(iterationsPerWorker, numWorkers);

	    // Experimentation results in CSV format for easier processing
            try (FileWriter fw = new FileWriter("XP_piJava.txt", true)) {
            	fw.write(String.format("%s;%d;%d;%d\n", scalabilityType.equalsIgnoreCase("strong") ? "1" : "2",numWorkers, totalIterations, executionTime));
            }
        }
        
        
    }

    private static long runExperiment(long iterationsPerWorker, int numWorkers) throws InterruptedException, ExecutionException {
        long startTime = System.currentTimeMillis();

        List<Callable<Long>> tasks = new ArrayList<>();
        for (int i = 0; i < numWorkers; ++i) {
            tasks.add(new Worker(iterationsPerWorker));
        }

	ExecutorService exec = Executors.newFixedThreadPool(numWorkers);
        List<Future<Long>> results = exec.invokeAll(tasks);
	long total = 0;
    
	// Assemble the results.
	for (Future<Long> f : results)
	    {
		// Call to get() is an implicit barrier.  This will block
		// until result from corresponding worker is ready.
		total += f.get();
	    }
	double pi = 4.0 * total / iterationsPerWorker / numWorkers;
        long stopTime = System.currentTimeMillis();

	exec.shutdown();
        return stopTime - startTime; // Return execution time in milliseconds
    }
}

class Worker implements Callable<Long> {
    private long numIterations;  // Utiliser long pour gérer des itérations plus grandes

    public Worker(long num) {
        this.numIterations = num;
    }

    @Override
    public Long call() {
        long circleCount = 0;
        Random prng = new Random();
        for (long j = 0; j < numIterations; j++) {  // Boucle avec long
            double x = prng.nextDouble();
            double y = prng.nextDouble();
            if ((x * x + y * y) < 1) ++circleCount;
        }
        return circleCount;
    }
}
