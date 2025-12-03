import pygame, simpleGE

""" Text input demo """

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.lblOut = simpleGE.Label()
        self.lblOut.center = (320, 100)
        self.lblOut.size = (300, 30)
        self.lblOut.text = "Please enter your name"
        
        self.txtName = simpleGE.TxtInput()
        self.txtName.center = (320, 200)
        self.txtName.text = ""
        
        self.btnClickMe = simpleGE.Button()
        self.btnClickMe.center = (320, 300)
        self.btnClickMe.text = "Click me"
        
        self.sprites = [self.lblOut,
                        self.txtName,
                        self.btnClickMe]
        
    def processEvent(self, event):
        self.txtName.readKeys(event)
        
    def process(self):
        if self.btnClickMe.clicked:
            name = self.txtName.text
            self.lblOut.text = f"Hi there, {name}!"
            
def main():
    game = Game()
    game.start()
    
if __name__ =="__main__":
    main()