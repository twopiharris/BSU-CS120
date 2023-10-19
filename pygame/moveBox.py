""" moveBox.py
    illustrates basic motion
    in the IDEA/ALTER framework
    moves a rect across the screen """



#Initialize
import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("move a box")
    
    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    
    #make a red 25 x 25 box
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((255, 0, 0))
    
    # set up some box variables
    box_x = 0
    box_y = 200
    
    #ACTION
    
        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        #Loop
    while keepGoing:
    
        #Time
        clock.tick(30)
    
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        #modify box value
        box_x += 5
        #check boundaries
        if box_x > screen.get_width():
            box_x = 0
    
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()