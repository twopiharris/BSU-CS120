import pygame, simpleGE

""" tileMap.py
    demonstrate basic tbw 
    tile images from lpc Atlas - openGameArt
    http://opengameart.org/content/lpc-tile-atlas
    """
    
class Tile(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("grass.png"),
            pygame.image.load("dirt.png"),
            pygame.image.load("water.png")]
        
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
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Click on a tile to edit")
        self.tileset = []
        
        self.ROWS = 15
        self.COLS = 20
        
        self.loadMap()
        
        self.sprites = [self.tileset]
        
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
            #newTile.setPosition((xPos, yPos))
            newTile.x = xPos
            newTile.y = yPos
            self.tileset[row].append(newTile)
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()