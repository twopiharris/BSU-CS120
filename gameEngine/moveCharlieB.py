import pygame, simpleGE

""" moveCharlieB.py """

class MyScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        self.setCaption("Using polling in update of extended scene")
        self.charlie = simpleGE.Sprite(self)
        self.charlie.setImage("Charlie.png")
        self.charlie.setSize(50, 50)
        self.sprites = [self.charlie]
      
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.charlie.x -= 5
        if self.isKeyPressed(pygame.K_RIGHT):
            self.charlie.x += 5
        if self.isKeyPressed(pygame.K_UP):
            self.charlie.y -= 5
        if self.isKeyPressed(pygame.K_DOWN):
            self.charlie.y += 5


def main():
    scene = MyScene()
    scene.start()
    
if __name__ == "__main__":
    main()