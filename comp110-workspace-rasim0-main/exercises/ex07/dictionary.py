"""EX 07 - Dictionary Functions."""

__author__ = "730325555"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in a dictionary."""
    inverted: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        # If keys are not unique 
        if value in inverted:
            raise KeyError("Keys are not unique!")
        inverted[value] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, returns the most frequently occurring color."""
    freq: dict[str, int] = {}
    # Iterates over input dictionary to store in function dictionary 
    for name in dictionary:
        color = dictionary[name]
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1
    color_most: str = ""
    appear_first: str = ""
    max_occur: int = 0
    # Iterates over function dictionary to find favorite color
    for color in freq:
        color_count = freq[color]
        # Updates variables associated with color, its count, and appeareance in dictionary 
        if color_count > max_occur:
            color_most = color
            max_occur = color_count
            appear_first = color
        # Conditional if there is tie
        elif color_count == max_occur:
            if color == appear_first:
                color_most = color
    # If there is no most frequent occuring color will print empty string
    if max_occur == 1:
        return ""
    else:
        return color_most


def count(list1: list[str]) -> dict[str, int]:
    """Returns a dictionary containing the counts of each item in the input list."""
    dictionary: dict[str, int] = {}
    for key in list1:
        # Updates the value by 1 if key is already in dictionary
        if key in dictionary:
            dictionary[key] += 1
        # Substantiates the key with a value of 1 in dictionary
        else:
            dictionary[key] = 1 
    return dictionary
