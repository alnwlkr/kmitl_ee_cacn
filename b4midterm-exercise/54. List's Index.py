#54. List's Index
M = [2, 20, 8, 10, 4, 6, 16, 18]
N = [1, 3, 9, 7, 11, 15, 19]
while(True):
    x = int(input())
    if (x >= 1 and x <= 20):
        if (x in N):
            i = N.index(x)
            print(x, ' is in N at index [', i, ']', sep='')
            quit()
        elif (x in M):
            i = M.index(x)
            print(x,' is in M at index [',i,']',sep='')
            quit()
        else:
            print(x, 'is not in neither M nor N')
            quit()