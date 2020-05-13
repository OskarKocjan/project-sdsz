import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from  Point import Point
from fetchPointsFromCSV import makeDicFromCsv


def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph
#siema


N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)
streets =["Basztowa", "Juliana Dunajewskiego", "Podwale", "Floriana Straszewskiego", "Podzamcze", "Świętego Idziego", "Świętej Gertrudy","Westerplatte","Teatr Słowackiego "]

df = pd.read_csv('points.csv', encoding='utf8')

points = makeDicFromCsv(df)
print(points)


x = [ round(lon,7) for lon in df.lon ]
y = [ round(lat,7) for lat in df.lat ]






fig, ax = plt.subplots(figsize=(7,9))
ax.scatter(x, y, zorder=1, alpha= 1, c='red', s=10)
ax.set_title('I obwodnica Krakowa')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

graph, = plt.plot([], [], 'o')
ani = FuncAnimation(fig, animate, frames=200, interval=200)
plt.show()




