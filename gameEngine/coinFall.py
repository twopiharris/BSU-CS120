import pygame, simpleGE, random

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        newX = random.randint(0, 640)
        self.x = newX
        self.y = 10
        self.fallSpeed = random.randint(5,10)
        
    def process(self):
        self.y += self.fallSpeed
       
    def checkBounds(self):
        if self.rect.bottom > self.scene.background.get_height():
            self.reset()
            
def main():
    scene = simpleGE.Scene()
    
    coin = Coin(scene)
    scene.sprites = [coin]
    
    """
    coins = []
    
    for i in range(200):
        coins.append(Coin(scene))
    scene.sprites = coins
    """
    
    scene.start()
    
if __name__ == "__main__":
    main()
