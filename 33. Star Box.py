#33. Star Box
width = abs(int(input()))
height = abs(int(input()))

for i in range(0,height):
    for j in range(0,width):
        print('*', end='')
    print('')