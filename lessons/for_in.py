"""An example of for in syntax."""

# names: list[str] = ["Colleen", "Eve", "Prisca", "Jenna"]

# #  Example of iterating through names using a while loop
# print("while output:")
# i: int = 0
# while i < len(names):
#     name: str = names[i]
#     print(name)
#     i += 1

# #  The following for...in loop is the same as the while loop
# print("for...in output:")
# for name in names:
#     print(name)

ys: list[int] = [110, 120]
for y in ys:
    print(y)

i: int = 0 
ys: list[int] = [110, 120]
while i < len(ys):
    y: int = ys[i]
    print(y)
    i += 1