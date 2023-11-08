""" guiDemoGE.py 
    demonstrates the GUI objects in
    simpleGE
"""

import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        #initialize background to yellow
        self.background.fill((0xff, 0xff, 0x00))
        
        self.addLabels()
        self.addButton()
        self.addScroller()
        self.addMultiLabel()
        
        self.sprites = [self.lblTitle, self.label,
                        self.lblButton, self.button,
                        self.lblScroller, self.scroller,
                        self.multi]
    
    def addLabels(self):
        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = "simpleGE GUI Demo"
        self.lblTitle.center = (320, 40)
        self.lblTitle.size = (300, 30)
        
        self.label = simpleGE.Label()
        self.label.font = pygame.font.Font("goodfoot.ttf", 40)
        self.label.text = "Label"
        self.label.fgColor = (0xCC, 0x00, 0x00)
        self.label.bgColor = (0xCC, 0xCC, 0x00)
        self.label.center = (320, 100)
        self.label.size = (100, 50)
        
    def addButton(self): 
        self.lblButton = simpleGE.Label()
        self.lblButton.center = (200, 180)
        self.lblButton.text = "Button"
        
        self.button = simpleGE.Button()
        self.button.center = (450, 180)
        self.button.text = "don't click me"
    
    def addScroller(self):
        self.lblScroller = simpleGE.Label()
        self.lblScroller.text = "scroller"
        self.lblScroller.center = (200, 250)
        
        self.scroller = simpleGE.Scroller()
        self.scroller.center = (450, 250)
        self.scroller.minValue= 0
        self.scroller.maxValue = 250
        self.scroller.value = 200
        self.scroller.increment = 5
    
    def addMultiLabel(self):
        self.multi = simpleGE.MultiLabel()
        self.multi.textLines = [
            "This is a multiline text box.",
            "It's useful when you want to",
            "put larger amounts of text",
            "on the screen. Of course, you",
            "can change the colors and font."
            ]
        self.multi.size = (400, 200)
        self.multi.center = (320, 370)
        
    def update(self):        
        if self.button.clicked:
            self.lblButton.text = "Ouch!"
            self.background.fill((0x00, 0x00, 0x00))
            self.screen.blit(self.background, (0, 0))
        
        self.lblScroller.center = (self.scroller.value, 250)

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    