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
	"""creates box with height n and length 2"""
	grid_ends()
	for i in range(n):
		grid_middle2()



def grid_ends_4():
    print '+ - - - - + - - - - + - - - - + - - - - +'

def grid_middle_4():
    for i in range(4):
        print '|','       ','|','       ','|','       ','|','       ','|'
    grid_ends_4() 

def grid_total_4(n):
    """creates box with height n and length 4"""
    grid_ends_4()
    for i in range(n):
        grid_middle_4()


if __name__ == "__main__":
    grid_total(2)
    grid_total_4(4)

