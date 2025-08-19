import simpleGE, pygame, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.ball = Ball(self)
        self.paddle = Paddle(self)
        self.setCaption("Press R to reset ball")
        
        self.sprites = [self.ball, self.paddle]
        
    def process(self):
        maxDY = 5
        if self.ball.collidesWith(self.paddle):
            #just bounce back in X
            self.ball.dx *= -1  
            
            #get the difference between ball and paddle's center
            relY = self.ball.y - self.paddle.y
            print(f"Difference of ys: {relY}")
            
            #divide that by paddle height to normalize (-.5 to .5)
            relY /= self.paddle.rect.height
            print(f"Normalized -.5 to .5: {relY}")
            
            #multiply by two to get (-1 to 1)
            relY *= 2
            print (f"normalized to -1 to 1: {relY}")
            
            #multiply by maxDY to get (-maxDY to maxDY)
            relY *= maxDY
            print (f"Normalized to -maxDY to maxDY: {relY}")
            print()
            self.ball.dy = relY
            
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.ball.position = (600, 240)
                self.ball.dx = -5
                self.ball.dy = 0
                
class Ball(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("lightblue", (10, 10))
        self.boundAction = self.BOUNCE
        
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)

        self.dx = 5

class Paddle(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.colorRect("green", (10, 50))
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()