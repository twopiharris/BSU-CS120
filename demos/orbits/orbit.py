import pygame, simpleGE, math

""" orbit.py
    Newton's law of Universal gravitation

      m1 * m2
f =   ------   G
      d^2
      
"""
class Ship(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "cruise": pygame.image.load("shipCruise.png"),
            "left":   pygame.image.load("shipLeft.png"),
            "right":  pygame.image.load("shipRight.png"),
            "thrust": pygame.image.load("shipThrust.png")}
        self.copyImage(self.images["cruise"])
        self.setAngle(90)
        self.mass = 1
        self.boundAction = self.CONTINUE
        
    def process(self):
        self.copyImage(self.images["cruise"])
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle += 5
            self.copyImage(self.images["right"])
        if self.isKeyPressed(pygame.K_RIGHT):
            self.imageAngle -= 5
            self.copyImage(self.images["left"])    
        if self.isKeyPressed(pygame.K_UP):
            self.addForce(.05, self.imageAngle)
            self.copyImage(self.images["thrust"])   
        if self.isKeyPressed(pygame.K_SPACE):
            self.scene.background.fill("black")
            
class Planet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Pluto.gif")
        self.setSize(30, 30)
        self.mass = 500
        self.x = 320
        self.y = 240
        
    def gravitate(self, body):
        distance = self.distanceTo(self.scene.ship.position)
        force = (body.mass * self.mass)/distance **2
        direction = self.scene.ship.dirTo(self.position)
        self.scene.ship.addForce(force, direction)
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("arrows to control ship, space to clear trace")
        self.ship = Ship(self)
        self.ship.position = (320, 200)
        self.ship.setAngle(0)
        self.ship.speed = 3
        
        self.planet = Planet(self)
        
        self.sprites = [self.ship, self.planet]
        
    def process(self):
        self.planet.gravitate(self.ship)
        self.ship.drawTrace("gray")
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    

