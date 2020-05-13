import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from fetchPointsFromCSV import makeDicFromCsv



# def animate(i):
#     graph.set_data(x[:i+1], y[:i+1])
#     return graph



N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)
streets =["Basztowa", "Juliana Dunajewskiego", "Podwale", "Floriana Straszewskiego", "Podzamcze", "Świętego Idziego", "Świętej Gertrudy","Westerplatte","Teatr Słowackiego"]

df = pd.read_csv('points.csv', encoding='utf8')

points = makeDicFromCsv(df)
x=[]
y=[]
for key,values in points.items():
    for value in values:
        x.append(value.x)
        y.append(value.y)

print(y)

fig, ax = plt.subplots(figsize=(7,9))
ax.scatter(y, x, zorder=1, alpha= 1, c='red', s=10)
ax.set_title('I obwodnica Krakowa')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])

#graph, = plt.plot([], [], 'o')
#ani = FuncAnimation(fig, animate, frames=200, interval=200)
plt.show()




