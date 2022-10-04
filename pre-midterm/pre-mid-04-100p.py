#Pre mid 04.py
def mylen(x):
    #เช็ก len ของ x ก่อนแล้วถ้ายาวเท่ากัน ให้เช็ก lower ของข้อความ x 
    #(lower เพราะ A != a จึงต้องแปลงเป็นตัวใดตัวหนึ่งก่อนค่อยเทียบ)
    return (-len(x),x.lower())
lst = []

while True:
    x = input().strip()
    if x == '~END~':
        break
    else:
        lst.append(x)
        
lst.sort(key=mylen)
print(*lst,sep='\n')
