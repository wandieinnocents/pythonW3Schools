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

#altering a value
thisDictionary["year"] = 10000
print(thisDictionary)

#printing keynames in dictionary

print("print keynames in dictionary in loop")
for x in thisDictionary:
    print(x)

#print values in dictionary
for x_values  in thisDictionary:
    print(thisDictionary[x_values])

#using values()
for x_vals in thisDictionary.values():
    print(x_vals)

#loop throuth items
for x,y in thisDictionary.items():
    print(x,y)




















