""" adventure.py 
    "choose your adventure" style game
    implements finite state machine
    Thanks to pizzadude.dk for font
"""

import pygame, simpleGE

class Node(object):
    def __init__(self, title, desc, aText, aIndex, bText, bIndex):
        self.title = title
        self.description = desc
        self.aText = aText
        self.aIndex = aIndex
        self.bText = bText
        self.bIndex = bIndex

class GameScreen(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
       
        self.lblTitle = simpleGE.Label()
        self.lblTitle.font = pygame.font.Font("goodfoot.ttf", 50)
        self.lblTitle.center = (320, 35)
        self.lblTitle.size = (350, 60)
        
        self.lblDescription = simpleGE.MultiLabel()
        self.lblDescription.font = pygame.font.Font("goodfoot.ttf", 30)
        self.lblDescription.bgColor = (0xff, 0xff, 0x99)
        self.lblDescription.center = (320,240)
        self.lblDescription.size = (400, 250)
        
        self.btnA = simpleGE.Button()
        self.btnA.bgColor = (0x99, 0x99, 0x66)
        self.btnA.font = pygame.font.Font("goodfoot.ttf", 30)
        self.btnA.center = (110, 420)
        self.btnA.size = (200, 40)
        
        self.btnB = simpleGE.Button()
        self.btnB.bgColor = (0x99, 0x99, 0x66)
        self.btnB.font = pygame.font.Font("goodfoot.ttf", 30)
        self.btnB.center = (530, 420)
        self.btnB.size = (200, 40)
        
        self.sprites = [self.lblTitle, self.lblDescription, 
                        self.btnA, self.btnB]
                        
        self.background.fill((0xff, 0xff, 0x99))
        
    def loadNode(self, node):
        self.lblTitle.text = node.title
        self.lblDescription.textLines = node.description
        self.btnA.text = node.aText
        self.btnB.text = node.bText
        self.aIndex = node.aIndex
        self.bIndex = node.bIndex
        
    def update(self):
        if self.btnA.clicked:
            if self.aIndex == -1:
                self.keepGoing = False
            else:
                self.loadNode(self.nodeList[self.aIndex])
        
        if self.btnB.clicked:
            if self.bIndex == -1:
                self.keepGoing = False
            else:
                self.loadNode(self.nodeList[self.bIndex])

def main():
    
    nodeList = []

    #0
    nodeList.append( Node(
        "On Burning Ship",
        [   "Your vacation is going fine",
            "except you wake up to find",
            "your cruise ship is on fire.",
            "",
            "Do you attempt to fight the",
            "fire or jump overboard?"
        ],
        "Put out Fire", 1,
        "Jump", 2
        ))
    
    #1
    nodeList.append(Node(
        "Sink",
        [   "As you pour water on the",
            "flames, they only grow in ",
            "intensity.",
            "You find yourself engulfed",
            "in the inferno.",
            "",
            "You lose."
        ],
        "start over", 0,
        "quit", -1))
    
    #2
    nodeList.append(Node(
        "In Water",
        [   "You find yourself in the",
            "water. You see a lifeboat",
            "nearby, and some debris ",
            "floating off in the distance.",
            "",
            "Which do you swim toward?",
            ""
        ],
        "life boat", 3,
        "debris", 4))
    
    #3
    nodeList.append(Node(
        "Too Crowded",
        [   "As you reach the lifeboat, you can",
            "see it is already crowded to",
            "overflowing. Still, you climb in,",
            "but your weight causes the boat",
            "and all its passengers to slip",
            "under the waves.",
            ""
        ],
        "start over", 0,
        "quit", -1))
    
    #4
    nodeList.append(Node(
        "On Shore",
        [   "The floating debris keeps you",
            "afloat until you drift to a tiny",
            "island. You are exhausted. Do you",
            "rest to rebuild your strength, or",
            "try to start a fire?",
            "",
            ""
        ],
        "rest", 5,
        "build fire", 6))
    
    #5
    nodeList.append(Node(
        "Rested",
        [   "You feel well rested. Now you",
            "must decide what to do next:",
            "",
            "Build that fire, or start",
            "exploring the island?",
            "",
            ""
        ],
        "build fire", 6,
        "explore", 7))
    
    #6
    nodeList.append(Node(
        "Building Fire",
        [   "You are trying",
            "unsuccessfully to build",
            "a fire.",
            "",
            "",
            "",
            ""
        ],
        "keep trying", 6,
        "start over", 0))
    
    #7      
    nodeList.append(Node(
        "Supplies",
        [   "As you explore the island,",
            "you discover several crates of",
            "supplies that drifted from the",
            "ship before it sank. You now have",
            "the tools to build a shelter or",
            "go hunting. Which will you do ",
            "first?"
        ],
        "build shelter", 9,
        "go hunting", 8))
    
    #8
    nodeList.append(Node(
        "Wild Pig",
        [   "As you trudge through the ",
            "jungle, you spot a wild pig.",
            "You throw your spear and miss.",
            "The pig charges at you. Do you",
            "tackle it or run away?",
            "",
            ""
        ],
        "tackle", 10,
        "run away", 11))
    
    #9
    nodeList.append(Node(
        "Ship",
        [   "As you begin work on your",
            "shelter, you see a ship on the",
            "distant horizon.",
            "",
            "Will you swim out to the ship,",
            "or build a signal fire?",
            ""
        ],
        "make signal", 13,
        "swim out", 12))
    
    #10
    nodeList.append(Node(
        "Miss",
        [   "You miss the pig, and it disapears",
            "into the jungle",
            "",
            "",
            "",
            "",
            ""
        ],
        "chase it", 10,
        "return to camp", 11))
    
    #11
    nodeList.append(Node(
        "Supplies Gone",
        [   "As you return to your camp,",
            "you find that the tide has",
            "swept away all your supplies.",
            "",
            "You now have no chance of",
            "survival.",
            "You lose."
        ],
        "start over", 0,
        "quit", -1))
    
    #12
    nodeList.append(Node(
        "Drown",
        [   "You swim towards the ship, but",
            "they never see you, and you",
            "are pulled into the middle of",
            "the ocean by a deadly current",
            "",
            "You lose.",
            ""
        ],
        "start over", 0,
        "quit", -1))
    
    #13
    nodeList.append(Node(
        "Rescued",
        [   "You build a signal fire",
            "with the supplies you found.",
            "",
            "The smoke climbs into the sky,",
            "and the ship comes in to rescue",
            "you.",
            "You win!"
        ],
        "start over", 0,
        "quit", -1))
    
    nodeList.append(Node(
        "",
        [   "",
            "",
            "",
            "",
            "",
            "",
            "",
        ],
        "", 0,
        "", 0))
    
    
    game = GameScreen()
    game.nodeList = nodeList
    game.loadNode(nodeList[0])
    game.setCaption("Island Adventure")
    game.start()
    
if __name__ == "__main__":
    main()