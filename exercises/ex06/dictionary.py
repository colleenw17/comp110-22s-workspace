"""Testing dictionaries."""

__author__ = "730319000"


def invert(switch: dict[str, str]) -> dict[str, str]:
    """Inverting the keys so they become vaues and vice versa."""
    inv: dict[str, str] = {}
    for x in switch:
        inv[switch[x]] = x
    return inv


def favorite_color(popular: dict[str, str]) -> str:
    """Seeing how many times a color appears (as a value)."""
    color: dict[str, int] = {}
    empty: str = ""
    max: int = 0
    for x in popular:
        if popular[x] in color:
            color[x] += 1
        else:
            color[x] == 1
    for y in color:
        if color[y] > max:
            max = color[y]
            empty = y 
        else:
            if color[y] == max:
                empty = y[1]
    return empty     


def count(count_freq: list[str]) -> dict[str, int]:
    """Counting how many times a value occurs."""
    count_list: dict[str, int] = {}
    for y in count_freq:
        if y in count_list:
            count_list[y] += 1
        else:
            count_list[y] == 1
    return count_list
