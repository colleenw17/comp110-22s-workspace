"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730319000"


class Simpy:
    """An assignment."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialization of attributes."""
        self.values = values

    def __repr__(self) -> str:
        """Something."""
        return f"Simpy({self.values})"

    def __str__(self) -> str:
        """Makes object a string."""
        return f"Simpy({self.values})"

    def fill(self, filling: float, repeat: int) -> None:
        """Create a list with certain values that repeat a certain number of times. Aka repeating the float value int number of times."""
        self.values: list[float] = []
        i: int = 0
        while i < repeat:
            self.values.append(filling)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the attribute with a certain range of values."""
        assert step != 0.0
        self.values: list[float] = []
        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        else:  
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Compute and returns sums of values list."""
        total: float = 0.0
        for x in range(0, len(self.values)):
            total += self.values[x]
        return total
    
    def __add__(self, other: Union[Simpy, float]) -> Simpy:
        """Adding to expressions."""
        a: Simpy = Simpy([])
        if isinstance(other, float):
            i: int = 0
            while i < len(self.values):
                a.values.append(self.values[i] + other)
                i += 1
        else:
            assert(len(self.values) == len(other.values))
            i: int = 0
            while i < len(self.values):
                a.values.append(self.values[i] + other.values[i])
                i += 1
        return a

    def __pow__(self, other: Union[Simpy, float]) -> Simpy:    
        """Raising one expression to the power of the other."""
        a: Simpy = Simpy([])
        if isinstance(other, float):
            i: int = 0
            while i < len(self.values):
                a.values.append(self.values[i] ** other)
                i += 1
        else:
            assert(len(self.values) == len(other.values))
            i: int = 0
            while i < len(self.values):
                a.values.append(self.values[i] ** other.values[i])
                i += 1
        return a

    def __eq__(self, other: Union[Simpy, float]) -> list[bool]:
        """Another one, if two values are equal it's True."""
        a: list[bool] = []
        if isinstance(other, float):
            i: int = 0
            while i < len(self.values):
                a.append(self.values[i] == other)
                i += 1
        else:
            assert(len(self.values) == len(other.values))
            i: int = 0
            while i < len(self.values):
                a.append(self.values[i] == other.values[i])
                i += 1
        return a

    def __gt__(self, other: Union[float, Simpy]) -> list[bool]:
        """Another one, which one has the greater relationship between the values."""
        a: list[bool] = []
        if isinstance(other, float):
            i: int = 0
            while i < len(self.values):
                a.append(self.values[i] > other)
                i += 1
        else:
            assert(len(self.values) == len(other.values))
            i: int = 0
            while i < len(self.values):
                a.append(self.values[i] > other.values[i])
                i += 1
        return a
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Another one. Subscription notation."""
        if isinstance(rhs, int):
            x = self.values[rhs] 
            return x
        else:
            empty: list[float] = []
            for x in range(0, len(rhs)):
                if rhs[x] is True:
                    empty.append(self.values[x])
        return Simpy(empty)