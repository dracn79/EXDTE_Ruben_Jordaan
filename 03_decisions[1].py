#this repeats the question all the time
keep_going = ""
while keep_going == "":

#questions and answers
#.lower() makes input be lowercase
  if_like_coffee = input ("do you like coffee? ").lower()
  
  if if_like_coffee == 'yes' or if_like_coffee == 'y':
    print("I like coffee too!")
  elif if_like_coffee == 'no' or if_like_coffee == 'n':
    print("you missing out!")
  else:
    print("I don't understand")
  #this code will allow the user to end the program or continue
  keep_going = input("Press <enter> to continue or any other key to quit ")
  print("")