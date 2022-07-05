#!/usr/bin/env python3

# This program will generate a diceware password

# Import the random module
import random

# Get the list of words from the diceware word list or download it if it doesn't exist
try:
    with open("diceware.txt") as f:
        words = f.read().splitlines()
except FileNotFoundError:
    print("Downloading diceware.txt...")
    import urllib.request
    urllib.request.urlretrieve("https://theworld.com/~reinhold/diceware8k.txt", "diceware.txt")
    with open("diceware.txt") as f:
        words = f.read().splitlines()

# Get the number of words to generate
num_words = int(input("How many words would you like to generate? "))

# Generate the password
password = ""
for i in range(num_words):
    # Get the word from the list of words
    word = random.choice(words)
    # Add the word to the password
    password += word + "_"

# Print the password
print("Your password is: " + password)