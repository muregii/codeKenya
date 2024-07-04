public class Fibonacci {

    /**
     * Calculates the nth term in the Fibonacci sequence using recursion.
     *
     * return The nth term in the Fibonacci sequence.
     */
    public static int fibonacci(int n) {
        if (n <= 1) {
            // Base cases: The first two terms are 0 and 1
            return n;
        } else {
            // Recursive case: F(n) = F(n-1) + F(n-2)
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }


}