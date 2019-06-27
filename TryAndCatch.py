#exception handling in python

#error since no variable x is defined

try:
    print(x)
except:
    print("An exeption has occured!")


#name errror

try:
    print(x)
except NameError:
    print("vairable x is not defined")
except:
    print("something else went wrong")

#when no errors are raised

try:
    print("Hello errors")
except:
    print("something went wrong")
else:
    print("nothing went wrong")