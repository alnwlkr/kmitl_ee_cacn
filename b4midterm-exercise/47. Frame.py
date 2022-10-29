#47. Frame
str = input()
for i in range(len(str) + 2):
    print('*',end='')
print()
print('*',end='')
print(str, '*', sep='')
for i in range(len(str) + 2):
    print('*',end='')