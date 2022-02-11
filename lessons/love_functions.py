"""Some examples of tender love."""

from unittest.util import strclass


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"

def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note = love(to) + "\n" #  concatenation 
        i = i + 1
    return love_note

print(spread_love)
print(love("Lauren"))
#quuiz function spread_love


#  can work in the reppel by saying "from lessons.love)functions import love" and then you can type love("") and it'll print
#  can say result: str = love("") to get rid of isngle quotes from before then print(result)