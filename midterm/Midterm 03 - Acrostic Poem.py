lst = []
while True:
    temp = input()
    if temp == '~END~':
        break
    lst.append(temp)
for i in range(len(lst)):
    print(lst[i][0],end='')
print()