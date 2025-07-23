# Exercises:
# 1. Implement a function to count the number of items of a specific value.
# e.g., count([1, 2, 2, 3, 2, 1, 2, 3, 4], 2) -> 4

# 2. Implement a function to return the index of the first occurrence of a value.
# e.g., index([1, 2, 2, 3, 2, 1, 2, 3, 4, 5, 2], 4) -> 8

# 3. Sum of Numbers: Write a function that calculates the sum of all numbers from
# 1 to n using a for loop.

# 4. Even Numbers: Write a function that prints all even numbers from 1 to n
# using a for loop.

# 5. Factorial: Write a function to compute the factorial of a number n
# using a for loop.

# 6. Prime Factorization: Write a function that returns the prime factors of a
# given number using a for loop.
# (a)If a number is prime
# (b)the prime factors of a given number using a for loop
# 6(b)the prime factors of a given number using a for loop

def determ(dlist, dnum):
  count = 0
  for i in range(len(dlist)):
    if dlist[i] == dnum:
      count = count + 1
  return count

determ([1, 2, 2, 2, 3, 4, 5], 2)




def firstOcc(dlist, dnum):
  occurrence = ""
  times = 0
  for i in range(len(dlist)):
    if dlist[i] == dnum and times == 0:
      occurence = i
      times = 1
  return occurence
firstOcc([1, 2, 2, 2, 3, 4, 5], 2)



def sum(n):
  countS = 0
  for i in range(1, n+1):
    countS = countS + i
  return countS

sum(3)



def evenN(n):
  countE = 0
  evenL = []
  for i in range(0, n+1):
    if countE < n:
      countE = i + 2
      if (countE % 2) != 0:
        countE += 0
      else:
       evenL.append(countE)

  return evenL

evenN(12)



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