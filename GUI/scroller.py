import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.lblOut = simpleGE.Label()
        self.lblOut.center = (320, 100)
        self.lblOut.text = "50"
        
        self.scroller = simpleGE.Scroller()
        self.scroller.value = 50
        self.scroller.minValue = 0
        self.scroller.maxValue = 100
        self.scroller.center = (320, 200)
        
        self.sprites = [self.lblOut,
                        self.scroller]
        
    def process(self):
        self.lblOut.text = f"{self.scroller.value}"
        self.scroller.text = f"<-  {self.scroller.value}  ->"
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()