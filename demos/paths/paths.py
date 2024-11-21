import pygame, simpleGE

""" path.py

    a tool for managing paths
"""
class Path(object):
    def __init__(self, sprite, pointList, speed = 5):
        super().__init__()
        self.sprite = sprite
        self.pointList = pointList
        self.counter = 0
        self.speed = speed
        self.currentPoint = self.pointList[self.counter]
        self.nextPoint = self.pointList[self.counter + 1]
        self.sprite.speed = self.speed
        self.sprite.moveAngle = sprite.dirTo(self.nextPoint)
        
    def turnToNextPoint(self):
        self.sprite.speed = self.speed
        self.currentPoint = self.nextPoint
        self.counter += 1
        if self.counter >= len(self.pointList):
            self.counter = 0
        self.nextPoint = self.pointList[self.counter]
        self.sprite.moveAngle = self.sprite.dirTo(self.nextPoint)
        
    def setPoints(self, pointList):
        self.pointList = pointList
        
    def setSpeed(self, speed):
        self.speed = speed
    
    def process(self):
        #check for turns
        if self.sprite.distanceTo(self.nextPoint) < 15:
            self.turnToNextPoint()
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.player = simpleGE.Sprite(self)
        self.player.colorRect("green", (25, 25))
        self.player.position = (58, 32)
        pointList = (
            (58, 32),
            (514, 49),
            (521, 180),
            (63, 179),
            (65, 287),
            (562, 292),
            (564, 399),
            (38, 413)
        )
        self.path = Path(self.player, pointList, 7)
        
        self.sprites = [self.player]
        
    def process(self):
        self.path.process()
        self.player.drawTrace("white")

    def processEvent(self, event):
        """ print out mouse clicks
            to use for creating a path """
        
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()