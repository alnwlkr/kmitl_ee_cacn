#55. Is Palindrome ?
def pld(st):
    i = 0
    n = len(st) - 1
    rev = []
    while (n >= 0):
        rev.append(st[n])
        n -= 1
    rev = ''.join(rev)
    return (st == rev)
    
st = input()
st = st.replace(" ","")
if (len(st) > 0 and len(st) <= 100):
    if (pld(st)):
        print('It is Palindrome.')
    else:
        print('It is not Palindrome.')