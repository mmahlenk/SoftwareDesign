"""Chapter 4 Exercises
Author: Marisa Mahlenkamp
"""	

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
	for i in range(length):
		fd(t, 100)
		lt(t)

# square(bob, 4)

def polygon(t, length, n):
	for i in range(n):
		fd(t, length)/
		lt(t, 360.0/n)

# polygon(bob, 20, 15)

def circle(t, r):
	circumference = 2 * math.pi * r
	n = int(circumference / 3) + 1
	length = circumference / n
	polygon(t, length, n)

bob.delay = 0.003

circle(bob, 40)

def arc(t, r, angle):
	circum = (2 * math.pi * r) * (angle / 360.0)
	n = int(circum / 3) + 1
	arc_length = circum / float(n)
	arc_angle = angle / float(n)
	for i in range(n):
		fd(t, arc_length)
		lt(t, arc_angle)

arc(bob, 40, 180)	

wait_for_user()