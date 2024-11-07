""" charlieGE.py """
import pygame, simpleGE

scene = simpleGE.Scene()
scene.setImage("campus.jpg")

charlie = simpleGE.Sprite(scene)
charlie.setImage("Charlie.gif")
charlie.setSize(50, 50)
# charlie.dx = 5
# charlie.dy = 5

charlie.speed = 5
charlie.moveAngle = 45

scene.sprites = [charlie]
scene.start()
