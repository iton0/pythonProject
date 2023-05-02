"""EX 04 - List Utils."""

__author__ = "730325555"


def all(list1: list[int], number: int) -> bool:
    """Indicates whether or not all the numbers in the list are the same as the given number."""
    if len(list1) == 0:  # Message if the list is empty
        return False
    list_idx = 0 
    while list_idx < len(list1):
        if list1[list_idx] != number:
            return False
        list_idx += 1
    return True

        
def max(input: list[int]) -> int:
    """Gives the max of a list of numbers."""
    if len(input) == 0:  # Message if the list is empty
        raise ValueError("max() arg is an empty List")
    list_idx = 1
    max_val = input[0]
    while list_idx < len(input):
        if input[list_idx] > max_val:
            max_val = input[list_idx]
        list_idx += 1
    return max_val


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Indicates whether of not every element at the same index is equal in two lists."""
    if len(list1) == 0 and len(list2) == 0:  # Even though the lists are independent of each other on the heap, they are deeply equal to each other
        return True
    if len(list1) != len(list2):  # This is why this if statement and the two above ones are implemented in this function 
        return False
    list_idx = 0 
    while list_idx < len(list1):  
        if list1[list_idx] != list2[list_idx]:
            return False
        list_idx += 1
    return True
