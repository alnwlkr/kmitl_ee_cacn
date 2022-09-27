while True:
    num = int(input())
    if (num >= 1 and num <= 20):
        break

M = [2, 20, 8, 10, 4, 6, 16, 18]
N = [1, 3, 9, 7, 11, 15, 19]
if (num in M or num in N):
    if(num in M):
        print(num," is in M at index [",M.index(num),"]",sep='')
    else: 
        print(num," is in N at index [",N.index(num),"]",sep='')
else:
    print(num,"is not in neither M nor N")