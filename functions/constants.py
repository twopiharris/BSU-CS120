#!/usr/bin/python3.8

""" constants.py
    Illustrates use of constants

"""

# let's imagine our game will always have the same players
# we can define constants to make it easier to work with them
NUM_PLAYERS = 4
PLAYER_NAMES = ("Elizabeth", "Matthew", "Jacob", "Ben")

def main():
    """ demonstrate use of constants """

    for playerNum in range(NUM_PLAYERS):
        thePlayer = PLAYER_NAMES[playerNum]
        print (f"{playerNum}) {thePlayer}")

main()