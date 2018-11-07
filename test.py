print("hello world!")


import numpy as np
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

plt.Circle((0,0), 1, color='blue')
