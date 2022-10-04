#Pre mid 06.py
time = input()
tl = time.split()
if tl[3] == 'AM':
    if tl[0] == '12':
        tl[0] = '0'
elif tl[3] == 'PM':
    if tl[0] != '12':
        tl[0] = str(int(tl[0]) + 12)

print(tl[0],tl[1],tl[2],sep=':')