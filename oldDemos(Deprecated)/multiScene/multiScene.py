import pygame, simpleGE

""" multi - scene
    go from one scene to another """

    
class Scene1(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.next = ""
        self.lblOutput = simpleGE.Label()
        self.lblOutput.center = ((320, 240))
        self.lblOutput.size = ((300, 30))
        self.lblOutput.text = "Scene 1 can allow for choice"
        
        self.btn2 = simpleGE.Button()
        self.btn2.center = ((220, 340))
        self.btn2.text = "Go to scene 2"
        
        self.btn3 = simpleGE.Button()
        self.btn3.center = ((420, 340))
        self.btn3.text = "Go to scene 3"
        
        
        self.sprites = [self.lblOutput, self.btn2, self.btn3]
        
    def update(self):
        if self.btn2.clicked:
            self.next = "2"
            self.stop()
            
        if self.btn3.clicked:
            self.next = "3"
            self.stop()            
        
class Scene2(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.lblOutput = simpleGE.Label()
        
        self.lblOutput.bgColor = ((0, 0, 0))
        self.lblOutput.fgColor = ((255, 255, 255))
        
        self.lblOutput.center = ((320, 240))
        self.lblOutput.size = ((300, 30))
        self.lblOutput.text = "Scene 2 quits when done"
        self.lblOutput.transparentBackground = True
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = ((320, 340))
        self.btnQuit.text = "Quit"
        
        self.sprites = [self.lblOutput, self.btnQuit]
        
    def update(self):
        if self.btnQuit.clicked:
            self.stop()     

class Scene3(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.lblOutput = simpleGE.Label()
        self.lblOutput.center = ((320, 240))
        self.lblOutput.text = "Scene 3"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = ((320, 340))
        self.btnQuit.text = "Quit"
        
        self.sprites = [self.lblOutput, self.btnQuit]
        
    def update(self):
        if self.btnQuit.clicked:
            self.stop()     

def main():
    
    scene2 = Scene2()
    scene2.start()
    
    scene1 = Scene1()
    scene1.start()

    next = scene1.next
    
    if next == "2":
        scene2 = Scene2()
        scene2.start()
    if next == "3":
        scene3 = Scene3()
        scene3.start()
    
if __name__ == "__main__":
    main()
    