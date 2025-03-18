import numpy as np
import matplotlib.pyplot as plt

numbers=[-1,1]
x=0
y=0
direction=["x","y"]
pos_x=[0]
pos_y=[0]

for i in range(1000):
    pick_num=np.random.choice(numbers)
    pick_direct=np.random.choice(direction)
    if pick_direct=="x":
        x+=pick_num
    else:
        y+=pick_num
    pos_x.append(x)
    pos_y.append(y)
    
plt.plot(pos_x,pos_y)
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.scatter(0,0, color='green')
plt.scatter(pos_x[-1],pos_y[-1],color='red')
plt.show()