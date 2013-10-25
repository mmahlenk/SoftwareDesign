"""Chapter 12, Exercise 12.4 Solution

Author: Marisa Mahlenkamp
"""

def make_dict():
    """Reads lines from a file and builds a dictionary where each 
    word is a key that maps to the same word.

    returns: dictionary
    """
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = word
    return d

d = make_dict()
# print d 

def make_word_children(word, d):
    """Function that creates a list of a word's 'children' that are in 
    the dictionary when removing one letter.

    returns: list
    """
    t = list(word)
    val = [] 
    if len(t)==1:
        val.append('')
    for i in range(len(word)):
        child = t[:]
        del child[i]
        child = ''.join(child)
        if child in d:
            val.append(child)
    return val

# print make_word_children('i', d)


def reducible(word, d):
    """Function that return True if a word can be reducible using words in the 
    dictionary. 

    returns: boolean
    """
    if word == '':
        return True
    else:
        t = make_word_children(word, d)
        for child in t:
            ans = reducible(child, d)
            return ans
    return False


print reducible('complecting', d)


def check_all_words(d):
    """Function that creates a list of all reducible words in the dictionary.

    returns: list
    """
    known = {}
    reducible_words = []
    for word in d:
        if word in known:
            reducible_words.append(word)
        if reducible(word, d):
            reducible_words.append(word)
            known[word] = word 
    return reducible_words 

t = check_all_words(d)

# print t

def sort_reducible_words(t):
    """Function that takes the list of all reducible words and sorts it by length.

    returns: list
    """
    words = []
    for word in t:
        words.append((len(word), word))
    words.sort(reverse=True)

    sorted_words = []
    for length, word in words:
        sorted_words.append(word)
    return sorted_words


print sort_reducible_words(t)

answer = sort_reducible_words(t)

print answer[0]
