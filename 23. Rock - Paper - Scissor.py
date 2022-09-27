#23. Rock - Paper - Scissor
p1 = input()
p2 = input()

if p1 == p2:
  print("Draw")
elif p1 == "Rock":
  if p2 == "Paper":
    print("Paper wins")
  else:
    print("Rock wins")
elif p1 == "Paper":
  if p2 == "Scissors":
    print("Scissors wins")
  else:
    print("Paper wins")
elif p1 == "Scissors":
  if p2 == "Rock":
    print("Rock wins")
  else:
    print("Scissors wins")
