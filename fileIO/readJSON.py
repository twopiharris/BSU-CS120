""" readJSON.py
    uses the json library to read a JSON
    file and store it in memory as a dictionary
"""

import json

def main():
    inFile = open("fred.json", "r")
    fred = json.load(inFile)
    print(fred)

    inFile.close()

main()

