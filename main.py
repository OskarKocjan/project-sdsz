import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation
from fetchPointsFromFile import makeDicFromCsv,distance
from Point import Point
import json

with open("roads.json", 'r') as f:
    datastore = json.load(f)

data = datastore["tracks"]
# data = datastore["tracks"][0]["coordinates"]
# data1 = datastore["tracks"][1]["coordinates"]
points = []
for track in data:
    for coords in track["coordinates"]:
        points.append(Point(coords[0],coords[1]))
# points = [Point(el[0],el[1]) for el in data]
x = [point.getX() for point in points]
y = [point.getY() for point in points]





# def animate(i):
#     graph.set_data( x[:i+1],y[:i+1])
#     return graph

def sortPoints(dict):
    for key in dict:
        for i in range(len(dict[key])-1):
            for j in range(len(dict[key])-1-i):
                if(dict[key][j].x < dict[key][j+1].x):
                    dict[key][j], dict[key][j+1] = dict[key][j+1], dict[key][j]

    return dict



N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)
streets =["Basztowa", "Juliana Dunajewskiego", "Podwale", "Floriana Straszewskiego", "Podzamcze", "Świętego Idziego", "Świętej Gertrudy","Westerplatte","Teatr Słowackiego"]

df = pd.read_csv('points.csv', encoding='utf8')

#points = makeDicFromCsv(df)

# x = []
# y = []




# for p in points['"Juliana Dunajewskiego"']:
#     print(p.x, p.y)

# a = [2,4,10,12]
# for i in range(1,len(a)):
#     print(i)
#     if(a[i]-a[i-1]>2):
#         print(i,len(a))
#         a.insert(i,a[i-1]+1)



# for key,values in points.items():
#     for value in values:
#         x.append(value.y)
#         y.append(value.x)
#
# for i in range(1,len(x)):
#     if(distance(x[i-1],y[i-1],x[i],y[i])>10):
#         print(i,x[i-1],y[i-1],x[i],y[i])
# print(len(x))





fig, ax = plt.subplots(figsize=(7,9))

ax.scatter(x,y, zorder=1, alpha= 1, c='red', s=0.5)


ax.set_title('I obwodnica Krakowa')
#ax.set_xlim(BBox[0],BBox[1])
#ax.set_ylim(BBox[2],BBox[3])


#graph, = plt.plot([], [], 'o')
#ani = FuncAnimation(fig, animate, frames=1500, interval=30)

plt.show()




