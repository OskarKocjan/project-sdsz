from Point import Point
from math import sin, cos, sqrt, atan2,radians
import os
import json


def distance(x1, y1, x2, y2):
        # Earth radius in meters
        R = 6372800

        phi1, phi2 = radians(y1), radians(y2)
        dphi = radians(y2 - y1)
        dlambda = radians(x2 - x1)

        a = sin(dphi / 2) ** 2 + \
            cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2

        return 2 * R * atan2(sqrt(a), sqrt(1 - a))


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


def ChangePointsFromFloatToInt(file):
    with open(file, 'r') as f:
        datastore = json.load(f)


    data = datastore["tracks"]

    points = []
    for track in data:
        for coords in track["coordinates"]:
            points.append(Point(coords[0], coords[1]))


    kx = 1
    ky = 1

    rx = abs(points[0].getX() - points[1].getX())
    ry = abs(points[0].getY() - points[1].getY())

    rx = 1 / rx

    ry = 1 / ry

    for i in range(len(points)):
        points[i].setX(round(((points[i].getX() * (kx + rx)) - 481100) * 10))
        points[i].setY(round(((points[i].getY() * (ky + ry)) - 1343150) * 10))



    xmin = points[0].getX()
    ymin = points[0].getY()


    for i in range(len(points)):
        if(points[i].getX() < xmin):
            xmin = points[i].getX()

        if (points[i].getY() < ymin):
            ymin = points[i].getY()


    for i in range(len(points)):
        points[i].setX(points[i].getX() - xmin)
        if (points[i].getX() % 2 == 1):
            points[i].setX(points[i].getX() + 1)
        points[i].setX(points[i].getX() / 2)
        if (points[i].getX() % 2 == 1):
            points[i].setX(points[i].getX() + 1)
        points[i].setX(points[i].getX() / 2)
        points[i].setX(int(points[i].getX()))


        points[i].setY(points[i].getY() - ymin)
        if (points[i].getY() % 2 == 1):
            points[i].setY(points[i].getY() + 1)
        points[i].setY(points[i].getY() / 2)

        points[i].setY(int(points[i].getY()))

        rememberX = points[i].getX()
        points[i].setX(points[i].getY() + 70)
        points[i].setY(rememberX + 30)

    i = 0

    for track in data:
        for coords in track["coordinates"]:
            coords.clear()
            coords.append(Point(points[i].getX(), points[i].getY()))
            i += 1

        track['coordinates'] = sum(track['coordinates'],[])



    return data, points