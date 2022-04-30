"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730319000"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        # There is nothing in the list (1->2->3->None)
        raise ValueError("last cannot be called with None")
    if head.next is None:
        # head.next is 2->3->None then 3->None and then you know you're on the last value bc next is None
        return head.data
    else:
        # 2->3->None bc head is redefined as this and then you "loop" thru again and head = 3->None
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Giving a value(data) at the index it occurs at."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if head == 0:
        # head.next??
        return head.data
    else:
        return 0
        

def max(head: Optional[Node]) -> int:
    """Returns the max data value in the Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        i: int = 0
        if head.next is None:
            # if head.next is greater than a value return that value (in head.next)
            return head.data
        else:
            # Is the next node the max value?
            i = max(head.next)
        if i > head.data:
            return i
        else:
            return head.data


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a Linked List of Nodes with the same value and in the same order."""
    i: int = 0
    if items[i] == items.next[i]:
        return
    else:
        return None
    

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Return a new list that scaled the old list by a certain factor."""
    if head is None:
        return None
    else:
        i = scale()
        return scale(head * factor) 