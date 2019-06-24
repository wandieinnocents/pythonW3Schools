#pythonLists

#lists = collections are changable and ordered
#turple = collections which are ordered and unchangable
#set = unordered and un-indexed collection
#dictionary = unordered , changable and indexed

#lists
myList = ["wandie","innocent","matovu","ronald","julius"]
print(myList)

#accessing items in list
#second element array [1]
print(myList[1])

#change item in list
myList[0] = "kavuma"
print(myList)

#looping in list.
#prints all items in myList
for x in myList:
    print(x)

#check if items exists in list

if "kavuma" in myList:
    print("Item exists in the list")
else:
    print("item does not exist")

#determine items in a list
print(len(myList))

#append item to list
myList.append("sample_added_item")
print(myList)

#remove item from the list
myList.remove("sample_added_item")
print(myList)


#remove_item from list with index
#pop removes last item if not index is specified

myList.pop()
print(myList)

#use del to remove specified index
del myList[1]
print(myList)


#make a copy of list and store the values in anothe variable

copyList = myList.copy()
print(copyList)

print("original List")
lst = [10, 11, 12, 13, 14, 15]


print(lst.reverse())

print("Reversed List")
print(lst)





















