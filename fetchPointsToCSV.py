import overpy
import csv
import numpy as np
from math import sin, cos, sqrt, atan2,radians


#   N
# W + E
#   S

def distanceOnEarth(x1,x2,y1,y2):
    R = 6372800  # Earth radius in meters


    phi1, phi2 = radians(y1), radians(y2)
    dphi = radians(y2 - y1)
    dlambda = radians(x2 - x1)

    a = sin(dphi / 2) ** 2 + \
        cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2

    return 2 * R * atan2(sqrt(a), sqrt(1 - a))



api = overpy.Overpass()
streets =['"Basztowa"', '"Juliana Dunajewskiego"', '"Podwale"', '"Floriana Straszewskiego"', '"Podzamcze"', '"Świętego Idziego"', '"Świętej Gertrudy"','"Westerplatte"','"Teatr Słowackiego "']
row_list = [["id","lon","lat"]]



for street in streets:
    result = api.query('[out:json];way["name"='+street+'](50.0526,19.9284,50.0676,19.9484);out;')
    ways = result.ways

    for i in range(len(result.ways)):
        for j in range(len(result.ways[i].get_nodes(resolve_missing=True))):
            row_list.append([
                result.ways[i].get_nodes(resolve_missing=True)[j].id,
                result.ways[i].get_nodes(resolve_missing=True)[j].lon,
                result.ways[i].get_nodes(resolve_missing=True)[j].lat
            ])



for i in range(2, len(row_list)):
    lon1 = row_list[i][1]
    lat1 = row_list[i][2]
    lon2 = row_list[i-1][1]
    lat2 = row_list[i-1][2]
    print(str(lon2)+ " "+str(lat2)+ " "+ str(distanceOnEarth(lon1,lon2,lat1,lat2)))





with open('points.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

