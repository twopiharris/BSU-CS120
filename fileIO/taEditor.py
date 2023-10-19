#!/usr/bin/python3.8
import json

""" taEditor.py
    text adventure editor
    Allows you to create, edit, save and load text
    adventure games
"""

def main():
    game = getDefaultGame()

    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice =="1":
            game = getDefaultGame()
        elif menuChoice == "2":
            print("Loading a game")
            game = loadGame()
        elif menuChoice == "3":
            saveGame(game)
        elif menuChoice == "4":
            print( "create or edit a node")
            editNode(game)
        elif menuChoice == "5":
            playGame(game)
        else:
            print("something went wrong")

def getMenuChoice():
    keepGoing = True
    while keepGoing:
        print("""
        0) exit
        1) load default game
        2) load a game file
        3) save the current game
        4) edit or add a node
        5) play the current game""")

        menuChoice = input("What will you do? ")
        if menuChoice in ("0", "1", "2", "3", "4", "5"):
            keepGoing = False
        else:
            print ("That is not a valid choice. Pick 0-5")
    return menuChoice

def playGame(game):
    keepGoing = True
    nextNode = "start"
    while keepGoing:
        nextNode = playNode(game, nextNode)
        if nextNode == "quit":
            keepGoing = False

def playNode(game, currentNode):
    nodeNames = game.keys()
    if currentNode in nodeNames:
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
    else:
        print(f"{currentNode} is not a valid node.  Exiting the game")
        nextNode = "quit"

    return nextNode

def getDefaultGame():
    game = {
        "start": ("Default start node", "start over", "start", "quit", "quit")
    }

    return game

def editNode(game):
    """ lists current nodes, asks for a node choice
        allows user to edit that node """
    print("Current status of entire game:")
    print(json.dumps(game, indent=2))

    print ("Current node names: ")
    nodeNames = game.keys()
    for nodeName in nodeNames:
        print(f"  {nodeName}")

    newNodeName = input("Choose node to edit or enter new node name: ")
    if newNodeName in nodeNames:
        newNode = game[newNodeName]
    else:
        newNode = ("", "", "", "", "")

    (desc, menuA, nodeA, menuB, nodeB) = newNode

    newDesc = getField("Description", desc)
    newMenuA = getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)

    newNode = (newDesc, newMenuA, newNodeA, newMenuB, newNodeB)
    game[newNodeName] = newNode

def getField(fieldName, currentVal):
    """ gets a field, keeps current value if null """
    field = input(f"{fieldName} ({currentVal}): ")
    if field == "":
        field = currentVal
    return field

def saveGame(game):
    """ saves the game to a file """
    fileName = "game.json"
    outFile = open(fileName, "w")
    json.dump(game, outFile, indent = 4)
    outFile.close()
    print("Saving this file...")
    print(json.dumps(game, indent = 4))

def loadGame():
    """ loads the game from the file """
    fileName = "game.json"
    inFile = open(fileName, "r")
    game = json.load(inFile)
    inFile.close()
    return game

main()