"""EX 06 - Choose Your Own Adventure."""

__author__ = "730325555"


# Importation of the randint function from the random library
from random import randint

# Global variables
points: int 
player: str = ""
num: int = randint(0, 100)
end_game: bool = False
usr_quit: bool = False

# Named constants
UP_ARROW: str = "\U00002B06"
DOWN_ARROW: str = "\U00002B07"
CLOSE_ARROW: str = "\U00002194"
 

def greet() -> None:
    """Greets the user and introduces game."""
    global player
    player = input("Enter name: ")
    while len(player) < 3:  # User name must be at least 3 characters long
        player = input(f"{player} is too short: ")
    print("====================") 
    print(f"Welcome {player} to") 
    print("Guess The Number.")
    print("====================")
    print("You have 10 guesses.")
    print("If anytime during the game you want to quit or start a new game type in 'quit' or 'new', respectively.")
    print("On your 5th guess it will prompt you whether or not you would like to take a chance on resetting your guesses.")
    print("But be careful there is also a chance that the amount of guesses you have decreases; even goes to zero!")
    print("Enjoy!")
    

def guess() -> None:
    """Prompts the user to guess number and tells them how close the guess is to the number."""
    global points, end_game, num, usr_quit
    usr_guess = input(f"{player} guess the number: ")
    if usr_guess == "quit":  # If the user would like to quit the program 
        usr_quit = True
        end_game = True
        return 
    if usr_guess == "new":  # If the user would like to start a new game loop
        print("======================")
        print("Starting new game. . .")
        print("======================")
        points = 1
        num = randint(0, 100)
    # This section of the code emojifies to tell the user if they are too high, low, or if they are within -+ 5 digits of the number 
    lower_bound = (int(usr_guess) >= num - 5)
    upper_bound = (int(usr_guess) <= num + 5)
    if int(usr_guess) == num: 
        end_game = True
    elif int(usr_guess) > num and not upper_bound:
        print(f"{DOWN_ARROW} Lower")
        points += 1
    elif int(usr_guess) < num and not lower_bound:
        print(f"{UP_ARROW} Higher")
        points += 1
    elif lower_bound or upper_bound:  # If guess is within -+ 5 range of number
        print(f"{CLOSE_ARROW} Close")
        points += 1

    
def incrs_chance(param: int) -> int:
    """Prompts the user if they would like to take a chance on lowering number of guesses left. Given a user input will do such or not.""" 
    point_change: dict[int, int] = {0: + randint(1, 10), 1: - randint(1, 10)}  # Dictionary for either increase or decrease of number by number
    print(f"{player} do you want to take a chance on resetting or having less number of turns?")
    player_choice: str = input("y/n: ")
    while player_choice != "y" and player_choice != "n":  # Prompt is user does enter valid input
        player_choice = input("Your answer either has to be y or n ")
    if player_choice == "y":
        param += point_change[randint(0, 1)] 
        if param > 10:  # If the parameter is now greater than 10 it will initiliaze the variable such that the game loop ends
            param = 11
        elif param < 0:  # If the parameter is now less than 0 it will initialize the variable such that the game loop starts back at the beginning 
            param = 1
        print(f"You have {param} guesses now.") 
    elif player_choice == "n":
        return param
    return param


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global points
    points = 1
    greet()  # Call of the greet function
    while points < 11 and not end_game:
        print(f"=== Guess {points}/10 ===")
        guess()  # Call of the guess function
        if points == 5:
            points = incrs_chance(points)  # Call of the incrs_chance function
    if end_game and usr_quit:
        print(f"{player} please come back. This is a graded assignment!")
    elif end_game: 
        print(f"The number is {num}!")
        print(f"You got it in {points}/10 guesses.")            
    else:
        print(f"The number was {num}")
        print("X/10 - Sorry, try again!")
    

# This allows the code to be run as a module and for others to import the functions for use 
if __name__ == "__main__":
    main()
