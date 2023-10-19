
""" keepGoingVan.py
    minivan.py
    Simulates a car trip with small children
    modifies minivan.py to make it easier to work with
    """


keepGoing = True
while keepGoing:
    print("We're still driving...")

    tripFinished = input("Are we there yet? ")
    tripFinished = tripFinished.upper()
    if tripFinished.startswith("Y"):
        keepGoing = False

print ("Can we go home now?")

