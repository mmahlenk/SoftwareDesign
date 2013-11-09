"""Chapter 14, Exercise 14.6 Solution "Secret Problem"

Author: Marisa Mahlenkamp
"""

import urllib
import string
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    """ This code was found at stackoverflow to strip the HTML from the text. 
    http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
    """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ' '.join(self.fed)

# print type(MLStripper)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def create_url():
    """Returns the url for the zipcode input by the user.

    returns: string
    """
    url = ['http://www.uszip.com/zip/']
    zipcode = raw_input('Enter zipcode:\n')
    url.append(zipcode)
    
    return ''.join(url)

# print create_url()
wellesley = create_url()


def zipcode_data(url):
    """Function that opens the zipcode url, strips it of HTML (using the
        strip_tags function) and then searches for the appropriate information
        and prints it. 

        url: string
    """
    zipcode_info = urllib.urlopen(url)
    t =[]
    for line in zipcode_info:
        text = strip_tags(line)
        if "zip code" in text:
            t.append(text)
        if "Total population" in text:
            line = text.strip()
            populationText = line.split(' H')[0].split(' p')[0]
    print t[0].split(' z')[0]
    print populationText


zipcode_data(wellesley)



