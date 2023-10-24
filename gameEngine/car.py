import pygame, gameEngine, random

""" car image - Andy Harris
    coin image - https://opengameart.org/content/coin-icon
    coin sound - https://opengameart.org/content/plingy-coin
"""

def main():
  pygame.mixer.init()
  scene = gameEngine.Scene()
  scene.background.fill(pygame.Color("papayawhip"))
  scene.setCaption("Baby You Can Drive My Car!")
  scene.car = Car(scene)
  scene.coin = Coin(scene)
  scene.sprites = [scene.car, scene.coin]

  scene.start()

class Car(gameEngine.SuperSprite):
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
    if keys[pygame.K_RIGHT]:
      self.turnBy(-5)
    if keys[pygame.K_UP]:
      self.forward(5)
    if keys[pygame.K_DOWN]:
      self.forward(-5)

  def checkCollision(self):
    if self.collidesWith(self.scene.coin):
      self.coinSound.play()
      self.scene.coin.reset()

  def checkEvents(self):
    self.checkKeys()
    self.checkCollision()

class Coin(gameEngine.SuperSprite):
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
