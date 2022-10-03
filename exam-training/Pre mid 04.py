#Pre mid 04.py
def mylen(x):
    return len(x)*-1
lst = []
while True:
    x = input().strip()
    if x == '~END~':
        break
    else:
        lst.append(x)
lst.sort()
lst.sort(key=mylen)
print(*lst,sep='\n')