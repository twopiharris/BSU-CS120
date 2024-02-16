import pygame, simpleGE

class TransparentLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
    
    def update(self):
        super().update()
        self.image.set_colorkey(self.bgColor)
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill(pygame.Color("papayawhip"))
        
        self.lblOutput = TransparentLabel()
        self.lblOutput.center = ((320, 240))
        self.lblOutput.bgColor = ("papayawhip")
        self.lblOutput.fgColor = ("black")   
        self.lblOutput.text = "Hi there."

        self.sprites = [self.lblOutput]      
        

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()