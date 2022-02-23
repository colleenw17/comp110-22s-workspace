"""Implementing a skelton code."""

__author__ = "730319000"


def only_evens(numbers: list[int]) -> int:
    """Extracting only even numbers from a list."""
    total: int = 0
    for number in numbers:
        total % 2 == 0
        total += number
    return total

    
def sub(list_sub: list[int], start: int, end: int) -> list[int]:
    """Extracting a subset of numbers from a list."""
    list1: list[int] = []
    # while start < len(list_sub):
    #     list1 += list_sub[start]
    #     start += end
    while len(list_sub) == 0:
        return list1
    else:
        while start < len(list_sub):
            if start < end:
                list1.append(list_sub[start])
            start += 1 
        return list1
        
    # for set in list_sub:
    #     len(list1) == 0
    #     start += end
    # return list1

    # if len(list_sub) == 0:
    #     return list1
    #     i += 0
    #     #  dont need i bc start, end do the same thing
    # else:
    #     if start < 0:
    #         return list1
    #         list1 += 0
    #     else:
    #         return list1
    #         list1 -= 0


def concat(list_evens: list[int], second_list_sub: list[int]) -> list[int]:
    """Adding the two previous lists together."""
    for i in second_list_sub:
        list_evens.append(i)
    return list_evens
    # empty_list: list[int] = []
    # list_evens.append(empty_list)
    # sub_list.append(empty_list)
    # return list_evens + sub_list    
