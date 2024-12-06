import java.io.*;
import java.net.*;


import static java.lang.Integer.parseInt;

/**
 * Worker is a server. It computes PI by Monte Carlo method and sends 
 * the result to Master.
 */
public class WorkerSocket {
    static int port = 25545; //default port
    private static boolean isRunning = true;
    
    /**
     * compute PI locally by MC and sends the number of points 
     * inside the disk to Master. 
     */
    public static void main(String[] args) throws Exception {

	if (!("".equals(args[0]))) port= parseInt(args[0]);
	System.out.println(port);
	System.out.println(port);
    ServerSocket s = new ServerSocket(port);
    System.out.println("Server started on port " + port);
    Socket soc = s.accept();

    // BufferedReader bRead for reading message from Master
    BufferedReader bRead = new BufferedReader(new InputStreamReader(soc.getInputStream()));

    // PrintWriter pWrite for writing message to Master
    PrintWriter pWrite = new PrintWriter(new BufferedWriter(new OutputStreamWriter(soc.getOutputStream())), true);
	String str;
    while (isRunning) {
	    str = bRead.readLine();          // read message from Master
	    if (!(str.equals("END"))){
            System.out.println("Server receives totalCount = " +  str);

            // pWrite.println(str);         // send number of points in quarter of disk

            //str = monteCarlo(parseInt(str));
            long total;
            total = new Master().doRun(parseInt(str), 1);

            pWrite.println(""+total);         // send total of points in quarter of disk

	    }else{
		isRunning=false;
	    }	    
        }
        bRead.close();
        pWrite.close();
        soc.close();
   }

   public String monteCarlo(int nbIteration) {
       int total = 0;
       // compute
       for (int j = 0; j < nbIteration ; j++){
           double x = Math.random();
           double y = Math.random();
           if (x * x + y * y <= 1){
               total ++;
           }
       }
       return String.valueOf(total);
   }
}