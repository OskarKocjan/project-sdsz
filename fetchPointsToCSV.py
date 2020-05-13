import overpy
import csv
from math import sin, cos, sqrt, atan2,radians


#   N
# W + E
#   S

def distanceOnEarth(x1,x2,y1,y2):
    # Earth radius in meters
    R = 6372800

    phi1, phi2 = radians(y1), radians(y2)
    dphi = radians(y2 - y1)
    dlambda = radians(x2 - x1)

    a = sin(dphi / 2) ** 2 + \
        cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2

    return 2 * R * atan2(sqrt(a), sqrt(1 - a))



api = overpy.Overpass()
streets =['"Basztowa"', '"Juliana Dunajewskiego"', '"Podwale"', '"Floriana Straszewskiego"', '"Podzamcze"', '"Świętego Idziego"', '"Świętej Gertrudy"','"Westerplatte"','"Teatr Słowackiego "']
row_list = [["id","street","lon","lat"]]



for street in streets:
    result = api.query('[out:json];way["name"='+street+'](50.0526,19.9284,50.0676,19.9484);out;')
    ways = result.ways

    for i in range(len(result.ways)):
        for j in range(len(result.ways[i].get_nodes(resolve_missing=True))):
            row_list.append([
                result.ways[i].get_nodes(resolve_missing=True)[j].id,
                street,
                result.ways[i].get_nodes(resolve_missing=True)[j].lon,
                result.ways[i].get_nodes(resolve_missing=True)[j].lat
            ])


with open('points.csv', 'w', newline='',encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)


