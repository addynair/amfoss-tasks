package main

import (
    "fmt"
)

func ifPrime(num int) bool {
    if num <= 1 {
        return false
    }

    if num == 2 {
        return true
    }

    if num%2 == 0 {
        return false
    }

    for i := 3; i*i <= num; i += 2 {
        if num%i == 0 {
            return false
        }
    }

    return true
}

func main() {
    var n int
    fmt.Print("Enter n: ")
    fmt.Scan(&n)

    if n < 2 {
        fmt.Println("Not able to find prime numbers in the specified range.")
        return
    }

    fmt.Printf("Prime numbers up to %d are:\n", n)
    for i := 2; i <= n; i++ {
        if ifPrime(i) {
            fmt.Printf("%d ", i)
        }
    }
    fmt.Println()
}

