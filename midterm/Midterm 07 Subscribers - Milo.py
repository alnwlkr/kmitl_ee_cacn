#Midterm 07 Subscribers

def delsuf(slst):
   if (len(slst) == 3):

    if (slst[2] == 'K'):
        slst[1] = float(slst[1]) * 1_000
    elif (slst[2] == 'M'):
        slst[1] = float(slst[1]) * 1_000_000
    elif (slst[2] == 'B'):
        slst[1] = float(slst[1]) * 1_000_000_000
    slst[1] = int(slst[1])
    slst.pop(2)
   else:
    slst[1] = int(slst[1])
   return slst


lst = []
while (True):
    tmp = input()
    if tmp == '~END~':
        break
    lst.append(tmp)

for i in range(len(lst)):
    lst[i] = lst[i].split()

for i in range(len(lst)):
    lst[i] = delsuf(lst[i])

lst.sort(key = lambda x:(-1 * x[1], -len(x[0]), x[0].lower()))

for i in range(len(lst)):
    print(*lst[i], sep=' ')
