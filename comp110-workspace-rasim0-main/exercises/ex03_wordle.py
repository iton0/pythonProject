"""EX 03 - Structured Wordle."""

__author__ = "730325555"


def contains_char(string: str, char: str) -> bool:
    """This function takes a string and a single character. It will then see if the character is in the string. If it is it will print True otherwise it will print False."""
    assert len(char) == 1
    idx_var = 0
    char_exist = False
    while not char_exist and idx_var < len(string):
        if string[idx_var] == char:
            char_exist = True
        else:
            idx_var += 1
    # This will either return True or False since the char_exist variable is assigned a boolean
    return char_exist


def emojified(guess: str, secret: str) -> str:
    """This function takes a guess string and a secret string. It then codifies the results based on matching the indexes: Green = Both indexes match; Yellow = correct character but wrong index; White = wrong character (It will use the contains_char function to test for white and yellow boxes)."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji = ""
    idx_var = 0
    # This will look at each character starting with the first index and make a green box if the user characters' indexes match all the secret characters' indexes
    while idx_var < len(secret):
        if guess[idx_var] == secret[idx_var]:
            emoji += f"{GREEN_BOX}"
    # Here is the implementation of the contains_char function to check for the yellow and white squares
        elif contains_char(secret, guess[idx_var]):
            emoji += f"{YELLOW_BOX}"
        else:
            emoji += f"{WHITE_BOX}"
        idx_var += 1    
    return emoji


def input_guess(exp_length: int) -> str:
    """This function keeps prompting the user for a guess until it reaches the expected character count. It will then return the user's guess."""
    usr_input = input(f"Enter a {exp_length} character word: ")
    while len(usr_input) != exp_length:
        usr_input = input(f"That wasn't {exp_length} chars! Try again: ")
    return str(usr_input)


def main() -> None:
    """The entrypoint of the program and main game loop."""    
    # The state of the game includes 3 variables
    secret_word = "codes"
    usr_turn = 1
    usr_win = False
    # This is the main game loop which utilizes the above three functions
    while usr_turn < 7 and not usr_win:
        print(f"=== Turn {usr_turn}/6 ===")
        usr_guess = input_guess(len(secret_word))
        print(emojified(usr_guess, secret_word))
        # If the user guesses the correct word it will result in the variable usr_win to be assigned True. Otherwise the user goes to their next turn
        if usr_guess == secret_word:
            usr_win = True
        else:
            usr_turn += 1
    # If the user guesses correctly within 6 turns a message will print that they won in their respective turn. Otherwise they are told that they did not guess within the alloted six turns
    if usr_win:
        print(f"You won in {usr_turn}/6 turns!")            
    else:
        print("X/6 - Sorry, try again tomorrow!")


# This allows the code to be run as a module and for others to import the functions for use 
if __name__ == "__main__":
    main()
