#python dictionaries

thisDictionary = {

    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1996
}

print(thisDictionary)

#referencing items in a dictionary

print(thisDictionary["brand"])
print(thisDictionary["model"])
print(thisDictionary["year"])

#anothe format

#print("using : get()")
value_return = thisDictionary.get("brand")
print(value_return)

