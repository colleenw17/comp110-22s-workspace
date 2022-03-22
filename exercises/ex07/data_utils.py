"""Dictionary related utility functions."""

__author__ = "730319000"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of  a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {} 
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(unmutated: dict[str, list[str]], resulting_rows: int) -> dict[str, list[str]]:
    """Returns the first couple of rows (N) in a long dictionary."""
    result: dict[str, list[str]] = {}
    for x in unmutated: 
        first_row: list[str] = []
        i: int = 0
        if resulting_rows > len(unmutated[x]):
            resulting_rows = len(unmutated[x])
        while i < resulting_rows: 
            first_row.append(unmutated[x][i])
            i += 1
        result[x] = first_row
    return result


def select(unmutated2: dict[str, list[str]], relevant: list[str]) -> dict[str, list[str]]:
    """Selecting the columns relevant to the analysis."""
    result: dict[str, list[str]] = {}
    for item in relevant:
        result[item] = unmutated2[item]
    return result


def concat(columns1: dict[str, list[str]], columns2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two column-based tables to perform an analysis. Adding more values to a column header that already exists."""
    result: dict[str, list[str]] = {}
    for item in columns1:
        result[item] = columns1[item]
    for item2 in columns2:
        if item2 in result: 
            i: int = 0
            while i < len(columns2[item2]):
                result[item2].append(columns2[item2][i])
                i += 1
        else:
            result[item2] = columns2[item2]
    return result


def count(count_freq: list[str]) -> dict[str, int]:
    """Counting how many times a value occurs."""
    count_list: dict[str, int] = {}
    for y in count_freq:
        if y in count_list:
            count_list[y] += 1
        else:
            count_list[y] = 1
    return count_list