import simpleGE, pygame
""" labels.py
    demonstrates labels
    Barrieceto font from google fonts
    
"""

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 340)
        self.counter = 0
        self.text = "0"
        self.timer = simpleGE.Timer()
        
    def process(self):
        self.text = f"{self.timer.getElapsedTime():.2f}"

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        
        
        self.lblBasic = simpleGE.Label()
        self.lblBasic.center = (100, 100)
        self.lblBasic.text = "Basic Label"
        
        self.lblColors = simpleGE.Label()
        self.lblColors.center = (300, 100)
        self.lblColors.bgColor = "white"
        self.lblColors.fgColor = "blue"
        self.lblColors.text = "Changing colors"
        self.lblColors.size = (200, 30)
        
        self.lblClear = simpleGE.Label()
        self.lblClear.clearBack = True
        self.lblClear.fgColor = "black"
        self.lblClear.center = (500, 100)
        self.lblClear.text = "Clear Back"
        
        
        myFont = pygame.font.Font("Barriecito-Regular.ttf", 30)
        self.lblFont = simpleGE.Label()
        self.lblFont.font = myFont
        self.lblFont.clearBack = True
        self.lblFont.fgColor = "black"
        self.lblFont.text = "Custom Font"
        self.lblFont.center = (320, 240)
        self.lblFont.size = (250, 50)
        
        self.lblTimer = LblTimer()
        
        self.sprites = [self.lblBasic, 
                        self.lblColors,
                        self.lblClear,
                        self.lblFont,
                        self.lblTimer]
        

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()