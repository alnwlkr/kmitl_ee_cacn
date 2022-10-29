sec = int(input())
print(sec//86400, (sec%86400)//3600, (sec%3600)//60, sec%60)