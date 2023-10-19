""" printJSON.py
    Use JSON to pretty print a dictionary
"""

import json

def main():
    fred = {
        "name": "Fred Flintstone",
        "company": "Slate Rock",
        "email": "fred@slateRock.com"
    }

    print(json.dumps(fred, indent = 2))

main()
