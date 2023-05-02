"""Challenge Question 04 - Dict Function Writing."""


def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    """Given a list of strings and a list of numbers, creates a dictionary with matching indexes from both lists, respectively."""
    new_dict: dict[str,int] = {}
    if len(keys) != len(values) or len(keys) + len(values) == 0:
        return new_dict
    for idx in range(len(keys)):
        new_dict[keys[idx]] = values[idx]
    return new_dict
