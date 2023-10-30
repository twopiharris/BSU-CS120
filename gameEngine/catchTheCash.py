""" catchTheCash.py """
import pygame, simpleGE, random


class Charlie(simpleGE.BasicSprite):
    """ moves on bottom of screen with arrows """
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.moveSpeed = 5
        self.y = 400

    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Coin(simpleGE.BasicSprite):
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
        self.fallSpeed = random.randint(5,10)
	
    def checkEvents(self):
        self.y += self.fallSpeed
        timeLeft = 30 - self.scene.timer.getElapsedTime()
        self.scene.lblTime.text = f"Time left: {timeLeft:.2f}"
        if timeLeft < 0:
            self.scene.stop()

        if self.collidesWith(self.scene.charlie):
            self.scene.score += 1
            self.scene.lblScore.text = f"score: {self.scene.score}"
            self.coinSound.play()
            self.reset()


def main():
    scene = simpleGE.Scene()
    scene.charlie = Charlie(scene)
    scene.coin = Coin(scene)

    scene.lblScore = simpleGE.Label()
    scene.lblScore.text = "Score: 0"
    scene.lblScore.center = (50, 50)
    scene.score = 0

    scene.lblTime = simpleGE.Label()
    scene.lblTime.text = "Time left: 30"
    scene.lblTime.center = (550, 50)

    scene.timer = simpleGE.Timer()

    scene.sprites = [scene.lblScore, scene.lblTime, scene.charlie, scene.coin]

    scene.start()

if __name__ == "__main__":
  main()        
        
