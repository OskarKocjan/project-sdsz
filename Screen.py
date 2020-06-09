import pygame
from fetchPointsFromFile import *
from Car import Car
from InterfaceStuff import *
import time
from RepeatedTimer import RepeatedTimer, start_traffic_lights
from random import randint
from SimulationStatistics import add_stats, making_file_statistic, run_stats
import matplotlib.pyplot as plt
from StoppableThread import thread_with_trace


class Screen:
    def __init__(self, data, points, streets, resolution, colors, over):
        self.data = data
        self.points = points
        self.resolution = resolution
        self.streets = streets
        self.colors = colors
        self.over = over
        self.cars = self.initialize_cars()
        self.iteration = 0


    def initialize_points(self, screen):
        for i in range(len(points)):
            pygame.draw.circle(screen, self.colors["white"], self.points[i].get_cords(), 3)

    def initialize_cars(self):
        cars = []
        for i in range(70):
            if (i % 2 == 0):

                car = Car(self.streets[0], data, self.colors["blue"], "car" + str(i), self.over, randint(0,2))
            else:
                car = Car(self.streets[1], data, self.colors["red"], "car" + str(i), self.over, randint(0,2))
            cars.append(car)
        return cars

    def start(self):



        car1 = Car(streets1, data, self.colors['blue'], "car", over, 0)

        car2 = Car(streets2, data, self.colors['red'], "car2", over, 1)

        car3 = Car(streets3, data, self.colors['blue'], "car3", over, 2)

        car4 = Car(streets4, data, self.colors['red'], "car4", over, 3)

        making_file_statistic()
        thread = thread_with_trace(target=run_stats)


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
        pause_message(screen, self.resolution, self.colors)

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
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            pause(clockobject)
                        elif event.key == pygame.K_RIGHT:
                            tick = max(tick + 5, 3)
                        elif event.key == pygame.K_LEFT:
                            tick = max(tick - 5, 3)

                for car in self.cars:
                    car.move(screen, points)
                    print(car.get_curr_p().get_index())

                for pkt in self.data:
                    if pkt['name'] == 'basztowa-ccw':
                        for cord in pkt['coordinates']:
                            if cord.get_taken():
                                print("taken",cord.get_index())


                add_stats(self.cars, self.iteration)
                self.iteration += 1
                show_statistics(screen, self.colors)
                pygame.display.update()

                pass

        finally:
            thread.kill()
            thread.join()
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






# # FILHARMONIA
# tmp1 = ["bagatela-filharmonia-ccw",  "strasz-franc-skret"]
# tmp2 = ["franc-strasz-skret", "filharmonia-gertrudy-ccw"]
# tmp3 = ["zwierzyniecka-strasz-skret", "filharmonia-gertrudy-ccw"]


# # IDZIEGO chyba działa wszystko
# tmp1 = ["filharmonia-gertrudy-ccw", "idziego-gertrudy-skret","gertrudy-poczta-ccw","gertrudy-sienna-skret"] # "idziego-stradom-prosto"
# #tmp1 = ["idziego-gertrudy-skret"] # "idziego-stradom-prosto"
# tmp2 = ["stradom-gert-skret", "gertrudy-poczta-ccw","gertrudy-sienna-skret"]
# tmp3 = ["bernard-gertrudy-prosto", "gertrudy-poczta-ccw","gertrudy-sienna-skret"]
# tmp4 = ["gertrudy-poczta-cw", "gertrudy-stradom-skret" ]

#POCZTA jak obra w prawo to cos dupi sie
# tmp1 = ["gertrudy-poczta-ccw", "gertrudy-sienna-skret"]
# tmp2 = ["westerplatte-right-cw", "westerplatte-gertrudy-prosto", "gertrudy-poczta-cw" ]
# tmp3 = ["staro-sienna-prosto"]
# tmp4 = ["sienna-staro-prosto"]

# SLOWACKIEGO dziala
# tmp1 = ["westerplatte-right-ccw", "westerplatte-basztowa-skret", "basztowa-ccw"]
# tmp2 = [ "basztowa-cw", "basztowa-westerplatte-skret", "westerplatte-right-cw", "westerplatte-staro-skret"]
# tmp3 = ["pawia-westerplatte-prosto", "westerplatte-right-cw","westerplatte-staro-skret"]
# tmp4 = ["lubicz-westerplatte-skret", "westerplatte-right-cw","westerplatte-staro-skret"]

# BAGATELA
tmp1 = ["karmelicka-dunaj-skret","basztowa-dunaj-cw"] #1370
tmp2 = ["karmelicka-podwale-skret", "bagatela-filharmonia-ccw"] #1354
tmp3 = ["basztowa-dunaj-ccw", "dunaj-podwale-prosto","bagatela-filharmonia-ccw" ]


# roads for tests
tmp = ["gertrudy-poczta-ccw", "gertrudy-staro-skret"]
tmp2 = ["basztowa-cw", "basztowa-westerplatte-skret","westerplatte-right-cw","westerplatte-staro-skret" ]
streets = [tmp, tmp2, streets1, streets2, streets3, streets4]

#making file
#making_file_statistic()
#run_stats()


s = Screen(data, points, streets, resolution, colors, over)
s.start()










