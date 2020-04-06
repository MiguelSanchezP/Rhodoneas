#Conjecture
#When k = a/b if a is odd and b even or viceversa a total of b times 2pi is requiered for closing the flower
#When k = a/b and both a and b are odd, a total of b/2 times 2pi is required for closing the flower 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import time

iterations=1000
final = False
fig = plt.figure()
ax = plt.axes(xlim=(-1,1), ylim=(-1,1))
rose, = ax.plot([],[],'r')

def init():
	rose.set_data([],[])
	return rose,


def animate(i):
	global final
	num = 5/8
	thetas = np.linspace(0, (2*np.pi)*8, iterations)
	x = np.cos(num*thetas)*np.cos(thetas)
	y = np.cos(num*thetas)*np.sin(thetas)
	rose.set_data(x[0:i], y[0:i])
	if i == 0 and final:
		final = False
		time.sleep(10)
	elif i==0 and not final:
		final = True
	return rose,


animation.FuncAnimation(fig, animate, init_func=init, frames=iterations, interval=10, blit=True)
plt.show()
