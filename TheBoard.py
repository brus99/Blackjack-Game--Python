###########Learning to create a board game from scratch using Pygames Public Documentation#########################

import pygame
color = (255,255,255)                           #white canvas
blacksquare = (0,0,0)                              #my checkerboard square colors
brownsquare = (165,42,42)
screenwidth = 640
screenheight= 640


screen = pygame.display.set_mode((screenwidth,screenheight))             
pygame.display.set_caption('Checkers')                                #creating surface object/gametitle

##############creating my checker board###########################################################################


screen.fill(color)                                      #fill method to color my surface object that I will draw on

def makethecolumn(x,y):                                    #creates one row of the game board
    num = 0
    for i in range(1,9):
        if num%2==0:
            square = (x,y,80,80)
            pygame.draw.rect(screen,brownsquare,square)             #pygame builtin draw.(shape) to create a square
            y+=80                                                   
        else:
            square = (x,y,80,80)
            pygame.draw.rect(screen,blacksquare,square)
            y+=80
        num+=1
def alternate(x,y):                                     #creates alternate row 
    num = 0
    for i in range(1,9):
        if num%2==0:
            square = (x,y,80,80)
            pygame.draw.rect(screen,blacksquare,square)
            y+=80
        else:
            square = (x,y,80,80)
            pygame.draw.rect(screen,brownsquare,square)
            y+=80
        num+=1
def finishtheboard(x):                             #calls alternate and makethecolumn functions. Runs 8 times to generate the board 
    for i in range (1,9):                          
        if i%2==0:
            makethecolumn(x,0)
            x+=80
        else:
            alternate(x,0)
            x+=80
finishtheboard(0)                 
################################Run The Application##############################################

while True:                                                                              
    for event in pygame.event.get() :                  #infinte loop that breaks when quit is executed
        if event.type == pygame.QUIT:           
            quit()
        pygame.display.update()


