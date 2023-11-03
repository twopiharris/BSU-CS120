import pygame, simpleGE

""" space.py 
    illustrates space movement using simpleGE
    ship images modified from Ari's spritelib.
"""

class Ship(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "cruise": pygame.image.load("shipCruise.png"),
            "left":   pygame.image.load("shipLeft.png"),
            "right":  pygame.image.load("shipRight.png"),
            "thrust": pygame.image.load("shipThrust.png")}
        self.imageMaster = self.images["cruise"]
        
    def checkEvents(self):
        self.imageMaster = self.images["cruise"]
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.rotateBy(5)
            self.imageMaster = self.images["right"]
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.rotateBy(-5)
            self.imageMaster = self.images["left"]    
        if self.scene.isKeyPressed(pygame.K_UP):
            self.addForce(.2, self.rotation)
            self.imageMaster = self.images["thrust"]
            
def main():
    game = simpleGE.Scene()
    game.setCaption("Pygame in SPAAAAACE!")
    ship = Ship(game)
    game.sprites = [ship]
    game.start()
    
if __name__ == "__main__":
    main()

