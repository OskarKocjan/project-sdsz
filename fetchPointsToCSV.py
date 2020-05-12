import overpy
import csv


#   N
# W + E
#   S


api = overpy.Overpass()
streets =['"Basztowa"', '"Westerplatte"', '"Juliana Dunajewskiego"', '"Podwale"', '"Floriana Straszewskiego"', '"Podzamcze"', '"Świętej Gertrudy"']
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

with open('points.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)