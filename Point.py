class Point:

    def __init__(self, x = 0, y = 0, color = 'white', taken = 0):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__taken = taken

    def __str__(self):
        return '('+str(self.__x)+', '+str(self.__y)+')'

    def setColor(self, color):
        self.__color = color

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getColor(self):
        return self.__color

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getCords(self):
        return (self.getX(), self.getY())

    def setCords(self, x , y ):
        self.setY(y)
        self.setX(x)

    def getTaken(self):
        return self.__taken

    def setTaken(self, taken):
        self.__taken = taken

    def checkTaken(self):

        if self.getTaken() == 1:
            return True

        else:
            return False