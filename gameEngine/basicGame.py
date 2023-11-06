import pygame, simpleGE, random

class Charlie(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.y = 400
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5
     
class Coin(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(50, 50)
        self.sound = simpleGE.Sound("coin.wav")
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen.get_width())
        self.y = 10
        self.dy = random.randint(5, 10)
        
    def checkBounds(self):
        if self.rect.bottom > self.screen.get_height():
            self.reset()
            
    def checkEvents(self):
        if self.collidesWith(self.scene.charlie):
            self.sound.play()
            self.scene.lblScore.score += 1
            self.reset()
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (100, 50)
        self.text = "Score: 0"
        self.score = 0
        
    def update(self):
        super().update()
        self.text = f"Score: {self.score}"

class LblTime(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.center = (500, 50)
        self.timer = simpleGE.Timer()
        
    def update(self):
        super().update()
        timeLeft = 10 - self.timer.getElapsedTime()
        self.text = f"Time left: {timeLeft:.2f}"
        if timeLeft < 0:
            self.scene.endGame()

class BtnQuit(simpleGE.Button):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.center = (-1000, -1000)
        self.text = "Quit"
        
    def update(self):
        super().update()
        if self.clicked:
            self.scene.stop()
            
    def makeVisible(self):
        self.center = (150, 200)
        
class BtnReset(simpleGE.Button):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.center = (-1000, -1000)
        self.text = "Restart"
        
    def update(self):
        super().update()
        if self.clicked:
            self.scene.reset()
            
    def makeVisible(self):
        self.center = (450, 200)
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.charlie = Charlie(self)
        self.coins = []
        for i in range(10):
            self.coins.append(Coin(self))
        
        self.lblScore = LblScore()
        
        self.lblTime = LblTime(self)
        self.gameOver = False
        
        self.btnQuit = BtnQuit(self)
        self.btnReset = BtnReset(self)
        
        self.sprites = [self.lblTime, self.lblScore, 
                        self.charlie, self.coins,
                        self.btnQuit, self.btnReset]
        
    def endGame(self):
        self.btnQuit.makeVisible()
        self.btnReset.makeVisible()
        self.lblTime.text = "Time left: 0.00"
        
        # hide all the coins
        for coin in self.coins:
            coin.dx = 0
            coin.dy = 0
            coin.x = -1000
            coin.y = -1000
            
    def reset(self):
        self.btnQuit.center = (-1000, -1000)
        self.btnReset.center = (-1000, -1000)
        for coin in self.coins:
            coin.reset()
        self.lblTime.timer.start()
        self.lblScore.score = 0
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()