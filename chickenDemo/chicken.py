import simpleGE, pygame, random

"""
Asset Attributions:

chicken spritesheet - AntumDeluge: https://opengameart.org/content/lpc-chicken-rework  
egg image- GoopyBus: https://opengameart.org/content/egg-item-sprite
colored eggs - modified AJH in Gimp
grass - LuminousDragonGames: https://opengameart.org/content/blended-textures-of-dirt-and-grass
background music - congusbongus: https://opengameart.org/content/chicken-n-corn
sound effects
bock.wav - ImadeIt: https://opengameart.org/content/chicken-sound-effect (modified in audacity AJH)
powerUp.wav, hitHurt.wav - AJH in jsfxr: https://sfxr.me
"""

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.setImage("grass.png")
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        pygame.joystick.init()
        try:
            self.joy = pygame.joystick.Joystick(0)
        except:
            self.joy = None

        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        
        self.bock = simpleGE.Sound("Bock.wav")
        self.moreTime = simpleGE.Sound("powerUp.wav")
        self.loseEggs = simpleGE.Sound("hitHurt.wav")
        #background sound
        pygame.mixer.music.load("chicken_n_corn_loop.mp3")
        pygame.mixer.music.play(-1)
        
        self.chicken = Chicken(self)
        self.eggs = []
        for i in range(10):
            self.eggs.append(Egg(self))
            
        self.blueEgg = BlueEgg(self)
        
        self.redEggs = self.makeSpriteGroup(RedEgg(self))
        self.addGroup(self.redEggs)
        
        self.sprites = [self.chicken, self.eggs,
                        self.redEggs, self.blueEgg,
                        self.lblScore, self.lblTime]
        
    def process(self):
        for egg in self.eggs:
            if self.chicken.collidesWith(egg):
                self.bock.play()
                egg.reset()
                self.score += 1
                self.lblScore.text = f"Eggs: {self.score}"
        
        if self.chicken.collidesWith(self.blueEgg):
            self.moreTime.play()
            self.blueEgg.reset()
            self.timer.totalTime += 10
            self.redEggs.add(RedEgg(self))
            
        for redEgg in self.redEggs:    
            if self.chicken.collidesWith(redEgg):
                self.loseEggs.play()
                redEgg.reset()
                #self.score = 0
                self.score -= 5
                if self.score < 0:
                    self.score = 0
                self.lblScore.text = f"Eggs: {self.score}"
            
        self.lblTime.text = f"Time: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            self.stop()

class Chicken(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.position = (320, 240)
        self.anim = simpleGE.SpriteSheet("chicken.png", (32, 32), 4, 3)
        
    def process(self):
        row = 2

        if self.scene.joy:
            ax = self.scene.joy.get_axis(0)
            ay = self.scene.joy.get_axis(1)
            #print (f"{ax=}, {ay=}")
        
            if ax < -.2:
                row = 3
                self.x -= 5
            if ax > .2:
                row = 1
                self.x += 5
            if ay < -.2:
                row = 0
                self.y -= 5
            if  ay > .2:
                row = 2
                self.y += 5
        else: #no joystick, use keys
            
            if self.isKeyPressed(pygame.K_LEFT):
                row = 3
                self.x -= 5
            if self.isKeyPressed(pygame.K_RIGHT):
                row = 1
                self.x += 5
            if self.isKeyPressed(pygame.K_UP):
                row = 0
                self.y -= 5
            if self.isKeyPressed(pygame.K_DOWN):
                row = 2
                self.y += 5
        
        self.copyImage(self.anim.getNext(row)) 
            
class Egg(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("egg.png")
        self.setSize(15, 15)
        self.reset()
        
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)
        
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)
        
class RedEgg(Egg):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("eggRed.png")
        self.setSize(15, 15)
        
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = random.randint(0, self.screenHeight)
        
        # go a little slower than standard eggs
        self.dx = random.randint(-1, 1)
        self.dy = random.randint(-1, 1)        
        
class BlueEgg(Egg):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("eggBlue.png")
        self.setSize(15, 15)
 
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Eggs: 0"
        self.center = (100, 100)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.text = "Time: 10"
        self.center = (400, 100)

class Intro(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        
        self.status = "quit"
        self.score = score
        
        self.setImage("grass.png")
        
        pygame.mixer.music.load("chicken_n_corn_loop.mp3")
        pygame.mixer.music.play(-1)
        
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "You are a hen",
            "You've laid some eggs, but they are",
            "rolling all over the yard!",
            "catch as many as you can in 30 seconds.",
            "Some eggs are not like the others..."
            ]
        self.lblInstructions.center = (320, 240)
        self.lblInstructions.size = (440, 200)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (320, 100)
        self.lblScore.size = (400, 30)
        self.lblScore.text = f"Previous Score: {self.score}"

        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (150, 400)
        self.btnPlay.text = "(P)lay"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (500, 400)
        self.btnQuit.text = "(Q)uit"
        
        self.eggs = []
        for i in range(10):
            self.eggs.append(Egg(self))
        
        #try to initialize joystick
        pygame.joystick.init()
        try:
            self.joy = pygame.joystick.Joystick(0)
        except:
            self.joy = None

        
        self.sprites = [
            self.eggs,
            self.lblScore,
            self.lblInstructions,
            self.btnPlay,
            self.btnQuit
            ]

    def process(self):
        
        #play on play button, p key, or keypad button 0
        if self.btnPlay.clicked:
            self.status = "play"
            self.stop()
        if self.isKeyPressed(pygame.K_p):
            self.status = "play"
            self.stop()
        if self.joy:
            if self.joy.get_button(0):
                self.status = "play"
                self.stop()
        
        #quit on quit button, q key, or keypad button 1
        if self.btnQuit.clicked:
            self.status = "quit"
            self.stop()
        if self.isKeyPressed(pygame.K_q):
            self.status = "quit"
            self.stop()
        if self.joy:
            if self.joy.get_button(1):
                self.status = "quit"
                self.stop()          

def main():
    keepGoing = True
    score = 0
    
    while keepGoing:
        intro = Intro(score)
        intro.start()
        
        if intro.status == "quit":
            keepGoing = False
        else:
            game = Game()
            game.start()
            score = game.score
    
if __name__ == "__main__":
    main()
