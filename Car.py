from Point import Point
from time import sleep
import pygame
from random import randint



class Car:

    def __init__(self, streets, data, color, name, v=1, a=0, v_changed=0):
        self.__currentStreet = streets[0]
        self.__data = data
        self.__track = self.set_track(streets, data)
        self.__a = a
        self.__v = v
        self.__color = color
        self.get_first_three_and_last()
        self.name = name
        self.__v_max = v + 1
        self.__v_changed = v_changed
        self.__street_names = streets
        self.__overtake_track = self.set_overtake_track(['westerplatte-right-ccw', 'westerplatte-left-ccw', 'westerplatte-right-cw', 'westerplatte-left-cw' ], data)


    def get_first_three_and_last(self):
        for item in self.__track:
            if (item['name'] == self.__currentStreet):
                self.set_curr_p(item["coordinates"][0])
                self.set_prev_p(item["coordinates"][1])
                self.set_next_p(item["coordinates"][2])

    def get_street_points(self):
        for item in self.__track:
            if (item['name'] == self.__currentStreet):
                lenght = len(item['coordinates'])
                self.set_curr_street_p(item["coordinates"][0])
                self.set_curr_street_c(item["coordinates"][1])
                self.set_curr_street_n(item["coordinates"][2])
                self.set_curr_street_l(item["coordinates"][lenght-1])

    def set_track(self,streets,data):

        track = []
        for street in streets:
            for road in data:
                if (road['name'] == street):
                    track.append(road)

        return track

    def set_track_from_track(self, track):
        self.__track = track

    def set_overtake_track(self, streets, data):
        track = []

        for street in streets:
            for road in data:
                if (road['name'] == street):
                    track.append(road['coordinates'])


        return track


    def get_data(self):
        return  self.__data

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

    def get_track(self):
        return self.__track

    def get_v(self):
        return self.__v

    def get_a(self):
        return self.__a


    def get_overtake_track(self):
        return self.__overtake_track



    def set_v(self, v):
        self.__v = v

    def set_a(self, a):
        self.__a = a

    def get_prev_p(self):
        return self.__prevP

    def get_next_p(self):
        return self.__nextP

    def get_curr_p(self):
        return self.__currP

    def set_curr_p(self, currP):
        self.__currP = currP

    def set_prev_p(self, prevP):
        self.__prevP = prevP

    def set_next_p(self, nextP):
        self.__nextP = nextP

    def get_neigh(self):
        return [self.get_next_p(),self.get_prev_p()]

    def set_neigh(self, point1, point2):
        self.__nextP = point1
        self.__prevP = point2

    def set_last_p(self,lastP):
        self.__lastP = lastP

    def get_last_p(self):
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

    def get_current_street_coords(self):
        for road in self.__track:
            if(road['name'] == self.get_current_street()):
                return road['coordinates']

    def get_current_street(self):
        return self.__currentStreet

    def set_current_street(self, street):
        self.__currentStreet = street




    # funkcja sprawdzająca czy punkty przed nim sa zajete, jesli tak -> zwolnij
    def check_points_in_front(self, points):

        currIndex = self.__currP.get_index()
        nextIndex = currIndex
        j = 0
        for i in range(0, self.get_v() + 1):


                if(points[nextIndex].get_cords() == self.curr_street_l.get_cords()):
                    dict = self.get_track()
                    index = self.get_street_names().index(self.get_current_street())
                    nextPoint = dict[(index+1)%len(self.get_street_names())]['coordinates'][0]
                    nextIndex = nextPoint.get_index()
                    j = 1
                else:
                    nextIndex = nextIndex + j
                    j = 1

                if points[nextIndex].get_taken():
                    self.set_v(min(self.get_v(), i))
                    self.set_v_change(1)
                    if points[nextIndex].get_lights() == "red":
                        print("au")
                        self.set_v(-1)

    def accel_random(self):

        random = randint(0, 100)
        if (random > 5):
            self.set_v(min(self.get_v()+1, self.get_vmax()))
        else:
            self.set_v(max(self.get_v() - 1, 0))
            self.set_v(max(self.get_v() - 1, 0))


    def check_if_line_free(self , points):
        procent_go = 90
        oposite, indexes = self.opposite_rl()
        list1 = indexes[0]
        list2 = indexes[1]
        rem_j = 1
        global_index = self.get_next_p().get_index()

        for i in range(len(self.get_overtake_track()[list2])):
            print(global_index, ' ', self.get_overtake_track()[list2][i].get_index())
            if(global_index == self.get_overtake_track()[list2][i].get_index()):
                great_index = i
                break

        giga_index = self.get_overtake_track()[list1][great_index].get_index()

        for j in range(0, self.get_vmax()):
            if(points[giga_index - j].get_taken()):
                procent_go = 20
                rem_j = j

        return procent_go, oposite, rem_j, giga_index, list1

    def change_line(self, points):
        split = self.get_current_street().split('-')
        if(split[1] == 'left' or split[1] == 'right'):
            procent_go, street, can_go, index, overtake_index = self.check_if_line_free(points)
            if(can_go):
                overtake = self.get_overtake_track()
                procent = randint(0,100)
                if(procent < procent_go):
                    curr_street = self.get_current_street()
                    track = self.get_track()
                    street_names = self.get_street_names()
                    print(curr_street)
                    print(street)


                    self.set_prev_p(points[index - 1])
                    self.set_curr_p(points[index])
                    self.set_next_p(points[index + 1])

                    print(str(self.get_curr_p()))
                    print(str(self.get_next_p()))

                    change_index = street_names.index(curr_street)
                    street_names[change_index] = street
                    self.set_street_names(street_names)

                    self.set_current_street(street)

                    for item in track:
                        if (item['name'] == curr_street):
                            item['name'] = street
                            for i in range(len(item['coordinates'])):
                                item['coordinates'][i] = overtake[overtake_index][i]
                            self.set_curr_street_l(item["coordinates"][len(item['coordinates']) - 1])
                            self.set_curr_street_p(item["coordinates"][0])
                            self.set_curr_street_c(item["coordinates"][1])
                            self.set_curr_street_n(item["coordinates"][2])
                            break

                    self.set_track_from_track(track)



    def opposite_rl(self):
        check = self.get_current_street()
        split = check.split('-')
        if(split[1] == 'left'):
            text = split[0] + '-' + 'right' + '-' + split[2]
            if (split[2] == 'ccw'):
                index_number = [0, 1]  # pierwszy to ten na który zmieniamy, a drugi to na którym byliśmy
            else:
                index_number = [2, 3]
        else:
            text = split[0] + '-' + 'left' + '-' + split[2]
            if (split[2] == 'ccw'):
                index_number = [1, 0]
            else:
                index_number = [3, 2]


        return text, index_number

    def check_if_taken(self, streets, points):
        data = self.get_data()
        points_to_check = []
        for road in data:
            if road['name'] in streets:

                if road['name'] == "westerplatte-right-cw" or road['name'] == "westerplatte-left-cw":
                    length = len(road['coordinates'])
                    for i in range(length-1-1, length-28, -1):
                        points_to_check.append(road['coordinates'][i])

                if road['name'] == "gertrudy-poczta-ccw":
                    length = len(road['coordinates'])
                    for i in range(length-1-1, length-23, -1):
                        points_to_check.append(road['coordinates'][i])

                else:
                    for pkt in road['coordinates']:
                        points_to_check.append(pkt)


                for pkt in points_to_check:
                    if pkt.get_taken():

                        if self.get_current_street() == "gertrudy-poczta-ccw":
                            points[376].set_taken(1)
                            break

                        if self.get_current_street() == "westerplatte-left-cw" or self.get_current_street() == "westerplatte-right-cw":
                            points[962].set_taken(1)
                            break

                    else:

                        if self.get_current_street() == "gertrudy-poczta-ccw":
                            if points[376].get_lights() == "green":
                                points[376].set_taken(0)
                            else:
                                pass

                        if self.get_current_street() == "westerplatte-left-cw" or self.get_current_street() == "westerplatte-right-cw":
                            if points[962].get_lights() == "green":
                                points[962].set_taken(0)
                            else:
                                pass



    def check_right_hand_rule(self, points):

        possible_ways = ["gertrudy-poczta-ccw","westerplatte-left-cw","westerplatte-right-cw"]
        #print(self.get_curr_p().get_index(), self.get_curr_street_l().get_index(),self.get_current_street())
        streets = []

        if self.get_curr_p().get_index() == self.get_curr_street_l().get_index()-1 and self.get_current_street() in possible_ways:
            index = self.get_street_names().index(self.get_current_street())

            if self.get_current_street() == "gertrudy-poczta-ccw":

                if self.get_street_names()[index + 1] == "gertrudy-sienna-skret":

                    tmp = ["westerplatte-sienna-skret", "westerplatte-right-cw", "westerplatte-left-cw" ]
                    streets = tmp

            elif self.get_current_street() == "westerplatte-left-cw" or self.get_current_street() == "westerplatte-right-cw":

                if self.get_street_names()[index + 1] == "westerplatte-staro-skret":
                    tmp = ["gertrudy-poczta-ccw", "gertrudy-staro-skret"]
                    streets = tmp


        self.check_if_taken(streets, points)





    def move(self, screen, points):



        self.get_street_points()

        self.check_right_hand_rule(points)

        self.check_points_in_front(points)

        self.change_point(screen, points)

        if(self.get_v_change() == 0):
            self.accel_random()
        else:
            self.set_v_change(0)







    def change_point(self, screen, points):



        # petla predkosci dla danego pojazdu
        for i in range(self.__v):

            track = self.get_track()

            pygame.draw.circle(screen, self.__color, self.get_curr_p().get_cords(), 3)
            pygame.draw.circle(screen, (255, 255, 255), self.get_prev_p().get_cords(), 3)

            # ustawianie czy zajety czy nie
            points[self.get_curr_p().get_index()].set_taken(1)
            points[self.get_prev_p().get_index()].set_taken(0)

            self.set_prev_p(self.get_curr_p())
            self.set_curr_p(self.get_next_p())

            changeLine = 0

            for dictionaries in track:
                if dictionaries['name'] == self.get_current_street():
                    for i in range(len(dictionaries['coordinates'])):
                        if(self.get_next_p().same(dictionaries['coordinates'][i])):
                            if(i != len(dictionaries['coordinates']) - 1):
                                self.set_next_p(dictionaries['coordinates'][i+1])

                            else:
                                changeLine = 1

                            break

                elif(changeLine == 1):
                    self.set_next_p(dictionaries['coordinates'][0])
                    self.set_current_street(dictionaries['name'])
                    break


            lastRoadList = self.get_track()[len(self.get_track())-1]['coordinates']
            if(self.get_curr_p().get_cords() == lastRoadList[len(lastRoadList)-1].get_cords()):
                 firstRoadDict = self.__track[0]
                 self.set_current_street(firstRoadDict['name'])
                 self.set_next_p(firstRoadDict['coordinates'][0])




