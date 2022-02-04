"""Finally - A structured Wordle."""
__author__ = "730319000"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    turn: int = 6
    play: bool = True
    SECRET: str = "codes"

    while play and i <= turn: 
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(SECRET))
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {i}/6 turns!")
            return None
        elif i == turn:
            print("X/6 - Sorry, try again tomorrow!")
        i += 1    
    

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
        enter = input(f"That wasn't {expectedlen} chars! Try again: ")
        i += 1
    return(enter)


if __name__ == "__main__":
    main()