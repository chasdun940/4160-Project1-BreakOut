#IMPORTS
import pygame
import models.paddle as p
import models.walls as w
import models.ball as b
import models.bricks as br

# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Initialize game
pygame.init()
pygame.display.set_caption("BREAKOUT")
surface = pygame.display.set_mode(SCREEN_SIZE)

# Color of my window
screenColor = (0, 0, 0)

def draw():
    surface.fill(screenColor)
    pygame.draw.rect(surface, p.paddleColor, p.paddle)
    pygame.draw.rect(surface, w.WallColor, w.wallOne)
    pygame.draw.rect(surface, w.WallColor, w.wallTwo)
    pygame.draw.rect(surface, w.WallColor, w.wallThree)
    pygame.draw.rect(surface, b.ballColor, b.ballCol)
    for x in br.brickList:
        pygame.draw.rect(surface, x.brickColor, x.brick)
    pygame.display.update()