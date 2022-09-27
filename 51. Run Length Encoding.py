#51. Run Length Encoding
def encode(str1):
    n = len(str1)
    result = ''
    i = 0
    is_same = 1
    cnt = 0
    while i <= n:
        if (i == 0):
            cnt += 1
        elif (i == n):
            result += str(cnt) + str1[i - 1]
        elif (str1[i] == str1[i - 1]):
            cnt += 1
        elif (str1[i] != str1[i - 1]):
            result += str(cnt) + str1[i - 1]
            cnt = 1
        i += 1
    return result

str1 = input()

if (len(str1) <= 255):
    print(encode(str1))