""" lander.py 
    lunar lander program using simpleGE
"""

import pygame, simpleGE, random

class Lander(simpleGE.SuperSprite):
    def __init__(self, scene):
        simpleGE.SuperSprite.__init__(self, scene)
        self.thrust = .1
        self.sideThrust = .05
        self.setImage("lander.gif")
        self.setAngle(90)
        self.inFlight = True

    def checkEvents(self):
        self.checkKeys()
        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.dy -= self.thrust
            self.inFlight = True
            
        if keys[pygame.K_LEFT]:
            self.dx += self.sideThrust
            self.inFlight = True
            
        if keys[pygame.K_RIGHT]:
            self.dx -= self.sideThrust
            self.inFlight = True
        
        self.updateVector()
        
class Platform(simpleGE.SuperSprite):
    def __init__(self, scene):
        simpleGE.SuperSprite.__init__(self, scene)
        self.setImage("platform.gif")
        self.reset()
        
    def reset(self):
        #pick random position on screen
        self.x = random.randint(0, self.screen.get_width())
        
        #make sure it's in bottom half of screen
        screenHeight = self.screen.get_height()
        self.y = random.randint(screenHeight/2, screenHeight)

class Game(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.setCaption("Lunar Lander - arrow key to begin")
        self.lander = Lander(self)
        
        self.platform = Platform(self)
        
        self.lblInfo = simpleGE.Label()
        self.lblInfo.center = (320, 20)
        self.lblInfo.size = (300, 30)

        self.sprites = [self.lander, self.platform, self.lblInfo]
        self.gravity = .02
    
    def update(self):
        #add force of gravity
        if self.lander.inFlight == True:
            self.lander.addDY(self.gravity)
        self.checkLanding()
        
        self.updateInfo()
        
    def checkLanding(self):
        #check collisions
        if self.lander.collidesWith(self.platform):
            #check for good landing
            if self.lander.dx < .5:
                if self.lander.dx > -.5:
                    if self.lander.dy >= 0:
                        if self.lander.dy < 1:
                            print("nice landing")
                        else:
                            print("too much vertical velocity")
                    else:
                        badDY = self.lander.dy
                        print("must approach from top %.2f" % badDY)
                else:
                    print("going too fast to left")
            else:
                print ("going too fast to right")
            
            self.lander.dx = 0
            self.lander.dy = 0
            self.lander.updateVector()
            self.lander.inFlight = False

    def updateInfo(self):
        info = "dx: %.2f, dy: %.2f" % (self.lander.dx, self.lander.dy)
        self.lblInfo.text = info
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()