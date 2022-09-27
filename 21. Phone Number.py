#21. Phone Number

n = input()
inter = input()

if len(n) == 9 or len(n) == 10 and n.startswith('0'):
  if inter == 'Domestic':
    print (n[:-8] + ' ' + n[-8:-4] + ' ' + n[-4:])
  if inter == 'International':
    print('+66' + n[1:-8] + ' ' + n[-8:-4] + ' ' + n[-4:])

