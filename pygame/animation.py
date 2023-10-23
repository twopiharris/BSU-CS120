#animation.py
import pygame, random


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("He flies!!!   press <space> for a new direction, <m> to change bound mode")
        
    background = pygame.image.load("campus.jpg")
    background.convert()
    background = pygame.transform.scale(background, (640, 480))
    
    charlie = pygame.image.load("charlie.png")
    charlie.convert_alpha()
    charlie = pygame.transform.scale(charlie, (100, 100))
    charlie_x = 320
    charlie_y = 240
    
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    
    clock = pygame.time.Clock()
    keepGoing = True
    mode = "bounce"
    
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dx = random.randint(-10, 10)
                    dy = random.randint(-10, 10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    if mode == "bounce":
                        mode = "wrap"
                    else:
                        mode= "bounce"

        charlie_x += dx
        charlie_y += dy
            
        if mode == "bounce":
            # bounce - using rect         
    
            c_rect = charlie.get_rect()
            c_rect.left = charlie_x
            c_rect.top = charlie_y
            
            if c_rect.right > screen.get_width():
                dx *= -1
            if c_rect.left < 0:
                dx *= -1
            if c_rect.top < 0:
                dy *= -1
            if c_rect.bottom > screen.get_height():
                dy *= -1
    
        else:
            # wrap        
            if charlie_x > screen.get_width():
                charlie_x = 0
            if charlie_x < 0:
                charlie_x = screen.get_width()
                
            if charlie_y > screen.get_height():
                charlie_y = 0
            if charlie_y < 0:
                charlie_y = screen.get_height()
            
        
        
        screen.blit(background, (0,0))
        screen.blit(charlie, (charlie_x, charlie_y))
        
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
    
