import pygame, simpleGE, math

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
        self.setSpeed(self.scene.scrVelocity.value)
        self.calcVector()
        
    def checkEvents(self):
        if self.visible:
              self.addDY(1)
        else:
            self.setSpeed(0)
            
    def calcVector(self):
        # vector projection was not happening correctly.
        # will be corrected in next version of simpleGE
        theta = self.dir / 180.0 * math.pi
        self.dx = math.cos(theta) * self.speed
        self.dy = math.sin(theta) * self.speed
        self.dy *= -1        
        
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
        if self.scene.isKeyPressed(pygame.K_UP):
            scroller = self.scene.scrVelocity
            if scroller.value < scroller.maxValue:
                scroller.value += 1
        if self.scene.isKeyPressed(pygame.K_DOWN):
            scroller = self.scene.scrVelocity
            if scroller.value > scroller.minValue:
                scroller.value -= 1            
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.scene.bullet.fire()

class ScrVelocity(simpleGE.Scroller):
    def __init__(self):
        super().__init__()
        self.minValue = 0
        self.maxValue = 30
        self.value = 15
        self.center = ((200, 450))

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.gun = Gun(self)
        self.bullet = Bullet(self, self.gun)
        self.scrVelocity = ScrVelocity()

        self.sprites = [self.bullet, self.gun, self.scrVelocity]

        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()