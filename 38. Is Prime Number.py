#38. Is Prime Number ?.py
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

if(is_prime(n)):
    print('Yes')
else:
    print('No')