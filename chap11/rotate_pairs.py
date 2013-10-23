"""Chapter 11 Exercise 11.10 Solution
Author: Marisa Mahlenkamp
"""

def rotate_word(word, rotated):
    """Function that a string and returns the string with each letter
    rotated by the desired integer. 

    word: string
    rotated: integer 

    returns: string
    """

    new_word = ''
    for letter in word:
        new_ord = ord(letter) + rotated
        if new_ord > 122:            
            new_ord = (new_ord + 96) % 122
        new_char = chr(new_ord)
        new_word += new_char
    return new_word

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


t = make_word_dict()
# print t

def rotate_pair(d):
    """Function that iterates through a dictionary to find rotate pairs 
    of words and prints both in the pair.
    """
    for element in d:
        length = len(element)
        for i in range(1, 25):
            rotated = rotate_word(element, i)
            if rotated in d:
                print element, rotated, i


rotate_pair(t)
