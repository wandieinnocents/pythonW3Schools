#python lambda expressions
#lambda is used when an anonymous function is needed for a short period of time.

#sum of a number using lambda

x = lambda a:a+10
print(x(5))

#multiple arguments
y = lambda  o,p : o + p
print(y(4,5))

#summing up three arguments

w = lambda x,y,z : x+y+z
print(w(1,3,6))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))