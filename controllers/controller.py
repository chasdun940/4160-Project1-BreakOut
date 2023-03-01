#IMPORTS
import pygame, sys, time
import views.view as v
import models.paddle as p
import models.walls as w
import models.ball as b
import models.bricks as br

sleepNum = 0.005

#Function for moving the paddle collison with walls is done here as well
def move_rect(gameRect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not p.paddle.colliderect(w.wallOne):
        p.paddle.move_ip(-p.paddleSpd,0)
    elif keys[pygame.K_d] and not p.paddle.colliderect(w.wallThree):
        p.paddle.move_ip(p.paddleSpd,0)

#Function for calculating the balls movement
def move_circle(gameRect):
    b.ballCol.move_ip(b.ballSpdX, b.ballSpdY)
    ball_collide(p.paddle)
    ball_collide(w.wallOne)
    ball_collide(w.wallTwo)
    ball_collide(w.wallThree)
    for x in br.brickList:
        if (ball_collide(x.brick)):
            br.brickList.remove(x)
    game_over()


#A function that handles ball collison with the called obj
def ball_collide(obj):
    if (b.ballCol.bottom >= obj.top and b.ballCol.bottom <= obj.top
        and b.ballCol.right >= obj.left and b.ballCol.left <= obj.right):
        b.ballSpdY *= -1
        return True
    elif (b.ballCol.top <= obj.bottom and b.ballCol.top >= obj.bottom
        and b.ballCol.right >= obj.left and b.ballCol.left <= obj.right):
        b.ballSpdY *= -1
        return True
    elif (b.ballCol.right >= obj.left and b.ballCol.right <= obj.left
        and b.ballCol.top <= obj.bottom and b.ballCol.bottom >= obj.top):
        b.ballSpdX *= -1
        return True
    elif (b.ballCol.left <= obj.right and b.ballCol.left >= obj.right
        and b.ballCol.top <= obj.bottom and b.ballCol.bottom >= obj.top):
        b.ballSpdX *= -1
        return True

#A function that speeds up the game
def spdUp():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        return 0.0
    return 0.006


#A function that detects if the ball went past the paddle
#Or if all the blocks are destroyed
def game_over():
    if(b.ballCol.top >= 650) or len(br.brickList) == 0:
        pygame.quit()
        sys.exit()

    


#Function for exiting the game
def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    exit()    
    move_rect(p.paddle)
    move_circle(b.ballCol)
    v.draw()
    sleepNum = spdUp()
    time.sleep(sleepNum)