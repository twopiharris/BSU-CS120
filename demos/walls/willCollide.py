import pygame, simpleGE

""" willCollide """

class Thing(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (50, 50))
        self.moveSpeed = 5
        
    def process(self):
        barrier = self.scene.barrier
        if self.isKeyPressed(pygame.K_LEFT):
            if not self.willCollide(barrier):
                self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            if not self.willCollide(barrier):
                self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed

    def willCollide(self, target):
        # checks to see if sprite will collide with the
        # target on the next frame without actually
        # moving it
        
        collision = False
        
        newWidth = self.rect.width 
        newHeight = self.rect.height
        
        biggerRect = self.rect.inflate(newWidth, newHeight)
        if biggerRect.colliderect(target.rect):
            collision = True
        
        return collision
            
        
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.thing = Thing(self)
        
        self.barrier = simpleGE.Sprite(self)
        self.barrier.colorRect("red", (50, 50))
        self.barrier.position = (320, 240)
        
        self.sprites = [self.thing,
                        self.barrier]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    
