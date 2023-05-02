"""EX 05 - More Lists Utils."""

__author__ = "730325555"


def only_evens(list1: list[int]) -> list[int]:
    """Returns even number(s) from a list of numbers."""
    list_even = []
    if len(list1) == 0:  # Message if the list is empty
        return list_even
    idx = 0
    while idx < len(list1):
        if list1[idx] % 2 == 0:
            list_even.append(list1[idx])
        idx += 1
    return list_even


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists of numbers returns a new list with elements from the first list and second list, respectively."""
    list_new = []
    if len(list1) == 0 and len(list2) == 0:  # Message if both of the lists are empty     
        return list_new
    idx1 = 0
    idx2 = 0
    while idx1 < len(list1):
        list_new.append(list1[idx1])
        idx1 += 1
    while idx2 < len(list2):
        list_new.append(list2[idx2])
        idx2 += 1
    return list_new


def sub(list1: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list of numbers, a start index, and an end index (not inclusive), generates a list which is a subset of the given list, between the specified start index and the end index - 1."""
    list_new = [] 
    if len(list1) == 0 or start_index >= len(list1) or end_index <= 0:
        return list_new
    if start_index < 0:
        start_index = 0
    if end_index > len(list1):
        end_index = len(list1)
    while start_index <= end_index - 1:
        list_new.append(list1[start_index])    
        start_index += 1
    return list_new
