#27. Lotto
#Check nearbyprize
def nearbyprize(no1,my):
	if (no1 == '000000'):
		if (my == '000001' or my == '999999'):
			return True
	elif (no1 == '999999'):
		if (my == '000000' or my == '999998'):
			return True
	elif (abs(int(no1) - int(my)) == 1):
			return True
	return False

#check last 2 digit
def cl2(l2,my):
	return(my[4:6] == l2)

#check first 3 digit
def	cf31(f31,my):
	return(my[:3] == f31)

def	cf32(f32,my):
	return(my[:3] == f32)

#check last 3 digit
def cl31(l31,my):
	return(my[-3:] == l31)

def cl32(l32,my):
	return(my[-3:] == l32)

no1=input()
l2=input()
f31=input()
f32=input()
l31=input()
l32=input()
my=input()

prize = 0
#Check len of every var
if (len(no1) == 6 and len(l2) == 2 and len(f31) == 3 and len(f32) == 3 and len(l31) == 3 and len(l32) == 3 and len(my) == 6):
	if (no1 == my):
		prize += 6000000
	if (nearbyprize(no1,my)):
		prize += 100000
	if (cl2(l2,my)):
		prize += 2000
	if (cf31(f31,my)):
		prize += 4000
	if (cf32(f32,my)):
		prize += 4000
	if (cl31(l31,my)):
		prize += 4000
	if (cl32(l32,my)):
		prize += 4000
	print(prize)