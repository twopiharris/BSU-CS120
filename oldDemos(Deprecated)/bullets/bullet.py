import pygame, simpleGE, random, space

""" bullet.py """

class Bullet(simpleGE.SuperSprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.imageMaster = pygame.Surface((5, 5))
        self.imageMaster.fill(pygame.Color("white"))
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        self.show()
        self.setPosition(self.parent.rect.center)
        self.setMoveAngle(self.parent.rotation)
        self.setSpeed(20)
        
        
class Ship(space.Ship):
    def __init__(self, scene):
        super().__init__(scene)


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.ship = Ship(self)
        self.bullet = Bullet(self, self.ship)
        self.sprites = [self.ship, self.bullet]
        
        #self.bullets

    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullet.fire()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()

        