"""Author: Marisa Mahlenkamp - Chapter 10
Testing out the bisect module
"""

from bisect import *

def make_word_list1():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

sorted_t = make_word_list1()
    


# is_in_list(sorted_t, 'zymurgies')
