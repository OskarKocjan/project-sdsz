import pygame
import json
from Point import Point
from fetchPointsFromFile import ChangePointsFromFloatToInt

x = []
y = []




red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


y, x = ChangePointsFromFloatToInt("roads.json")

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((1629, 812))

running = True
pygame.display.set_caption("Cracow Road Simulation")

screen.fill(black)
for i in range(len(x)):
    pygame.draw.circle(screen,white,(x[i],y[i]),1)



# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((255,225,255))

    pygame.display.update()

    pass
