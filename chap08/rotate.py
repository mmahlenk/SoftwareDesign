
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
        if new_ord > 122:            
            new_ord = (new_ord + 96) % 122
        new_char = chr(new_ord)
        new_word += new_char
    return new_word
    

print rotate_word('xyz', 10)


