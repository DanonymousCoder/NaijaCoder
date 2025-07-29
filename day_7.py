# 1. Implement linear_search_while(lst, target) using a while loop
# and count the #ops.
# 2. Implement sum_linear_search_while(lst) to sum all
# elements in a list and count the #ops.
# 3. Find the smallest element in a list using binary search.
# 3. Count the number of target element using binary search

# 1.

def linear_search_while(lst, target):
  ops = 0
  n = 0

  while n < len(lst):
    ops = ops + 1
    
    if lst[n] == target:
      print(f"Number found at index {n} after {ops} iterations")
      n = n+1
    else: n = n+1

  return n
test = [1, 2, 3, 4, 5]
target = 3

result = linear_search_while(test, target)

if result == -1:
  print(f"Not found")







def sum_linear_search_while(lst):
  if len(lst) == 0:
    return 0
  
  return lst[0] + sum_linear_search_while(lst[1:])

sum_linear_search_while([1, 2, 3, 4, 5, 6])