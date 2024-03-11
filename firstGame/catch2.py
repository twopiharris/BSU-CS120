import pygame, simpleGE

""" catch the Cash 2
    Add Charlie
"""

class Charlie(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Charlie.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Campus.jpg")
        self.charlie = Charlie(self)
        self.sprites = [self.charlie]
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()

