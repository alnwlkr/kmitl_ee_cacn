#31. Easy Loop

n = int(input())

while (n != 0):
    if (n > 0):
        print(n, '', end='')
        n -= 1
    else:
        print(n, '', end='')
        n += 1
print(n, end='')
