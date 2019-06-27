#working with regular expressions

import re

word = "The rain in spain"
look_words = re.search("^The.*spain$", word)

if(look_words):
    print("Words are found man")
else:
    print("no words matching")


#working with findall function
#returns a list containing all matches

other_word = "The rain is in Spain an aisha"
match_word = re.findall("ai",other_word)
print(match_word)

#searching
search_it = "The man in the hood"
find = re.search("mand",search_it)

if(find):
    print("word is found")
else:
    print("word is not found")