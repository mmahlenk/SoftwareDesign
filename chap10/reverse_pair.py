"""Author: Marisa Mahlenkamp
Solution to Chapter 10 Exercise 10-13
"""

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
# print sorted_t

def is_reverse_pair(t):
    """Takes sorted list and prints all words that are reverse pairs.

    returns: strings
    """
    for element in t:
        new = element[::-1]
        if new in t and new != element:
            print new + ' ' + new[::-1]



is_reverse_pair(sorted_t)
