 # dont' need the boolean vairable unless after "You won" you want to say bool = False
 while play and i < turn:
        
        print(f"=== Turn {i}/6 ===")
        if input_guess(len(SECRET)):
            print(emojified(, SECRET))
        i += 1
        else:
            print("X/6 - Sorry, try again tomorrow!")

def contains_char(word: str, one_char: str) -> bool:
    """Figuring out if a single character is found in the index of a word."""
    
    assert len(one_char) == 1

    i: int = 0
    while i < len(word):
        if word[i] == one_char:
            return True
        i += 1  
    return False

def emojified(guess: str, secret: str) -> str:
    """Using two words of equal length to test for yellow or white boxes."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    assert len(guess) == len(secret)

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1 
    return(emoji)

def input_guess(expectedlen: int) -> str:
    """If you're guess is not the correct length, try again until you reach the correct length."""
    enter: str = input(f"Enter a {expectedlen} character word: ")
    i: int = 0
    while expectedlen != len(enter):
        enter: str = input(f"That wasn't {expectedlen}! Try again: ")
        i += 1
    if expectedlen == enter:
        print(enter)
    return(enter)


#########
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
