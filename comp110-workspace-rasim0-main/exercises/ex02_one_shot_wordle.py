"""EX 02 - One Shot Wordle."""

__author__ = "730325555"


secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
indx_var = 0
emoji = ""
user_word = input(f"What is your {len(secret_word)}-letter guess? ")

# If the user word is not the length of the secret word's characters, it will prompt the user to input a word that fits the length of the secret word  
while len(user_word) != len(secret_word):
    user_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# This will look at each character starting with the first index and make a green box if the user characters' indexes match all the secret characters' indexes
while indx_var < len(secret_word):
    char_exist = False
    indx_alt = 0
    if user_word[indx_var] == secret_word[indx_var]:
        emoji += f"{GREEN_BOX}"
    else:
        # This section of code runs when the user word's and secret word's indexes do not match
        while not char_exist and indx_alt < len(secret_word):   
            if secret_word[indx_alt] == user_word[indx_var]:
                char_exist = True  
            else:    
                indx_alt += 1
        # If it finds that the user word's and secret word's indexes do not match but is found anywhere else in the secret word it will print yellow squares
        if char_exist:
            emoji += f"{YELLOW_BOX}"
        # Otherwise it will print white sqaures to say that letter(s) from the user word are not found in the secret word
        else:
            emoji += f"{WHITE_BOX}"
    indx_var += 1 
print(emoji)
    
if user_word != secret_word:
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")
