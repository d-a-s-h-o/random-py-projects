#!/usr/bin/env python3

# This program will play a game of wordle with the user

# Import the random module
import random

# Make a random list of words
word_list = ["apple", "banana", "cherry", "durian", "eggplant", "grape", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "peach", "pineapple", "plum", "pomegranate", "raspberry", "strawberry", "tangerine", "watermelon"]

# Pick a random word from the list
word = random.choice(word_list)

# Make a list of the letters in the word
word_letters = list(word)

# Make a list of the letters in the word, but with blanks
word_letters_blanks = list("_" * len(word))

# Ask the user to think of a letter in the word
print("Please think of a letter in the word!")

# Def a function to check if the letter is in the word
def check_letter(letter, word_letters):
    # If the letter is in the word
    if letter in word_letters:
        # Return True
        return True
    # If the letter is not in the word
    else:
        # Return False
        return False

    # Define a function to check if the word is complete
def check_word(word_letters_blanks, word_letters):
    # If the word is complete
    if word_letters_blanks == word_letters:
        # Return True
        return True
    # If the word is not complete
    else:
        # Return False
        return False

    # Define a function to replace the letter in the word
def replace_letter(letter, word_letters, word_letters_blanks):
    # For each letter in the word
    for i in range(len(word_letters)):
        # If the letter is in the word
        if letter == word_letters[i]:
            # Replace the letter in the word with a blank
            word_letters_blanks[i] = letter
    # Return the word with the letter replaced
    return word_letters_blanks

    # Define a function to replace the word
def replace_word(word, word_letters, word_letters_blanks):
    # For each letter in the word
    for i in range(len(word_letters)):
        # If the letter is in the word
        if word_letters[i] in word:
            # Replace the letter in the word with a blank
            word_letters_blanks[i] = word_letters[i]
    # Return the word with the letter replaced
    return word_letters_blanks

    # Define a function to play the game
def play_game(word, word_letters, word_letters_blanks):
    # While the word is not complete
    while check_word(word_letters_blanks, word_letters) == False:
        # Ask the user to think of a letter in the word
        letter = input("Enter a letter: ")
        # If the letter is in the word
        if check_letter(letter, word_letters) == True:
            # Replace the letter in the word with a blank
            word_letters_blanks = replace_letter(letter, word_letters, word_letters_blanks)
            # Print out the word with the letter replaced
            print("The word is: " + "".join(word_letters_blanks))
        # If the letter is not in the word
        else:
            # Print out that the letter is not in the word
            print("The letter is not in the word!")
    # Print out that the word is complete
    print("The word is complete!")

    # Play the game
play_game(word, word_letters, word_letters_blanks)