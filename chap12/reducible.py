"""Chapter 12, Exercise 12.4 Solution

Author: Marisa Mahlenkamp
"""

def make_dict():
    """Reads lines from a file and builds a dictionary where each 
    word is a key that maps to the same word.

    returns: dictionary
    """
    d = dict()
    fin = open('short.txt')
    for line in fin:
        word = line.strip()
        d[word] = word
    return d

d = make_dict()


def make_word_children(word, d):
    """Function that creates a list of a word's 'children' words 
    when removing one letter.

    returns: list
    """
    t = list(word)
    val = [] 
    if len(t)==1:
        return ''
    for i in range(len(word)):
        child = t[:]
        del child[i]
        child = ''.join(child)
        if child in d:
            val.append(child)
    return val

# print make_word_children('keely')


def reducible(word, d):
    # if word == '':
    #     print "EMPTY"
    #     return True
    # else:
    #     t = make_word_children(word, d)
    #     for child in t:
    #         print child
    #         ans = reducible(child, d)
    #         print child, ans
    #         return ans
    # return False


    res = []
    for child in make_word_children(word, d):
        t = reducible(child, d)
        if t:
            res.append(child)
    return res

print reducible('sprite', d)


def check_all_words(d):
    for word in d:
        print reducible(word, d)


# check_all_words(d)

