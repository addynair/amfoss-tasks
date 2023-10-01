#include <iostream>

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }

    if (num == 2) {
        return true;
    }

    if (num % 2 == 0) {
        return false;
    }

    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    if (n < 2) {
        std::cout << " No prime numbers in the specified range." << std::endl;
        return 0;
    }

    std::cout << "Prime numbers up to " << n << " are:" << std::endl;
    for (int i = 2; i <= n; ++i) {
        if (isPrime(i)) {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}

