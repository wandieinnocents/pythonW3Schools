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
