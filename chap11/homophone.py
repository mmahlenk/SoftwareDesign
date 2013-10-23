"""Chapter 11, Exercise 11.11 Solution
Author: Marisa Mahlenkamp
"""

from pronounce import read_dictionary

def make_word_dict():
    """Reads lines from a file and builds a 
    dictionary where key and value are the same.

    returns: dictionary
    """
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = word
    return d


d = make_word_dict()
# print d

def is_homophone(d):
    for word in d:
        word1 = word[1:]
        word2 = word[0]+word[2:]
        if read_dictionary(word) == read_dictionary(word1) and read_dictionary(word1) == read_dictionary(word2):
            print word, word1, word2


is_homophone(d)



