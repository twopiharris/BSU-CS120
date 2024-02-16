import pygame, simpleGE, math

""" orbit.py """


class Ship(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "cruise": pygame.image.load("shipCruise.png"),
            "left":   pygame.image.load("shipLeft.png"),
            "right":  pygame.image.load("shipRight.png"),
            "thrust": pygame.image.load("shipThrust.png")}
        self.imageMaster = self.images["cruise"]
        self.mass = 1
        self.x = 320
        self.y = 150
        self.setDX(2)
        
    def checkEvents(self):
        self.imageMaster = self.images["cruise"]
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.rotateBy(5)
            self.imageMaster = self.images["right"]
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.rotateBy(-5)
            self.imageMaster = self.images["left"]    
        if self.scene.isKeyPressed(pygame.K_UP):
            self.addForce(.02, self.rotation)
            self.imageMaster = self.images["thrust"]
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.scene.background.fill("black")
            
class Planet(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Pluto.gif")
        self.setSize(30, 30)
        self.mass = 500
        self.x = 320
        self.y = 240
        
    def gravitate(self, body):
        distance = self.distanceTo(self.scene.ship.rect.center)
        force = (body.mass * self.mass)/distance **2
        direction = self.scene.ship.dirTo(self.rect.center)
        self.scene.ship.addForce(force, direction)
        

        """
        thetaX = self.x - body.x
        thetaY = self.y - body.y
        distance = math.sqrt((thetaX ** 2) + (thetaY ** 2))
        
        #normalize theta
        thetaX /= distance
        thetaY /= distance
        force = (body.mass * self.mass)/distance **2
        
        thetaX *= force
        thetaY *= force
        
        body.dx += thetaX
        body.dy += thetaY
        body.updateVector()
        """
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("arrows to control ship, space to clear trace")
        self.ship = Ship(self)
        self.planet = Planet(self)
        
        self.sprites = [self.ship, self.planet]
        
    def update(self):
        self.planet.gravitate(self.ship)
        self.ship.drawTrace("gray")
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    

