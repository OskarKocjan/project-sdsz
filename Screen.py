import pygame
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import pause
import time
from RepeatedTimer import RepeatedTimer, start_traffic_lights


class Screen:
    def __init__(self, data, points, streets, resolution, colors):
        self.data = data
        self.points = points
        self.resolution = resolution
        self.streets = streets
        self.colors = colors
        self.cars = self.initialize_cars()

    def initialize_points(self, screen):
        for i in range(len(points)):
            pygame.draw.circle(screen, self.colors["white"], self.points[i].get_cords(), 3)

    def initialize_cars(self):
        cars = []
        for i in range(70):
            if (i % 2 == 0):

                car = Car(tmp, data, self.colors["blue"], "car" + str(i), 0)
            else:
                car = Car(tmp2, data, self.colors["red"], "car" + str(i), 0)
            cars.append(car)
        return cars

    def start(self):
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

                for car in self.cars:
                    car.move(screen, points)
                    # print(car.get_curr_p().get_index())

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

# roads for tests
tmp = ["gertrudy-poczta-ccw", "gertrudy-staro-skret"]
tmp2 = ["basztowa-cw", "basztowa-westerplatte-skret","westerplatte-left-cw","westerplatte-staro-skret" ]

streets = [tmp, tmp2]

s = Screen(data, points, streets, resolution, colors)
s.start()










