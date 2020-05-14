from Point import Point
from math import sin, cos, sqrt, atan2,radians

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


