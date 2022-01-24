"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730319000"

character_word: str = input("Enter a 5-character word: ")
if len(character_word) != 5:
        print("Error: Word must contain 5 characters")
        exit()
else: 
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()

print("Searching for " + single_character + " in " + character_word)

if character_word [0] == single_character:
    print (single_character + " found at index 0")
if character_word [1] == single_character:
    print (single_character + " found at index 1")
if character_word [2] == single_character:
    print (single_character + " found at index 2")
if character_word [3] == single_character:
    print (single_character + " found at index 3")
if character_word [4] == single_character:
    print (single_character + " found at index 4")

match = 0
if single_character == character_word [0]:
    match = match + 1
    print("No instances of " + single_character + " found in " + character_word)


if single_character == character_word [1]:
    match = match + 1
    print(str(match) + " instance of " + str(single_character) + " found in " + str(character_word))
else:
    if match == 2:
        print(str(match) + " instances of " + str(single_character) + " found in " + str(character_word))
    else:
        print(str(match) + " instances of " + str(single_character) + " found in " + str(character_word))


if single_character == character_word [2]:
    match = match + 1

if single_character == character_word [3]:
    match = match + 1

if single_character == character_word [4]:
    match = match + 1
