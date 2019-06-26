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
#prints values 0 - 8
print("range specified")
for p in range(2,9):
    print(p)

#increaseing sequence by certain number in range
print("Adding a sequence of like 2,3 ")
#param1 = first value param2 = last value param 3 = sequence
for x in range(2, 30, 3):
  print(x)

print("nested loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)