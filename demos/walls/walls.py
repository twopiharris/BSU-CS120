import pygame, random, simpleGE

""" walls.py 
    predictive collision detection

"""

class Player (simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((50, 50))
        self.imageMaster.fill(pygame.Color("blue"))
        self.rect = self.imageMaster.get_rect()
        self.moveSpeed = 5
        self.setPosition((100, 100))

    def checkEvents(self):
        self.setDX(0)
        self.setDY(0)
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.setDX(-self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.setDX(self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_UP):
            self.setDY(-self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.setDY(self.moveSpeed)        

    def collidesSolid(self, target):
        """ overwritten collision handler
            treats all objects as solids """
        result = False
        # larger gap less likely to overlap
        # but will seem to 'jump' more
        gap = 10
            
        if self.rect.colliderect(target.rect):
            result = True
            if self.dx > 0:
                self.setDX(0)
                self.changeXby(-(self.moveSpeed + gap))
            if self.dx < 0:
                self.setDX(0)
                self.changeXby(self.moveSpeed + gap)
            if self.dy > 0:
                self.setDY(0)
                self.changeYby(-(self.moveSpeed + gap))
            if self.dy < 0:
                self.setDY(0)
                self.changeYby(self.moveSpeed + gap)
                
        return result

class Target(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((50, 50))
        self.imageMaster.fill(pygame.Color("white"))
        self.rect = self.imageMaster.get_rect()
        self.setPosition((320, 240))
        
    def reset(self):
        newX = random.randint(0, 640)
        newY = random.randint(0, 480)
        self.setPosition((newX, newY))

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.player = Player(self)
        self.targets = []
        for i in range(10):
            newTarget = Target(self)
            newTarget.reset()
            self.targets.append(newTarget)
        self.sprites = [self.player]
        for target in self.targets:
            self.sprites.append(target)

    def update(self):
        for target in self.targets:
            self.player.collidesSolid(target)

        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()


