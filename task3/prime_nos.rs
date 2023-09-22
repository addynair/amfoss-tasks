use std::io;

fn if_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..=(num as f64).sqrt() as u32 {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    println!("Enter n :");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    let n: u32 = input
        .trim()
        .parse()
        .expect("Invalid input. Please enter again.");

    println!("Prime numbers up to {}:", n);

    for num in 2..=n {
        if if_prime(num) {
            println!("{}", num);
        }
    }
}

