#Pre mid 02.py
def normalcheck(ms,cl,sp,zm):
    if zm == 'Y':
        if ms >= 2:
            if cl == 'Y' or sp <= 2:
                return True
    else:
        if ms >= 4:
            if cl == 'Y' or sp <= 2:
                return True
    return False
    
def rarecheck(ms,cl,sp,zm):
    if zm == 'Y':
        if ms >= 4:
            if cl == 'Y' or sp <= 1:
                return True
    else:
        if ms >= 6:
            if cl == 'Y' or sp <= 1:
                return True
    return False
    
ms = int(input())
cl = input()
sp = int(input())
zm = input()

nc = normalcheck(ms,cl,sp,zm)
rc = rarecheck(ms,cl,sp,zm)
if nc or rc:
    if nc:
        print('Normal Moly!!!')
    if rc:
        print('Rare Moly!! How cute!!!')
else:
    print('try again')