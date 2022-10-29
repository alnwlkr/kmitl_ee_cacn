name = input()
w = float(input())
h = float(input()) / 100
bmi =  w/((h)**2)
print('Name:', '%s' %(name))
print('Weight:', '%d' %(int(w)), 'kg.')
print('Height:', '%.2f' %(h), 'm.')
print('BMI:', '%.2f' %(bmi))