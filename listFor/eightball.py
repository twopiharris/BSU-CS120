#!/usr/bin/python3.8
import random

""" magic eight ball
    demonstrates lists and for loops

    Andy Harris for CS 120
    9/5/23
"""

fortunes = ["yes", "no", "it's likely", "it's doubtful",
            "absolutely positive", "not going to happen",
            "for sure", "never never never"]

# produce a menu

print("""
What will you do?
1: print all the fortunes
2: print a specific fortune
3: get a random fortune""")

choice = input("what will you do? ")
if choice == "1":
    #print all the fortunes
    for (fortuneID, fortune) in enumerate(fortunes):
        print(f"{fortuneID}: {fortune}")

elif choice == "2":
    # ask for a fortune and print it out
    fortuneID = input("Please enter a number 0-7:")

    """
    # easy 'pythonic' solution
    if fortuneID in ("0", "1", "2", "3", "4", "5", "6", "7"):
        fortuneID = int(fortuneID)
        print(fortunes[fortuneID])
    else:
        print("Must be 0-7")

    """

    #more traditional approach
    if fortuneID.isdigit():
        fortuneID = int(fortuneID)
        if fortuneID <= 7:
            if fortuneID >= 0:
                print(fortunes[fortuneID])
            else:
                print("fortune must be zero or greater")
        else:
            print("fortune must be seven or less")
    else:
        print("fortune must be a number")

elif choice == "3":
    # ask a question and produce a random fortune
    question = input("What is your question? ")
    numFortunes = len(fortunes)
    fortuneID = random.randrange(numFortunes)
    print(fortunes[fortuneID])

else:
    # not an appropriate menu choice. Gently scold
    print("The only legal inputs were 1, 2, and 3")
