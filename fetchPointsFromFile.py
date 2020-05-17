from Point import Point
from math import sin, cos, sqrt, atan2,radians
import json


def makeDicFromCsv(df):
    points = {}
    for i in range(len(df)):
        points.update({df.street[i]:[]})

    for key, values in points.items():
        for i in range(len(df)):
            points[key].append(Point(round(df.lat[i],7), round(df.lon[i],7)))
    return points

def distance(x1, y1, x2, y2):
        # Earth radius in meters
        R = 6372800

        phi1, phi2 = radians(y1), radians(y2)
        dphi = radians(y2 - y1)
        dlambda = radians(x2 - x1)

        a = sin(dphi / 2) ** 2 + \
            cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2

        return 2 * R * atan2(sqrt(a), sqrt(1 - a))

def ChangePointsFromFloatToInt(file):
    with open(file, 'r') as f:
        datastore = json.load(f)

    data = datastore["tracks"]

    points = []
    for track in data:
        for coords in track["coordinates"]:
            points.append(Point(coords[0], coords[1]))

    x = [point.getX() for point in points]
    y = [point.getY() for point in points]

    kx = 176 / x[0]
    ky = 363 / y[0]

    rx = abs(x[0] - x[1])
    ry = abs(y[0] - y[1])

    rx = 1 / rx

    ry = 1 / ry

    for i in range(len(x)):
        x[i] = round(((x[i] * (kx + rx)) - 481100) * 10)

    for i in range(len(y)):
        y[i] = round(((y[i] * (ky + ry)) - 1343150) * 10)

    xmin = min(x)
    ymin = min(y)

    for i in range(len(x)):
        x[i] = x[i] - xmin
        if (x[i] % 2 == 1):
            x[i] += 1
        x[i] = x[i] / 2
        if (x[i] % 2 == 1):
            x[i] += 1
        x[i] = x[i] / 2
        x[i] = int(x[i])

    for i in range(len(y)):
        y[i] = y[i] - ymin
        if (y[i] % 2 == 1):
            y[i] += 1
        y[i] = y[i] / 2
        y[i] = int(y[i])

    return x, y