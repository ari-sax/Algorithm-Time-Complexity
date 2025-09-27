/** 
 * @author Aryan Saxena
 * Purpose: Measure runtime of nested loops algorithm repeatedly for smoother experimental results
 */
public class ComplexityExperiment {
    public static void main(String[] args) {
        int[] nValues = {1000, 3000, 10000, 30000, 100000, 300000, 1000000, 3000000, 10000000, 30000000, 100000000};
        
        for (int n : nValues) {
            // Initialize arrays
            double[] a = new double[n];
            double[] b = new double[n];
            for (int i = 0; i < n; i++) {
                a[i] = Math.random();
                b[i] = Math.random();
            }

            long startTime = System.nanoTime();
            double sum = 0;
            int repetitions = 10000; // repeat the snippet many times
            
            for (int rep = 0; rep < repetitions; rep++) {
                int j = 5;
                while (j < Math.log(n)) {
                    int k = 5;
                    while (k < n) {
                        sum += a[j] * b[k];
                        k = (int) Math.pow(k, 1.5);
                    }
                    j = (int) (1.2 * j);
                }
            }
            
            long endTime = System.nanoTime();
            long elapsed = endTime - startTime;

            System.out.println("n = " + n + " | Time = " + elapsed + " ns");
        }
    }
}