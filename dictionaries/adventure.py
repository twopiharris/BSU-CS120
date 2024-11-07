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
        "start": ["You are in a hallway", "door to east", "east", "door to south", "south"],
        "east" : ["You fell into a pit. You Lose.", "Quit", "quit", "Start Over", "start"],
        "south": ["You see a treasure chest and a sword. Which will you grab?", "Chest", "chest", "Sword", "sword"],
        "chest": ["The treasure chest opens a trap door to the original room.", "Open", "start", "Try to close it", "start"],
        "sword": ["You found the sword of destiny. You win!", "Quit", "quit", "Start over", "start"]
    }

    return game

def playNode(game, currentNodeKey):
    (desc, menuA, nodeA, menuB, nodeB) = game[currentNodeKey]

    print (f"""
    {desc}
    1) {menuA}
    2) {menuB}
    """)
    userChoice = input("Your choice: ")

    if userChoice == "1":
        nextNodeKey = nodeA
    elif userChoice == "2":
        nextNodeKey = nodeB
    else:
        print ("Not a valid input. Please enter '1' or '2.'")
        nextNodeKey = currentNode

    return nextNodeKey

main()