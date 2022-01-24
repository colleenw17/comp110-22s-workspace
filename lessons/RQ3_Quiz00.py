"""Practice with if-then-else statements."""

# Implement the logic to print
# A when <25
# B when >= 25 and <50
# C when >75
# D when >= 5- and <= 75

choice: int = int(input("Enter a number: "))

if choice <25:
    print("A")
else:
    if choice <50:
        print("B")
    else:
        if choice >75:
            print("C")
        else:
            print("D")