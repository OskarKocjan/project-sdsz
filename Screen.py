import pygame
from Point import Point
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import pause
import time


def initializePoints(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].getCords(), 5)


resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

# fetching essential data from json
data, points = ChangePointsFromFloatToInt("roads.json")


# trasy od lubicz wszsytkie
streets = [
    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-karmelicka-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-franc-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-stradom-prosto"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-staro-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-sienna-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-westerplatte-prosto", 'westerplatte-right-ccw', "westerplatte-lubicz-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-westerplatte-prosto", 'westerplatte-right-ccw', "westerplatte-pawia-prosto"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-westerplatte-prosto", 'westerplatte-left-ccw', "westerplatte-lubicz-skret"],

    ["lubicz-basztowa-prosto", 'basztowa-ccw', "basztowa-ccw-basztowa-prosto", 'basztowa-dunaj-ccw',
     "dunaj-podwale-prosto", 'bagatela-filharmonia-ccw', "strasz-strasz-prosto", 'filharmonia-gertrudy-ccw',
     "idziego-gertrudy-skret",
     'gertrudy-poczta-ccw', "gertrudy-westerplatte-prosto", 'westerplatte-left-ccw', "westerplatte-pawia-prosto"],
]

# set track to car


# dookoła obwodnicy start od:  'filharmonia-gertrudy-ccw'
streets1 = [
           "filharmonia-gertrudy-ccw",
            "idziego-gertrudy-skret",
           "gertrudy-poczta-ccw",
            "gertrudy-westerplatte-prosto",
           "westerplatte-right-ccw",
            "westerplatte-basztowa-skret",
           "basztowa-ccw",
            "basztowa-ccw-basztowa-prosto",
           "basztowa-dunaj-ccw",
            "dunaj-podwale-prosto",
            "bagatela-filharmonia-ccw",
           "strasz-strasz-prosto",
           ]


car = Car(streets[8], data, red, "car", 2)


car2 = Car(streets[1], data, blue, "car2", 4)

car3 = Car(streets[2], data, green, "car3", 6)


# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode(resolution)

#running condition and title
running = True
pygame.display.set_caption("Cracow Road Simulation")

# time delay
clockobject = pygame.time.Clock()
tick = 20

# background color
screen.fill(black)

# draw road
initializePoints(points)

#Pause message
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('To Pause press P To Continue press C', True, green)
textRect = text.get_rect()
textRect.center = (resolution[0] // 2, resolution[1] // 2)
screen.blit(text, textRect)




"""
car.move(screen, points)
car.set_vmax(0)
car.setV(0)
"""

print(len(car.get_street_names()))
start_time = time.time()

#points[1241].setTaken(1)

#Main Loop
while running:


    #print(time.time() - start_time)

    clockobject.tick(tick)


    occupied = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause(clockobject)
            elif event.key == pygame.K_RIGHT:
                tick = max(tick + 5, 3)
            elif event.key == pygame.K_LEFT:
                tick = max(tick - 5, 3)

    car.move(screen, points)
    #print(car.get_curr_street_p(), car.get_curr_street_c(), car.get_curr_street_n(), car.get_curr_street_l().getIndex())


    car2.move(screen, points)
    car3.move(screen, points)
    #print(car.getV(), car2.getV(), car3.getV())


    # taktyczna petla do sprawdzania ile w globalnej liscie points jest zajetych puntkow
    for i in range(len(points)):
        if (points[i].getTaken() == 1):
            occupied += 1
    #print(occupied)

    pygame.display.update()

    pass


