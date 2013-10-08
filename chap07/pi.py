"""Solution to Exercise 7.5 from Think Python. 

Author: Marisa Mahlenkamp
"""

from math import *

def estimate_pi():
    k = 0
    guess_pi = 0
    c = (2 * sqrt(2))/9801.0
    while abs(guess_pi - (1/pi)) > 1e-15:
        num = (factorial(4 * k))*(1103.0 + (26390.0 * k))
        denom = ((factorial(k))**4) * (396.0**(4 * k))
        guess_pi += c * (num / denom)
        k = k + 1
    return 1/guess_pi



print estimate_pi()
print pi