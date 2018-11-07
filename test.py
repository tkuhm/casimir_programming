print("hello world!")


import numpy as np
import matplotlib
matplotlib.use("Agg") # this you need for new version of matplotlib to work
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


p = 5
print("The radius of the circle is", p)

def circumference(r):
    """This function calculates the circumference of a circle"""
    return 2*np.pi*r

print("the circumference of the circle is", circumference(p))

def surface_area(r):
    """This function calculates the surface area of a circle"""
    return np.pi*r**2

print("The surface area of the circle is", surface_area(p))

bluecircle = plt.Circle((0,0), 1, color='blue')
redcircle = plt.Circle((1,1), 1, color='red')
yellowcircle = plt.Circle((-1,-1), 1, color='yellow')
greencircle = plt.Circle((-1,1), 1, color='green')
pinkcircle = plt.Circle((1,-1), 1, color='pink')

fig, ax = plt.subplots()

ax.set_xlim((-2, 2)) # this makes the circle centered
ax.set_ylim((-2, 2))

ax.set_aspect('equal') #this makes the circle round
ax.add_artist(bluecircle) #this stackoverflow told me to do..
ax.add_artist(redcircle)
ax.add_artist(yellowcircle)
ax.add_artist(greencircle)
ax.add_artist(pinkcircle)


#plt.xlabel(r'nice axis', size=15)
#plt.ylabel(r'another size thing', size=15)
#plt.title('Many beautiful circles', size=20)


fig.savefig('circles.png')
