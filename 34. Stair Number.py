#34. Stair Number
n = int(input())
if (n < 0):
    exit()
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j,'', end='')
    print('')