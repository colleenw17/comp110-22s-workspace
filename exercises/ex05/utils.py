"""Implementing a skelton code."""

__author__ = "730319000"


def only_evens(numbers: list[int]) -> list[int]:
    """Extracting only even numbers from a list."""
    i: int = 0
    empty_evens: list[int] = []
    while len(numbers) > i:
        if numbers[i] % 2 == 0:
            empty_evens.append(numbers[i])
        i += 1
    return empty_evens

    
def sub(list_sub: list[int], start: int, end: int) -> list[int]:
    """Extracting a subset of numbers from a list."""
    list1: list[int] = []
    while len(list_sub) == 0:
        return list1
    else:
        if start < 0:
            start = 0
        while start < len(list_sub):
            if start < end:
                list1.append(list_sub[start])
            start += 1 
        return list1
        
   
def concat(list_evens: list[int], second_list_sub: list[int]) -> list[int]:
    """Adding the two previous lists together."""
    for i in second_list_sub:
        list_evens.append(i)
    return list_evens