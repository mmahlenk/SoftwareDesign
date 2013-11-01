"""Chapter 11, Exercise 11.11 Solution
Author: Marisa Mahlenkamp
"""

from pronounce import read_dictionary


def create_word_list(filename):
    fin = open(filename)
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def create_word_dict(filename):
    fin = open(filename)
    d = {}
    for line in fin:
        word = line.strip()
        d[word] = word 
    return d  

t = create_word_list('words.txt')
d = create_word_dict('words.txt')
d2 = read_dictionary()


def homophone_list(t, d, d2):
    for word in t:
        first = word[1:]
        second = word[0] + word[2:]
        if is_homophone(word, first, second, d, d2):
            print word, first, second 


def is_homophone(word, first, second, d, d2):
    if first not in d or second not in d:
        return False
    if first not in d2 or second not in d2 or word not in d2:
        return False
    return d2[word] == d2[first] and d2[first] == d2[second]


if __name__ == '__main__':
    homophone_list(t, d, d2)