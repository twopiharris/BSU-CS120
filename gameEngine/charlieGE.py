import pygame, gameEngine

scene = gameEngine.Scene()
scene.background = pygame.image.load("campusResized.jpg")

charlie = gameEngine.SuperSprite(scene)
charlie.setImage("Charlie.gif")
charlie.setSize(50, 50)
charlie.setDX(5)
charlie.setDY(5)
charlie.setBoundAction(charlie.BOUNCE)

scene.sprites = (charlie)
scene.start()

