#working with python classes

class myClass:
    x = 5

print(myClass)

#use class to create objects

p1 = myClass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


name1 = Person("wandie",44)
person2 = Person("kavua",4)

print(name1.name)
print(name1.age)
print(person2.name)