import sys
import re
# import numpy as np
# import pandas as pd
# from sklearn import ...


def word_search(line):
    '''req:
        - fn takes in a str
        - find all words that satisfy conditions:
            1. contains letters, digits, or underscore
            2. starts w/ a capital letter A-Z
            3. has at least one digit 0-9
        - use regex
        - print list of words in order
    '''
    # initialize regex pattern to look out for
    # split str into list/arr
    # initialize found_word var to see if we return NONE or not
    # iterate through each word in arr
    # if word matches regex pattern, print word and set found_word to True
    # if found_word is False, print none
    words = line.split()
    pattern = r'^[A-Z][a-zA-Z0-9_]*[0-9][a-zA-Z0-9_]*$'
    found_word = False

    for word in words:
        if re.match(pattern, word):
            print(word)
            found_word = True

    if not found_word:
        print('NONE')


for line in sys.stdin:
    word_search(line)
