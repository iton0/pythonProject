"""Example function for unit tests"""


def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total = 0.0
    for x in range(len(xs)):
      sum_total += xs[x]
    return sum_total
