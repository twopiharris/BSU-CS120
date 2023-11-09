import pygame, simpleGE
""" hideShow test """

class Game(simpleGE.Scene):
    
    """ used only for testing purposes. not a formal part of simpleGE """
    def __init__(self):
        super().__init__()
        self.red = simpleGE.SuperSprite(self)
        self.red.imageMaster = pygame.Surface((50, 50))
        self.red.imageMaster.fill(pygame.Color("red"))
        self.red.setPosition((320, 240))
        
        self.blue = simpleGE.SuperSprite(self)
        self.blue.imageMaster = pygame.Surface((50, 50))
        self.blue.imageMaster.fill(pygame.Color("blue"))
        self.blue.setPosition((220, 240))
 
        self.sprites = [self.red]
        
        self.blueGroup = self.makeSpriteGroup([self.blue])
        self.addGroup(self.blueGroup)
        
    def update(self):
        
        #control blue with keys
        if self.isKeyPressed(pygame.K_LEFT):
            self.blue.x -= 5
        if self.isKeyPressed(pygame.K_RIGHT):
            self.blue.x += 5

        """
        if self.red.collidesWith(self.blue):
            self.setCaption("Collision! (B or R to toggle sprites)")
        else:
            self.setCaption("No collision. (B or R to toggle sprites)")
        """
        
        collider = self.red.collidesGroup(self.blueGroup)
        if collider:
            self.setCaption("Group collision (B or R to toggle sprites)")
        else:
            self.setCaption("No group collision (B or R to toggle sprites)")
     
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                if self.blue.visible:
                    self.blue.hide()
                else:
                    self.blue.show()
                    
            if event.key == pygame.K_r:
                if self.red.visible:
                    self.red.hide()
                else:
                    self.red.show()
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    