import pygame
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import *
import time
from RepeatedTimer import RepeatedTimer, start_traffic_lights
from random import randint
from SimulationStatistics import add_stats, making_file_statistic, run_stats
from Streets import streets
import matplotlib.pyplot as plt
import threading
from Streets import streets


class Screen:
    def __init__(self, data, points, streets, resolution, colors, over):
        self.data = data
        self.points = points
        self.resolution = resolution
        self.streets = streets
        self.colors = colors
        self.over = over
        self.cars = []
        self.iteration = 0
        self.initialize_cars()


    def initialize_points(self, screen):
        for i in range(len(points)):
            pygame.draw.circle(screen, self.colors["white"], self.points[i].get_cords(), 3)

    def initialize_cars(self):
        for i in range(100):
            car = Car(self.streets[randint(0, len(self.streets)-1)], data, self.colors["red"], "car"+str(i), self.over, randint(0, 2))
            self.cars.append(car)

    def check_if_reached_end(self):
        for i in range(len(self.cars)):
            if self.cars[i].track_end:
                del self.cars[i]
                break


    def start(self):

        making_file_statistic()
        thread = threading.Thread(target=run_stats)

        # initialize
        pygame.init()

        # create screen
        screen = pygame.display.set_mode(resolution)

        # running condition and title
        running = True
        pygame.display.set_caption("Cracow Road Simulation")

        # time delay
        clockobject = pygame.time.Clock()
        tick = 10

        # background color
        screen.fill(self.colors["black"])

        # draw road
        self.initialize_points(screen)

        # pause and velocity message
        text = ['To Pause press P To Continue press C', 'Average V: ', 'Average V_max: ', 'Percentage difference: ', 'Iteration: ', 'km/h', 'Number of Cars: ']
        message(screen, (self.resolution[0] // 2, self.resolution[1] // 2), self.colors, text[0])
        message(screen, (100, 50), self.colors, text[1])
        message(screen, (450, 50), self.colors, text[5])
        message(screen, (145, 100), self.colors, text[2])
        message(screen, (450, 100), self.colors, text[5])
        message(screen, (200, 700), self.colors, text[3])
        message(screen, (90, 800), self.colors, text[4])
        message(screen, (140, 750), self.colors, text[6])

        # thread for counting time - to handle traffic lights
        rt = RepeatedTimer(1.00, start_traffic_lights, points, screen)

        try:
            thread.start()


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

                self.check_if_reached_end()
                print("Current num of vehicles: ", len(self.cars))

                add_stats(self.cars, self.iteration)
                self.iteration += 1
                show_statistics(screen, self.colors)

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
    "grey": (22, 22, 22)
}

# fetching essential data from json
data, points = change_points_from_float_to_int("roads.json")
over = set_overtake_track(data)

s = Screen(data, points, streets, resolution, colors, over)
s.start()










