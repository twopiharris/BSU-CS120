""" bouncingCharlie.py """

import pygame, simpleGE, random

class Charlie(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(100, 100)
        self.reset()
        
    def reset(self):
        """pick random dx and dy"""
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.reset()
            
    def checkBounds(self):
        if self.rect.left <= 0:
            self.dx *= -1
        if self.rect.right >= self.screen.get_width():
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1
        if self.rect.bottom >= self.screen.get_height():
            self.dy *= -1
            
def main():
    scene = simpleGE.Scene()
    scene.setCaption("space bar to change direction")
    charlie = Charlie(scene)
    scene.sprites = [charlie]

    scene.start()
    
if __name__ == "__main__":
    main()
    