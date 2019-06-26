#working with the for loops
#used in iterationn of data in dictionary, turple, set

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#looping throuth a world

word = "banana"
for w in word:
    print(w)

#using the break statement

names = ["wandie","innocent","kavuma"]
for position in names:

    if(position == "innocent"):
        continue
    print(position)

print("range of 4")
#range of 4
for x in range(4):
    print(x)

print("range of 10")
#range of 10
for y in range(10):
    print(y)

#specifying start value in range
print("range specified")
for p in range(2,9):
    print(p)