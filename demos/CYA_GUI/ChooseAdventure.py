import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.nodes = {}

        self.getDefaultGame()
        
        self.background.fill("lightBlue")
        
        self.lblDescription = simpleGE.MultiLabel()
        self.lblDescription.textLines = [
            "Description",
            "will go",
            "here"]        
        self.lblDescription.center = (320, 150)
        self.lblDescription.size = (300, 250)
        
        self.btnA = simpleGE.Button()
        self.btnA.text = "choice a"
        self.btnA.center = (150, 350)
        self.btnA.size = (200, 40)
        
        self.btnB = simpleGE.Button()
        self.btnB.text = "choice b"
        self.btnB.center = (500, 350)
        self.btnB.size = (200, 40)
        
        self.sprites = [self.lblDescription,
                        self.btnA,
                        self.btnB]

        self.currentKey = "start"
        self.displayNode(self.currentKey)


    def getDefaultGame(self):
        self.nodes = {
            "start": [["Do you want to win or lose?", "this can be ", "multiple lines"], "I want to win", "win", "I deserve to lose", "lose"],
            "win":   [["YOU WIN!!!"], "start over", "start", "quit", "quit"],
            "lose":  [["Sorry. You lost."], "start over", "start", "quit", "quit"]
        }
    
    def displayNode(self, nodeKey):
        currentNode = self.nodes[nodeKey]
        (description, menuA, nodeA, menuB, nodeB) = currentNode
        self.lblDescription.textLines = description
        self.btnA.text = menuA
        self.nodeA = nodeA
        self.btnB.text = menuB
        self.nodeB = nodeB
    
    def process(self):
        if self.btnA.clicked:
            if self.nodeA == "quit":
                self.stop()
            else:
                self.displayNode(self.nodeA)
        
        if self.btnB.clicked:
            if self.nodeB == "quit":
                self.stop()
            else:
                self.displayNode(self.nodeB)
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    