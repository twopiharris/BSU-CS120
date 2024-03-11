import pygame, simpleGE

""" timerDemo.py
    not a GUI element, but frequently related to them
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        
        self.lblTimer = simpleGE.Label()
        self.lblTimer.center = (320, 100)
        self.lblTimer.text = "0"
        
        self.lblTimeLeft = simpleGE.Label()
        self.lblTimeLeft.center = (320, 200)
        self.lblTimeLeft.text = "10"
        
        self.btnReset = simpleGE.Button()
        self.btnReset.center = (320, 300)
        self.btnReset.text = "Reset Timer"
        
        self.sprites = [self.lblTimer,
                        self.lblTimeLeft,
                        self.btnReset]
        
    def process(self):
        self.lblTimer.text = f"{self.timer.getElapsedTime():.2f}"
        self.lblTimeLeft.text = f"{self.timer.getTimeLeft():.2f}"
        
        if self.btnReset.clicked:
            self.timer.start()
        
        if self.timer.getTimeLeft() <= 0:
            self.timer.start()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
