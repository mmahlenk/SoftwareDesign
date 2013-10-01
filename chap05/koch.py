"""Chapter 5 Exercise 5.5
Author: Marisa Mahlenkamp
"""

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

def koch(t, length, n):
	angle = 60
	if n == 0:
		fd(t, length)
		return
	koch(t, length/3.0, n-1)
	lt(t, angle)
	koch(t, length/3.0, n-1)
	rt(t, 180-angle)
	koch(t, length/3.0, n-1)
	lt(t, angle)
	koch(t, length/3.0, n-1)

def snowflake(t, length, n):
	koch(t, length, n)
	rt(t, 120)
	koch(t, length, n)
	rt(t, 120)
	koch(t, length, n)
	
bob.delay = .002

# snowflake(bob, 180, 4)


koch(bob, 180, 4)
wait_for_user()