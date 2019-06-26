#conditional statements

a = 20
b = 300
if(a>b):
    print("A is greater than B")
elif(a < b):
    print("A is less that B")
else:
    print("invalid")

print("A") if a > b else print("=") if a == b else print("B")