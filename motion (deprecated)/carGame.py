import pygame, simpleGE, random

""" car image - Andy Harris
    coin image - https://opengameart.org/content/coin-icon
    coin sound - https://opengameart.org/content/plingy-coin
"""

class Car(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("car.png")
        self.setSize(100, 50)
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.turnBy(5)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.turnBy(-5)
        if self.scene.isKeyPressed(pygame.K_UP):
            self.forward(5)
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.forward(-5)
        
def main():
    game = simpleGE.Scene()
    game.background.fill("papayawhip")
    game.car = Car(game)
    game.sprites = [game.car]
    game.start()
    
if __name__ == "__main__":
    main()
    
            