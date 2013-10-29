"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Uses this code for solution to Chapter 13, Exercise 13.8
Markov Analysis
Author: Marisa Mahlenkamp
"""

import string
import random


def book_word_list(filename, skip_header=True):
    """Creates a list of all the words in the file.

    filename: string
    skip_header: boolean

    returns: list
    """
    t = []
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        # replace hyphens with spaces before splitting
        line = line.replace('-', ' ')
        
        for word in line.split():
            # remove punctuation and convert to lowercase
            # if desired, can remove 'string.punctuation' to keep punctuation in text
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            t.append(word)

    return t

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def markov_dict(t):
    """Creates a dictionary where key is suffix and maps to all possible prefixes. 

    t = list of words from text 

    returns: dictionary
    """
    d = {}
    i = 0 
    for i in range(len(t) - 2):
        if (t[i], t[i+1]) in d:
            d[(t[i], t[i+1])].append(t[i+2])
        else: 
            d[(t[i], t[i+1])] = [t[i+2]]
    return d 

def markov_text(start, length, d):
    """Function that generates a block of text based on markov dictionary.

    start: tuple of strings
    length: integer (determines length of text)
    d: dictionary

    returns: string
    """
    t = [start[0], start[1]] 
    
    for i in range(length):
        values = d[(t[-2], t[-1])]
        suffix = random.choice(values)
        t.append(suffix)


    return ' '.join(t)





words_list = book_word_list('emma.txt')
# print words_list[:500]
dictionary = markov_dict(words_list)
print markov_text(('the', 'other'), 100, dictionary)

