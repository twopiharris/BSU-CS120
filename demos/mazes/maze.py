# maze tester
# works with ANY maze image as long as it has solid black walls.
# sample mazes generated as svg files from https://mazesforfun.com/maze-generator
# You might need to resize and add a white background in a tool like gimp.
# note if you make player faster, it may skip some walls. You can make walls
# thicker to prevent this

import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("maze_hex.png")
        #self.setImage("maze_rect.png")
        self.setCaption("R for rect, F for funky, T for triangle maze")
        self.player = Player(self)
        
        self.sprites = [self.player]

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.setImage("maze_rect.png")
                self.screen.blit(self.background, (0, 0))
            if event.key == pygame.K_f:
                self.setImage("maze_funky.png")
                self.screen.blit(self.background, (0, 0))
            if event.key == pygame.K_t:
                self.setImage("maze_triangle.png")
                self.screen.blit(self.background, (0, 0))

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (20, 20))
        self.moveSpeed = 2
        self.position = (10, 10)

    def getColorAt(self, x, y):
        colorUnder = self.scene.background.get_at((int(x), int(y)))
        return colorUnder
        
    def canMove(self, direction):
        canMove = True
        
        if direction == "LEFT":
            if self.getColorAt(self.x - self.moveSpeed, self.y) == (0, 0, 0):
                canMove = False
        if direction == "RIGHT":
            if self.getColorAt(self.x + self.moveSpeed, self.y) == (0, 0, 0):
                canMove = False
        if direction == "UP":
            if self.getColorAt(self.x, self.y - self.moveSpeed) == (0, 0, 0):
                canMove = False
        if direction == "DOWN":
            if self.getColorAt(self.x, self.y + self.moveSpeed) == (0, 0, 0):
                canMove = False
                
        return canMove

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            if self.canMove("LEFT"):
                self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.canMove("RIGHT"):
                self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            if self.canMove("UP"):
                self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            if self.canMove("DOWN"):
                self.y += self.moveSpeed

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    