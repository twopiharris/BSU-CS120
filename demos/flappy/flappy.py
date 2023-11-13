import pygame, simpleGE, random

""" flappy.py 
    basic flappy bird prototype """
    
class Charlie(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.setPosition((100, 100))
        
    
    def checkEvents(self):
        self.addForce(.1, 270)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.setDY(0)
            self.addForce(5, 90)    

class Barrier(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((80, 200))
        self.imageMaster.fill(pygame.Color("green"))
        self.setPosition((600, 0))    
        self.setDX(-3)
        
    def checkBounds(self):
        #only check for leave left
        if self.x < 0:
            self.scene.reset()
            
    def checkEvents(self):
        if self.collidesWith(self.scene.charlie):
            self.scene.reset() 
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.charlie = Charlie(self)
        self.upperBarrier = Barrier(self)
        self.lowerBarrier = Barrier(self)
        self.gap = 400
        self.reset()
        self.sprites = [self.charlie, self.upperBarrier, self.lowerBarrier]
        
    def reset(self):        
        self.topPosition = random.randint(0, 200)
        self.bottomPosition = self.topPosition + self.gap
        self.upperBarrier.setPosition((640, self.topPosition))
        self.lowerBarrier.setPosition((640, self.bottomPosition))
        
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    
        