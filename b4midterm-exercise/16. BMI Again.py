#16. BMI Again
w = float(input())
h = float(input()) / 100
bmi = w/(h**2)
if bmi < 18.5:
  print('Underweight')
elif bmi >= 18.5 and bmi < 25:
  print('Normal')
elif bmi >= 25 and bmi < 30:
  print('Overweight')
else:
  print('Obese')