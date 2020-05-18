




class Point:


    def __init__(self, x = 0, y = 0, color = 'white'):
        self.__x = x
        self.__y = y
        self.__color = color

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
        self.selfX(x)