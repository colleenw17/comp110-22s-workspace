"""Tests for utils file"""

___author___ = "730319000"

#  from csv import list_dialects
from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == 0


def test_only_evens_single() -> None:
    numbers: list[int] = [2]
    assert only_evens(numbers) == 2


def test_only_evens_multiple() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert only_evens(numbers) == 10


def test_sub_empty() -> None:
    list_sub: list[int] = []
    assert sub(list_sub, 1, 3) == []


def test_sub_single() -> None:
    list_sub: list[int] = [2]
    assert sub(list_sub, 0, 1) == [2]


def test_sub_multiple() -> None:
    list_sub: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_sub, 1, 3) == [2, 3]


def test_concat_empty() -> None:
    list_evens: list[int] = []
    second_list_sub: list[int] = []
    assert concat(list_evens, second_list_sub) == list_evens


def test_concat_single() -> None:
    list_evens: list[int] = [1, 2, 3, 4]
    second_list_sub: list[int] = [5, 6, 7]
    assert concat(list_evens, second_list_sub) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_multiple() -> None:
    list_evens: list[int] = [-1, 0, 5]
    second_list_sub: list[int] = [10, 22, 13]
    assert concat(list_evens, second_list_sub) == list_evens