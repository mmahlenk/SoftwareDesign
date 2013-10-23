"""Chapter 12, Exercise 12.4 Solution

Author: Marisa Mahlenkamp
"""

def make_anagram_dict():
    """Reads lines from a file and builds a 
    dictionary where key is the sorted list of letters 
    and it maps to list of anagrams.

    returns: dictionary
    """
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = list(word)
        t.sort()
        sort_letters = ''.join(t)
        if sort_letters not in d:
            d[sort_letters] = [word]
        else:
            d[sort_letters].append(word)
    return d

d = make_anagram_dict()

def sort_anagram_dict(d):
    """Takes the dictionary of anagrams and sorts it by descending order
    into a list.

    returns: list
    """
    t = []
    for word in d:
        an_length = len(d[word])
        if an_length > 1:
            t.append((an_length, d[word]))
    t.sort(reverse=True)
    return t

print sort_anagram_dict(d)

def bingo(d):
    """Function that only returns a list of anagrams that has at least 
    8 characters.

    returns: list
    """
    t = []
    for word in d:
        if len(word) == 8:
            an_length = len(d[word])
            if an_length > 1:
                t.append((an_length, d[word]))
    t.sort(reverse=True)
    return t

answer = bingo(d)

# print answer[0]

