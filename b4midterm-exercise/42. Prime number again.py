#42. Prime number again.py
#Note no need to strip white space at the end of the line
import math

def is_prime(n):
  if (n < 2):
      return False
  i = 2
  if (n == 2):
      return True
  while(i <= (math.sqrt(n))):
    if (n % i == 0):
      return False
    i += 1
  return True

n1 = int(input())
n2 = int(input())

check = 0

if (n1 <= n2):
  for i in range(n1 + 1, n2, 1):
    if(is_prime(i) and i != n2):
      print(i, end=' ')
      check = 1
    elif(is_prime(i) and i == n2):
      print(i, end='')
      check = 1
else:
  for i in range(n1 - 1, n2, -1):
    if(is_prime(i) and i != n2):
      print(i, end=' ')
      check = 1
    elif (is_prime(i) and i == n2):
      print(i, end='')
      check = 1

if (check == 0):
  print('Null')