#!/usr/bin/python3.8
import csv

"""
    given a CSV file of a CYA game in
    node, desc, menuA, nodeA, menuB, nodeB
    format

    Opens the file
    Converts to a dictionary of lists in
    node: [desc, menuA, nodeA, menuB, nodeB]
    format

    Andy Harris, 9/26/2023
    for BSU CS 120
"""

def main():
    game = loadGame()
    printGame(game)

def loadGame():
    game = {}
    fileName = "Island.csv"
    inFile = open(fileName, "r")
    csvReader = csv.reader(inFile)

    for row in csvReader:
        (nodeName, desc, menuA, nodeA, menuB, nodeB) = row
        game[nodeName] = [desc, menuA, nodeA, menuB, nodeB]

    inFile.close()
    return game

def printGame(game):
    for nodeName, items in game.items():
        print (f" \"{nodeName}\": {items},")

main()