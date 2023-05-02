from lessons.Dictionaries.zip import zip 


def test_empty() -> None:
    assert zip([], []) == {}


def test_long_lists() -> None:
    assert zip(["a", "b", "c"], [9, 2, 3]) == {"a": 9, "b": 2, "c": 3}


def test_short_lists() -> None:
    assert zip(["a"], [9]) == {"a": 9}

