"""File to define Bear class."""


class Bear:
    """Bear class."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Constructs new bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates day for bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Simulates eating for bear."""
        self.hunger_score += num_fish
        return None
    