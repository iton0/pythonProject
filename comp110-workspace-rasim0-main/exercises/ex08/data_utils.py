"""EX 08 - Data Wrangling."""

__author__ = "730325555"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    result: list[str] = []
    # Step through table
    for row in table:
        # save every value under key "header"
        if header in row:
            result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that its a dictionary with column headers."""
    result: dict[str, list[str]] = {}
    # Loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returns a specific number of top rows of a table."""
    result: dict[str, list[str]] = {}
    for column in table:
        values = table[column]
        new_list: list[str] = []
        for items in range(rows):
            if items < len(values):
                new_list.append(values[items])
        result[column] = new_list
    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Reformats data with specific subset of columns."""
    result: dict[str, list[str]] = {}
    for names in column:
        result[names] = table[names]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Prodcues a new table from two combined column-based tables."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]
    for column in second:
        if column in result:
            result[column] += second[column]
        else:
            result[column] = second[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Returns frequency of values in a list."""
    result: dict[str, int] = {}
    for items in values:
        if items in result:
            result[items] += 1
        else:
            result[items] = 1
    return result
