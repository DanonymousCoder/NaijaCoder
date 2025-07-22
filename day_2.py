# 6(b)the prime factors of a given number using a for loop
def checkPrimeFac(n):
  primeFs = []

  for w in range(2, n+1):
    if (n % w) == 0:

      def checkPrime(n):
        for i in range(1, n):
          i = i + 1
          if w == 2:
            return w
          elif i < n:
            if (n % i) == 0:
              return 0
          else:
            return w
      
      if (checkPrime(w) != 0):
        primeFs.append(w)

  
  return {primeF for primeF in primeFs}

print(checkPrimeFac(130))