""" collisionTest.py """

import pygame, simpleGE

class MovyThing(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Blue", (50, 50))
        
    def process(self):
        #self.speed = 0
        self.correction = (0, 0)
        if self.isKeyPressed(pygame.K_a):
            self.x -= 5
            self.correction = (5, 0)
        elif self.isKeyPressed(pygame.K_d):
            self.x += 5
            self.correction = (-5, 0)
        elif self.isKeyPressed(pygame.K_w):
            self.y -= 5
            self.correction = (0, 5)
        elif self.isKeyPressed(pygame.K_s):
            self.y += 5
            self.correction = (0, -5) 

        #barrier check
        barrier = self.scene.barrier
        if self.collidesWith(barrier):
            self.x += self.correction[0]
            self.y += self.correction[1]
            
            
class DrivyThing(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("car.png")
        self.setSize(50, 30)
        self.setAngle(45)
        
    def process(self):
        
        if self.isKeyPressed(pygame.K_UP):
            self.speed += .1
        if self.isKeyPressed(pygame.K_DOWN):
            self.speed -= .1
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle += 5 
            self.moveAngle += 5
        if self.isKeyPressed(pygame.K_RIGHT):
            self.imageAngle -= 5 
            self.moveAngle -= 5
            
        if self.speed > 5:
            self.speed = 5
            
        barrier = self.scene.barrier
        if self.collidesWith(barrier):

            self.x -= self.dx
            self.y -= self.dy
            self.speed = 0

class Game(simpleGE.Scene):
    
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        self.setCaption("WASD for box, arrows for car")
        self.drivy = DrivyThing(self)
        self.drivy.position = (500, 100)
        self.movy = MovyThing(self)
        
        self.barrier = simpleGE.Sprite(self)
        self.barrier.colorRect("red", (100, 100))
        self.barrier.x = 320
        self.barrier.y = 240
        self.sprites = [self.barrier,
                        self.movy,
                        self.drivy] 
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()