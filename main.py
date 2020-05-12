import numpy as np
import overpy
import matplotlib.pyplot as plt

#   N
# W + E
#   S

api = overpy.Overpass()
result = api.query("node(50.0526,19.9284,50.0676,19.9484);out;")
# for i in range(len(result.nodes)):
#     print(result.nodes[i])


#tekst

N = 50.0676
E = 19.9484
S = 50.0526
W = 19.9284

BBox = (W, E, S, N)

img = plt.imread('./map.png')
fig, ax = plt.subplots(figsize=(10,5))
ax.set_title('Obwodnica')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(img,extent=BBox)

plt.show()





