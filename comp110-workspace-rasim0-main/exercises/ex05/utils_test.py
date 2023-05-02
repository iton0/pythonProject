"""EX 05 - Unit Tests."""

__author__ = "730325555"


from exercises.ex05.utils import only_evens, sub, concat 


def test_all_evens() -> None:  # Use case
    """For all even numbers."""
    assert only_evens([22, 36, 98]) == [22, 36, 98]


def test_negatives() -> None:  # Use case
    """For all negative numbers."""
    assert only_evens([-22, -1, -5, -10]) == [-22, -10]


def test_empty() -> None:  # Edge case 
    """If the list entered is empty."""
    assert only_evens([]) == list


def test_few() -> None:  # Use case
    """For a small list."""
    assert sub([11, 12], 0, 2) == [11, 12]


def test_many() -> None:  # Use case
    """For a big list."""
    assert sub([11, 23, 234, 123, 1, 2, 5], 2, 5) == [234, 123, 1]


def test_xtreme_indexes() -> None:  # Edge case
    """For indexes that are not in range of length of list."""
    assert sub([1, 2, 3, 4, 5, 7, 8], -4, 10) == [1, 2, 3, 4, 5, 7, 8]


def test_small_lists() -> None:  # Use case
    """For two small lists."""
    assert concat([11, 12], [0, 23]) == [11, 12, 0, 23]


def test_big_lists() -> None:  # Use case
    """For two big lists."""
    assert concat([0, 1, 2, 3, 4, 5, 6], [-6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, -6, 5, 4, 3, 2, 1, 0]


def test_empty_list() -> None:  # Edge case
    """For one empty list."""
    assert concat([], [2, 3, 4, 5]) == [2, 3, 4, 5]
