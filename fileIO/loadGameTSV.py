#!/usr/bin/python3.8
"""
    given a TSV file of a CYA game in
    node, desc, menuA, nodeA, menuB, nodeB
    format

    Opens the file
    Converts to a dictionary of lists in
    node: [desc, menuA, nodeA, menuB, nodeB]
    format.

    Copy this content to use it in your own program...
"""

def main():
    game = loadGame()
    printGame(game)

def loadGame():
    game = {}
    fileName = "island.tsv"
    inFile = open(fileName, "r")

    breakpoint()
    for line in inFile:
        line = line.rstrip("\n")
        data = line.split("\t")
        (nodeName, desc, menuA, nodeA, menuB, nodeB) = data
        game[nodeName] = [desc, menuA, nodeA, menuB, nodeB]
    inFile.close()
    return game

def printGame(game):
    for nodeName, items in game.items():
        print (f"   \"{nodeName}\": {items},")

main()