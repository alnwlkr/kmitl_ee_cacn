lst = ['NULL']
while True:
    temp = input()
    if temp == '~END~':
        break
    lst.append(temp)
def check(lst):
    for i in range(len(lst)):
        if lst[i] == 'black' and i % 13 == 0:
            if lst[15] == 'black':
                return True
            return False
        elif lst[i] == 'white' and i % 17 == 0:
            return True
        elif lst[i] == 'gray' and i % 2 == 0:
            if lst[i + 1] == 'white':
                return True
    return True
print(check(lst))