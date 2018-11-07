print("hello world!")

import numpy as np

p = 5
print("The radius of the circle is", p)

def circumference(r):
    """This function calculates the circumference of a circle"""
    return 2*np.pi*r

print("the circumference of the circle is", circumference(p))

def surface_area(r):
    """ what's up """
    return np.pi*r**2

print("The surface area of the circle is", surface_area(p))
