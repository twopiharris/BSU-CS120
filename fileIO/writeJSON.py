""" writeJSON.py
    saves a dictionary in JSON format

"""

import json

def main():
    fred = {
        "name": "Fred Flintstone",
        "company": "Slate Rock",
        "email": "fred@slateRock.com"
    }

    outFile = open("fred.json", "w")
    json.dump(fred, outFile, indent=2)
    outFile.close()
    print("saved Fred data to fred.json")

main()
