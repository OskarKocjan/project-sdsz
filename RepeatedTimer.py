from threading import Timer

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


seconds = 0

def start_traffic_lights(points,tick):
    global seconds
    print(seconds, tick)
    seconds += 1
    if(seconds == 1):
        # filharmonia
        # 104 - strasz-strasz-prosto
        # 1393 - zwierzycniek-strasz-skret
        # 1399 - franc-strasz-skret
        print("zielone")
        points[104].setTaken(0)
        points[1393].setTaken(1)
        points[1399].setTaken(1)

    elif(seconds == 6):
        print("czerwone")
        points[104].setTaken(1)
        points[1393].setTaken(0)
        points[1399].setTaken(0)
        seconds = -10



