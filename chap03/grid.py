"""Solution to an exercise in Think Python.

Author: Marisa Mahlenkamp
"""

def grid_ends():
	print '+ - - - - + - - - - +'

def grid_middle2():
	for i in range(4):
		print '|','       ','|','       ','|'
	grid_ends() 

def grid_total(n):
	"""creates box with height n"""
	grid_ends()
	for i in range(n):
		grid_middle2()

grid_total(2)
