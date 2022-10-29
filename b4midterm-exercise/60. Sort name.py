#60. Sort name
lst = []
for i in range(20):
    lst.append(input().lower().title())
lst = sorted(lst)
print(*lst,sep="\n")