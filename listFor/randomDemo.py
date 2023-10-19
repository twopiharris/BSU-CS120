#!/usr/bin/python3.8

""" randomDemo.py
    Andy Harris
    9/1/2023

    demonstrates common features of random library
"""

import random

#use randint to create a random value within a range
dieRoll = random.randint(1, 6)
print(dieRoll)
print()



# Randomness is easier to see when you have several random values
# so I'll make a loop

for i in range(10):
    dieRoll = random.randint(1, 6)
    print(f"You rolled a {dieRoll}")

print()


#let's say you have a card hand
cards = ["Ace of Spades", "King of Diamonds", "Three of clubs", "Two of Hearts"]

numCards = len(cards)

#randRange lets you get a legal index from a list
#it normally gives a 0 - n-1 value, just like the range operator

cardNum = random.randrange(numCards)
print(f"You rolled a {cardNum}")
print(f"That's the {cards[cardNum]}")



# we can feed a number to the seed function, or a string (which will be
# converted to a number)

random.seed("CS 120")

# now produce some random numbers
for i in range(10):
    print(random.randint(1, 10), end = " ")

print()

# try it again and you'll get a new set of random numbers
for i in range(10):
    print(random.randint(1, 10), end = " ")
print()


#but reset the seed:
random.seed("CS 120")

#and you'll get the first sequence again!
for i in range(10):
    print(random.randint(1, 10), end = " ")
print()
