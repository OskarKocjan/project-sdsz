import pygame
from Point import Point
from fetchPointsFromFile import *
from Car import Car


def initializePoints(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].getCords(), 2)


resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


# fetching data from json
data, points = ChangePointsFromFloatToInt("roads.json")

# set track to car
streets = ["bagatela-filharmonia-ccw","filharmonia-gertrudy-ccw", "gertrudy-poczta-ccw", "westerplatte-right-ccw", "basztowa-ccw", "basztowa-dunaj-ccw" ]
car = Car(streets, data, (255, 0, 0), 1,)
#car2 = Car(streets, data, (0, 255, 0), 40)


# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode(resolution)

#running condition and title
running = True
pygame.display.set_caption("Cracow Road Simulation")

# time delay
clockobject = pygame.time.Clock()

# background color
screen.fill(black)

# draw road
initializePoints(points)


#Main Loop
while running:


    clockobject.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    car.move(screen)
    #car2.move(screen)


    pygame.display.update()

    pass


