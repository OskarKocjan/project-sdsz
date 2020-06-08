import pygame
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import pause
import time
from RepeatedTimer import RepeatedTimer, start_traffic_lights


class Screen:
    def __init__(self, data, points, streets, resolution, colors, over):
        self.data = data
        self.points = points
        self.resolution = resolution
        self.streets = streets
        self.colors = colors
        self.over = over
        self.cars = self.initialize_cars()


    def initialize_points(self, screen):
        for i in range(len(points)):
            pygame.draw.circle(screen, self.colors["white"], self.points[i].get_cords(), 3)

    def initialize_cars(self):
        cars = []
        for i in range(70):
            if (i % 2 == 0):

                car = Car(tmp, data, self.colors["blue"], "car" + str(i), self.over, 0)
            else:
                car = Car(tmp2, data, self.colors["red"], "car" + str(i), self.over, 0)
            cars.append(car)
        return cars

    def start(self):

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
            "bagatela-filharmonia-ccw",
        ]

        streets3 = [

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

        streets4 = [

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
            "idziego-gertrudy-skret",
        ]

        car1 = Car(streets1, data, self.colors['blue'], "car", over, 0)

        car2 = Car(streets2, data, self.colors['red'], "car2", over, 1)

        car3 = Car(streets3, data, self.colors['blue'], "car3", over, 2)

        car4 = Car(streets4, data, self.colors['red'], "car4", over, 3)




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
        screen.fill(self.colors["black"])

        # draw road
        self.initialize_points(screen)

        # pause message
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('To Pause press P To Continue press C', True, self.colors["green"])
        text_rect = text.get_rect()
        text_rect.center = (resolution[0] // 2, resolution[1] // 2)
        screen.blit(text, text_rect)

        # thread for counting time - to handle traffic lights
        rt = RepeatedTimer(1.00, start_traffic_lights, points, screen)

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

                #for car in self.cars:
                #    car.move(screen, points)
                    # print(car.get_curr_p().get_index())

                car1.move(screen, points)
                car2.move(screen, points)
                car3.move(screen, points)
                car4.move(screen, points)

                pygame.display.update()

                pass

        finally:
            rt.stop()


resolution = (1800, 900)

colors = {
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "cyan": (0, 255, 255),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}


# fetching essential data from json
data, points = change_points_from_float_to_int("roads.json")


# # FILHARMONIA
# tmp1 = ["bagatela-filharmonia-ccw",  "strasz-franc-skret"]
# tmp2 = ["franc-strasz-skret", "filharmonia-gertrudy-ccw"]
# tmp3 = ["zwierzyniecka-strasz-skret", "filharmonia-gertrudy-ccw"]


# # IDZIEGO
# tmp1 = ["filharmonia-gertrudy-ccw", "idziego-gertrudy-skret"] # "idziego-stradom-prosto"
# tmp2 = ["gertrudy-poczta-cw", "gertrudy-stradom-skret" ]
# tmp3 = ["bernard-stradom-skret"]
# tmp4 = ["stradom-gert-skret", "gertrudy-poczta-ccw" ]

# POCZTA
tmp1 = ["gertrudy-poczta-ccw", "gertrudy-staro-skret"]
tmp2 = ["basztowa-cw", "basztowa-westerplatte-skret", "westerplatte-right-cw", "westerplatte-staro-skret" ]
tmp3 = ["sienna-staro-prosto"]
tmp4 = ["staro-sienna-prosto"]

# # SLOWACKIEGO
# tmp1 = ["westerplatte-left-ccw","westerplatte-basztowa-skret", "basztowa-ccw" ]
# tmp2 = [ "basztowa-cw","basztowa-westerplatte-skret", "westerplatte-right-cw" ]
# tmp3 = ["pawia-westerplatte-prosto" , "westerplatte-right-cw"]
# tmp4 = ["lubicz-basztowa-prosto" , "basztowa-ccw"]

over_streets = ['westerplatte-right-ccw', 'westerplatte-left-ccw', 'westerplatte-right-cw','westerplatte-left-cw']
over = set_overtake_track(over_streets, data)


# roads for tests
tmp = ["gertrudy-poczta-ccw", "gertrudy-staro-skret"]
tmp2 = ["basztowa-cw", "basztowa-westerplatte-skret","westerplatte-left-cw","westerplatte-staro-skret" ]

streets = [tmp, tmp2]

s = Screen(data, points, streets, resolution, colors, over)
s.start()










