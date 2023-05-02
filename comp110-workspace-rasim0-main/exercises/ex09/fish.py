"""File to define Fish class."""


class Fish:
    """Fish class."""
    
    age: int

    def __init__(self):
        """Constructs new fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates a day for fish."""
        self.age += 1
        return None
    