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
        
    def report(self):
        print(f"""
        {self.name}
        hp: {self.hp}
        shield: {self.shield}
        """)
        
    def apply(self, card):
        self.hp -= card.damage
        self.shield += card.shield
                
class Card(object):
    def __init__(self, name, damage, shield):
        self.name = name
        self.damage = damage
        self.shield = shield
        self.state = DECK
        
    def apply(self, character):
        character.hp -= damage
        character.shield += shield
        
    def display(self):
        print(f"""
        {self.name} 
        damage amount: {self.damage}
        shield amount: {self.shield}    
        """)
        
    def displayShort(self):
        location = STATES[self.state]
        print(f"{self.name:15} ({location:^7}) D: {self.damage:<3} S: {self.shield}")
        
class Fighter(Card):
    def __init__(self):
        super().__init__("Fighter", 3, 0)
        
class ShieldBearer(Card):
    def __init__(self):
        super().__init__("ShieldBearer", 0, 3)
        
class Healer(Card):
    def __init__(self):
        super().__init__("Healer", -2, 0)
        
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
        
    def showDeck(self):
        for card in self.cards:
            if card.state == DECK:
                card.display()

    def showHand(self):
        for card in self.cards:
            if card.state == HAND:
                card.display()
                
    def showDiscard(self):
        for card in self.cards:
            if card.state == DISCARD:
                card.display()

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

    def cardsInDeck(self):
        cardsLeft = 0
        for card in self.cards:
            if card.state == DECK:
                cardsLeft += 1
        return cardsLeft
    
    def discard(self, cardNum):
        hand = []
        for card in self.cards:
            if card.state == HAND:
                hand.append(card)
                
        currentCard = hand[cardNum]
        currentCard.state = DISCARD

    def deal(self, numCards):
        for cardNum in range(numCards):
            # reshuffle if necessary
            if self.cardsInDeck() <= 0:
                self.shuffle()

            keepGoing = True
            while keepGoing:
                currentCard = random.choice(self.cards)        
                if currentCard.state == DECK:
                    currentCard.state = HAND
                    keepGoing = False

def main():
    deck = Deck()
    print("Initial state: ")
    deck.showAllCards()
    
    print ("dealing 3 cards...")
    deck.deal(3)
    
    deck.showAllCards()
    
    deck.discard(0)
    deck.discard(0)
    deck.discard(0)

    print("discarding 3 cards")
    deck.showAllCards()

    print("dealing 4 cards - should trigger a shuffle")
    deck.deal(4)
    deck.showAllCards()
    
    print("Cards in hand:")
    deck.showHand()
    
    
    
if __name__ == "__main__":
    main()
