from threading import Timer
import pygame

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def swap(flag):
    if flag == 1: flag = 0
    else: flag = 1
    return flag


# filharmonia
seconds_filharmonia = 0
flag_filharmonia = 0

# idziego
seconds_idziego = 0
flag_idziego = 0

# poczta
seconds_poczta = 0
flag_poczta = 0

# slowackiego
seconds_slowackiego = 0
flag_slowackiego = 0

def start_traffic_lights(points,screen):

    global seconds_filharmonia, seconds_idziego, seconds_poczta, seconds_slowackiego
    global flag_filharmonia, flag_idziego, flag_poczta, flag_slowackiego



    grey = (191, 191, 191)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # line for lights
    pygame.draw.line(screen, grey, (86, 434), (110, 470))
    pygame.draw.line(screen, grey, (149, 465), (120, 490))

    # filharmonia lights
    if flag_idziego:
        pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
        pygame.draw.circle(screen, red, (100, 420), 10, 0)
        pygame.draw.circle(screen, grey, (100, 395), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (150, 440, 30, 55))
        pygame.draw.circle(screen, grey, (165, 480), 10, 0)
        pygame.draw.circle(screen, green, (165, 455), 10, 0)

    else:
        pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
        pygame.draw.circle(screen, grey, (100, 420), 10, 0)
        pygame.draw.circle(screen, green, (100, 395), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (150, 440, 30, 55))
        pygame.draw.circle(screen, red, (165, 480), 10, 0)
        pygame.draw.circle(screen, grey, (165, 455), 10, 0)

    # # idziego lights
    # if flag_idziego:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, (255, 0, 0), (100, 420), 10, 0)
    #     pygame.draw.circle(screen, grey, (100, 395), 10, 0)
    # else:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, grey, (100, 420), 10, 0)
    #     pygame.draw.circle(screen, (0, 255, 0), (100, 395), 10, 0)
    #
    # # poczta lights
    # if flag_idziego:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, (255, 0, 0), (100, 420), 10, 0)
    #     pygame.draw.circle(screen, grey, (100, 395), 10, 0)
    # else:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, grey, (100, 420), 10, 0)
    #     pygame.draw.circle(screen, (0, 255, 0), (100, 395), 10, 0)
    #
    # # slowackiego lights
    # if flag_idziego:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, (255, 0, 0), (100, 420), 10, 0)
    #     pygame.draw.circle(screen, grey, (100, 395), 10, 0)
    # else:
    #     pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
    #     pygame.draw.circle(screen, grey, (100, 420), 10, 0)
    #     pygame.draw.circle(screen, (0, 255, 0), (100, 395), 10, 0)





    seconds_filharmonia += 1
    seconds_idziego += 1
    seconds_poczta += 1
    seconds_slowackiego += 1


    # filharmonia
    # 104 - strasz-strasz-prosto
    # 1393 - zwierzycniek-strasz-skret
    # 1399 - franc-strasz-skret

    if seconds_filharmonia == 1:
        flag_filharmonia = swap(flag_filharmonia)
        points[104].set_taken(1)
        points[1393].set_taken(0)
        points[1399].set_taken(0)


    elif seconds_filharmonia == 10:
        flag_filharmonia = swap(flag_filharmonia)
        points[104].set_taken(0)
        points[1393].set_taken(1)
        points[1399].set_taken(1)
        seconds_filharmonia = -4



    # idziego
    # 1410 - idziego-gert-skret i idziego-gert-prosto
    # 1454 - stradom-gert-skret
    # 1429 - bernard-gert-prosto
    # 1435 - gert-stradom-skret

    if seconds_idziego == 1:
        flag_idziego = swap(flag_idziego)
        print("czerwone")
        points[1410].set_taken(1)
        points[1454].set_taken(1)
        points[1429].set_taken(0)
        points[1435].set_taken(0)

    elif seconds_idziego == 10:
        flag_idziego = swap(flag_idziego)
        print("zielone")
        points[1410].set_taken(0)
        points[1454].set_taken(0)
        points[1429].set_taken(1)
        points[1435].set_taken(1)
        seconds_idziego = -8



    # poczta
    # 1457 - gert-wester-prosto
    # 1482 - wester-gert-prosto
    # 1539 - sienna-staro-prosto
    # 1509 - staro-sienna-prosot

    if seconds_poczta == 1:
        flag_poczta = swap(flag_poczta)
        points[1457].set_taken(1)
        points[1482].set_taken(1)
        points[1539].set_taken(0)
        points[1509].set_taken(0)

    elif seconds_poczta == 6:
        flag_poczta = swap(flag_poczta)
        points[1457].set_taken(0)
        points[1482].set_taken(0)
        points[1539].set_taken(1)
        points[1509].set_taken(1)
        seconds_poczta = -10

    # slowackiego
    # 1578 - wester-ccw
    # 1608 - pawia-right
    # 1565 - basztowa-lubicz
    # 1631 - lubicz-basztowa

    if seconds_slowackiego == 1:
        flag_slowackiego = swap(flag_slowackiego)
        points[1578].set_taken(1)
        points[1608].set_taken(1)
        points[1565].set_taken(0)
        points[1631].set_taken(0)


    elif seconds_slowackiego == 8:
        flag_slowackiego = swap(flag_slowackiego)
        points[1578].set_taken(0)
        points[1608].set_taken(0)
        points[1565].set_taken(1)
        points[1631].set_taken(1)

        seconds_slowackiego = -8

    print(seconds_idziego)






