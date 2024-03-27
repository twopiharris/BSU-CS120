import pygame, simpleGE, random

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

class Box(simpleGE.SuperSprite):
    def __init__(self, scene, colorName = "yellow"):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((50, 50))
        self.imageMaster.fill(pygame.Color(colorName))
        self.setBoundAction(self.WRAP)
        self.hide()
        
    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = random.randint(0, self.screen.get_height())
        self.setDX(random.randint(-5, 5))
        self.setDY(random.randint(-5, 5))
        
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
        self.box = Box(self)
        
        self.blueBoxes = []
        for i in range(10):
            self.blueBoxes.append(Box(self, "blue"))
            
        self.sprites = [self.instructions, self.lblTimer, 
                        self.btnQuit, self.btnReset, 
                        self.box, self.blueBoxes]

    def pauseGame(self):
        self.lblTimer.hide()
        self.box.hide()
        for bbox in self.blueBoxes:
            bbox.hide()
            
        self.btnQuit.show((220, 240))
        self.btnReset.show((420, 240))

    def resetGame(self):
        self.instructions.hide()
        self.btnQuit.hide()
        self.btnReset.hide()
        self.lblTimer.show((320, 240))
        self.lblTimer.reset()

        self.box.show()
        self.box.reset()

        for bbox in self.blueBoxes:
            bbox.show()
            bbox.reset()
        
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
    