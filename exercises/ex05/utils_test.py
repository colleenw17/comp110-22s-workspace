"""Tests for utils file."""

___author___ = "730319000"

#  from csv import list_dialects
from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Testing the only_evens function with an empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_single() -> None:
    """Testing the only_evens function with an single item."""
    assert only_evens([2]) == [2]


def test_only_evens_multiple() -> None:
    """Testing the only_evens function with a multiple items."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_sub_empty() -> None:
    """Testing the sub function with an empty list."""
    list_sub: list[int] = [0]
    assert sub(list_sub, 1, 3) == []


def test_sub_single() -> None:
    """Testing the sub function with multiple items."""
    list_sub: list[int] = [2, 3, 4]
    assert sub(list_sub, 1, 2) == [3]


def test_sub_multiple() -> None:
    """Testing the sub function with a different set of multiple items."""
    list_sub: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_sub, -1, -3) == []


def test_sub_negative() -> None:
    """Testing the sub function with a different set of multiple items."""
    list_sub: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_sub, -1, 3) == [1, 2, 3]


def test_concat_empty() -> None:
    """Testing the concat function with an empty list."""
    list_evens: list[int] = []
    second_list_sub: list[int] = []
    assert concat(list_evens, second_list_sub) == list_evens


def test_concat_single() -> None:
    """Testing the concat function with a single item."""
    list_evens: list[int] = [1, 2, 3, 4]
    second_list_sub: list[int] = [5, 6, 7]
    assert concat(list_evens, second_list_sub) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_multiple() -> None:
    """Testing the concat function with multiple items."""
    list_evens: list[int] = [-1, 0, 5]
    second_list_sub: list[int] = [10, 22, 13]
    assert concat(list_evens, second_list_sub) == list_evens