#by default a variable is a public variable in class
# in python there is no true way of making a variable private so 
# _ before a name is taken as a private variable for eg: _age
# In Nepal we use __ to make a variable private


class Person:
    def __init__(self,fn, ln, a, addr):
        self.f_name = fn
        self.l_name = ln
        self.age = a
        self.address = addr
        print(id(self))

p = Person('Carrie', 'Bradshaw', 35, 'Manhattan')
print(id(p))
print('********************************')
a = Person('Samantha', 'Highland', 40, 'Manhattan')
print(id(a))
