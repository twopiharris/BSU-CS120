#!usr/local/bin/python3.8

""" dictionary.py
    demostrates dictionaries
"""

def main():
    #you can add keys and values to a dictionary
    #dictionary is denoted by curly braces ({})

    stateCap ={
      "Illinois": "Springfield",
      "Indiana": "Indianapolis",
      "Wisconsin": "Madison"
    }

    #add an element to a dictionary with array-like syntax
    stateCap["Florida"] = "Tallahassee"

    #return an arbitrary value with the key:
    print(stateCap["Wisconsin"])

    #use a loop to iterate through keys
    for state in stateCap:
      #order of dictionary items is not specified
      capital = stateCap[state]
      print(f"The capital of {state} is {capital}")

    print()
    print()

    #items creates a cleaner interface to dictionary elements
    for state, cap in stateCap.items():
      print (f"{state:15} {cap:15}")

    print()

    #you can also step through just the keys or values if you want
    print("Keys")
    for key in stateCap.keys():
        print(f"  {key}")
    print()

    print("Values")
    for value in stateCap.values():
        print(f"  {value}")
    print()

    for capital in sorted(stateCap.values()):
        print (capital)

main()