import random
#this picks a random number between 0 and 10
number_picked = random.randrange(0,100)
#asks the user to input their guess
answer = int(input("what number is it? "))
yay = 0
while yay != 1:
  if answer > number_picked:
    print("too high")
    #this input makes it so the code don't repeat forever and allows the user to guess again
    answer = int(input("what number is it? "))
  elif answer < number_picked:
    print("too low")
    
    answer = int(input("what number is it? "))
  else:
    #the game congrats the user if they guess the number
    print("congrats")
    yay = 1
 
