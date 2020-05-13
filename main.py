import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation


def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph




N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)

df = pd.read_csv('points.csv')
x = [ round(lon,7) for lon in df.lon ]
y = [ round(lat,7) for lat in df.lat ]

#img = plt.imread('./map.png')
fig, ax = plt.subplots(figsize=(7,9))
ax.scatter(x, y, zorder=1, alpha= 1, c='red', s=10)
ax.set_title('I obwodnica Krakowa')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
#ax.imshow(img,extent=BBox)
graph, = plt.plot([], [], 'o')

ani = FuncAnimation(fig, animate, frames=300, interval=200)
plt.show()




