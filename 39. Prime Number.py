#39. Prime Number
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

n = int(input())
for i in range(2,n+1):
    if(is_prime(i)):
        print(i, end=' ')