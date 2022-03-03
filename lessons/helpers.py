"""Demonstrate defining a module imported elsewhere."""

#  Added later on 1
THE_ANSWER: int = 42


# Added later on 2
def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


#  Added later on 1
print("helpers.py was evaluated.")

#  Added later on 2
#  idiom for making a module able to run as a program 
# or have its global definitions imported
if __name__ == "__main__":
    main()
else:
    #  Not normally here
    print(f"helpers.py was imported: {__name__}")