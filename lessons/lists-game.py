"""Examples of using lists in a simple 'game'. """

from random import randint

rolls: list[int] = list()  #  setting up an empty list

while len(rolls) == 0 or rolls[len(rolls) -1] != 1: #  the first time you roll is equal to 0 then next turn or you roll something not equal to 1
    rolls.append(randint(1,6))

print(rolls)

#  Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

#  Sum the values of our rolls!
i: int = 0 
sum: int = 0

while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")

# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# print(rolls) 

# #  Access an individual item
# print(rolls[0])
# print(rolls[1])

# #  Access the length of a list (number of items)
# print(len(rolls))

# #  Access the last item of a list 
# # the last index will be one less than the length
# print(rolls[len(rolls) - 1])

# #  Another way to Access the last item of a list 
# last_index: int = len(rolls) - 1
# print(rolls[last_index])