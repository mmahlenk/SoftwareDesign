"""Chapter 5 Exercise 5.5
Author: Marisa Mahlenkamp
"""

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

def draw(t, length, n):
		if n == 0:
			return
		angle = 50
		fd(t, length*n)
		lt(t, angle)
		draw(t, length, n-1)
		rt(t, 2*angle)
		draw(t, length, n-1)
		lt(t, angle)
		bk(t, length*n)

draw(bob, 15, 3)

wait_for_user()