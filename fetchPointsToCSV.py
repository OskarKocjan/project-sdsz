import overpy
import csv

#   N
# W + E
#   S

api = overpy.Overpass()
#streets =['"Basztowa"', '"Juliana Dunajewskiego"', '"Podwale"', '"Floriana Straszewskiego"', '"Podzamcze"', '"Świętego Idziego"', '"Świętej Gertrudy"','"Westerplatte"','"Teatr Słowackiego"','"Stary Kleparz"', '"Teatr Bagatela"','"Filharmonia"','"Poczta Główna"']
streets =['"Juliana Dunajewskiego"','"Floriana Straszewskiego"']
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


