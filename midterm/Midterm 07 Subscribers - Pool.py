x = input()
a = []
while x.lower() != '~end~':
  x = x.split()
  b = 1
  if len(x) == 2:b = 0
  else:b = ['l','K','M','B'].index(x[2])
  a.append([-float(x[1])*10**(b*3),-len(x[0]),x[0]])
  x = input()
a.sort()
for c,z,b in a:
  print(b,-int(c))