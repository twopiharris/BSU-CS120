import pygame, simpleGE

scene = simpleGE.Scene()
scene.background = pygame.image.load("campusResized.jpg")

charlie = simpleGE.BasicSprite(scene)
charlie.setImage("Charlie.gif")
charlie.setSize(50, 50)
charlie.dx = 5
charlie.dy = 5
#charlie.setBoundAction(charlie.BOUNCE)

scene.sprites = (charlie)
scene.start()
