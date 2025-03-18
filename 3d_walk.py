import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

numbers=[-1,1]
x=0
y=0
z=0
direction=["x","y","z"]
x_pos=[0]
y_pos=[0]
z_pos=[0]
for i in range(1000):
    pick_number=np.random.choice(numbers)
    pick_direction=np.random.choice(direction)
    if pick_direction == "x":
        x+=pick_number
    if pick_direction == "y":
        y+=pick_number
    else:
        z+=pick_number
    x_pos.append(x)
    y_pos.append(y)
    z_pos.append(z)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x_pos, y_pos, z_pos)
ax.scatter(0,0,0,color='green')
ax.scatter(x_pos[-1],y_pos[-1],z_pos[-1],color='red')
plt.show()