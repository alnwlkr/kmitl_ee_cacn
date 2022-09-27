#36. Star Triangle again.py
n = int(input()) + 1

for i in range(1,n):
  for j in range(i):
    print('*', end='')
  print('')