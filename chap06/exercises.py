"""Module that provides is_power.

Author of is_power: Marisa Mahlenkamp
"""

def is_power(a, b):
    """Returns true if a is a power of b (and implicitly if [a/b] is a power of b).
    
    a: positive integer
    b: positive integer

    returns: True or False
    """
    if a == 1:
        return True
    if a % b == 0:
        is_power(a/b, b)
        return True
    return False

print is_power(27, 3)
