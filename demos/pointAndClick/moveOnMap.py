import pygame, simpleGE

""" point and click
    various techniques for point and click
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            dir = self.ship.dirTo(mousePos)
            dist = self.ship.distanceTo(mousePos)
            if dist > 20:
                self.ship.setMoveAngle(dir)
                self.ship.setSpeed(3)
            else:
                self.ship.setSpeed(0)
        else:
            self.ship.setSpeed(0)
            
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    