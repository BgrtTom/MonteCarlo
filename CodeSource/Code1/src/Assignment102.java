// Estimate the value of Pi using Monte-Carlo Method, using parallel program
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
class PiMonteCarlo {
	AtomicInteger nAtomSuccess;
	int nThrows;
	double value;
	int nProcessors = 1; /* Runtime.getRuntime().availableProcessors(); nb processeur */
	class MonteCarlo implements Runnable {
		@Override
		public void run() {
			double x = Math.random();
			double y = Math.random();
			if (x * x + y * y <= 1)
				nAtomSuccess.incrementAndGet();
		}
	}
	public PiMonteCarlo(int i) {
		this.nAtomSuccess = new AtomicInteger(0);
		this.nThrows = i;
		this.value = 0;
	}
	public double getPi() {
		ExecutorService executor = Executors.newWorkStealingPool(nProcessors);
		for (int i = 1; i <= nThrows; i++) {
			Runnable worker = new MonteCarlo();
			executor.execute(worker);
		}
		executor.shutdown();
		while (!executor.isTerminated()) {
		}
		value = 4.0 * nAtomSuccess.get() / nThrows;
		return value;
	}

	public AtomicInteger getnAtomSuccess() {
		return nAtomSuccess;
	}
	public int getnProcessors() {
		return nProcessors;
	}
}
public class Assignment102 {
	public static void main(String[] args) {
		int ntot = 1000000;
		PiMonteCarlo PiVal = new PiMonteCarlo(ntot);
		long startTime = System.currentTimeMillis();
		double value = PiVal.getPi();
		long stopTime = System.currentTimeMillis();
		System.out.println("\nApprox value: " + value);
		System.out.println("Error: " + (Math.abs((value - Math.PI)) / Math.PI));
		System.out.println("Ntot: " + ntot);
		System.out.println("Ncible: " + PiVal.getnAtomSuccess());
		System.out.println("Difference to exact value of pi: " + (value - Math.PI));
		System.out.println("Available processors: " + PiVal.getnProcessors());
		System.out.println("Time Duration (ms): " + (stopTime - startTime));

		System.out.println( (value +";"+ Math.abs((value - Math.PI)) / Math.PI) +";"+ ntot +";"+ PiVal.getnProcessors() +";"+ (stopTime - startTime));

		try {
			FileWriter fw = new FileWriter("XP_assignement102.txt",true);
			fw.write((value +";"+ Math.abs((value - Math.PI)) / Math.PI) +";"+ ntot +";"+ PiVal.getnAtomSuccess() +";"+ PiVal.getnProcessors() +";"+ (stopTime - startTime) + "\n");
			fw.close();
		} catch (IOException ioe) {
			System.err.println("IOException: " + ioe.getMessage());
		}
	}
}

/*nb point / nb processus / nb cible / temps / erreur /pi*/