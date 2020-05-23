from Point import Point
import pygame

class Car(Point):


    def __init__(self, currP, prevP, nextP, v = 0, a = 0 ):
        self.__currP = currP
        self.__a = a
        self.__v = v
        self.__prevP = prevP
        self.__nextP = nextP


    def setTrack(self,streets,data):
        track = []
        for road in data:
            for street in streets:
                if (road['name'] == street):
                    track.append(road)
        self.__track = track

    def getTrack(self):
        return self.__track

    def getV(self):
        return self.__v

    def getA(self):
        return self.__a

    def setV(self, v):
        self.__v = v

    def setA(self, a):
        self.__a = a

    def getPrevP(self):
        return self.__prevP

    def getNextP(self):
        return self.__nextP

    def getCurrP(self):
        return self.__currP

    def setCurrP(self, currP):
        self.__currP = currP

    def setPrevP(self, prevP):
        self.__prevP = prevP

    def setNextP(self, nextP):
        self.__nextP = nextP

    def getNeigh(self):
        return [self.getNextP(),self.getPrevP()]

    def setNeigh(self, point1, point2):
        self.__nextP = point1
        self.__prevP = point2


    # def move(self, screen):
    #     pygame.draw.circle(screen, (255, 0, 0), self.getNextP().getCords(), 3)
    #     pygame.draw.circle(screen, (255, 255, 255), self.getCords(), 3)

    def move(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.getNextP().getCords(), 3)
        pygame.draw.circle(screen, (255, 255, 255), self.getCurrP().getCords(), 3)

        self.setPrevP(self.getCurrP())
        self.setCurrP(self.getNextP())


