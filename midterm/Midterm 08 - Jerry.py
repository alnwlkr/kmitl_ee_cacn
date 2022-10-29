n = int(input())
mpos = []
hpos = []
for i in range(n):
    mpos.append(int(input()))
for i in range(n):
    hpos.append(int(input()))
mpos.sort()
hpos.sort()
sec = []
for i in range(n):
    sec.append(abs(mpos[i] - hpos[i]))
print(max(sec))