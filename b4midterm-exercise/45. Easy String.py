#45. Easy String
def removedup(st):
    result=""
    for letter in st:
        if(letter in result):
            pass
        else:
            result += letter
    return result
str1 = input()
str2 = input()
if (len(str1) <= 60 and len(str2) <= 60):
    lst1 = []
    lst2 = []
    for letter in str1:
        lst1.append(letter)
    for letter in str2:
        lst2.append(letter)
    #INTERSECTION
    inter = ''.join(x for x in lst1 if x in lst2)
    inter = removedup(inter)
    if (len(inter) != 0):
        print(inter)
    else:
        print('none')
    #SET_A-B
    A_B = ''.join(x for x in lst1 if x not in lst2)
    A_B = removedup(A_B)
    if (len(A_B) != 0):
        print(A_B)
    else:
        print('none')
    #SET_B-A
    B_A = ''.join(x for x in lst2 if x not in lst1)
    B_A = removedup(B_A)
    if (len(B_A) != 0):
        print(B_A)
    else:
        print('none')
    #UNION = A + (B-A)
    union = str1 + B_A
    union = removedup(union)
    if (len(union) != 0):
        print(union)
    else:
        print('none')