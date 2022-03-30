"""Example of a class and object instantiation."""

# inventing a class named Pizza


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str  # or size: str or size: str = "small"
    toppings: int
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attrubutes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Pizza can calculate it's own price."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings == 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= tax

        return total


def price(pizza: Pizza) -> float:
    """Calculate the price of a Pizza."""
    total: float = 0.0
    if pizza.size == "large":
        total += 10.0
    else:
        total += 8.0

    total += pizza.toppings == 0.75

    if pizza.extra_cheese:
        total += 1.0
    return total


a_pizza: Pizza = Pizza("large", 3)
a_pizza.size = "large"
a_pizza.toppings = 3 
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${price(a_pizza)}")
#  Calculating price
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0, )
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")