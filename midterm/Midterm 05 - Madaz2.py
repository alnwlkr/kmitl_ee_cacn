old = input().lower().replace(' ','')
new = input().lower().replace(' ','')

lold = list(old)
lnew = list(new)

for i in lnew[:]:
    if i in lold:
        lnew.remove(i)
        lold.remove(i)

print(len(lnew) == 0)