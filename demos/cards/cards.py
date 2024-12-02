import pygame, simpleGE, random

# public domain card images from here:
# https://tekeye.uk/playing_cards/svg-playing-cards#google_vignette


#keep some of the constants from the earlier game
NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

# these rank names fit the way the cards are named in the files
FILE_RANK_NAME = ("ace", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "jack", "queen", "king")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
STATE = ("deck", "showing", "discarded")

DECK = 0
SHOWING = 1
DISCARDED = 2

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.cardSlot = CardSlot(self)
        self.cardSlot.position = (320, 240)
        
        self.setupCards()
        
        self.sprites = [self.cardSlot]
        
    def setupCards(self):
        self.cards = []
        for cn in range(NUMCARDS):
            self.cards.append(Card(cn))
            
        
class CardSlot(simpleGE.Sprite):
    """ a sprite for showing a card.
        make one for every position on the table where you want
        a card to appear.  """
    
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("svg_playing_cards/backs/frog.svg")
        
    def process(self):
        """ at the moment, it simply rolls a new
            card every time it is clicked.
            at the moment I'm getting any card.
            you could also limit this to only get cards in the deck
            (look at the card state)
            You can also set the card state to showing or
            discarded for more control.
        """
        
        if self.clicked:
            cardNum = random.randrange(NUMCARDS)
            currentCard = self.scene.cards[cardNum]
            self.copyImage(currentCard.image)
        
class Card(object):
    def __init__(self, cardNum):
        super().__init__()

        self.id = cardNum
        self.suit = cardNum // 13
        self.rank = cardNum % 13
        
        self.suitName = SUITNAME[self.suit]
        self.rankName = RANKNAME[self.rank]
        
        self.state = DECK
        
        # set up the filename so we can get the right image
        self.cardFileName = "svg_playing_cards\\fronts\\"
        self.cardFileName += SUITNAME[self.suit] + "_"
        self.cardFileName += FILE_RANK_NAME[self.rank] + ".svg"
        #print(self.cardFileName)
        
        # grab the image and store it
        self.image = pygame.image.load(self.cardFileName)
        
        self.value = self.rank
        # for now, the value of the card is the rank. For a
        # blackjack game, you'd adjust so face cards are 10
        # and ace is 1 or 11
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()