"""Chapter 5 Exercise: Module that makes a Dragon Curve
Author: Marisa Mahlenkamp
"""

from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()
print bob


	
def dragon_start(t, dist, n):
	"""Function that moves the turtle initially and then calls 
	dragon_x to start the recursion. 

	t: Turtle
	dist: positive number
	n: suggested to not exceed 10

	returns: Turtle movement in shape of a Dragon curve
	"""
	if n == 0:
		return 
	fd(t, dist)
	dragon_x(t, dist, n)


def dragon_x(t, dist, n):
	if n == 0: 
		return
	dragon_x(t, dist, n-1)
	rt(t)
	dragon_y(t, dist, n-1)
	fd(t, dist)


def dragon_y(t, dist, n):	
	if n == 0: 
		return
	fd(t, dist)
	dragon_x(t, dist, n-1)
	lt(t)
	dragon_y(t, dist, n-1)
	

bob.delay = .01


dragon_start(bob, 15.5, 10)


wait_for_user()