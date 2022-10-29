lst = []
for i in range(10):
    lst.append(float(input()))
lst.sort()
print('%.2f' %(min(lst)))
print('%.2f' %(max(lst)))