from Point import Point

class Car(Point):



    def __init__(self, x, y, color,taken, v = 0, a = 0):
        super().__init__(x, y, color, taken)
        self.__a = a
        self.__v = v





    @classmethod
    def fromPoint(cls, point, v = 0, a = 0):
        return cls(point.getX(), point.getY(), point.getColor(), point.getTaken(), v, a)