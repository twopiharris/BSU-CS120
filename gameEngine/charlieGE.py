""" charlieGE.py """
import pygame, simpleGE

scene = simpleGE.Scene()
scene.background = pygame.image.load("campus.jpg")
scene.background = pygame.transform.scale(scene.background, (640, 480))

charlie = simpleGE.BasicSprite(scene)
charlie.setImage("Charlie.gif")
charlie.setSize(50, 50)
charlie.dx = 5
charlie.dy = 5

scene.sprites = [charlie]
scene.start()
