i: int = 0
intro: str = input("What is your 6-letter guess? ")
SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
max_i: int = 5
exists: bool = False
alt: int = 0
# Answer to part 1
if intro == SECRET:
    print("Woo! You got it!")
    quit()
else: 
    if len(intro) == 6 and len(intro) != SECRET:
        print("Not quite. Play again soon!")
        quit()
    while len(intro) != len(SECRET): #doesn't need to have i < 4 with i = i+1 bc its supposed to repeat until a 6-letter word guess
        intro = input("That was not 6 letters! Try again: ")
    else:
        print("Not quite. Play again soon!")
# Answer to part 2
while i < len(SECRET):
    if intro[i] == SECRET[i]:
        print(GREEN_BOX, end =" ")
    else:
        print(WHITE_BOX, end =" ")
    i = i + 1
    max_i += 1

# Some of part 3?
if intro == SECRET:
    while i < len(SECRET):
        if intro[i] == SECRET[i]:
            print(GREEN_BOX, end =" ")
        else:
            while exists and alt < len(SECRET):
                if intro[alt] == SECRET[alt]:
                    print(WHITE_BOX, end = " ")
                    exists = True
                else:
                    print(YELLOW_BOX, end = "")
                    alt = alt + 1
        i = i + 1
        max_i += 1
    print("Woo! You got it!")
    quit()
else: 
    if len(intro) == len(SECRET) and len(intro) != SECRET:
        while i < len(SECRET):
            if intro[i] == SECRET[i]:
                print(GREEN_BOX, end =" ")
            else:
                while exists and alt < len(SECRET):
                    if intro[alt] == SECRET[alt]:
                        print(WHITE_BOX, end = " ")
                        exists = True
                    else:
                        print(YELLOW_BOX, end = "")
                        alt = alt + 1
            i = i + 1
            max_i += 1
        print("Not quite. Play again soon!")
        quit()
    while len(intro) != len(SECRET): 
        intro = input("That was not 6 letters! Try again: ")
    else:
        while i < len(SECRET):
            if intro[i] == SECRET[i]:
                print(GREEN_BOX, end =" ")
            else:
                while exists and alt < len(SECRET):
                    if intro[alt] == SECRET[alt]:
                        print(WHITE_BOX, end = " ")
                        exists = True
                    else:
                        print(YELLOW_BOX, end = "")
                        alt = alt + 1
            i = i + 1
            max_i += 1
        print("Not quite. Play again soon!")
#print(intro)
#if intro == SECRET:
#   print("Woo! You got it!")
#    quit()
#else: # the guess does not equal the answer
#        #print("Not quite. Play again soon!")
        #reassign a variable??
#    if len(intro) == 6 and len(intro) != SECRET:
#        print("Not quite. Try again later!")
#        quit()
#    while i < 4:
#        print(input("That was not 6 letters! Try again: "))
#        i = i + 1
#    else:
#        print("Not quite. Try again later!")

 while intro[0] == SECRET[0]:
            print(GREEN_BOX)
            quit()
        else:
            print(WHITE_BOX)
            i = i - 1

checking: int = intro[0] == SECRET[0]


#establish a variable to keep place of string and then initialize it to the first index
#idk but this prints 6 green boxes horizontally sooo??
while intro[0] == SECRET[0] and i < 5:
    print(GREEN_BOX, end =" ")
    i = i - 1
    quit()
else:
    print(WHITE_BOX)


while intro[0] == SECRET[0] and i < 5:
    print(GREEN_BOX, end =" ")
    i = i + 1
    while intro[1] == SECRET[1]:
        print(GREEN_BOX, end =" ")
        i = i + 1
        while intro[2] == SECRET[2]:
            print(GREEN_BOX, end =" ")
            i = i + 1
            while intro[3] == SECRET[3]:
                print(GREEN_BOX, end =" ")
                i = i + 1
                while intro[4] == SECRET[4]:
                    print(GREEN_BOX, end =" ")
                    i = i + 1
                    while intro[5] == SECRET[5]:
                        print(GREEN_BOX)
                        i = i + 1

