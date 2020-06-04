import pygame
from Point import Point
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import pause
import time
from RepeatedTimer import RepeatedTimer,start_traffic_lights


def initialize_points(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].getCords(), 3)





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
            "bagatela-filharmonia-ccw",
           "strasz-strasz-prosto",
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

           ]

tmp = ["bagatela-filharmonia-ccw", "strasz-strasz-prosto", "filharmonia-gertrudy-ccw",]
tmp2 = ["zwierzyniecka-strasz-skret", "filharmonia-gertrudy-ccw",]


car = Car(tmp, data, red, "car", 0)

car2 = Car(tmp2, data, blue, "car2", 0)

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
tick = 15

# background color
screen.fill(black)

# draw road
initialize_points(points)

# pause message
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('To Pause press P To Continue press C', True, green)
textRect = text.get_rect()
textRect.center = (resolution[0] // 2, resolution[1] // 2)
screen.blit(text, textRect)


# thread for counting time to handle traffic lights
rt = RepeatedTimer(20 / tick, start_traffic_lights,points,tick)

try:

    # Main Loop
    while running:

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
        #print(car.getCurrP().getIndex())
        car2.move(screen, points)
        #car3.move(screen, points)


        # taktyczna petla do sprawdzania ile w globalnej liscie points jest zajetych puntkow
        # for i in range(len(points)):
        #     if (points[i].getTaken() == 1):
        #         occupied += 1
        #print(occupied)

        pygame.display.update()

        pass

finally:
    rt.stop()

#idziego
# 1410 - idziego-gertrudy-skret






