import pygame, simpleGE

""" testJoystick 
    simple utility to check joystick
    values.  Current values of all
    buttons and axes will appear in console
    Nothing is intended to appear on screne
    but simpleGE scene is still used for convenience
"""


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("Joystick test: Check console for joystick values")
        pygame.joystick.init()
        self.joy = pygame.joystick.Joystick(0)

        self.txtAxes = simpleGE.MultiLabel()
        self.txtAxes.size = (300, 480)
        self.txtAxes.center = (100, 240)
        self.txtAxes.textLines = ["Axes"]
        
        self.txtButtons = simpleGE.MultiLabel()
        self.txtButtons.size = (300, 480)
        self.txtButtons.center = (500, 240)
        self.txtButtons.textLines = ["Buttons"]
        
        
        self.sprites = [self.txtAxes,
                        self.txtButtons]

    def process(self):
        outList = []
        axes = self.joy.get_numaxes()
        for i in range(axes):
            axis = self.joy.get_axis(i)
            outList.append(f"Axis {i}: {axis:.3f}")
        self.txtAxes.textLines = outList
            
        outList = []
        numButtons = self.joy.get_numbuttons()
        for i in range(numButtons):
            button = self.joy.get_button(i)
            outList.append(f"Button {i}: {button}")
            
        self.txtButtons.textLines = outList
        
def main():
    game = Game()
    game.start()
        
    
if __name__ == "__main__":
    main()
    