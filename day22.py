class Person:
    __school_name = 'Paragon'
    __scool_address = 'Tilganga' 
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def set_age(self,new_age):
        if new_age <0:
            print('Invalid age')
        else:
            self.__age = new_age
    def get_age(self):
        return self.__age

p = Person('Pooh', 'Marasini', 23)
p.set_age(-10)
print(p.get_age())

# Decorator:
# In python everything is an object
# decorator takes a function , extends the function and returns a function


# def calc():
#     def wrap():
#         pass
#     add()
# @calc # modify this, not accurate
# def add():
#     a = 0
#     for a in range(10000000):
#         i = i + a

# to find the processing time of add() without actually modifying the code of function
# then we use a decorator

# Four pillars of OOP:
# Encapsulation: grouping of properties, attributes of  a class within a class
# Abstraction
# Polymorphism
# Inheritance 
