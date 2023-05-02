"""File to define River class."""

__author__ = "730325555"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears; removes if above specific age."""
        new_bear: list[Bear] = [] 
        new_fish: list[Fish] = []
        for i in range(len(self.bears)):
            if self.bears[i].age <= 5:
                new_bear.append(self.bears[i])
        for i in range(len(self.fish)):
            if self.fish[i].age <= 3:
                new_fish.append(self.fish[i])
        self.bears = new_bear
        self.fish = new_fish
        return None
    
    def remove_fish(self, amount: int):
        """Removes specific number of frontmost fish."""
        self.fish = self.fish[amount:]
        return None

    def bears_eating(self):
        """Simulates bear eating fish."""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger level of the bears."""
        new_bear: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                new_bear.append(i)
        self.bears = new_bear
        return None
        
    def repopulate_fish(self):
        """Repopulates fish depending on number of fish."""
        new = ((len(self.fish)) // 2) * 4
        for i in range(new):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates bear depending on number of bears."""
        new = (len(self.bears)) // 2
        for i in range(new):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints day and number of fish/bears associated with that day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulate one week of life in ther river."""
        for i in range(7):
            self.one_river_day()
        return None
    