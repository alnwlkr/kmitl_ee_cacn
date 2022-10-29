kv = int(input())
on = float(input())
off = float(input())
price = 0
if on + off > 0:
    if kv >= 12 and kv <= 24:
        price += on*5.1135 + off*2.6037 + 312.24
    elif kv < 12:
        price += on*5.7982 + off*2.6369 + 38.22
    price += (on+off)*0.9343
    price *= 1.07
print('%.4f' %price)