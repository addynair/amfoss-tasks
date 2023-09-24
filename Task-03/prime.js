
function isPrime(n) {
  if (n <= 1) {
    return false;
  }

  
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }

  return true;
}

function printPrimesUpToN(n) {
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      console.log(i);
    }
  }
}


let n = parseInt("Enter a number:"); 
printPrimesUpToN(n);

