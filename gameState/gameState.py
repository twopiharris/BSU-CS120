import pygame, simpleGE

"""
gameState.py
illustrates how to swap between states

"""
class Intro(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        
        self.status = "quit"
        self.score = score
        
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "The instructions for the game will go ",
            "here.  It will be some good instructions"]
        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (400, 100)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 100)
        self.lblScore.size = (400, 30)
        self.lblScore.text = f"Previous Score: {self.score}"

        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 400)
        self.btnPlay.text = "Play"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 400)
        self.btnQuit.text = "Quit"
        
        self.sprites = [
            self.lblScore,
            self.lblInstructions,
            self.btnPlay,
            self.btnQuit
            ]

    def process(self):
        if self.btnPlay.clicked:
            self.status = "play"
            self.stop()
        if self.btnQuit.clicked:
            self.status = "quit"
            self.stop()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.background.fill("lightblue")
        
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

    keepGoing = True
    score = 0
    
    while keepGoing:
        intro = Intro(score)
        intro.start()
        
        if intro.status == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
            score = game.score

if __name__ == "__main__":
    main()
    