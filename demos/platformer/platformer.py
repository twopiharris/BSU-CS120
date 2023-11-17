""" platformer """

import pygame, simpleGE

class Charlie(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.setPosition((50, 400))
        self.inAir = True
            
    def checkEvents(self):
        if self.inAir:
            self.addForce(.2, 270)
        
        if self.y > 450:
            self.inAir = False
            self.y = 450
            self.setDY(0)          
        
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5
            
        if self.scene.isKeyPressed(pygame.K_UP):
            if not self.inAir:
                #self.y -= 10
                self.addForce(6, 90)
                self.inAir = True
                
        platform = self.collidesGroup(self.scene.platformGroup)
        if platform:
            if self.dy > 0:
                overlap = platform.rect.top - self.rect.bottom
                self.changeYby(overlap + 1)
                self.setDY(0)
                self.inAir = False
        else:
            self.inAir = True

class Platform(simpleGE.SuperSprite):
    def __init__(self, scene, position):
        super().__init__(scene)
        self.setPosition(position)
        self.imageMaster = pygame.Surface((50, 50))
        self.imageMaster.fill(pygame.Color("red"))
        
    def update(self):
        super().update()
        if self.mouseDown():
            self.setPosition(pygame.mouse.get_pos())

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("arrows to move and jump. drag platforms around")

        self.charlie = Charlie(self)
        self.sprites = [self.charlie]

        platforms = [Platform(self, (100, 450)), Platform(self, (150, 450)), 
                     Platform(self, (200, 450)), Platform(self, (250, 450)),
                     Platform(self, (300, 350)), Platform(self, (350, 350))]
        
        self.platformGroup = self.makeSpriteGroup(platforms)
        self.addGroup(self.platformGroup)

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    