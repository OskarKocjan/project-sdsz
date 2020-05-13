from Point import Point

def makeDicFromCsv(df):
    points = {}
    for i in range(len(df)):
        points.update({df.street[i]:[]})

    for key, values in points.items():
        for i in range(len(df)):
            points[key].append(Point(df.lat[i], df.lon[i]))
    return points