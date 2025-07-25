# Exercises:
# 1. Factorial Recursion:
# Rewrite the factorial fraction using recursion.
# 2. Fibonacci Recursion:
# Write a recursive function to compute the Fibonacci
# sequence up to n numbers.
# 3. Sum of Digits
# Write a recursive function to calculate the sum of digits
# of a positive integer.
# 4. Palindrome Check:
# Write a recursive function to check if a given string is a
# palindrome.

def facRec(num):
  if num <= 1:
    return 1

  return num * facRec(num-1)

facRec(8)





def fibRec(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1

  return fibRec(num-1) + fibRec(num-2)

fibRec(9)





def sumPos(num):
  if num == 0:
    return 0
  
  return num + sumPos(num - 1)

print(sumPos(102))