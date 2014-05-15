import sys

name = raw_input ("What is your name? ")
if (name=="Andrew" or name=="Clara" or name=="andrew" or name=="clara"):
    print ("Welcome superior being!")
elif (name== "Colin" or name=="Riley" or name=="riley" or name=="colin"):
    print ("Sorry... access denied. IQ level is insufficient")
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


#Initiate PyGame
pygame.init()
width, height = 1000, 500
screen= pygame.display.set_mode((width, height))

#Declare Variables
x = 500
y = 250
speed = 2.5
moveX = 3
moveY = 3
keys = [False, False, False, False, False, False, False, False, False, False, False, False, False]
counter = 0
paddleY = 20
paddle1Y= 20
paddleX = 10
paddle1X= 950
paddle_width = 30
paddle_height = 112
ball_width = 38
ball_height = 30
lscore = 0
rscore = 0

# Loading images
RPaddle = pygame.image.load("LeftPaddle.png")
LPaddle = pygame.image.load("RightPaddle.png")
Ball= pygame.image.load("Shamichael.png")
RPaddle = pygame.transform.scale(RPaddle, (paddle_width, paddle_height))
LPaddle = pygame.transform.scale(LPaddle, (paddle_width, paddle_height))
Ball = pygame.transform.scale(Ball, (ball_width, ball_height))

#Start game
running = 1
exitcode = 0
while running:
    screen.fill(0x8F5498)
    screen.blit(Ball, (x,y))
    screen.blit(RPaddle, (paddle1X,paddle1Y))
    screen.blit(LPaddle, (paddleX,paddleY))
    pygame.display.flip()

    #Closability
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        #Keys
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

    LPaddlerect=pygame.Rect(paddleX, paddleY, paddle_width, paddle_height)
    RPaddlerect=pygame.Rect(paddle1X, paddle1Y, paddle_width, paddle_height)
    Ballrect=pygame.Rect(x, y, ball_width, ball_height)

    if Ballrect.colliderect(RPaddlerect):
        moveX = -moveX
    if Ballrect.colliderect(LPaddlerect):
        moveX = -moveX

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

    #Creating boundaries
    if (paddleY >= 0 and paddleY <= 388):
        if keys[0]:
            paddleY-= 4*speed
        elif keys[2]:
            paddleY+= 4*speed
    else:
        if paddleY < 0:
            paddleY = 0
        else:
            paddleY = 350
    if (paddle1Y >= 0 and paddle1Y <= 388):
        if keys[1]:
            paddle1Y-= 4*speed
        elif keys[3]:
            paddle1Y+= 4*speed
    else:
        if paddle1Y < 0:
            paddle1Y = 0
        else:
            paddle1Y = 350

    




            
    """if (paddleX >= 0 and paddleX <= 960):
        if keys[4] and counter == 5:
            paddleX-= 4
        elif keys[6] and counter == 5:
            paddleX+= 4
    else:
        if paddleX < 0:
            print("left player lost")
            sys.exit()
        else:
            print("right player lost")
            sys.exit()

    if(paddle1X >= 0 and paddle1X <= 960):
        if keys[5] and counter == 5:
            paddle1X-= 4
        elif keys[7] and counter == 5:
            paddle1X+= 4
    else:


        if paddle1X < 0:
            paddle1X = 0
        else:
            paddle1X = 960"""

    x += moveX*speed
    y += moveY*speed

    if x < 0:
        lscore = lscore + 1
        speed += 0.1
        
        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Score: "+str(lscore)+" | "+str(rscore), True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+48
        screen.blit(text, textRect)

        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Left player lost.", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(text, textRect)
        pygame.display.flip()
        x = 500
        y = 250

        while keys[12]== False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        keys[12]=True 


        keys[12]= False
        paddleY = 20
        
    if x > 950:
        rscore = rscore + 1
        speed += 0.1

        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Score: "+str(lscore)+" | "+str(rscore), True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+48
        screen.blit(text, textRect)

        pygame.font.init()
        font = pygame.font.Font(None, 24)
        text = font.render("Right player lost.", True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24
        screen.blit(text, textRect)
        pygame.display.flip()
        x = 500
        y = 250

        while keys[12]== False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key==K_SPACE:
                        keys[12]=True 



        keys[12]= False
        paddle1Y = 30
                
    if y > 460 or y < 0:
        moveY = -moveY



    






    
