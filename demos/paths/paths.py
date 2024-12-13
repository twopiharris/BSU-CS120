import pygame, simpleGE

""" path.py

    a tool for managing paths
"""

class Path(object):
    """ A tool for adding a linear interpolation path
        to any sprite.
        
        required parameters:
        * sprite - the SimpleGE sprite you want to animate
        * pointList - a tuple of coordinate tuples
                      each is a point you want the sprite
                      to visit

        optional parameter:
        * speed - the speed at which you want the sprite to
                  move. Defaults at 7 ppf
                  
        properties you can change:
        * sprite - the sprite
        * pointList - the pointList. must have at least two points
        * counter - the index of the position you are LEAVING
        * currentPoint - the point you are LEAVING
        * nextPoint - the point you are HEADING towards
        * rotate - if True, turns the sprite towards the next point
        * threshold - distance from the point to count as a trigger
                      defaults to 15, should be roughly twice speed
                      or you might 'overshoot' the target.    
    """
    
    def __init__(self, sprite, pointList, speed = 7):
        super().__init__()
        #set initial attributes
        self.sprite = sprite
        self.pointList = pointList
        self.counter = -1
        self.speed = speed
        self.threshold = 15
        self.rotate = False
        
        #initialize the sprite at position zero
        self.currentPoint = self.pointList[0]
        self.nextPoint = self.pointList[1]
        self.sprite.position = self.currentPoint
        self.turnToNextPoint()
            
    def turnToNextPoint(self):
        self.sprite.speed = self.speed
        self.currentPoint = self.nextPoint
        self.counter += 1
        if self.counter >= len(self.pointList):
            self.counter = 0
        self.nextPoint = self.pointList[self.counter]
        self.sprite.moveAngle = self.sprite.dirTo(self.nextPoint)
        if self.rotate:
            self.sprite.imageAngle = self.sprite.moveAngle
        
    def setPoints(self, pointList):
        self.pointList = pointList
        
    def setSpeed(self, speed):
        self.speed = speed
    
    def process(self):
        #check for turns
        if self.sprite.distanceTo(self.nextPoint) < self.threshold:
            self.turnToNextPoint()
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.player = simpleGE.Sprite(self)
        self.player.colorRect("green", (50, 25))
            
        pointList = (
            (30, 31),
            (278, 163),
            (579, 34),
            (297, 191),
            (585, 403),
            (298, 226),
            (50, 423),
            (283, 218)
        )

        self.path = Path(self.player, pointList, 15)
        self.path.rotate = True
        self.path.threshold = 7
        
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