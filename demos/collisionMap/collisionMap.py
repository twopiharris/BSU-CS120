import pygame, simpleGE

""" collisionMap Demo
    describe how to use a collision map
    
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("trackBW.png")
        
        self.car = Car(self)
        self.prettyTrack = simpleGE.Sprite(self)
        self.prettyTrack.setImage("trackColor.png")
        self.prettyTrack.position = (320, 240)
        self.prettyTrack.hide()
        self.sprites = [self.prettyTrack,
                        self.car]
        self.setCaption("B for black and white, C for color")
        
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print("B and W")
                self.prettyTrack.hide()
                
            if event.key == pygame.K_c:
                print("Color")
                self.prettyTrack.show()
                
        
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
            
        colorUnder = self.colMap.get_at((int(self.position[0]),
                                        int(self.position[1])))
        if colorUnder == (255, 255, 255):
            self.moveSpeed = 1
        else:
            self.moveSpeed = 5
    

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()