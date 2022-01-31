
while i < 5:
    intro[0] == SECRET[0]
    print(GREEN_BOX)
    i = i + 1
else:
    intro[0] != SECRET[0]
    print(WHITE_BOX)
    i = i + 1
# Gather a guess from the user; 4 guesses
#intro: str = input("What is your 6-letter guess? ")

#maximum: int = 6
#again: str = input("That was not 6 letters! Try again: ") 
# Run "again" 4 times then stop

#while maximum != SECRET:
  #  print("Not quite. Play again soon!"))
 #   quit()

#while maximum == SECRET:
  #  print("Woo! You got it!"))
 #   quit()

#while i < len(word):
  #  print(input("That was not 6 letters! Try again: "))
#else:
 #   print("Not quite. Play again soon!")

#while i < len(word):
 #   print(input("That was not 6 letters! Try again: "))
#while i < 4:
    #print("Not quite. Play again soon!")
    #i = i +
####
 #   while i < 4:
   # print(input("That was not 6 letters! Try again: "))
#else:
  #  print("Not quite. Play again soon!")

 #   SECRET: str = ("python")
#word = ['python']

#while i > 0:
   # print(input("That was not 6 letters! Try again: "))
   # if i == word:
     #   print(input("Woo! You got it!"))
      #  quit()
  #  else:
    #    attempts = attempts - 1

SECRET: str = ("python")

maximum: str = input("That was not 6 letters! Try again: ")
if len(maximum) == 6:
    print("Woo! You got it!")
    quit()
else:
    print(("That was not 6 letters! Try again: ")
    print("Not quite. Play again soon!")
    quit()
    -----
maximum: str = input("That was not 6 letters! Try again: ")
if len(maximum) != 6:
    while i < 4: #repeats 4 times with the last statement 
        print(input("That was not 6 letters! Try again: "))
        i = i + 1
        print("Not quite. Play again soon!")
else:
    if len(maximum) != SECRET:
        print("Not quite. Play again soon!")
        quit()
    else:
        print("Woo! You got it!")
        quit()
        -------
        if len(maximum) == 6:
    if len(maximum) != SECRET:
        print("Not quite. Play again soon!")
        quit()
    else:
        print("Woo! You got it!")
        quit()
else:
    while i < 4: 
        print(input("That was not 6 letters! Try again: "))
        i = i + 1
    else:
        print("Not quite. Play again soon!")
        quit()