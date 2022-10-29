#57. Reverse word-1
def rev(st):
    i = 0
    n = len(st) - 1
    rev = []
    while (n >= 0):
        rev.append(st[n])
        n -= 1
    rev = ''.join(rev)
    return(rev)
st = input()
if (len(st) > 0 and len(st) <= 100):
    print(rev(st))