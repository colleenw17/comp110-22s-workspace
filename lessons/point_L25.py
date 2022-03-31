"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float
    
    def __init__(self, x: float, y: float):
        """Initialize a Point with its x, y components."""
        self.x = x
        self.y = y

    def sacle_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float) -> Point:
        """Immutable: multiplies components by factors."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point

    def __str__(self) -> str:
        """Produce a str represntation of a Point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str represenation as a Point for Python."""
        return f"Point({self.x}, {self.y})"        


p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)
# Can now add 
print(p1)
# OR
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

# Can get rid of once def __str__ is added
# print(f"({p0.x}, {p0.y})")
# print(f"({p1.x}, {p1.y})")

p1_repr: str = repr(p1)
print(p1_repr)