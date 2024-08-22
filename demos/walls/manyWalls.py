""" collisionTest.py """

import pygame, simpleGE, collisions
class MovyThing(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("Blue", (50, 50))
        
    def process(self):
        self.speed = 0
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
        for barrier in self.scene.walls:
            if self.collidesWith(barrier):
                self.x += self.correction[0]
                self.y += self.correction[1]
            
class LblOut(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 30)
        self.size = (200, 30)
        self.fgColor = "blue"
        self.bgColor = "white"
        self.clearBack = True
         
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
            
        for barrier in self.scene.walls:
            if self.collidesWith(barrier):
                self.x -= self.dx * 2
                self.y -= self.dy * 2
                self.speed = 0
          
class Wall(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("red", (50, 50))
        
    def process(self):
        if self.mouseDown:
            self.position = pygame.mouse.get_pos()
        
class Game(simpleGE.Scene):

    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        self.setCaption("WASD for box, arrows for car, drag red barriers")
        self.drivy = DrivyThing(self)
        self.drivy.position = (500, 100)
        self.movy = MovyThing(self)
        
        self.walls = []
        for i in range(10):
            newWall = Wall(self)
            newWall.y = 300
            newWall.x = (i * 50) + 125
            self.walls.append(newWall)
        
        self.lblOut = LblOut()
        self.sprites = [self.lblOut, 
                        self.walls,
                        self.movy,
                        self.drivy]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()