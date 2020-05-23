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

#convert from GeoJson
# convertGeoJsonToJson("../coords/intersections/kleparz.json")



# fetching coords from json
data, points = ChangePointsFromFloatToInt("roads.json")
print(data[0]['coordinates'][0].getCords())
# set track to car
streets = ["basztowa-ccw","basztowa-dunaj-ccw"]
pkts = getFirstThreeAndLast(data, "basztowa-ccw")



#car = Car.fromPoint(pkts[1], pkts[0], pkts[2])

#car.setTrack(streets, data)



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

    clockobject.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #car.move(screen)
    # car.setCords(points[i].getX(), points[i].getY())
    # car.setNeigh(points[i+1], points[i-1])

    i += 1
    if(i == len(points)-1):
        i = 1

    pygame.display.update()

    pass


