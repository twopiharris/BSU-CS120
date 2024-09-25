import pygame, simpleGE, math

""" skid.py
    add skidding behavior to car physics model
    not perfect but works pretty well...
"""

class Car(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("car.png")
        self.setSize(30,20)
        self.drag = .07
        self.accel = .5
        self.turnRate = 5
        self.grip = .95
        
    def process(self):
        # turn more like a space ship
        
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle += self.turnRate
        elif self.isKeyPressed(pygame.K_RIGHT):
            self.imageAngle -= self.turnRate            
        elif self.isKeyPressed(pygame.K_UP):
            self.addForce(self.accel * self.grip, self.imageAngle)
            
        #add small momentum force
        self.addForce(self.speed * (1 - self.grip), self.imageAngle)
      
        #compensate for drag.
        self.speed *= (1 - self.drag)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("gray")
        
        self.car = Car(self)
        self.car.position = (200, 200)
                
        self.sprites = [self.car]
        
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()