#working with regular expressions

import re

word = "The rain in spain"
look_words = re.search("^The.*spain$", word)

if(look_words):
    print("Words are found man")
else:
    print("no words matching")