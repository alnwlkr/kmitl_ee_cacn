#45. Easy String
str1 = input()
str2 = input()
if (len(str1) <= 60 and len(str2) <= 60):
    lst1 = []
    lst2 = []
    for letter in str1:
        lst1.append(letter)
    for letter in str2:
        lst2.append(letter)
    #print(lst1)
    #print(lst2)
    inter = ''.join(x for x in lst1 if x in lst2)
    if (len(inter) != 0):
        print(inter)
    else:
        print('none')
    A_B = ''.join(x for x in lst1 if x not in lst2)
    if (len(A_B) != 0):
        print(A_B)
    else:
        print('none')
    B_A = ''.join(x for x in lst2 if x not in lst1)
    if (len(B_A) != 0):
        print(B_A)
    else:
        print('none')
    union = str1 + B_A
    if (len(union) != 0):
        print(union)
    else:
        print('none')
else:
    print('none')