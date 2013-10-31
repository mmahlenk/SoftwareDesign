"""Solution to an exercise in Think Python.

Author: Marisa Mahlenkamp
"""

def grid_ends(length):
	print '+ - - - - ' * length + '+'


def grid_middle(length):
	for i in range(4):
		print '|         ' * length + '|'
	grid_ends(length) 


def grid_total(n, length):
	"""creates box with height n and width length"""
	grid_ends(length)
	for i in range(n):
		grid_middle(length)



if __name__ == "__main__":
    grid_total(2, 2)
    grid_total(4, 4)

