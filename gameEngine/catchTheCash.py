""" catchTheCash.py 
    coin image - https://opengameart.org/content/coin-icon
    coin sound - https://opengameart.org/content/plingy-coin
"""
import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.charlie = Charlie(self)
        
        self.coins = []
        for i in range(5):
            self.coins.append(Coin(self))
            
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50, 50)
        self.score = 0

        self.lblTime = simpleGE.Label()
        self.lblTime.text = "Time left: 30"
        self.lblTime.center = (550, 50)

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30

        self.sprites = [self.lblScore, self.lblTime, self.charlie, self.coins]

    def update(self):
        timeLeft = self.timer.getTimeLeft()
        if timeLeft < 0:
            self.stop()
        self.lblTime.text = f"Time left: {timeLeft:.2f}"
        self.lblScore.text = f"score: {self.score}"

class Charlie(simpleGE.Sprite):
    """ moves on bottom of screen with arrows """
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.moveSpeed = 5
        self.y = 400

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Coin(simpleGE.Sprite):
    """ falls from top of screen at random speed
       when reset appears at new speed and position
       at top of screen """
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(50, 50)
        self.coinSound = simpleGE.Sound("coin.wav")
        self.reset()

    def reset(self):
        newX = random.randint(0, 640)
        self.x = newX
        self.y = 10
        self.dy = random.randint(5,10)
        
    def process(self):
        if self.collidesWith(self.scene.charlie):
            self.scene.score += 1
            self.coinSound.play()
            self.reset()
        
    def checkBounds(self):
        if self.rect.bottom > self.screen.get_height():
            self.reset()

def main():
    game = Game()
    game.start()
    print (f"final score: {game.score}")

if __name__ == "__main__":
    main()        
        
