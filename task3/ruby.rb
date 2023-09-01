    def if_prime(number)
        return false if number <= 1
        (2..Math.sqrt(number)).none? { |i| number % i == 0 }
    end
    
    
    print "Enter n: "
    n = gets.chomp.to_i
    
    
    puts "Prime numbers up to #{n}:"
    (2..n).each { |number| puts number if if_prime(number) }
    
  