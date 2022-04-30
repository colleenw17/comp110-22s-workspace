"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, linkify, value_at

__author__ = "730319000"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    index = 3
    assert last(linked_list) == None


def test_value_at_empty() -> None:
    """Last of an empty should return a IndexError."""
    linked_list = Node(10, Node(30, Node(20, None)))
    index = 2 
    assert value_at(linked_list, index) == 20    


def test_value_at_non_empty() -> None:
    """Last of an empty should return the data value at a given index."""
    linked_list = Node(10, Node(30, Node(20, None)))
    index = 2 
    assert value_at(linked_list, index) == 20    


def test_max_empty() -> None:
    """Last of an empty should return a ValueError."""
    with pytest.raises(ValueError):
        max(None)    


def test_max_non_empty() -> None:
    """Last of an empty list should return the max data value."""
    linked_list = (Node(10, Node(30, Node(20, None))))
    assert max(linked_list) == 30


def test_linkify_empty_or_not() -> None:
    """Last of an empty list should return None."""
    items = [10, 20, 30]
    assert linkify(items) == 10


def test_linkify_non_empty() -> None:
    """Last of an empty should return the data value of a new list in the same order as the input list."""
    items = [10, 20, 30]
    assert linkify(items) == 10


def test_scale_empty() -> None:
    """Last of an empty should return None."""  
    linked_list = Node(1, Node(2, Node(3, None)))
    factor = 2
    assert scale(linked_list, factor) == 3


def test_scale_non_empty() -> None:
    """Last of an empty should return the scaled data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    factor = 2
    assert scale(linked_list, factor) == 3