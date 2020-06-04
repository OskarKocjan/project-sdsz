import pygame
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import pause
import time
from RepeatedTimer import RepeatedTimer, start_traffic_lights


def initialize_points(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, white, points[i].get_cords(), 3)


resolution = (1800,900)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# fetching essential data from json
data, points = change_points_from_float_to_int("roads.json")


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


# roads for tests
tmp = ["filharmonia-gertrudy-ccw","idziego-gertrudy-skret","gertrudy-poczta-ccw"]
tmp2 = ["pawia-westerplatte-prosto"]#,"gertrudy-poczta-ccw",]
tmp3 = ["basztowa-cw","basztowa-lubicz-prosto"]#, "gertrudy-poczta-ccw",]
tmp4 = ["lubicz-basztowa-prosto"]#, "gertrudy-poczta-ccw",]


# initialize cars
car = Car(tmp, data, red, "car", 0)

car2 = Car(tmp2, data, blue, "car2", 0)

car3 = Car(tmp3, data, green, "car3", 0)

car4 = Car(tmp4, data, cyan, "car4", 0)


cars = []
for i in range(50):
    car = Car(streets[randrange(len(streets))], data, red, "car"+str(i), randrange(3))
    cars.append(car)

# initialize
pygame.init()


# create screen
screen = pygame.display.set_mode(resolution)


# running condition and title
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


# thread for counting time - to handle traffic lights
rt = RepeatedTimer(1.0, start_traffic_lights, points, screen)



try:

    # Main Loop
    time.sleep(1)
    while running:
        clockobject.tick(tick)

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

        #car.move(screen, points)

        #car2.move(screen, points)

        #car3.move(screen, points)

        #car4.move(screen, points)

        for car in cars:
            car.move(screen, points)

        pygame.display.update()

        pass

finally:
    rt.stop()






