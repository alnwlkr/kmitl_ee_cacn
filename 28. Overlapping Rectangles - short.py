#28. Overlapping Rectangles

def width_check(la,ra,lb,rb):
	if ((ra - lb> 0) and (rb - la > 0)):
		return min([ra - lb, rb - la, ra - la, rb - lb])
	return 0
def	height_check(ta,ba,tb,bb):
	if ((tb - ba > 0) and (ta - bb > 0)):
		return min([tb - ba, ta - bb, ta - ba, tb - bb])
	return 0

xa1=int(input())
ya1=int(input())
xa2=int(input())
ya2=int(input())
xb1=int(input())
yb1=int(input())
xb2=int(input())
yb2=int(input())

print(width_check(xa1,xa2,xb1,xb2)*height_check(ya1,ya2,yb1,yb2))