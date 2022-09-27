#25. Coin Reward

n = float(input())
if n >= 0 and n <= 500:
  c = 0.05*n
elif n <= 5000:
  c = 25 + 0.10*(n - 500)
elif n <= 10000:
  c = 475 + 0.15*(n - 5000)
elif n <= 20000:
  c = 1225 + 0.20*(n - 10000)
elif n <= 50000:
  c = 3225 + 0.25*(n - 20000)
else:
  c = 10725 + 0.30*(n - 50000)
print('%.2f' %(c))