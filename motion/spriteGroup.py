""" spriteGroup.py 
    demonstrates spriteGroups """
    
import pygame, random, simpleGE, space, orbit

class Planet(orbit.Planet):
    def __init__(self, scene):
        super().__init__(scene)
        self.reset()
        
    def reset(self):
        self.x = (random.randint(0, self.screen.get_width()))
        self.y = (random.randint(0, self.screen.get_height()))
        self.setDX(random.randint(-5, 5))
        self.setDY(random.randint(-5, 5))
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.ship = space.Ship(self)
        planets = []
        for i in range(5):
            planets.append(Planet(self))
        self.planetGroup = self.makeSpriteGroup(planets)
        self.sprites = [self.ship]
        self.addGroup(self.planetGroup)
        
    def update(self):
        planetHit = self.ship.collidesGroup(self.planetGroup)
        if planetHit:
            planetHit.reset()
            
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    
        
        
    