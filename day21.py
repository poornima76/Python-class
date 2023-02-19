#types of methods in class:
# 1. instance method
# 2. class method
# 3. object method
# class Person:
#     school_name = 'Paragon'
#     scool_address = 'Tilganga' 
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# method that access the instance variable is called an instance method
#     def get_first_name(self):# this is an instance method, we can access even the static variables
#         print(self.first_name)
# # class method are the methods that access the class level variable
#     @classmethod
#     def get_school_name(cls):  # it is a decorator
#         print(Person.school_name) # we cannot access an instance variable 
# # static method is the method that does not depend on class level or instance level variable
#     @staticmethod
#     def govt_holiday(): # it can be parameterized or parameter less
#         print('Dashain yayyyyy')
# p = Person('umesh','regmi')
# p.get_first_name()
# Person.get_school_name()
# Person.govt_holiday()



#create a class called Deerwalk schoolname, address, fname, lname, phno, one method with full name return
# 2nd method returns age
# 3rd return school name
# takes variable no of number, returns mean
# 4th prints holidays 

class Deerwalk:
    school_name = 'Deerwalk'
    school_addr = 'Sifal'
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
    def getfullname(self):
        return self.f_name + ' ' +  self.l_name
    def get_age(self):
        return self.age
    @classmethod
    def sch_name(cls):
        return Deerwalk.school_name
    def mean_num(*args):
        sum = 0
        for item in args:
            sum = sum + item
        sum = sum/len(args)
        print(f'Mean is: {sum}')
    @staticmethod
    def holiday():
        print('Dashain')
        print('Tihar')
        print('Loshar')


p = Deerwalk('Ram', 'Koju',13)
print(p.getfullname())
school = Deerwalk.sch_name()
print(school)
age = p.get_age()
print(age)

Deerwalk.mean_num(1,2,4,6,7,8,7)
Deerwalk.holiday()

