#working with pip
import  camelcase

c = camelcase.CamelCase()

#word to change to camelcase
word = "we are not in our moods of coding please!"

#change to camelcase
print(c.hump(word))