import random
number_picked = random.randrange(0,100)

answer = int(input("what number is it? "))
yay = 0
while yay != 1:
  if answer > number_picked:
    print("too high")
    answer = int(input("what number is it? "))
  elif answer < number_picked:
    print("too low")
    answer = int(input("what number is it? "))
  else:
    print("congrats")
    yay = 1
 
