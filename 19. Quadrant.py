#19. Quadrant
x = int(input())
y = int(input())

if x == 0 and y == 0:
  print('O')
elif y == 0:
  print('X')
elif x == 0:
  print('Y')
elif x > 0 and y > 0:
  print('Q1')
elif x < 0 and y > 0:
  print('Q2')
elif x < 0 and y < 0:
  print ('Q3')
elif x > 0 and y < 0:
  print('Q4')