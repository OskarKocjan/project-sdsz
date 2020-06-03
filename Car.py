from Point import Point
from time import sleep
import pygame
from random import randint

class Car():


    def __init__(self,streets,data,color,name, v = 1, a = 0, v_changed = 0):
        self.__currentStreet = streets[0]
        self.__track = self.setTrack(streets, data)
        self.__a = a
        self.__v = v
        self.__color = color
        self.getFirstThreeAndLast()
        self.name = name
        self.__v_max = v + 1
        self.__v_changed = v_changed
        self.__street_names = streets

    def getFirstThreeAndLast(self):
        for item in self.__track:
            if (item['name'] == self.__currentStreet):
                self.setCurrP(item["coordinates"][0])
                self.setPrevP(item["coordinates"][1])
                self.setNextP(item["coordinates"][2])

    def get_street_points(self):
        for item in self.__track:
            if (item['name'] == self.__currentStreet):
                lenght = len(item['coordinates'])
                self.set_curr_street_p(item["coordinates"][0])
                self.set_curr_street_c(item["coordinates"][1])
                self.set_curr_street_n(item["coordinates"][2])
                self.set_curr_street_l(item["coordinates"][lenght-1])

    def setTrack(self,streets,data):

        track = []
        for street in streets:
            for road in data:
                if (road['name'] == street):
                    track.append(road)

        return track

    def set_curr_street_p(self,prev):
        self.curr_street_p = prev

    def set_curr_street_c(self, curr):
        self.curr_street_p = curr

    def set_curr_street_n(self, next):
            self.curr_street_p = next

    def set_curr_street_l(self,last):
        self.curr_street_l = last

    def get_curr_street_p(self):
        return self.curr_street_p

    def get_curr_street_c(self):
        return self.curr_street_p

    def get_curr_street_n(self):
        return self.curr_street_p

    def get_curr_street_l(self):
        return self.curr_street_l

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

    def setLastP(self,lastP):
        self.__lastP = lastP

    def getLastP(self):
        return self.__lastP

    def set_vmax(self, vmax):
        self.__v_max = vmax

    def get_vmax(self):
        return self.__v_max


    def get_v_change(self):
        return self.__v_changed

    def set_v_change(self, bool):
        self.__v_changed = bool


    def set_street_names(self,streets):
        self.__street_names = streets

    def get_street_names(self):
        return self.__street_names


    def getCurrentStreetCoords(self):
        for road in self.__track:
            if(road['name'] == self.getCurrentStreet()):
                return road['coordinates']

    def getCurrentStreet(self):
        return self.__currentStreet

    def setCurrentStreet(self, street):
        self.__currentStreet = street


    # funkcja sprawdzająca czy punkty przed nim sa zajete, jesli tak -> zwolnij
    def checkPointsInFront(self, points):

        currIndex = self.__currP.getIndex()
        nextIndex = currIndex
        j = 0
        for i in range(0, self.getV() + 1):


                if(points[nextIndex].getCords() == self.curr_street_l.getCords()):
                    dict = self.getTrack()
                    index = self.get_street_names().index(self.getCurrentStreet())
                    nextPoint = dict[(index+1)%len(self.get_street_names())]['coordinates'][0]
                    nextIndex = nextPoint.getIndex()
                    j = 1
                else:
                    nextIndex = nextIndex + j
                    j = 1

                if points[nextIndex].getTaken():
                    self.setV(min(self.getV(), i))
                    self.set_v_change(1)

    def accel_random(self):

        random = randint(0, 100)
        if (random > 5):
            self.setV(min(self.getV()+1, self.get_vmax()))
        else:
            self.setV(max(self.getV() - 1, 0))







    def move(self, screen, points):

        self.get_street_points()

        self.checkPointsInFront(points)

        self.change_point(screen, points)

        if(self.get_v_change() == 0):
            self.accel_random()
        else:
            self.set_v_change(0)






    def change_point(self, screen, points):


    
        # petla predkosci dla danego pojazdu
        for i in range(self.__v):

            track = self.getTrack()

            pygame.draw.circle(screen, self.__color, self.getCurrP().getCords(), 5)
            pygame.draw.circle(screen, (255, 255, 255), self.getPrevP().getCords(), 5)

            # ustawianie czy zajety czy nie
            points[self.getCurrP().getIndex()].setTaken(1)
            points[self.getPrevP().getIndex()].setTaken(0)

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


            lastRoadList = self.getTrack()[len(self.getTrack())-1]['coordinates']
            if(self.getCurrP().getCords() == lastRoadList[len(lastRoadList)-1].getCords()):
                 firstRoadDict = self.__track[0]
                 self.setCurrentStreet(firstRoadDict['name'])
                 self.setNextP(firstRoadDict['coordinates'][0])




