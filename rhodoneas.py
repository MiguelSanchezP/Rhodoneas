import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import time

iterations=100000
fps = 100
final = False
fig = plt.figure()
ax = plt.axes(xlim=(-1,1), ylim=(-1,1))
rose, = ax.plot([],[],'r')
coeffs = input("Posa un numero (si és fracció, l'irreduible): ")
num = int(coeffs.split("/")[0])
if len(coeffs)>1:
	den = int(coeffs.split("/")[1])
else:
	den = 1
k = num/den
num_imparell = False
den_imparell = False
if num%2 != 0:
	num_imparell = True
elif den%2 != 0:
	den_imparell = True

if num_imparell and den_imparell:
	rounds = den/2
else:
	rounds = den
thetas = np.linspace(0, (2*np.pi)*rounds, iterations)
x = np.cos(k*thetas)*np.cos(thetas+np.pi/2)
y = np.cos(k*thetas)*np.sin(thetas+np.pi/2)


def init():
	rose.set_data([],[])
	return rose,


def animate(i):
	global final
	rose.set_data(x[0:i], y[0:i])
	if i == 0 and final:
		time.sleep(10)
	elif i == 0 and not final:
		final = True
	return rose,


animation.FuncAnimation(fig, animate, init_func=init, frames=iterations, interval=1000/fps, blit=True)
plt.show()
