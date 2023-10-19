#!/usr/bin/python3.8

import random

""" eightball.py
    solves the 'magic eight ball'
"""

fortunes = ("yes", "no", "it's likely", "it's doubtful",
            "absolutely positive", "not going to happen",
            "for sure", "never never never")

print("""
Magic eight ball
1) print all the fortunes
2) print a specific fortune
3) get a random fortune """)

userChoice = input("Please choose 1, 2, or 3: ")
if userChoice == "1":
    #print all the fortunes
    for (id, fortune) in enumerate(fortunes):
        print(f"{id}) {fortune}")
    print()

elif userChoice == "2":
    #ask for a fortuneID
    id = input("Please enter a number 0 - 7: ")
    #check to see if it's legit
    if id in ("0", "1", "2", "3", "4", "5", "6", "7"):
        #return the appropriate fortune
        id = int(id)
        print(fortunes[id])
    else:
        print("That was not a legal value")

elif userChoice == "3":
    question = input("What is your question? ")
    id = random.randrange(len(fortunes))
    print(fortunes[id])

else:
    print("Please enter 1, 2, or 3")
