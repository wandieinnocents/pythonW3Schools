#functions in python

#writing the function
def func():
    print("This is a function ")

#using two parameters
def callNames(fname,lname):
    print(fname + lname + " Innocent")

#using default values
def defValues(id = "student"):
    print("Student identity is : " + id)

#writing a looping function
def loopingValues(values):
    for x in values:
        print(x)

#function main declaration
def main():
    #calling a function
    func()
    callNames("wandie"," opio")
    print("using default function values")
    defValues("admin")


    defValues()

    #looping values
    print("looping values")
    fruits = ["mangoes","oranges","pineapples"]
    print(fruits)

    names = ["wandie","innocent","kavuma"]
    print(names)





#block of class main
if __name__ == '__main__':main()
