#working with pip
import  camelcase

c = camelcase.CamelCase()

word = "we are not in our moods of coding please!"

#change to camelcase
print(c.hump(word))