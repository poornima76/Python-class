# static and instance:
#instance (object level variable):
# variables whose value changes from object to object is called instance variable

# an instance with self attached to it is 
# class Person: # Pascal case
#     def __init__(self, first_name, last_name, age): 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
        


#static variables (class level variable):
# variables that do not change from object to object but from class to class is static variable.
# class NMB_Bank:
#     ceo_name = 'Dean' # if the value is given to the variable then it is static variable
#     ph_no = '9862575511'
#     def __init__(self, first_name, last_name, age): 
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         print(NMB_Bank.ceo_name)

# p = NMB_Bank('Pooh', 'Marasini', 120)
# print(p.first_name)
# print(NMB_Bank.ceo_name)

# for static variable we can use an object to call the static variable 
# However we should not use the object name eg: p.ceo_name so we always use class name


# instance static and class
# create a class named School with school name, ph_no, address , student first_name,last name and age
# Then create an object print all the variables within and outside the class
# 
class School:
    school_name = 'Paragon'
    school_address = 'Tilganga'
    ph_no = '01-4476762' 
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        print(School.school_name)
        print(School.school_address)
        print(School.ph_no)
        print(f_name)
        print(l_name)
        print(age)

s = School('Nima', 'Sherpa', 19)
print('*****************************')
print(School.school_name)
print(School.school_address)
print(School.ph_no)
print(s.f_name)
print(s.l_name)
print(s.age)

# use median when there is outliers present in the data
# central tendency:
# 1. Mean
# 2. Median
# 3. Mode
# Standard deviation is used as an improvement of variance
