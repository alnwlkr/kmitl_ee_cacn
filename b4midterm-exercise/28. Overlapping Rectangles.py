#28. Overlapping Rectangles

def width_check(la,ra,lb,rb):
	#width_check(xa1,xa2,xb1,xb2)
	#la = xa1 | ra = xa2 | lb = xb1 | rb = xb2
	if ((ra - lb> 0) and (rb - la > 0)):
		#print("width check passed")
		#list = [ra - lb, rb - la, ra - la, rb - lb]
		return min([ra - lb, rb - la, ra - la, rb - lb])
	#print("not pass width check")
	return 0
def	height_check(ta,ba,tb,bb):
	#height_check(ya1,ya2,yb1,yb2)
	#ta = ya1 | ba = ya2 | tb = yb1 | bb = yb2
	if ((tb - ba > 0) and (ta - bb > 0)):
		#print("height check passed")
		#list = [tb - ba, ta - bb, ta - ba, tb - bb]
		return min([tb - ba, ta - bb, ta - ba, tb - bb])
	#print("not pass width check")
	return 0

#Top left A
xa1=int(input())
ya1=int(input())
#Bottom Right A
xa2=int(input())
ya2=int(input())
#Top left B
xb1=int(input())
yb1=int(input())
#Bottom Right B
xb2=int(input())
yb2=int(input())

#print(width_check(xa1,xa2,xb1,xb2))
#print(height_check(ya1,ya2,yb1,yb2))
print(width_check(xa1,xa2,xb1,xb2)*height_check(ya1,ya2,yb1,yb2))