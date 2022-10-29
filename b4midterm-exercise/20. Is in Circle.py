#20. Is in Circle?
x = float(input())
y = float(input())
r = abs(float(input()))
xn = float(input())
yn = float(input())


print(not ((xn - x)**2 + (yn - y)**2) > r**2)