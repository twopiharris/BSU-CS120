""" Charlie.py
    illustrates basic motion
    image loading
    move Charlie the Cardinal
"""


#Initialize
import pygame

def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Charlie!")

    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("papayawhip")

    #load an image
    cardinal = pygame.image.load("Charlie.png")
    cardinal = cardinal.convert_alpha()
    cardinal = pygame.transform.scale(cardinal, (100, 50))

    # set up some cardinal variables
    cardinal_x = 0
    cardinal_y = 200

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

        #modify cardinal value
        cardinal_x += 5
        #check boundaries
        if cardinal_x > screen.get_width():
            cardinal_x = 0

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(cardinal, (cardinal_x, cardinal_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()