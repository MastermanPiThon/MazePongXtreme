import sys

name = raw_input ("What is your name? ")
if (name=="Colin" or name== "Riley"):
    print ("Welcome superior being!")
elif (name== "Andrew" or "Clara"):
    print ("Welcome, thou saucy, raw-boned, clotpole. You human trash! Who the hooey fooey said you could be here?! See ya!")
    sys.exit()

else:
    print ("Welcome insignificant human.")

answer = raw_input ("Do you want to play Maze Pong Xtreme? ")
if (answer=="Yes" or answer=="yes"):
    print("Awesome!")
elif (answer=="No" or answer=="no"):
    print("Too bad. You're playing anyway.")
else:
    print("I didn't understand that, but I'll asume you do.")
    print("Everybody likes Maze Pong Xtreme because I'm awesome.")

import pygame
from pygame.locals import*
import math
import random

pygame.init()
width, height = 1000, 500
screen= pygame.display.set_mode((width, height))

x = 500
y = 250
moveX = 3
moveY = 3
keys = [False, False, False, False, False, False, False, False, False, False, False, False]
counter = 0
paddleY = 20
paddle1Y= 20
paddleX = 10
paddle1X= 950

# Loading images
RPaddle = pygame.image.load("LeftPaddle.png")
LPaddle = pygame.image.load("RightPaddle.png")
Ball= pygame.image.load("Shamichael.png")
RPaddle = pygame.transform.scale(RPaddle, (40, 150))
LPaddle = pygame.transform.scale(LPaddle, (40, 150))
Ball = pygame.transform.scale(Ball, (50, 40))

running = 1
exitcode = 0
while running:
    screen.fill(0x8F5498)
    screen.blit(Ball, (x,y))
    screen.blit(RPaddle, (paddle1X,paddleY))
    screen.blit(LPaddle, (paddleX,paddle1Y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_UP:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
            elif event.key==K_LEFT:
                keys[4]=True
            elif event.key==K_a:
                keys[5]=True
            elif event.key==K_RIGHT:
                keys[6]=True
            elif event.key==K_d:
                keys[7]=True
            elif event.key==K_h:
                keys[8]=True
            elif event.key==K_o:
                keys[9]=True
            elif event.key==K_e:
                keys[10]=True
            elif event.key==K_y:
                keys[11]=True
            
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_UP:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_DOWN:
                keys[3]=False
            elif event.key==K_LEFT:
                keys[4]=False
            elif event.key==K_a:
                keys[5]=False
            elif event.key==K_RIGHT:
                keys[6]=False
            elif event.key==K_d:
                keys[7]=False
            elif event.key==K_h:
                keys[8]=False
            elif event.key==K_o:
                keys[9]=False
            elif event.key==K_e:
                keys[10]=False
            elif event.key==K_y:
                keys[11]=False

    if keys[8] and counter == 0:
        counter = 1
    if keys[9] and counter == 1:
        counter = 2
    if keys[9] and counter == 2:
        counter = 3
    if keys[10] and counter == 3:
        counter = 4
    if keys[11] and counter == 4:
        counter = 5
    if keys[0:6] and counter < 5:
        counter = 0

    if (paddleY >= 0 and paddleY <= 350):
        if keys[0]:
            paddleY-= 4
        elif keys[2]:
            paddleY+= 4
    else:
        if paddleY < 0:
            paddleY = 0
        else:
            paddleY = 350
    if (paddle1Y >= 0 and paddle1Y <= 350):
        if keys[1]:
            paddle1Y-= 4
        elif keys[3]:
            paddle1Y+= 4
    else:
        if paddle1Y < 0:
            paddle1Y = 0
        else:
            paddle1Y = 350
    if (paddleX >= 0 and paddleX <= 960):
        if keys[4] and counter == 5:
            paddleX-= 4
        elif keys[6] and counter == 5:
            paddleX+= 4
    else:
        if paddleX < 0:
            paddleX = 0
        else:
            paddleX = 960
    if (paddle1X >= 0 and paddle1X <= 960):
        if keys[5] and counter == 5:
            paddle1X-= 4
        elif keys[7] and counter == 5:
            paddle1X+= 4
    else:
        if paddle1X < 0:
            paddle1X = 0
        else:
            paddle1X = 960

    x += moveX
    y += moveY

    if x < 0 or x > 950:
        moveX = -moveX
    if y > 460 or y < 0:
        moveY = -moveY

    if x < 50 or x > 900:
        if paddleY < y and (paddleY + 149) > y:
            moveX = -moveX

        elif paddle1Y < y and (paddle1Y + 149) > y:
            moveX = -moveX

        elif paddleY < (y + 39) and (paddleY + 149) > (y + 39):
            moveX = -moveX

        elif paddle1Y < (y + 39) and (paddle1Y + 149) > (y + 39):
            moveX = -moveX






    
