"""Exercises from Chapter 9 of ThinkPython

Author: Marisa Mahlenkamp
"""

def triple_double():
    """Prints all words from a list that have consecutive double letters
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        triple_double_word(word)



def triple_double_word(word):
    """Tests if a word has three consecutive double letters and prints it if True
    """
    n = len(word)
    i = 0
    while i < (n - 1):
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            print word
            return True
        else:
            i += 1
    return False

triple_double()

# triple_double_word('bookkeeper')


def odom_is_palindrome():
    """Finds and prints all 6-digit numbers where the last 4 digits makes a palindrome.

    returns: integers
    """
    n = 100000
    l = 999999
    while n < l:
        s = str(n) # need to convert the integer to a string
        if s[2] == s[5] and s[3] == s[4]:
            print s
            n = int(s) # need to convert the string to an integer
            n += 1
        else:
            n = int(s)
            n += 1

# odom_is_palindrome()



