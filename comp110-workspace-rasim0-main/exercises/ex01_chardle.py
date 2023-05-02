"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730325555"


user_word = input("Enter a 5-character word: ")
if len(user_word) > 5 or len(user_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
user_char = input("Enter a single character: ")
if len(user_char) > 1 or len(user_char) < 1:
    print("Error: Character must be a single character")
    exit()
index_match = 0

print("Searching for " + user_char + " in " + user_word)
if user_char == user_word[0]:
    print(user_char + " found at index 0")
    index_match += 1
if user_char == user_word[1]:
    print(user_char + " found at index 1")
    index_match += 1
if user_char == user_word[2]:
    print(user_char + " found at index 2")
    index_match += 1
if user_char == user_word[3]:
    print(user_char + " found at index 3")
    index_match += 1
if user_char == user_word[4]:
    print(user_char + " found at index 4")
    index_match += 1
if index_match == 0: 
    print("No instances of " + user_char + " found in " + user_word)
if index_match == 1: 
    print(str(index_match) + " instance of " + user_char + " found in " + user_word)
if index_match > 1: 
    print(str(index_match) + " instances of " + user_char + " found in " + user_word)