# Basics of Python
# 0. Variables.
# 1. Functions. e.g len(a)
# 2. Strings
# 3. Loops(For Loops)
# 4. Lists
# 5. Range
# 7. Change a character to number and vice versa. e.g chr(74) ord("R")
# 8. Operators e.g addition, subtraction, modulus, floor(//) i.e without remainder, division, exponential(**), multiplication

a = 10
b = -5
a1 = 10.5
e = -3.14
g = 1.23e4 # = 1.23 x 10^{4}
h = 1.23e-4 # = 1.23 x 10^{-4}
a = "Hello\nWorld"
print(a)
a = "Hello" + "n" + "World"
print(a)

# Exercises
# ========
# 


welcome = "hello"
welcome2 = "world"
rewrite = ""
rewrite2 = ""

for w in range(len(welcome)):
  rewrite = welcome[w] + rewrite;

for w in range(len(welcome2)):
  rewrite2 = welcome2[w] + rewrite2;

print(rewrite)
print(rewrite2 + " " + rewrite)




cipher = "shift"
ciphered = ""

for c in cipher:
  cipheredn = ord(c)+3
  ciphered = ciphered + chr(cipheredn)
print(ciphered)





def conv(n):
  store = ""
  while(n>1):
    if(n % 2) == 1:
      store = "1" + store
    else:
      store = "0" + store
    n = n//2
  return store
conv(55)

def tryn(m):
  keep = ""
  while(m > 1):
    i = m % 2
    keep = str(i) + keep
    m = m//2
  return keep
tryn(55)