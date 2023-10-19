#!/usr/bin/python3.8

import random

""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    """ manages entire game """

    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

def initCards():
    """ create card deck of 52 ints, all in deck """
    cardDB = []
    for cardNum in range(NUMCARDS):
        cardDB.append(DECK)
    return cardDB

def showDB(cardDB):
    """ show the current status of the database """
    print("Card Database:")
    for (cardNum, location) in enumerate(cardDB):
        handName = HANDS[location]
        theCard = getCardName(cardNum)
        print (f"  {cardNum:2}) {theCard:20} {handName}")
    print()

def assignCard(cardDB, hand):
    """ picks a random card, assigns it to a hand
        repeats until it finds a valid card """

    keepGoing = True
    while keepGoing:
        cardNum = random.randrange(NUMCARDS)
        if cardDB[cardNum] == DECK:
            cardDB[cardNum] = hand
            keepGoing = False

def showHand(cardDB, hand):
    """ given a hand, prints out the name of all cards in that hand """

    handName = HANDS[hand]
    print (f"Cards in {handName}'s hand:")
    for cardNum in range(NUMCARDS):
        if cardDB[cardNum] == hand:
            cardName = getCardName(cardNum)
            print (f"   {cardName}")

    print()


def getCardName(cardNum):
    """ given a card number, returns the card's name with rank and suit """
    rank = cardNum % 13
    suit = cardNum // 13
    cardName = f"{RANKNAME[rank]} of {SUITNAME[suit]}"
    return cardName

main()
