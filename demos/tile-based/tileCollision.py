import pygame, simpleGE

""" tileCollision.py
    demonstrate basic tbw 
    tile images from lpc Atlas - openGameArt
    http://opengameart.org/content/lpc-tile-atlas
    """
   
class LblOutput(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (320, 25)
        self.text = "current tile: "        
    
class Player(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((20, 20))
        self.imageMaster.fill("blue")
        self.moveSpeed = 2

    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_UP):
            self.changeYby(-self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.changeYby(self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.changeXby(-self.moveSpeed)
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.changeXby(self.moveSpeed)
        
class Tile(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("grass.png"),
            pygame.image.load("dirt.png"),
            pygame.image.load("water.png")]
        
        self.stateName = ["grass", "dirt", "water"]
        
        self.setSize(32, 32)
        self.GRASS = 0
        self.DIRT = 1
        self.WATER = 2
        self.state = self.GRASS
        self.clicked = False
        self.active = False
        
    def setState(self, state):
        self.state = state
        self.image = self.images[state]
        
    def checkClick(self):
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

    def checkEvents(self):
        self.checkClick()
        if self.clicked:
            newState = self.state + 1
            if newState > 2:
                newState = 0
            self.setState(newState)    
            
        # look for player
        if self.collidesWith(self.scene.player):
            self.scene.lblOutput.text = self.stateName[self.state]
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Click on a tile to edit")
        self.tileset = []
        
        self.ROWS = 15
        self.COLS = 20
        
        self.loadMap()
        
        self.player = Player(self)
        self.lblOutput = LblOutput()
        
        self.sprites = [self.tileset, self.player, self.lblOutput]
        
    def loadMap(self):
        
      map = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],  
          [2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],  
          [2,2,2,2,2,2,0,0,0,0,1,0,0,0,0,0,2,2,2,2],  
          [0,2,2,2,2,2,2,0,0,0,1,0,0,0,2,2,2,2,2,0],  
          [0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,2,0,0,0,0],  
          [0,0,0,0,0,0,0,2,2,2,1,2,2,2,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
      ]
    
      for row in range(self.ROWS):
          self.tileset.append([])
          for col in range(self.COLS):
            currentVal = map[row][col]
            newTile = Tile(self)
            newTile.setState(currentVal)
            xPos = 16 + (32 * col)
            yPos = 16 + (32 * row)
            newTile.x = xPos
            newTile.y = yPos
            self.tileset[row].append(newTile)
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()