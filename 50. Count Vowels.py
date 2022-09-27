#50. Count Vowels
def Vow(str):
    str = str.lower()
    cnt = 0
    for i in str:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            cnt += 1
    return cnt
str = input()
print(Vow(str))