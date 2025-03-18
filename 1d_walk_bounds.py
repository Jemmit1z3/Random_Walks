import numpy as np
import matplotlib.pyplot as plt

numbers = [-1, 1]  
position_1 = 0
positions_1 = []  
position_2 = 0
positions_2 = []
pick_1=[]
pick_2=[]

for i in range(1000):
    if position_1 == 0: 
        position_1 += 1
        positions_1.append(position_1)
        pick_1.append(1)
    elif position_1 > 0:
        random_pick_1 = np.random.choice(numbers) 
        position_1 += random_pick_1
        positions_1.append(position_1)
        pick_1.append(random_pick_1)
for i in range(1000):
    if position_2 != -10:
        random_pick_2 = np.random.choice(numbers)
        position_2 += random_pick_2
        positions_2.append(position_2)
    else:
        break
    pick_2.append(random_pick_2)

plt.subplot(3,1,1)
plt.plot(range(1,1001), positions_1) 
plt.plot(range(1,i+1), positions_2)
plt.axhline(y = 0, color = 'black', linestyle = '-') 
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("Random Walk")

plt.subplot(3,1,2)
plt.plot(range(1,1001), pick_1)
plt.xlabel("Step")
plt.ylabel("Number Picked")

plt.subplot(3,1,3)
plt.plot(range(1,i+1), pick_2)
plt.xlabel("Step")
plt.ylabel("Number Picked")
plt.show()
