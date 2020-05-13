from Point import Point

def makeDicFromCsv(df):
    points = {}
    for i in range(len(df)):
        points.update({df.street[i]:[]})

    for key, values in points.items():
        for i in range(len(df)):
            points[key].append(Point(round(df.lat[i],7), round(df.lon[i],7)))
    return points


