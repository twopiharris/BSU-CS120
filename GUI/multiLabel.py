import pygame, simpleGE

"""multilabel.py """


textA = [
    "Far out in the uncharted backwaters",
    "of the unfashionable end of the Western",
    "Spiral Arm of the Galaxy lies a small",
    "unregarded yellow sun."
    ]

textB = [
    "Well, I am your king, you know",
    "I didn't vote for you.",
    "You don't vote for kings.",
    "How'd you become one then?",
    "The lady of the lake held aloft Excaliber, ",
    "signifying that I would be your king",
    "",
    "Strange women laying in ponds distributing", 
    "swords is no basis for a system of government"
]
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.setCaption("Click the label for another quote.")
        
        self.multiLabel = simpleGE.MultiLabel()
        self.multiLabel.center = (320, 240)
        self.multiLabel.size = (600, 400)
        self.multiLabel.textLines = textA
        self.state = "Hitchiker"
        
        self.sprites = [self.multiLabel]
    
    def process(self):
        if self.multiLabel.clicked:
            if self.state == "Hitchiker":
                self.state = "Grail"
                self.multiLabel.textLines = textB
            else:
                self.state = "Hitchiker"
                self.multiLabel.textLines = textA
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
