from threading import Timer
import pygame


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs,):
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
flag_filharmonia = 1

# idziego
seconds_idziego = 0
flag_idziego = 1

# poczta
seconds_poczta = 0
flag_poczta = 1

# slowackiego
seconds_slowackiego = 0
flag_slowackiego = 1


def start_traffic_lights(points, screen):

    global seconds_filharmonia, seconds_idziego, seconds_poczta, seconds_slowackiego
    global flag_filharmonia, flag_idziego, flag_poczta, flag_slowackiego


    seconds_filharmonia += 1
    seconds_idziego += 1
    seconds_poczta += 1
    seconds_slowackiego += 1

    grey = (191, 191, 191)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # lines for idziego
    pygame.draw.line(screen, grey, (86, 434), (100, 470))
    pygame.draw.line(screen, grey, (149, 465), (120, 490))
    pygame.draw.line(screen, grey, (30+30-1, 470+23), (76, 480))


    # lines for filharmonia
    pygame.draw.line(screen, grey, (770-1, 40+55), (750, 110))
    pygame.draw.line(screen, grey, (670+30-1, 40+55-1), (725, 110))
    pygame.draw.line(screen, grey, (770+1, 130+1), (743, 125))

    # lines for poczta
    pygame.draw.line(screen, grey, (830+10, 700+1), (828, 680))
    pygame.draw.line(screen, grey, (885+1, 610+55-15), (865, 665))
    pygame.draw.line(screen, grey, (810+20, 575+54), (838, 647))
    pygame.draw.line(screen, grey, (750+29, 650+1), (812, 657))

    # lines for slowackiego
    pygame.draw.line(screen, grey, (1551, 844 + 20), (1530, 845))
    pygame.draw.line(screen, grey, (1480+29, 844 - 1), (1520, 842))
    pygame.draw.line(screen, grey, (1480+30, 750 + 55), (1480+30+5, 750+70))
    pygame.draw.line(screen, grey, (1571, 780+25), (1545, 830)) #(1570, 780, 30, 55)


    # filharmonia lights
    if flag_filharmonia:
        pygame.draw.rect(screen, (46, 49, 49), (770, 40, 30, 55))
        pygame.draw.circle(screen, green, (770 + 15, 40 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (770 + 15, 40 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (670, 40, 30, 55))
        pygame.draw.circle(screen, grey, (670 + 15, 40 + 15), 10, 0)
        pygame.draw.circle(screen, red, (670 + 15, 40 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (770, 130, 30, 55))
        pygame.draw.circle(screen, grey, (770 + 15, 130 + 15), 10, 0)
        pygame.draw.circle(screen, red, (770 + 15, 130 + 40), 10, 0)

    else:
        pygame.draw.rect(screen, (46, 49, 49), (770, 40, 30, 55))
        pygame.draw.circle(screen, grey, (770 + 15, 40 + 15), 10, 0)
        pygame.draw.circle(screen, red, (770 + 15, 40 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (670, 40, 30, 55))
        pygame.draw.circle(screen, green, (670 + 15, 40 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (670 + 15, 40 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (770, 130, 30, 55))
        pygame.draw.circle(screen, green, (770 + 15, 130 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (770 + 15, 130 + 40), 10, 0)



    # idziego lights
    if flag_idziego:
        pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
        pygame.draw.circle(screen, green, (100, 420), 10, 0)
        pygame.draw.circle(screen, grey, (100, 395), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (150, 440, 30, 55))
        pygame.draw.circle(screen, red, (165, 455), 10, 0)
        pygame.draw.circle(screen, grey, (165, 480), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (30, 470, 30, 55))
        pygame.draw.circle(screen, red, (30 + 15, 470 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (30 + 15, 470 + 40), 10, 0)

    else:
        pygame.draw.rect(screen, (46, 49, 49), (85, 380, 30, 55))
        pygame.draw.circle(screen, grey, (100, 420), 10, 0)
        pygame.draw.circle(screen, red, (100, 395), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (150, 440, 30, 55))
        pygame.draw.circle(screen, grey, (165, 455), 10, 0)
        pygame.draw.circle(screen, green, (165, 480), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (30, 470, 30, 55))
        pygame.draw.circle(screen, grey, (30 + 15, 470 + 15), 10, 0)
        pygame.draw.circle(screen, green, (30 + 15, 470 + 40), 10, 0)





    # poczta lights
    if flag_poczta:
        pygame.draw.rect(screen, (46, 49, 49), (830, 700, 30, 55))
        pygame.draw.circle(screen, grey, (830 + 15, 700 + 15), 10, 0)
        pygame.draw.circle(screen, red, (830 + 15, 700 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (885, 610, 30, 55))
        pygame.draw.circle(screen, green, (885 + 15, 610 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (885 + 15, 610 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (810, 575, 30, 55))
        pygame.draw.circle(screen, grey, (810 + 15, 575 + 15), 10, 0)
        pygame.draw.circle(screen, red, (810 + 15, 575 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (750, 650, 30, 55))
        pygame.draw.circle(screen, green, (750 + 15, 650 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (750 + 15, 650 + 40), 10, 0)


    else:
        pygame.draw.rect(screen, (46, 49, 49), (830, 700, 30, 55))
        pygame.draw.circle(screen, green, (830 + 15, 700 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (830 + 15, 700 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (885, 610, 30, 55))
        pygame.draw.circle(screen, grey, (885 + 15, 610 + 15), 10, 0)
        pygame.draw.circle(screen, red, (885 + 15, 610 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (810, 575, 30, 55))
        pygame.draw.circle(screen, green, (810 + 15, 575 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (810 + 15, 575 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (750, 650, 30, 55))
        pygame.draw.circle(screen, grey, (750 + 15, 650 + 15), 10, 0)
        pygame.draw.circle(screen, red, (750 + 15, 650 + 40), 10, 0)


    # slowackiego lights
    if flag_slowackiego:
        pygame.draw.rect(screen, (46, 49, 49), (1550, 844, 30, 55))
        pygame.draw.circle(screen, grey, (1550 + 15, 844 + 15), 10, 0)
        pygame.draw.circle(screen, red, (1550 + 15, 844 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1480, 844, 30, 55))
        pygame.draw.circle(screen, green, (1480 + 15, 844 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (1480 + 15, 844 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1480, 750, 30, 55))
        pygame.draw.circle(screen, grey, (1480 + 15, 750 + 15), 10, 0)
        pygame.draw.circle(screen, red, (1480 + 15, 750 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1570, 780, 30, 55))
        pygame.draw.circle(screen, green, (1570 + 15, 780 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (1570 + 15, 780 + 40), 10, 0)

    else:
        pygame.draw.rect(screen, (46, 49, 49), (1550, 844, 30, 55))
        pygame.draw.circle(screen, green, (1550 + 15, 844 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (1550 + 15, 844 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1480, 844, 30, 55))
        pygame.draw.circle(screen, grey, (1480 + 15, 844 + 15), 10, 0)
        pygame.draw.circle(screen, red, (1480 + 15, 844 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1480, 750, 30, 55))
        pygame.draw.circle(screen, green, (1480 + 15, 750 + 15), 10, 0)
        pygame.draw.circle(screen, grey, (1480 + 15, 750 + 40), 10, 0)

        pygame.draw.rect(screen, (46, 49, 49), (1570, 780, 30, 55))
        pygame.draw.circle(screen, grey, (1570 + 15, 780 + 15), 10, 0)
        pygame.draw.circle(screen, red, (1570 + 15, 780 + 40), 10, 0)




    # filharmonia
    # 104 - strasz-strasz-prosto
    # 1393 - zwierzycniek-strasz-skret
    # 1399 - franc-strasz-skret

    if seconds_filharmonia == 1:
        flag_filharmonia = swap(flag_filharmonia)
        points[104].set_lights("red")
        points[1393].set_lights("green")
        points[1399].set_lights("green")

    elif seconds_filharmonia == 2:
        points[104].set_taken(1)
        points[1393].set_taken(0)
        points[1399].set_taken(0)

    elif seconds_filharmonia == 9:
        flag_filharmonia = swap(flag_filharmonia)
        points[104].set_lights("green")
        points[1393].set_lights("red")
        points[1399].set_lights("red")

    elif seconds_filharmonia == 10:
        points[104].set_taken(0)
        points[1393].set_taken(1)
        points[1399].set_taken(1)
        seconds_filharmonia = -4



    # idziego
    # 1446 - bernard
    # 1454 - stradom-gert-skret
    # 1429 - bernard-gert-prosto
    # 1435 - gert-stradom-skret

    if seconds_idziego == 1:
        flag_idziego = swap(flag_idziego)

    elif seconds_idziego == 2:
        points[1446].set_taken(0)

    elif seconds_idziego == 9:
        flag_idziego = swap(flag_idziego)

    elif seconds_idziego == 10:
        points[1446].set_taken(1)
        seconds_idziego = -8





    # poczta
    # 376 - gert-wester-prosto
    # 963 - wester-gert-prosto
    # 1539 - sienna-staro-prosto
    # 1509 - staro-sienna-prosot

    if seconds_poczta == 1:
        flag_poczta = swap(flag_poczta)

    elif seconds_poczta == 2:
        points[376].set_lights("red")
        points[963].set_lights("red")
        points[1539].set_lights("green")
        points[1509].set_lights("green")

        points[376].set_taken(1)
        points[963].set_taken(1)
        points[1539].set_taken(0)
        points[1509].set_taken(0)

    elif seconds_poczta == 7:
        flag_poczta = swap(flag_poczta)

    elif seconds_poczta == 8:
        points[376].set_lights("green")
        points[963].set_lights("green")
        points[1539].set_lights("red")
        points[1509].set_lights("red")

        points[376].set_taken(0)
        points[963].set_taken(0)
        points[1539].set_taken(1)
        points[1509].set_taken(1)
        seconds_poczta = -10





    # slowackiego
    # 733 - wester-ccw-left
    # 617 - wester-ccw-right

    # 1131 - basztowa
    # 1608 - pawia
    # 1631 - lubicz


    if seconds_slowackiego == 1:
        flag_slowackiego = swap(flag_slowackiego)

    elif seconds_slowackiego == 2:
        points[733].set_taken(1)
        points[617].set_taken(1)
        points[1608].set_taken(1)

        points[1131].set_taken(0)
        points[1631].set_taken(0)


    elif seconds_slowackiego == 7:
        flag_slowackiego = swap(flag_slowackiego)

    elif seconds_slowackiego == 8:
        points[733].set_taken(0)
        points[617].set_taken(0)
        points[1608].set_taken(0)

        points[1131].set_taken(1)
        points[1631].set_taken(1)

        seconds_slowackiego = -8









