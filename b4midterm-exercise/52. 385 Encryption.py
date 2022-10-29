#52. 385 Encryption
def decode (st):
    i = 0
    n = len(st)
    st2 = []
    while (i < n):
        if (i % 3 == 0):
            temp = chr(ord(st[i]) - 3)
        elif (i % 3 == 1):
            temp = chr(ord(st[i]) - 8)
        else:
            temp = chr(ord(st[i]) - 5)
        if (ord(temp) < 97):
            temp = chr(ord(temp) + 26)
        elif (ord(temp) > 122):
            temp = chr(ord(temp) - 26)
        st2.append(temp)
        i += 1
    return (''.join(st2))

st = input()
if (len(st) <= 50):
    st = st.lower()
    print(decode(st))