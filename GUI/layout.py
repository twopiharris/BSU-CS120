import pygame, simpleGE

""" layout.py
    Some common positions for elements in 
    a 640 x 480 screen """

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        
        lbl_150_100 = simpleGE.Label()
        lbl_150_100.center = (150, 100)
        lbl_150_100.text = "(150, 100)"
        
        lbl_320_100 = simpleGE.Label()
        lbl_320_100.center = (320, 100)
        lbl_320_100.text = "(320, 100)"
        
        lbl_500_100 = simpleGE.Label()
        lbl_500_100.center = (500, 100)
        lbl_500_100.text = "(500, 100)"
        
        lbl_150_240 = simpleGE.Label()
        lbl_150_240.center = (150, 240)
        lbl_150_240.text = "(150, 240)"
        
        lbl_320_240 = simpleGE.Label()
        lbl_320_240.center = (320, 240)
        lbl_320_240.text = "(320, 240)"
        
        lbl_500_240 = simpleGE.Label()
        lbl_500_240.center = (500, 240)
        lbl_500_240.text = "(500, 240)"
        
        
        
        
        
        self.sprites = [
            lbl_150_100,
            lbl_320_100,
            lbl_500_100,
            lbl_150_240,
            lbl_320_240,
            lbl_500_240,
            
            ]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
