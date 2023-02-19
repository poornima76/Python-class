# inheritance and polymorphism:

# inheritance:  the process of inheriting property and behavior from parent class
# it creates reusability

class Person:  #base class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def cal_sal(self):
        print('calculate salary')

class FullTimeEmployee(Person): #child class
    pass

class PartTimeEmployee(Person): #child class
    pass

p = PartTimeEmployee('umesh', 'regmi')
p.cal_sal()

# polymorphism:
# many forms is polymorphism 

class Person:  #base class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    # use this method to calculate salary on your respective class
    def cal_sal(self):
        pass

class FullTimeEmployee(Person): #child class
    def __init__(self, first_name, last_name, title):
        super().__init__(first_name, last_name)
        self.title = title  
    
    def cal_sal(self):
        print('full time class calculate salary')

class PartTimeEmployee(Person): #child class
    def __init__(self, first_name, last_name, hours):
        super().__init__(first_name, last_name)
        self.hours = hours  
     
    def cal_sal(self):
        print('part time class calculate salary')  

p = PartTimeEmployee('umesh', 'regmi', 'Developer')
p.cal_sal()


# every function is also an object.
# in a file a function with same name cannot be repeated twice so we cannot 
# implement function overloading to solve this problem we use *args and *kwargs