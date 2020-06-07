class Point:

    def __init__(self, x = 0, y = 0, color = 'white', taken = 0, index = 0):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__taken = taken
        self.__index = index
        self.__light = None

    def __str__(self):
        return '('+str(self.__x)+', '+str(self.__y)+')'

    def set_lights(self, light):
        self.__light = light

    def get_lights(self):
        return self.__light

    def set_color(self, color):
        self.__color = color

    def set_index(self, index):
        self.__index = index

    def get_index(self):
        return self.__index

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_color(self):
        return self.__color

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_cords(self):
        return (self.get_x(), self.get_y())

    def set_cords(self, x , y ):
        self.set_y(y)
        self.set_x(x)

    def get_taken(self):
        return self.__taken

    def set_taken(self, taken):
        self.__taken = taken

    def check_taken(self):

        if self.get_taken() == 1:
            return True

        else:
            return False

    def same(self, point):
        if(self.get_x() == point.get_x() and self.get_y() == point.get_y() and self.get_color() == point.get_color() and self.get_taken() == point.get_taken()):
            return True
        else:
            return False
