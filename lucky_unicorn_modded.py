import random


bet = int(input("how much you pay for? "))

  
  
  
keep_going="yes"
while keep_going=="yes":
  print("")
  animals = ["donkey", "horse", "zebra", "unicorn"]
  animal = random.choice(animals)
  print (animal)
  print("")
  if animal == "unicorn":
    bet = bet * 3
    print("you won:")
    print (bet)
    print("")
  if animal == "donkey":
    bet = bet / 2
    print("you lost half of your money:")
    print (bet)
    print("")
  if animal == "horse":
    bet = bet
    print("you won back your money:")
    print (bet)
    print("")
  if animal == "zebra":
    bet = bet - 5
    print("you lost:")
    print (bet)
    print("")
  if bet <= 0:
    keep_going = "no"
  if bet > 0:
    keep_going = input("again? ")
print ("game over")
  
