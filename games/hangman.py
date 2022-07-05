#!/usr/bin/env python3

# This program will play a game of hangman with the user

# Import the random module
import random

# Def a function to generate a random word
def random_word():
    # Set the word variable to a random word from the list of words
    word = random.choice(["apple", "banana", "orange", "grape", "pear", "strawberry", "kiwi", "blueberry", "raspberry", "blackberry", "mango", "cherry", "coconut", "durian", "dragonfruit", "fig", "grapefruit", "guava", "lemon", "lime", "lychee", "mango", "nectarine", "orange", "papaya", "passionfruit", "peach", "pear", "pineapple", "plum", "pomegranate", "raspberry", "starfruit", "strawberry", "tangerine", "tomato", "watermelon"])
    # Return the word variable
    return word


# Define a function to check if the user has guessed all the letters in the word
def check_win(word, guesses):
    # Set the win variable to False
    win = False
    # For each letter in the word
    for letter in word:
        # If the letter is in the list of guesses
        if letter in guesses:
            # Set the win variable to True
            win = True
        else:
            # Set the win variable to False
            win = False
            # Break out of the loop
            break
    # Return the win variable
    return win

# Define a function to check if the user has run out of guesses
def check_lose(guesses):
    # Set the lose variable to False
    lose = False
    # If the number of guesses is equal to or less than 0
    if len(guesses) <= 0:
        # Set the lose variable to True
        lose = True
    # Return the lose variable
    return lose

# Define a function to display the word with the correct letters filled in
def display_word(word, guesses):
    # Set the display variable to an empty string
    display = ""
    # For each letter in the word
    for letter in word:
        # If the letter is in the list of guesses
        if letter in guesses:
            # Add the letter to the display variable
            display += letter
        else:
            # Add an underscore to the display variable
            display += "_"
    # Return the display variable
    return display

# Define a function to display the user's guesses
def display_guesses(guesses):
    # Set the display variable to an empty string
    display = ""
    # For each letter in the list of guesses
    for letter in guesses:
        # Add the letter to the display variable
        display += letter
    # Return the display variable
    return display

# Define a function to play the game
def play_game():
    # Set the win variable to False
    win = False
    # Set the lose variable to False
    lose = False
    # Set the guesses variable to an empty list
    guesses = []
    # Set the word variable to a random word
    word = random_word()
    # Set the number of guesses to 8
    num_guesses = 8
    # While the user hasn't won and hasn't run out of guesses
    while win == False and lose == False:
        # Display the word with the correct letters filled in
        print("The word is: " + display_word(word, guesses))
        # Display the user's guesses
        print("Your guesses so far: " + display_guesses(guesses))
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")
        # If the user's guess is in the word
        if guess in word:
            # Add the guess to the list of guesses
            guesses.append(guess)
            # If the user has guessed all the letters in the word
            if check_win(word, guesses) == True:
                # Set the win variable to True
                win = True
        # If the user's guess is not in the word
        else:
            # Subtract 1 from the number of guesses
            num_guesses -= 1
            # If the user has run out of guesses
            if check_lose(guesses) == True:
                # Set the lose variable to True
                lose = True
        # Display the number of guesses left
        print("You have " + str(num_guesses) + " guesses left.")
    # If the user has won
    if win == True:
        # Display a message
        print("You win!")
    # If the user has run out of guesses
    if lose == True:
        # Display a message
        print("You lose!")
    # Display the word
    print("The word was: " + word)

# Call the play_game function
play_game()

# End of the program