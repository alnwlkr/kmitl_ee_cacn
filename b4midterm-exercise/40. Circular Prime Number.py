#40. Circular Prime Number
import math

def is_prime(n) :
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
	
def isCircularPrime(n):
    #count digit to check
    cnt = len(str(n))
    
    for i in range(1,cnt + 1):
        num = n
        #สกัด i ตัวหลังออกมา
        last = num % (10**i)
        #แยกชุดหน้า
        first = num // (10**i)
        #last เชื่อม first
        num = last*(10**(cnt - i)) + first
        if (not is_prime(num)):
            return False
    if (num != n):
        return False
    return True

def	sumOfCurcularPrimeFrom_n(n):
    sum = 0
    for i in range(2, n + 1):
        if (isCircularPrime(i)):
            sum += i
    return sum

print(sumOfCurcularPrimeFrom_n(int(input())))