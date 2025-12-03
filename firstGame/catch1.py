import pygame, simpleGE

""" catch the Cash 1
    Just get the background up and running
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Campus.jpg")
        self.sprites = []
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
