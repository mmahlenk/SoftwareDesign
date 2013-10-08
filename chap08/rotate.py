
"""Chapter 8, Exercise 8-12
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
        alpha = (new_ord + 96) % 122
        new_char = chr(alpha)
        new_word += new_char
    return new_word
    

print rotate_word('xyz', 3)


