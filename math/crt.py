#!/usr/bin/env python3

# This program will ask the user to think of a number, and will figure it our using the Chinese Remainder Theorem

# Ask the user to think of a number between 0 and 100
print("Please think of a number between 0 and 100!")

# Ask the user to enter the remainder of the division of the number by 3
remainder1 = int(input("Enter the remainder of your number divided by 3: "))

# Ask the user to enter the remainder of the division of the number by 5
remainder2 = int(input("Enter the remainder of your number divided by 5: "))

# Ask the user to enter the remainder of the division of the number by 7
remainder3 = int(input("Enter the remainder of your number divided by 7: "))

# Calculate the utility value of the number
utility_value = ((remainder1 * 70) + (remainder2 * 21) + (remainder3 * 15))

# While the utility value is greater than 105
while utility_value > 105:
    # Subtract 105 from the utility value
    utility_value -= 105

# Tell the user the utility value of the number
print("Your number is " + str(utility_value) + ".")
