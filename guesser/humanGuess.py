#!/usr/bin/python3.8
import random

""" humanGuess.py
    computer comes up with random
    int between 1 - 100
    human guesses number
    computer responds high, low, or correct
    returns number of tries it took
"""

correct = random.randint(1, 100)
tries = 0
keepGoing = True
while keepGoing:
    tries += 1
    if tries > 7:
        print("You should be able to solve this in 7 turns or less")
        print("You lose.")
        keepGoing = False
    else:
        response = input(f"{tries}) What is your guess? ")
        if response.isdigit():
            response = int(response)
            if response < correct:
                print("Too low")
            elif response > correct:
                print("Too high")
            else:
                print(f"You got it in {tries} turns!")
                print("You win!")
                keepGoing = False
        else:
            print("You needed to input a number")
