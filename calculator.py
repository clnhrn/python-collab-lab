"""
This module serves as the starter file for the Git Collaboration Challenge.
Group members will simultaneously add their assigned arithmetic functions
below the designated TODO comment to practice resolving merge conflicts.
"""

def welcome_message():
    print("Welcome to the Collaboration Calculator!")

# ==========================================
# TODO: Add your functions below this line
# ==========================================

def divide(a, b):
    return a / b if b != 0 else "Error"

def multiply(a, b): 
    return a * b


if __name__ == "__main__":
    welcome_message()