"""Unit tests for sum function"""

from lessons.Unit_Tests.sum import sum


def test_empty() -> None: # Example of Edge case ("atypical" usage)
    assert sum([]) == 0.0


def test_one_element() -> None: # Example of Edge case ("atypical" usage)
    assert sum([1.0]) == 1.0


def test_many() -> None: # Example of Use case ("typical" usage)
    assert sum([1.0, 2.0, 3.0]) == 6.0


def test_many_negatives() -> None: # Example of Use case ("typical" usage)
    assert sum([1.0, -2.0, 1.0]) == 0.0
