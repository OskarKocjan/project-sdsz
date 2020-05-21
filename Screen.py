import pygame
from Point import Point
from fetchPointsFromFile import ChangePointsFromFloatToInt,convertGeoJsonToJson
from Car import Car


def initializePoints(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].getCords(), 2)


resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#convert from GeoJson
#convertGeoJsonToJson("../coords/intersections/kleparz.json")


# fetching coords from json
# data, points = ChangePointsFromFloatToInt("./intersections/kleparz.json")
data, points = ChangePointsFromFloatToInt("roads.json")
car = Car.fromPoint(points[1],points[0], points[2])


# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode(resolution)

running = True
pygame.display.set_caption("Cracow Road Simulation")

# time delay
clockobject = pygame.time.Clock()

# background color
screen.fill(black)

# draw road
initializePoints(points)

i = 1 

# Main Loop
while running:

    clockobject.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    car.move(screen)
    car.setCords(points[i].getX(),points[i].getY())
    car.setNeigh(points[i+1],points[i-1])

    i += 1
    if(i == len(points)-1):
        i = 1

    pygame.display.update()

    pass


