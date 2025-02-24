import random

#this asks the user to input the amount of many they want 
bet = int(input("how much you pay for? "))

if bet > 100:
  print("you can not bet higher than 100 run the program again")
else:
  
  #this while code allows the user to keep on playing
  keep_going=""
  while keep_going =="":
    
    
    print("")
    #the code here makes the code pick a random animal in the list in the square brackets and than prints the picked animal
    animals = ["donkey", "horse", "zebra", "unicorn", "donkey", "horse", "zebra", "unicorn", "donkey", "horse", "zebra", "donkey", "horse", "zebra", "unicorn", "cow?", "donkey", "horse", "zebra", "unicorn", "donkey", "horse", "zebra", "unicorn", "donkey", "horse", "zebra", "donkey", "horse", "zebra", "unicorn", "cow?","SNAKE?!"]
    animal = random.choice(animals)
    print (animal)
    print("")
    #all the if below is the diffrent results that can happen
    
    
    if animal == "unicorn":
      #unicorn will double the money
      bet = bet * 2
      print("you won:")
      print (bet)
      print("")
      
    if animal == "donkey":
      #donkey will half your money
      bet = bet / 2
      print("you lost half of your money:")
      print (bet)
      print("")
    if animal == "horse":
      
      #horse litrually does nothing
      bet = bet
      print("you won back your money:")
      print (bet)
      print("")
      
    if animal == "zebra":
      #and zebra takes 10 from your bet
      bet = bet - 10
      print("you lost:")
      print (bet)
      print("")
      
      
      
    if animal == "cow?":
      #and cow is rare and is a jackpot times your money by 15
      bet = bet * 15
      print("!!!JACKPOT!!!")
      print (bet)
      print("")
      
      
    if animal == "SNAKE?!":
      #and snake is VERY rare and basicly remove all your money leaving 15 behined for you
      bet = bet - bet
      bet = bet + 15
      print("OH NO YOUR MONEY NOOOOOOO")
      print (bet)
      print("")
      
      
    if bet <= 0:
      keep_going = "no"
    if bet > 0:
      #this asks if the user wants to continue or stop by typing litrually
      keep_going = input("press enter to go again, type anything else to stop ")
      
      
      
#this will notify the user that the program has stopped
print ("game over")
