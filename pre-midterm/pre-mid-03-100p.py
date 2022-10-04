#Pre mid 03.py
def is_odd(num):
    return num % 2 == 1
num = input()
if num.isnumeric():
    if len(num) == 1:
        if is_odd(int(num)):
            print('Odd')
        else:
            print('Even')
    else:
        left = int(num[:len(num)//2])
        right = int(num[len(num)//2:])
        if is_odd(left) and is_odd(right):
            print('Oodd')
        elif not is_odd(left) and not is_odd(right):
            print('Eeven')
        elif is_odd(left) and not is_odd(right):
            print('Oeven')
        else:
            print('Eodd')