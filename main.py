import overpy
import matplotlib.pyplot as plt
import pandas as pd


N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)

df = pd.read_csv('points.csv')
x = [ round(lon,7) for lon in df.lon ]
y = [ round(lat,7) for lat in df.lat ]

#img = plt.imread('./map.png')
fig, ax = plt.subplots(figsize=(8,10))
ax.scatter(x, y, zorder=1, alpha= 0.2, c='red', s=10)
ax.set_title('I obwodnica Krakowa')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
#ax.imshow(img,extent=BBox)

plt.show()





