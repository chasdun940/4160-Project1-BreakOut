#IMPORTS
import pygame, random

# Brick vars
class Brick:
    def __init__(self, brickX, brickY, brickColor):
        self.brickX = brickX
        self.brickY = brickY
        self.brickColor = brickColor
        self.brickSize = brickWidth, brickHeight = 50, 10
        self.brick = pygame.Rect(brickX, brickY, brickWidth, brickHeight)

#Creating bricks
colorList = [(255,0,0), (0,255,0), (0,0,255), (0,255, 187), (187, 0, 255), (255, 187, 0)]
brickList = []
values = range(7)
valuesj = range(13)
for i in values:
    for j in valuesj:
        randomColor = random.randint(0,5)
        newBrick = Brick((j*50)+65+(j*2), (i*10)+150+(i*2), colorList[randomColor])

        brickList.append(newBrick)
