#looping in python

#printing values btn 1 and 6 with initial = 1
i = 1
while i<6:
    print(i)
    i = i+1

#using break statement..
print("Using the break statement to stop the loop")

a = 1
while a<6:
    print(a)
    if(a == 3):
        break
    a+=1

#using the continue statement
print("using the continue statment")

x = 1
while x<10:

    x = x+1
    if x == 5:
        continue
    print(x)

