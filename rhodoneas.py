#import multiple libraries
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
import time

#CONSTANTS
#---------
iterations=1000 #quantity of "parts" that the flower is going to be divided by (the larger it becomes, the smoother it looks, the more time it takes)
fps = 100 #frames per second on the animation
make_animated = True #animation boolean
sleep_seconds = 10 #time the flower pauses after being plotted
color = 'red' #specify the color of the rose

#CODE
#----
first = True #boolean to check when to pause
fig = plt.figure() #initialize the figure
ax = plt.axes(xlim=(-1,1), ylim=(-1,1)) #set limits of the axes
rose, = ax.plot([],[],color) #initialize the rose, variable
user_input = input("Type in a number (in case of a fraction in its lowest terms [a/b]): ") #ask for k
coeffs = user_input.split("/") #split the user input by the fraction slash
num = float(coeffs[0]) #assign numerator value
if len(coeffs)>1: #check for a denominator
	den = float(coeffs[1]) #assign denominator value
else:
	den = 1 #if there's no denominator give a value of 1
k=num/den #assign the value to k
num_odd = False
den_odd = False
if num%2 != 0: #check if the numerator is odd
	num_odd = True #assign value True to boolean checking if the numerator is odd
if den%2 != 0: #check if the denominator is odd
	den_odd = True #assign value True to boolean checking if the denominator is odd

if num_odd and den_odd: #check if both numerator and denominator are odd
	angle = np.pi*den #assign the value of the angle to close
else:
	angle = 2*np.pi*den #assign the value of the angle to close
thetas = np.linspace(0, angle, iterations) #creation of all the values that are going to be computed
x = np.cos(k*thetas)*np.cos(thetas) #multiply by the cosinus to get all x coordinates
y = np.cos(k*thetas)*np.sin(thetas) #multiply by the sinus to get all y coordinates


def initialize(): #definition of initialize
	rose.set_data([],[]) #establish the array on the rose variable
	return rose,


def animate(i): #definition for the animation
	global first #modification of global variable final
	rose.set_data(x[0:i], y[0:i]) #add one more value of x and y to the rose array
	if i == 0 and not first: #check if the flower has been completed and it's not the first plotting
		time.sleep(sleep_seconds) #sleep for the specified time
	if first: #check if it is the very start of the plotting
		first=False; #know it's not the first time
	return rose,


if make_animated: #if animated
	animation.FuncAnimation(fig, animate, init_func=initialize, frames=iterations, interval=1000/fps, blit=True) #call the animation with all functions and user specifications
else:
	plt.plot(x,y, color) #plot the flower directly
plt.show() #show plots
