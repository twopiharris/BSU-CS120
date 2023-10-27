import pygame, simpleGE

""" moveCharlie.py """

class MyScene(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill("papayawhip")
        self.setCaption("Using doEvents in extended scene")
        self.charlie = simpleGE.BasicSprite(self)
        self.charlie.setImage("Charlie.png")
        self.charlie.setSize(50, 50)
        self.sprites = [self.charlie]

        
    def doEvents(self, event):
        if event.type == pygame.KEYPRESSED:
            if event.key == pygame.K_LEFT:
                self.charlie.x -= 5
            if event.key == pygame.K_RIGHT:
                self.charlie.x += 5
            if event.key == pygame.K_UP:
                self.charlie.y -= 5
            if event.key == pygame.K_DOWN:
                self.charlie.y += 5
        
def main():
    scene = MyScene()
    scene.start()
    
if __name__ == "__main__":
    main()