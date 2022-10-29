#15. Grade II
x = float(input())
if x >= 0 and x < 60:
  print('F')
elif x >= 60 and x < 65:
  print('F+')
elif x >= 65 and x < 70:
  print('D')
elif x >= 70 and x < 75:
  print('D+')
elif x >= 75 and x < 80:
  print('C')
elif x >= 80 and x < 85:
  print('C+')
elif x >= 85 and x < 90:
  print('B')
elif x >= 90 and x < 95:
  print('B+')
elif x >= 95 and x <= 100:
  print('A')
else:
  print('ERR')