#31. Easy Loop

n = int(input())

i = 0
arr = [0] *(n + 1)
while (n != 0):
    if (n > 0):
        print(n, '', end='')
        n -= 1
    else:
        print(n, '', end='')
        n += 1
print(n, end='')