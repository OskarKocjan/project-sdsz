




class Point:

    x = 0
    y = 0
    color = 'white'


    def __init__(self, x, y, color = 'white'):
        self.x = x
        self.y = y
        self.color = color

    def setColor(self, color):
        self.color = color


    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getColor(self):
        return self.color

    def getX(self):
        return self.x

    def getY(self):
        return self.y


