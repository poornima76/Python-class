# class Person:
#     def __init__(self,fn, ln, a, addr):
#         self.f_name = fn
#         self.l_name = ln
#         self.age = a
#         self.address = addr

# p = Person('Carrie', 'Bradshaw', 35, 'Manhattan')
# a = Person('Samantha', 'Highland', 40, 'Manhattan')
# print(a.f_name)
# print(p.f_name)
# #creating an object:
# p  = Person()  #refernce variable is p and Person() is object
# # access object's attributes:
# print(p.f_name)
# #change field:
# p.f_name = 'Hari'
# #access property:
# print(p.f_name)


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

# >>>
# id of self : 4304182624
# id of p : 4304182624
# ********************************
# id of self: 4304182816
# id of a: 4304182816
# from this we can see that self is a pointer.
# self points to the current running object in the RAM
# it determines the size of object in RAM