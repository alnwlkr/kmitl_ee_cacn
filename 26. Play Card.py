#26. Play Card

x = int(input()) - 1
y = int(input()) - 1

card = ['A' , 'B', 'C']

temp = card[x]
card[x] = card[y]
card[y] = temp

print(card[1])
