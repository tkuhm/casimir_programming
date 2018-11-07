print("hello world!")


import numpy as np
import matplotlib
matplotlib.use("Agg") # this you need for new version of matplotlib to work
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()

ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
ax.set_aspect('equal')
ax.add_artist(bluecircle)

fig.savefig('bluecircle.png')
