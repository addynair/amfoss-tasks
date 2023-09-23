defmodule PrimeFinder do
  def is_prime(2), do: true
  def is_prime(n) when n > 2 do
    not Enum.any?(2..(n - 1), fn x -> rem(n, x) == 0 end)
  end

  def find_primes(n) when n >= 2 do
    Enum.filter(2..n, &is_prime/1)
  end

  def find_primes(1), do: []
  def find_primes(0), do: []
  def find_primes(_), do: IO.puts("Invalid input. Please enter a positive integer.")

  def start do
    IO.puts("Enter a positive integer (n):")
    case IO.read(:line) |> String.trim() |> String.to_integer() do
      n when n >= 0 -> IO.inspect(find_primes(n))
      _ -> IO.puts("Invalid input. Please enter a positive integer.")
    end
  end
end

PrimeFinder.start()
