"""One Shot - One step towards Wordle"""

__author__ = "730319000"

i: int = 0
intro: str = input("What is your 6-letter guess? ")
SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = ""
exists: bool = False
alt: int = 0

while len(intro) != len(SECRET):  #the length of my guess is not equal to the length of the answer so I have to try again
    intro = input("That was not 6 letters! Try again: ")

while i < len(SECRET): #when 0 < length of the answer and if the first index = to the answer index then a green box appears
    if intro[i] == SECRET[i]:
        guess = guess + GREEN_BOX
    else: 
        exists = False
        alt = 0
        while exists != True and alt < len(SECRET): #if the first index does not equal the answer index, and it doesn't exist in the answer then move ov
            if intro[i] == SECRET[alt]: #the letter is found in the answer in the correct spot so we can stop
                exists = True
            alt = alt + 1
        if exists == False: #the letter is not found in the answer so we stop and print a white box
            guess = guess + WHITE_BOX
        else:
            guess = guess + YELLOW_BOX
    i = i + 1
print(guess)

if intro == SECRET: #if we guess the answer we stop playing and if we don't guess the answer but it is 6 letters we stop
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
