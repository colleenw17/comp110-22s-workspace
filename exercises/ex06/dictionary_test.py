"""Testing the skeleton code for different functions using dictionaries."""

__author__ = "730319000"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_one() -> None:
    """Testing the invert function with a use case part 1."""
    switch: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(switch) == {"z": "a", "y": "b", "x": "c"}


def test_invert_two() -> None:
    """Testing the invert function with a use case part 2."""
    switch: dict[str, str] = {"apple": "red", "banana": "yellow", "blueberry": "blue"}
    assert invert(switch) == {"red": "apple", "yellow": "banana", "blue": "blueberry"}


def test_invert_empty() -> None:
    """Testing the invert function with an edge case."""
    switch: dict[str, str] = {}
    assert invert(switch) == {}


def test_favorite_color1() -> None:
    """Testing the return of the most numerous value mentioned part 1."""
    popular: dict[str, str] = {"Colleen": "yelllow", "Eve": "blue", "Grayson": "blue", "Duncan": "maroon"}
    assert favorite_color(popular) == "blue"


def test_favorite_color2() -> None:
    """Testing the return of the most numerous value mentioned part 2."""   
    popular: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Jordan": "blue"}
    assert favorite_color(popular) == "blue"


def test_favorite_color_empty() -> None:
    """Testing the return of the most numerous value mentioned in part 1."""
    popular: dict[str, str] = {}
    assert favorite_color(popular) == {}


def test_count_case1() -> None:
    """Testing the count function with a case 1."""
    freq: list[str] = ["yellow", "green", "green", "red"]
    assert count(freq) == {"yellow": 1, "green": 2, "red": 1}


def test_count_case2() -> None:
    """Testing the count function with a case 2."""
    freq: list[str] = ["red", "apple", "apple", "blue"]
    assert count(freq) == {"red": 1, "apple": 2, "blue": 1}


# def test_count_case_key_error() -> None:
#     """Testing the count function with a case 2."""
#     freq: list[str] = ["apple", "apple", "apple", "banana"]
#     assert count(freq) == {"apple, 3"}


def test_count_case_empty() -> None:
    """Testing the count function with a case 3."""
    freq: list[str] = []
    assert count(freq) == {}