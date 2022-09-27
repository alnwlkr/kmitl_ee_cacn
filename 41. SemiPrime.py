#41. SemiPrime.py
import math
def checkSemiprime(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
            
        if cnt >= 2:
            break
        
    if(num > 1):
        cnt += 1
    return cnt == 2

def countSemiprime(n):
    cnt = 0
    for i in range(2, n + 1):
        if (checkSemiprime(i)):
            cnt += 1
    return cnt
n = int(input())

print(countSemiprime(n))