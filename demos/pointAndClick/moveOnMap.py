import pygame, simpleGE

""" point and click
    various techniques for point and click
    
    pirate ship: https://opengameart.org/content/old-fashioned-pirate-ship
    map: https://opengameart.org/content/simple-map-tiles
    """
    
    
class Ship(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("ship_parallax_complete.png")
        self.setSize(100, 50)
        self.setPosition((320, 240))
        
    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("example_map.png")
        self.background = pygame.transform.scale(self.background, (640, 480))
        
        self.ship = Ship(self)
        
        self.sprites = [self.ship]
        
    def doEvents(self, event):
        # find direction from mouse position
        mousePos = pygame.mouse.get_pos()
        dir = self.ship.dirTo(mousePos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.ship.setMoveAngle(dir)
            self.ship.setSpeed(3)
        else:
                self.ship.setSpeed(0)
                
    def update(self):
        # move until close to mouse position
        mousePos = pygame.mouse.get_pos()
        dist = self.ship.distanceTo(mousePos)
        if dist < 5:
            self.ship.setSpeed(0)
        
            

        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    