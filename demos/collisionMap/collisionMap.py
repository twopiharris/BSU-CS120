import pygame, simpleGE

""" collisionMap Demo
    describe how to use a collision map


    Normally we would simply draw the color
    background in place and use the b&w version for
    collision mapping. It isn't necessary to ever show
    the collision map, but I put it in a large sprite
    for illustration purposes.
    
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("trackColor.png")
        
        self.car = Car(self)
        
        # It isn't necessary to build this sprite
        # I just did it for illustration purposes
        
        self.bwTrack = simpleGE.Sprite(self)
        self.bwTrack.setImage("trackBW.png")
        self.bwTrack.position = (320, 240)
        self.bwTrack.hide()
        self.sprites = [self.bwTrack,
                        self.car]
        self.setCaption("B for black and white, C for color")
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print("B and W")
                self.bwTrack.show()
                
            if event.key == pygame.K_c:
                print("Color")
                self.bwTrack.hide()
                
        
class Car(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (50, 25))
        self.moveSpeed = 5
        self.colMap = pygame.image.load("trackBW.png")
        
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.turnBy(5)
        if self.isKeyPressed(pygame.K_RIGHT):
            self.turnBy(-5)
        if self.isKeyPressed(pygame.K_UP):
            self.forward(self.moveSpeed)
        if self.isKeyPressed(pygame.K_DOWN):
            self.forward(-3)
        
        #here's the collision magic!
        colorUnder = self.colMap.get_at((int(self.position[0]),
                                        int(self.position[1])))
        
        # do whatever you want with various colors
        # in this case I go full speed on black (0, 0, 0)
        # and much slower on any other color.
        # you can add other colors for drag, 'oil stains', etc
        
        if colorUnder == (0, 0, 0):
            self.moveSpeed = 5
        else:
            self.moveSpeed = 1
    

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()