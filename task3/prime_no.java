import java.util.ArrayList;
import java.util.List;

public class PrimeNumbers {
    public static boolean ifPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number == 2) {
            return true;
        }
        if (number % 2 == 0) {
            return false;
        }

        for (int i = 3; i * i <= number; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static List<Integer> findPrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (ifPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    public static void main(String[] args) {
        System.out.print("Enter n: ");
        int n = Integer.parseInt(System.console().readLine());

        if (n < 2) {
            System.out.println("Please enter number greater than or equal to 2.");
        } else {
            List<Integer> primeNumbers = findPrimes(n);
            System.out.println("Prime numbers up to " + n + ":");
            for (int prime : primeNumbers) {
                System.out.print(prime + " ");
            }
            System.out.println();
        }
    }
}

