import pygame
import json
from Point import Point
from fetchPointsFromFile import ChangePointsFromFloatToInt
from numpy import subtract
from Car import Car

def runningRed(i):
    pygame.draw.circle(screen, white,points[i - 1].getCords(), 3)
    pygame.draw.circle(screen, red, points[i].getCords(), 3)

def initializeCars(points):

    cars = []

    for i in range(len(points)):
        cars.append(Car.fromPoint(points[i]))

    return cars

def initializePoints(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].getCords(), 5)




resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


data, points = ChangePointsFromFloatToInt("roads.json")

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode(resolution)

running = True
pygame.display.set_caption("Cracow Road Simulation")


clockobject = pygame.time.Clock()

screen.fill(black)

initializePoints(points)
cars = initializeCars(points)

i = 1 



# Game Loop
while running:

    clockobject.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
   
    runningRed(i)
    i += 1
    if(i == len(points)):
        i = 1


    pygame.display.update()

    pass


