from Point import Point
from time import sleep
import pygame

class Car():


    def __init__(self,streets,data,color, v = 1, a = 0):
        self.__currentStreet = streets[0]
        self.__track = self.setTrack(streets,data)
        self.__a = a
        self.__v = v
        self.__color = color
        self.getFirstThreeAndLast()


    def getFirstThreeAndLast(self):
        for item in self.__track:
            if (item['name'] == self.__currentStreet):
                length = len(item["coordinates"])
                self.__prevP = Point(item["coordinates"][0].getCords()[0], item["coordinates"][0].getCords()[1])
                self.__currP = Point(item["coordinates"][1].getCords()[0], item["coordinates"][1].getCords()[1])
                self.__nextP = Point(item["coordinates"][2].getCords()[0], item["coordinates"][2].getCords()[1])
                self.__lastP = Point(item["coordinates"][length-1].getCords()[0], item["coordinates"][length-1].getCords()[1])


    def setTrack(self,streets,data):
        track = []
        for road in data:
            for street in streets:
                if (road['name'] == street):
                    track.append(road)

        return track

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


    def getCurrentStreet(self):
        return self.__currentStreet

    def setCurrentStreet(self, street):
        self.__currentStreet = street


    def move(self, screen, points):

        # petla predkosci dla danego pojazdu
        for i in range(self.__v):

            # ustawianie globalnej zmiennej czy punkt zajety czy juz nie
            for i in range(len(points)):
                if (points[i].getCords() == self.getNextP().getCords()):
                    points[i].setTaken(1)
                elif (points[i].getCords() == self.getCurrP().getCords()):
                    points[i].setTaken(0)


            # taktyczne spanko dla lepszego wygladu
            sleep(0.01)

            track = self.getTrack()

            pygame.draw.circle(screen, self.__color, self.getNextP().getCords(), 3)
            pygame.draw.circle(screen, (255, 255, 255), self.getCurrP().getCords(), 3)

            self.setPrevP(self.getCurrP())
            self.setCurrP(self.getNextP())


            changeLine = 0

            for dictionaries in track:
                if dictionaries['name'] == self.getCurrentStreet():
                    for i in range(len(dictionaries['coordinates'])):
                        if(self.getNextP().same(dictionaries['coordinates'][i])):
                            if(i != len(dictionaries['coordinates']) - 1):
                                self.setNextP(dictionaries['coordinates'][i+1])

                            else:
                                changeLine = 1

                            break

                elif(changeLine == 1):
                    self.setNextP(dictionaries['coordinates'][0])
                    self.setCurrentStreet(dictionaries['name'])
                    break


            # if last street set to the first again and go around
            lastRoadList = self.getTrack()[len(self.getTrack())-1]['coordinates']
            if(self.getNextP().getCords() == lastRoadList[len(lastRoadList)-1].getCords()):
                firstRoadDict = self.__track[0]
                self.setCurrentStreet(firstRoadDict['name'])
                self.setNextP(firstRoadDict['coordinates'][0])


