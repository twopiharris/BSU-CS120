import pygame, simpleGE

"""
gameState.py
illustrates how to swap between states

"""
class Intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "The instructions for the game will go ",
            "here.  It will be some good instructions"]

        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (400, 100)
        
        self.sprites = [
            self.lblInstructions
            ]

        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 400)
        self.btnPlay.text = "Play"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (400, 400)
        self.btnQuit.text = "Quit"
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 100)
        self.lblScore.text = "Score: 0"
        
        self.btnClick = simpleGE.Button()
        self.btnClick.center = (320, 150)
        self.btnClick.text = "Click Me"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (320, 200)
        self.btnQuit.text = "End Game"
        
        self.sprites = [
            self.lblScore,
            self.btnClick,
            self.btnQuit]
        
    def process(self):
        if self.btnClick.clicked:
            self.score += 100
            self.lblScore.text = f"Score: {self.score}"
            
        if self.btnQuit.clicked:
            self.stop()
            

def main():
    intro = Intro()
    intro.start()
    
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    