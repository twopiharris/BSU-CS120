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
        self.NUM_BULLETS = 100
        self.currentBullet = 0          
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.ship))
                                
        self.sprites = [self.ship, self.bullets]

    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentBullet += 1
                if self.currentBullet >= self.NUM_BULLETS:
                    self.currentBullet = 0
                self.bullets[self.currentBullet].fire()
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()

        