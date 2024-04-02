import pygame, simpleGE, random
""" boundaries.py """

class Planet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("pluto.gif")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        newX = random.randint(0, self.screen.get_width())
        newY = random.randint(0, self.screen.get_height())
        self.position = (newX, newY)
        self.boundAction = self.WRAP
        if self.visible == False:
            self.show()
        
    def process(self):
        if self.isKeyPressed(pygame.K_SPACE):
            self.reset()
        if self.isKeyPressed(pygame.K_w):
            self.setBoundAction(self.WRAP)
        if self.isKeyPressed(pygame.K_b):
            self.setBoundAction(self.BOUNCE)
        if self.isKeyPressed(pygame.K_s):
            self.setBoundAction(self.STOP)
        if self.isKeyPressed(pygame.K_h):
            self.setBoundAction(self.HIDE)
        if self.isKeyPressed(pygame.K_c):
            self.setBoundAction(self.CONTINUE)
        
def main():
    game = simpleGE.Scene()
    game.setCaption("space = reset, (W)rap, (B)ounce, (S)top, (H)ide, (C)ontinue")
    planet = Planet(game)
    
    game.sprites = [planet]
    game.start()
    
if __name__ == "__main__":
    main()