y = []
for i in range(3):
	y.append(input())
for x in range(len(y)):
	for z in range (x + 1, len(y)):
		if y[x] > y[z]:
			y[x],y[z] = y[z],y[x]
print(y[1])
