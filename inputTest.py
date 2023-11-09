import pygame, simpleGE

""" inputTest.py """

class Game(simpleGE.Scene):
    
    """ used only for testing purposes. not a formal part of simpleGE """
    
    def __init__(self):
        super().__init__()
        
        self.txtInput = simpleGE.TxtInput()
        self.txtInput.text = "NAME"
        self.txtInput.center = (320, 140)
        self.txtInput.size = (100, 30)
        self.txtInput.bgColor = pygame.Color("white")
        
        self.btnClickMe = simpleGE.Button()
        self.btnClickMe.text = "Click Me"
        self.btnClickMe.center = (320, 180)
        self.btnClickMe.size = (100, 30)
        
        self.lblOutput = simpleGE.Label()
        self.lblOutput.text = "Type your name"
        self.lblOutput.center = (320, 220)
        self.lblOutput.size = (200, 30)
        
        self.sprites = [self.txtInput, self.btnClickMe, self.lblOutput]
        
    def doEvents(self, event):
        self.txtInput.readKeys(event)

    def update(self):
        if self.btnClickMe.clicked:
            name = self.txtInput.text
            self.lblOutput.text = f"Hi there, {name}!"

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    