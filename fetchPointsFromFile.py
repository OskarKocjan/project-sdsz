from Point import Point
from math import sin, cos, sqrt, atan2,radians,floor,ceil
from random import randrange
import os
import json

def convertGeoJsonToJson(file):
    #file = "../coords/intersections/kleparz.json"
    path = file.split("/")
    name = os.path.splitext(path[len(path)-1])[0]
    with open(file, 'r') as f:
            datastore = json.load(f)

            data = {}
            data['tracks'] = []
            for item in datastore["features"]:
                road = {}
                if(type(item["properties"]) is dict):
                    road['name'] = item["properties"]["name"]


                road['coordinates'] = item["geometry"]['coordinates']
                data['tracks'].append(road)


    with open('intersections/'+name+'.json', 'w') as outfile:
        json.dump(data, outfile)


def remove_duplicates(points):
    tmp1 = []
    for p in points:
        tmp1.append(p.getCords())

    tmp1 = list(dict.fromkeys(tmp1))

    tmp2 = []
    for p in tmp1:
        tmp2.append(Point(p[0],p[1]))

    return tmp2


def change_points_from_float_to_int(file):
    with open(file, 'r') as f:
        datastore = json.load(f)


    data = datastore["tracks"]

    points = []
    for track in data:
        for coords in track["coordinates"]:
            points.append(Point(coords[0], coords[1]))


    kx = 1
    ky = 1

    rx = abs(points[0].get_x() - points[1].get_x())
    ry = abs(points[0].get_y() - points[1].get_y())

    rx = 1 / rx

    ry = 1 / ry

    for i in range(len(points)):
        points[i].set_x(round(((points[i].get_x() * (kx + rx)) - 481100) * 10))
        points[i].set_y(round(((points[i].get_y() * (ky + ry)) - 1343150) * 10))



    xmin = points[0].get_x()
    ymin = points[0].get_y()


    for i in range(len(points)):
        if(points[i].get_x() < xmin):
            xmin = points[i].get_x()

        if (points[i].get_y() < ymin):
            ymin = points[i].get_y()


    for i in range(len(points)):
        points[i].set_x(points[i].get_x() - xmin)
        if (points[i].get_x() % 2 == 1):
            points[i].set_x(points[i].get_x() + 1)
        points[i].set_x(points[i].get_x() / 2)
        if (points[i].get_x() % 2 == 1):
            points[i].set_x(points[i].get_x() + 1)
        points[i].set_x(points[i].get_x() / 2)
        points[i].set_x(int(points[i].get_x()))


        points[i].set_y(points[i].get_y() - ymin)
        if (points[i].get_y() % 2 == 1):
            points[i].set_y(points[i].get_y() + 1)
        points[i].set_y(points[i].get_y() / 2)

        points[i].set_y(int(points[i].get_y()))

        rememberX = points[i].get_x()
        points[i].set_x(points[i].get_y() + 70)
        points[i].set_y(rememberX + 30)
        points[i].set_index(i)

    i = 0

    for track in data:
        for coords in track["coordinates"]:
            coords.clear()
            coords.append(points[i])
            i += 1

        track['coordinates'] = sum(track['coordinates'],[])

    return data, points





