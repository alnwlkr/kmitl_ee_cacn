#53. Longest Word

str1 = input()
n = len(str1)
if (n <= 100):
    lst = str1.split()
    print(max(lst, key=len))