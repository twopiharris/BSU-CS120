#!/usr/bin/python3.8

""" add Player
    works with a dynamic list of players
"""

def menu():
    """ continues until it gets a legal input, which is returned"""
    keepGoing = True
    while keepGoing:
        print("""
        0) exit
        1) show players
        2) add a player
        """)

        userChoice = input("Please choose 0, 1, or 2: ")
        if userChoice in ("0", "1", "2"):
            keepGoing = False
        else:
            print ("Please enter 0, 1, or 2")

    return userChoice

def showPlayers(players):
    """ show all the players """
    for player in players:
        print (player)

    print()

def addPlayer(players):
    """ add a player to the list """

    newPlayer = input("New player name? ")
    players.append(newPlayer)

def main():
    """ run menu, adding and showing players until user wants to quit """

    breakpoint()
    players = []
    keepGoing = True
    while(keepGoing):
        userChoice = menu()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            showPlayers(players)
        elif userChoice == "2":
            addPlayer(players)

main()