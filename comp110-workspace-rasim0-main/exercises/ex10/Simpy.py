"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730325555"


class Simpy:
    """Simpy class."""

    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Construct a Simpy object with a list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Return a string representation of the Simpy object."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, number: int) -> None:
        """Fill the Simpy object's values with a specific number of repeating values."""
        new: list[float] = []
        for idx in range(number):
            new.append(value)
        self.values = new
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the `values` attribute with range of float values."""
        assert step != 0.0
        new: list[float] = []
        idx: int = 0
        if step > 0:
            while start + idx * step < stop:
                new.append(start + idx * step)
                idx += 1
            self.values = new
        else:
            while start + idx * step > stop:
                new.append(start + idx * step)
                idx += 1
            self.values = new

    def sum(self) -> float:
        """Return the sum of all items in the `values` attribute."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return addition increased representation of the Simpy object."""
        new: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                new.append(self.values[idx] + rhs.values[idx])
        else:
            for idx in range(len(self.values)):
                new.append(self.values[idx] + rhs)
        return Simpy(new)
       
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return power increased representation of the Simpy object."""
        new: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                new.append(self.values[idx] ** rhs.values[idx])
        else:
            for idx in range(len(self.values)):
                new.append(self.values[idx] ** rhs)
        return Simpy(new)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return a mask based on the equality of each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        new: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                if self.values[idx] == rhs.values[idx]:
                    new.append(True)
                else:
                    new.append(False)
        else:
            for idx in range(len(self.values)):
                if self.values[idx] == rhs:
                    new.append(True)
                else:
                    new.append(False)
        return new
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return a mask based on the greater than relationship between each item in the `values` attribute with some other `Simpy` object or a `float` value."""
        new: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for idx in range(len(self.values)):
                if self.values[idx] > rhs.values[idx]:
                    new.append(True)
                else:
                    new.append(False)
        else:
            for idx in range(len(self.values)):
                if self.values[idx] > rhs:
                    new.append(True)
                else:
                    new.append(False)
        return new
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Return the element(s) of the Simpy object specified by the index(es) given in `rhs`."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new: list[float] = []
            for idx in range(len(rhs)):
                if rhs[idx]:
                    new.append(self.values[idx])
            return Simpy(new)
