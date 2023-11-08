import pygame, simpleGE

""" game control 
    demonstrate using GUI elements to control game """
    
class Instructions (simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = [
            "I am the instructions",
            "Click me to start",
            "the game"]
        self.center = ((320, 240))
        self.size = ((320, 120))

class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.timer = simpleGE.Timer()
        self.timeOver = False
        self.hide()
        
    def checkEvents(self):
        timeLeft = 5 - self.timer.getElapsedTime()
        self.text = f"{timeLeft:.2f}"
        
        # don't run time if hidden
        if self.center[0] < 0:
            timeLeft = 1000
            
        if timeLeft < 0:
            self.timeOver = True

    def reset(self):
        self.timeOver = False
        self.timer.start()
            
class BtnQuit(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Quit"
        self.hide()
        
class BtnReset(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Reset"
        self.hide()
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.instructions = Instructions()
        self.lblTimer = LblTimer()
        self.btnQuit = BtnQuit()
        self.btnReset = BtnReset()
        
        self.sprites = [self.instructions, self.lblTimer, 
                        self.btnQuit, self.btnReset]


    def pauseGame(self):
        self.lblTimer.hide()
        self.btnQuit.show((220, 240))
        self.btnReset.show((420, 240))

    def resetGame(self):
        self.instructions.hide()
        self.btnQuit.hide()
        self.btnReset.hide()
        self.lblTimer.show((320, 240))
        self.lblTimer.reset()
         
    def update(self):
        if self.instructions.clicked:
            self.resetGame()            
        if self.lblTimer.timeOver:
            self.pauseGame()
        if self.btnQuit.clicked:
            self.stop()
        if self.btnReset.clicked:
            self.resetGame()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
    