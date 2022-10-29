#59. Reverse word-3
st = input()
lst = st.split()
for word in lst:
    temp = list(word)
    temp.reverse()
    temp = ''.join(temp)
    print(temp, end=' ')