#!/usr/bin/python3.8

""" adventure.py
    basic 'choose your adventure' game
    with preset game using dictionary """


def main():
    game = getGame()
    keepGoing = True
    nextNode = "start"
    while keepGoing:
        nextNode = playNode(game, nextNode)
        if nextNode == "quit":
            keepGoing = False

def getGame():
    game = {
        "start": ["You are on a boat. It's on fire", 'Stay on the boat', 'stay', 'Jump in the water', 'water'],
         "stay": ['Did I mention the boat was ON FIRE?', 'Start over', 'start', 'Quit', 'quit'],
         "water": ['You are in the water. You see a lifeboat and some floating debris', 'Swim to the lifeboat', 'lifeboat', 'Cling to the debris', 'debris'],
         "lifeboat": ['You climb into safety in the boat. So does everyone else, and the boat slowly begins to sink', 'Start over', 'start', 'Quit', 'quit'],
         "debris": ["The debris isn't much. but eventually you feel sand beneath your feet. You are on an island! What will you do first?", 'Look for wreckage or survivors', 'search', 'Explore your new surroundings', 'explore'],
         "search": ['You see enough wreckage to build a simple shelter, but sadly no survivors. Do you:', 'Get some rest', 'rest', 'Explore the island to look for food', 'explore'],
         "explore": ['In your exhausted state, you look around the island. But you fail to notice the cliff. You lose.', 'Start over', 'start', 'Quit', 'quit'],
         "rest": ['You feel surprisingly well-rested after a night in your shelter.', 'Build a fire', 'fire', 'Look for food', 'food'],
         "fire": ["It's very difficult to start a fire without matches", 'Give up', 'food', 'Keep trying', 'fire'],
         "food": ['You decide to look for food. You find some berries. On the way back to the campsite you see another box that washed ashore. It has matches!', 'Keep looking for food', 'food2', 'try again to start the fire', 'fire2'],
         "food2": ["You keep looking for food, but you don't find anything. You get lost and never find your way back to camp. You lose.", 'Start over', 'start', 'Quit', 'quit'],
         "fire2": ['You go back to the fire and this time you can get it lit. In the distance, you see a dot on the horizon.', 'Swim to the ship', 'swim2', 'make the fire larger', 'signal'],
         "swim2": ["You swim to the boat, but it's farther than you thought. And it's hard to swim when you've barely eaten. You lose", 'Start over', 'start', 'Quit', 'quit'],
         "signal": ['You build the fire larger, sending a black plume of smoke into the sky. The ship notices you. You are saved!', 'Start over', 'start', 'Quit', 'quit'],
    }

    return game

def playNode(game, currentNode):
    (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]

    print (f"""
    {desc}
    1) {menuA}
    2) {menuB}
    """)
    userChoice = input("Your choice: ")

    if userChoice == "1":
        nextNode = nodeA
    elif userChoice == "2":
        nextNode = nodeB
    else:
        print ("Not a valid input. Please enter '1' or '2.'")
        nextNode = currentNode

    return nextNode

main()