import pygame, simpleGE

class Charlie(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
        if self.scene.isKeyPressed(pygame.K_UP):
            self.y -= 5
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.y += 5
            
def main():
    scene = simpleGE.Scene()
    scene.background.fill("papayawhip")
    scene.setCaption("Using checkEvents in extended BasicSprite")
    charlie = Charlie(scene)
    scene.sprites = [charlie]
    scene.start()
    
if __name__ == "__main__":
    main()
    
    