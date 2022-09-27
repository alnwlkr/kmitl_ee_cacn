#49. Counting
n = input()
n = n.casefold()
str = input()
str = str.casefold()
if (len(str) <= 150):
    print(str.count(n))