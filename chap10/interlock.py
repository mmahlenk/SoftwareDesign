"""Author: Marisa Mahlenkamp
Chapter 10 Solutions
"""

from inlist import *
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



def is_interlock(t, word):
    """Checks whether an interlocked word appears in sorted list.
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(t, evens) and in_bisect(t, odds)



sorted_t = make_word_list1()

def print_interlock(t):
    """Prints all words in sorted list that are made up of 2 interlocking words.
    t: list
    """
    for word in t:
        if is_interlock(t, word):
            print word, word[::2], word[1::2]

print_interlock(sorted_t)

