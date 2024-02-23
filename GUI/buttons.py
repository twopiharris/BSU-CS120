import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.counter = 0
        
        self.lblOut = simpleGE.Label()
        self.lblOut.text = "0"
        self.lblOut.center = (320, 100)
        
        self.btnAddOne = simpleGE.Button()
        self.btnAddOne.text = "+1"
        self.btnAddOne.center = (320, 200)
        
        self.btnReset = simpleGE.Button()
        self.btnReset.text = "reset"
        self.btnReset.center = (320, 300)
        
        self.sprites = [self.lblOut,
                        self.btnAddOne,
                        self.btnReset]
        
    def process(self):
        if self.btnAddOne.clicked:
            self.counter += 1
        if self.btnReset.clicked:
            self.counter = 0
        self.lblOut.text = f"{self.counter}"
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()