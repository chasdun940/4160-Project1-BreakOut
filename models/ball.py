#IMPORTS
import pygame
import random

# Ball vars
ballColor = (255, 200, 200)
ballRadius = 5
ballColSize = ballWidth, ballHeight = 10, 10
ballPos = ballX, ballY = 400, 300
if(random.randint(0,1)):
    ballSpdX = 1
else:
    ballSpdX = -1
ballSpdY = 1
ballCol = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
