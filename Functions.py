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

#returning values
def retValues(number):
    return 5*number

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

    #returning values on number input
    print("returning values on number usage")

    print(retValues(7))




#block of class main
if __name__ == '__main__':main()
