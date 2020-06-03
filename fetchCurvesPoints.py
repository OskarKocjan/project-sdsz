import json
import os


def bubbleSort(arr,what,how):
    if what == 'x':
        p = 0
    if what == 'y':
        p = 1

    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if(how == 'asc'):
                if arr[j][p] > arr[j + 1][p]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if (how == 'desc'):
                if arr[j][p] < arr[j + 1][p]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

def convertGeoJsonToJson(file):
    #file = "../coords/intersections/kleparz.json"
    path = file.split("/")
    name = os.path.splitext(path[len(path)-1])[0]
    with open(file, 'r') as f:
            datastore = json.load(f)

            data = {}
            data['coordinates'] = []
            for item in datastore["features"]:
                if(item["geometry"]['type'] == "Point"):
                    data['coordinates'].append(item["geometry"]['coordinates'])


            bubbleSort(data['coordinates'], 'x', 'asc')



    with open('../coords/intersections/specified/'+name+'.json', 'w') as outfile:
        json.dump(data, outfile)

file = "../coords/intersections/basztowa-cw-basztowa-prosto.json"
convertGeoJsonToJson(file)