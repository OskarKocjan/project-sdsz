import pygame
import json
from Point import Point
from fetchPointsFromFile import ChangePointsFromFloatToInt

def runningBlue(i):
    pygame.draw.circle(screen, white, (x[i - 1], y[i - 1]), 1)
    pygame.draw.circle(screen, red, (x[i], y[i]), 1)
    i += 1








x = []
y = []



resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


y, x = ChangePointsFromFloatToInt("roads.json")

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode(resolution)

running = True
pygame.display.set_caption("Cracow Road Simulation")


clockobject = pygame.time.Clock()

screen.fill(black)
for i in range(len(x)):
    pygame.draw.circle(screen,white,(x[i],y[i]),1)

i = 1 

# Game Loop
while running:

    clockobject.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((255,225,255))
    
   
    runningBlue(i)
    i += 1
    if(i == len(x)):
        i = 1


    pygame.display.update()

    pass


