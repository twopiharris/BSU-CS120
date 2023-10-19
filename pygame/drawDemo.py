""" drawDemo.py
    demonstrate using the drawing
    features in pygame"""

import pygame, math

def drawStuff(background):
    """ given a surface, draws a bunch of things on it """

    #draw a line from (5, 100) to (100, 100)
    pygame.draw.line(background, (255, 0, 0), (5, 100), (100, 100))

    #draw an unfilled square
    pygame.draw.rect(background, (0, 255, 0), ((200, 5), (100, 100)), 3)

    #draw a filled circle
    pygame.draw.circle(background, (0, 0, 255), (400, 50), 45)

    #draw an arc
    pygame.draw.arc(background, (0, 0, 0), ((5, 150), (100, 100)), 0, math.pi/2, 5)

    #draw an ellipse
    pygame.draw.ellipse(background, (0xCC, 0xCC, 0x00), ((150, 150), (150, 100)), 0)

    #draw lines,
    points = (
      (370, 160),
      (370, 237),
      (372, 193),
      (411, 194),
      (412, 237),
      (412, 160),
      (412, 237),
      (432, 227),
      (436, 196),
      (433, 230)
    )
    pygame.draw.lines(background, (0xFF, 0x00, 0x00), False, points, 3)

    #draw polygon
    points = (
      (137, 372),
      (232, 319),
      (383, 335),
      (442, 389),
      (347, 432),
      (259, 379),
      (220, 439),
      (132, 392)
    )
    pygame.draw.polygon(background, (0x33, 0xFF, 0x33), points)

    #compare normal and anti-aliased diagonal lines
    pygame.draw.line(background, (0, 0, 0), (480, 425), (550, 325), 1)
    pygame.draw.aaline(background, (0, 0, 0), (500, 425), (570, 325), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing commands")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    drawStuff(background)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
        screen.blit(background, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()