ifPrime :: Int -> Bool
ifPrime n
    | n <= 1 = False
    | n == 2 = True
    | n `mod` 2 == 0 = False
    | otherwise = not $ any (\x -> n `mod` x == 0) [3,5..isqrt n]
    where isqrt = floor . sqrt . fromIntegral

findPrimes :: Int -> [Int]
findPrimes n
    | n < 2 = []
    | otherwise = [x | x <- [2..n], ifPrime x]

main :: IO ()
main = do
    putStrLn "Enter n: "
    nStr <- getLine
    let n = read nStr :: Int
    let primes = findPrimes n
    putStrLn $ "Prime numbers up to " ++ show n ++ " are: " ++ unwords (map show primes)

