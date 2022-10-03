#Pre mid 01.py
n = float(input())
if n > 0 and n <= 150:
    price = 3.2484*n
elif n > 150 and n <= 400:
    price = 487.26 + 4.2218*(n-150)
else:
    price = 487.26 + 1055.45 + 4.4217*(n-400)

#Service Charge
if n != 0:
	price += 38.22
#FT
price += n*(0.9343)
#VAT
price = price*(1.07)
if n <= 0:
    price = 0
print('%.2f' %(price))