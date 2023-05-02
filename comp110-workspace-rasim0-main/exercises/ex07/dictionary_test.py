"""Unit Tests for invert, favorite_color, and count functions."""

__author__ = "730325555"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_empty_dict() -> None:
    """For empty dictionary."""
    assert invert({}) == {}


def test_one_key() -> None:
    """For one key value pair."""
    assert invert({"s": "a"}) == {"a": "s"}


def test_many_key() -> None:
    """For many key value pairs."""
    assert invert({"s": "a", "z": "b", "c": "r"}) == {"a": "s", "b": "z", "r": "c"}


with pytest.raises(KeyError):
    invert({'kris': 'jordan', 'michael': 'jordan'})


def test_no_frequency() -> None:
    """For no most frequent color."""
    assert favorite_color({"a": "yellow", "b": "blue", "c": "green"}) == ""


def test_all_same() -> None:
    """For all same color."""
    assert favorite_color({"a": "blue", "b": "blue", "c": "blue"}) == "blue"


def test_color_tie() -> None:
    """For a tie in most frequent color."""
    assert favorite_color({"a": "blue", "b": "yellow", "c": "green", "d": "green", "e": "yellow"}) == "yellow"


def test_empty_list() -> None:
    """For an empty list."""
    assert count([]) == {}


def test_one_str() -> None:
    """For one string in list."""
    assert count(["a"]) == {"a": 1}


def test_many_str() -> None:
    """For many strings in list."""
    assert count(["a", "b", "b", "c", "a"]) == {"a": 2, "b": 2, "c": 1} 
