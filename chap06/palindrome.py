"""Module that provides is_palindrome.

Author of is_palindrome: Marisa Mahlenkamp
"""


def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returns true if word is a palindrome.

    word: string

    returns: True or False
    """ 
    if len(word) == 0 or len(word) == 1:
        return True
    if first(word) == last(word):
        rest = middle(word) 
        is_palindrome(rest)
        return True
    return False

print is_palindrome('hannah')




