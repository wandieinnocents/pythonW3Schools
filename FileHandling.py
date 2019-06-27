# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)
import os

#open file for reading

# f = open("file_open.txt")
#open
f = open("demo.txt","r")
#read
print(f.read())

#read specific char
chara = open("demo.txt","r")
print(chara.read(5))

#appending items to a File
append_data = open("demo.txt","a")
append_data.write("We are the men")
append_data.close()

print("Reading data from new appended file")
read_append = open("demo.txt","r")
print(read_append.read())

#creating a new file
f = open("myfile.txt", "x")

os.remove("myfile.txt")