import pygame, simpleGE, random

""" car image - Andy Harris
    coin image - https://opengameart.org/content/coin-icon
    coin sound - https://opengameart.org/content/plingy-coin
"""

def main():
  pygame.mixer.init()
  scene = simpleGE.Scene()
  scene.background.fill(pygame.Color("papayawhip"))
  scene.setCaption("Baby You Can Drive My Car!")

  scene.car = Car(scene)
  scene.coin = Coin(scene)

  scene.lblTimer = simpleGE.Label()
  scene.lblTimer.center = (100, 30)

  scene.lblScore = simpleGE.Label()
  scene.lblScore.center = (550, 30)
  scene.lblScore.text = "Score: 0"

  scene.btnQuit = simpleGE.Button()
  scene.btnQuit.text = 'Quit'
  scene.btnQuit.hide()

  scene.sprites = [scene.lblTimer, scene.lblScore, 
                   scene.car, scene.coin, scene.btnQuit]

  scene.score = 0
  scene.timer = simpleGE.Timer()
  scene.MAXTIME = 30
  
  scene.start()

class Car(simpleGE.SuperSprite):
  def __init__(self, scene):
    super().__init__(scene)
    self.setImage("car.gif")
    self.setSize(50, 25)
    self.coinSound = pygame.mixer.Sound("coin.wav")
    self.setPosition((50, 50))

  def checkKeys(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.turnBy(5)
    elif keys[pygame.K_RIGHT]:
      self.turnBy(-5)
    if keys[pygame.K_UP]:
      self.forward(5)
    elif keys[pygame.K_DOWN]:
      self.forward(-5)

  def checkCollision(self):
    if self.collidesWith(self.scene.coin):
      self.scene.score += 1
      self.scene.lblScore.text = f"Score: {self.scene.score}"
      self.coinSound.play()
      self.scene.coin.reset()

  def checkTime(self):
    time = self.scene.timer.getElapsedTime()
    if time > self.scene.MAXTIME:
      self.scene.btnQuit.show((300, 200))
    else:
      timeLeft = self.scene.MAXTIME - time
      self.scene.lblTimer.text = f"time left: {timeLeft:.2f}"
    if self.scene.btnQuit.clicked:
        self.scene.stop()

  def checkEvents(self):
    self.checkTime()
    self.checkKeys()
    self.checkCollision()

class Coin(simpleGE.SuperSprite):
  def __init__(self, scene):
    super().__init__(scene)
    self.reset()
    self.setImage("Coin.png")
    self.setSize(25, 25)

  def reset(self):
    """ move to a new position """
    newX = random.randint(0, 640)
    newY = random.randint(0, 480)
    self.setPosition((newX, newY))

if __name__ == "__main__":
  main()
