#!/usr/bin/env python3

# This program will solve the quadratic equation
# ax^2 + bx + c = 0

# Ask the user to enter a, b, and c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# If the discriminant is greater than 0
if discriminant > 0:
    # Calculate the first root
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    # Calculate the second root
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    # Print out the roots
    print(f"The roots are {root1} and {root2}")
# If the discriminant is 0
elif discriminant == 0:
    # Calculate the root
    root = -b / (2 * a)
    # Print out the root
    print(f"The root is {root}")
# If the discriminant is less than 0
else:
    # Print out that there are no real roots
    print("There are no real roots")