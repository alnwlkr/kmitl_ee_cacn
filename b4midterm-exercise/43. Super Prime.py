#43. Super Prime
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

def prime_pos(n):
    pos = 0
    for i in range(1,n + 1):
        if(is_prime(i)):
            pos += 1
    return pos

def super_prime(n):
    return is_prime(prime_pos(n))

n = int(input())
if (is_prime(n)):
    if (super_prime(n)):
        print('Yes')
else:
    print('No')