""" card battle """

import random

# State constants
DECK = 0
HAND = 1
DISCARD = 2

STATES = ("deck", "hand", "discard")

class Character(object):
    def __init__(self, name, hp):
        super().__init__()
        self.name = name
        self.hp = hp
        self.shield = 0
        self.deck = Deck()
        
    def report(self):
        print(f"""
        {self.name}
        hp: {self.hp}
        shield: {self.shield}
        """)

    def pickAcard(self, state):
        hand = self.deck.makeHand(state)
        card = None
        for cardNum, card in enumerate(hand):
            print(f"{cardNum})  {card.name:15} {card.description}")
            
        choice = int(input(f"{self.name}: Which card will you play? "))
        if choice in range(len(self.deck.cards)):        
            card = hand[choice]
            print (f"picked {choice}. {card.name}")

        return card

class Card(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.state = DECK
        
    def apply(self, playerOne, playerTwo):
        pass
        """ overwrite this method to get the card to
            do something. PlayerOne is the player that
            plays the card, and PlayerTwo is playerOne's
            opponent.  For example, if you have a card
            that heals 1 point and does 2 points of damage,
            you could do this:
            
            playerOne.hp += 1
            playerTwo.hp -= 2
        """        

    def display(self):
        print(f"""
        {self.name} 
        {self.description}   
        """)
        
    def displayShort(self):
        location = STATES[self.state]
        print(f"{self.name:15} ({location:^7}) ")
        
class Fighter(Card):
    def __init__(self):
        super().__init__("Fighter", "does 3 points damage")
        
    def apply(self, playerOne, playerTwo):
        playerTwo.shield -= 3
        if playerTwo.shield < 0:
            playerTwo.hp += playerTwo.shield
            playerTwo.shield = 0
        
        print(f"{playerOne.name} hits {playerTwo.name}")
        
class ShieldBearer(Card):
    def __init__(self):
        super().__init__("ShieldBearer", "adds 3 shield")
        
    def apply(self, playerOne, playerTwo):
        playerOne.shield += 3
        print(f"{playerOne.name} adds three points of shield.")
        
class Healer(Card):
    def __init__(self):
        super().__init__("Healer", "heals two points")
        
    def apply(self, playerOne, playerTwo):
        playerOne.hp += 2
        print(f"{playerOne.name} heals two points of damage.")
        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.setDefaultDeck()
        
    def setDefaultDeck(self):
        self.cards.append(Fighter())
        self.cards.append(Fighter())
        self.cards.append(Fighter())
        self.cards.append(ShieldBearer())
        self.cards.append(ShieldBearer())
        self.cards.append(Healer())
    
    def showState(self, state):
        for card in self.cards:
            if card.state == state:
                card.display()
                
    def showStateShort(self, state):
        for card in self.cards:
            if card.state == state:
                card.displayShort()
                
    def makeHand(self, state):
        hand = []
        for card in self.cards:
            if card.state == state:
                hand.append(card)
        return hand
    
    def showAllCards(self):
        for card in self.cards:
            card.displayShort()
        print()

    def shuffle(self):
        """ return cards in discard back to deck """
        print("shuffling...")
        for card in self.cards:
            if card.state == DISCARD:
                card.state = DECK

    def getCardsInDeck(self):
        cardsLeft = 0
        for card in self.cards:
            if card.state == DECK:
                cardsLeft += 1
        return cardsLeft
    
    def deal(self, numCards, hand):
        # deals numCards cards only from the
        # deck changes the card's state to hand
        for cardNum in range(numCards):
            # reshuffle if necessary
            if self.getCardsInDeck() <= 0:
                self.shuffle()

            keepGoing = True
            while keepGoing:
                currentCard = random.choice(self.cards)        
                if currentCard.state == DECK:
                    currentCard.state = hand
                    keepGoing = False

def main():
    player1 = Character("Good", 10)
    player2 = Character("Evil", 10)
    
    print("Initial state: ")
    player1.deck.showAllCards()
    
    print ("dealing 3 cards to each player...")
    player1.deck.deal(3, HAND)
    player2.deck.deal(3, HAND)
    
    #deck.showAllCards()
    
    print("Player 1's hand: ")
    player1.deck.showStateShort(HAND)
    
    # two player battle
    keepGoing = True
    while keepGoing:
        player1.report()
        player2.report()
        
        card = player1.pickAcard(HAND)
        print (f"Playing {card.name}")
        card.apply(player1, player2)
        card.state = DISCARD
        if player2.hp <= 0:
            keepGoing = False
            print(f"{player1.name} wins!!")
        player1.deck.deal(1, HAND)

        player1.report()
        player2.report()

        if player2.hp > 0:
            card = player2.pickAcard(HAND)
            print (f"Playing {card.name}")
            card.apply(player2, player1)
            card.state = DISCARD
            if player1.hp <= 0:
                keepGoing = False
                print(f"{player2.name} wins!!!")
            
        player2.deck.deal(1, HAND)
        

        print("===================================================")
    
    
    
if __name__ == "__main__":
    main()
