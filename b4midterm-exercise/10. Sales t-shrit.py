price = int(input())
percent = int(input()) / 100
n = int(input())
result = (price - (price*percent)) * n
print('%.2f' %(result))