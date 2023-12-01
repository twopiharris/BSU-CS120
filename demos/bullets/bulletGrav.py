import pygame, simpleGE

""" bullets with gravity """


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
        
    def checkEvents(self):
        self.addDY(.1)
        
class Gun(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("turret.gif")
        self.setPosition((30, 450))
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.rotateBy(5)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.rotateBy(-5)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.scene.bullet.fire()


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.gun = Gun(self)
        self.bullet = Bullet(self, self.gun)

        self.sprites = [self.bullet, self.gun]

        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()