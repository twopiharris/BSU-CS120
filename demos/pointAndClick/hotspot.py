import pygame, simpleGE

""" hotspot.py
    demonstrates hot spots on a point and click map
"""

class HotSpot(simpleGE.BasicSprite):
    """ defines a rectangular area that can be 
        active or clicked.  By default, it is 
        semi-transparent white.  Once you have 
        positioned it, set transparent to True """
    
    def __init__(self, scene):
        super().__init__(scene)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 255, 255, 100))
        self.rect = self.image.get_rect()
        self.active = False
        self.clicked = False
        self.transparent = False
        
    def checkEvents(self):
        #check for clicked and active                
        
        self.clicked = False

        #check for mouse input
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = True

        #check for mouse release
        if self.active == True:
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.active = False
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True

        #check for transparency
        if self.transparent:
            self.image.fill(pygame.Color(255, 255, 255, 0))
        else:
            self.image.fill(pygame.Color(255, 255, 255, 100))
                    
    def setPosition(self, position):
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("example_map.png")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Find the hot spots")
        
        self.hsVolcano = HotSpot(self)
        self.hsVolcano.setSize(110, 100)
        self.hsVolcano.setPosition((120, 80))
        self.hsVolcano.transparent = True

        self.hsTree = HotSpot(self)
        self.hsTree.setPosition((400, 200))
        self.hsTree.setSize(100, 130)
        self.hsTree.transparent = True
        
        self.lblOutput = simpleGE.Label()
        self.lblOutput.center = ((320, 400))
        self.lblOutput.text = ""
        
        self.sprites = [self.hsVolcano, self.hsTree, self.lblOutput]
        
    def update(self):
        self.lblOutput.text = ""
        if self.hsVolcano.active:
            self.lblOutput.text = "Volcano"
        if self.hsTree.active:
            self.lblOutput.text = "Tree"
            
        if self.hsVolcano.clicked:
            print("You clicked on the volcano")
            
        if self.hsTree.clicked:
            print("You clicked on the tree")
        
def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()
        
       
