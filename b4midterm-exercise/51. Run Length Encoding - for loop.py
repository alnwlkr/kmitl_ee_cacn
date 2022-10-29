#51. Run Length Encoding - for loop
def encode(str1):
    n = len(str1)
    result = ''
    cnt = 0
    for i in range(n + 1):
        if (i == 0):
            cnt = 1
        elif (i == n):
            result += str(cnt) + str1[i - 1]
        elif (str1[i] == str1[i - 1]):
            cnt += 1
        elif (str1[i] != str1[i - 1]):
            result += str(cnt) + str1[i - 1]
            cnt = 1
    return result
str1 = input()

if (len(str1) <= 255):
    print(encode(str1))