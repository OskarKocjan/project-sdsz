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
blue = (0, 0, 255)

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


streets2 = [

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






streets3 = [

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
           "filharmonia-gertrudy-ccw",
           ]




streets4 = [

            "gertrudy-westerplatte-prosto",
           "westerplatte-right-ccw",
            "westerplatte-basztowa-skret",
           "basztowa-ccw",
            "basztowa-ccw-basztowa-prosto",
           "basztowa-dunaj-ccw",
            "dunaj-podwale-prosto",
            "bagatela-filharmonia-ccw",
           "strasz-strasz-prosto",
           "filharmonia-gertrudy-ccw",
            "idziego-gertrudy-skret",
           "gertrudy-poczta-ccw",
           ]




# roads for tests
tmp = ["gertrudy-poczta-ccw","gertrudy-staro-skret"]#"gertrudy-westerplatte-prosto","westerplatte-right-ccw"]
tmp2 = ["basztowa-cw","basztowa-westerplatte-skret","westerplatte-left-cw","westerplatte-staro-skret" ]
tmp5 = ["sienna-staro-prosto"]
tmp6 = ["staro-sienna-prosto"]



tmp3 = ["gertrudy-poczta-ccw","gertrudy-sienna-skret"]
tmp4 = ["basztowa-cw", "basztowa-westerplatte-skret", "westerplatte-left-cw", "westerplatte-gertrudy-prosto", "gertrudy-poczta-cw"] #"westerplatte-sienna-skret"



# initialize cars
car1 = Car(streets1, data, red, "car", 0)

car2 = Car(streets2, data, blue, "car2", 1)

car3 = Car(streets3, data, red, "car3", 2)

car4 = Car(streets4, data, blue, "car4", 3)


cars = []
for i in range(20):

    car = Car(tmp, data, red, "car" + str(i), 0)
    # if(i%2==0):
    # #car = Car(streets[randrange(len(streets))], data, red, "car"+str(i), randrange(3))
    #     car = Car(tmp, data, blue, "car"+str(i), 0)
    # else:
    #     car = Car(tmp2, data, red, "car" + str(i), 0)

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

#rt = RepeatedTimer(1.00, start_traffic_lights, points, screen)



ulice = ["westerplatte-staro-skret","gertrudy-sienna-skret"]
points[962].set_taken(1)
# pygame.draw.circle(screen, red, points[955].get_cords(), 3)

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

        car1.move(screen, points)
        #print(points[962].get_taken())
        #print(car1.get_curr_p().get_index(),car1.get_current_street())
        #print(car.get_curr_p().get_index())

        car2.move(screen, points)
        #print(car2.get_curr_street_l().get_index())
        #print(car2.get_curr_p().get_index())

        car3.move(screen, points)
        #print(car3.get_curr_p().get_index())

        car4.move(screen, points)

        #for car in cars:
        #    car.move(screen, points)
            #print(car.get_curr_p().get_index())

        pygame.display.update()

        pass

finally:
    pass
 #   rt.stop()






