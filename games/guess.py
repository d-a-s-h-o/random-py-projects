#!/usr/bin/env python3
# This program will guess a number between 0 and 100 until it gets it right

# Import the random module
import random

# Ask the user to think of a number between 0 and 100
print("Please think of a number between 0 and 100!")

# Set the initial guess to random number between 0 and 100
guess = random.randint(0, 100)
previous_guesses = []
higher_than = []
lower_than = []

# While the guess is not correct
state = 'false'
while state != 'correct':
    # Ask if the guess is too high or too low
    answer = input("Is your number higher than, lower than, or equal to " + str(guess) + "? [h,l,e] ")
    # If the answer is higher
    if answer == "h":
        # Add the guess to the list of higher than guesses
        higher_than.append(guess)
        # Set the guess between the previous guesses
        guess = random.randint(max(higher_than, default=0), min(lower_than, default=100))
    # If the answer is lower
    elif answer == "l":
        # Add the guess to the list of lower than guesses
        lower_than.append(guess)
        # Set the guess between the previous guesses
        guess = random.randint(max(higher_than, default=0), min(lower_than, default=100))
    # If the answer is correct
    else:
        # Set the state to correct
        state = "correct"
    # Add the previous guess to the list of previous guesses
    previous_guesses.append(guess)

# Print out the previous guesses
print("Your number is " + str(guess) + ".")
print("The previous guesses were: " + str(previous_guesses))