#functions :
#collection of statement that together performs a specific task

# def add():
#     print(2+3)

# add()
#positional arguments: order matters
# def name(fn, ln, age):
#     print(f"{fn} {ln}. Age is {age}")
# name(age=28, ln="Regmi", fn="Umesh") #keyword argument so the order of arguments does not matter

# def bank(fn, ln, age, balance=0): always write the default parameter at last
#     print(f"your balance is {balance}")

# bank(age=28, ln="Regmi", fn="Umesh") 
# bank(age=28, ln="Regmi", fn="Umesh",balance=100000) 
# >>>your balance is 0
# >>>your balance is 100000

# variable length 
# 1. variable length, positional argument: * gives multiple length: *args, stores in tuples
# 2. positional length, keyword argument: **kwargs,stores in dictionary 
# 
# def add(*args):
#     print(args)

# add(1,2)
# add(1,2,3)
# add(1,2,3,4)
# >>>(1, 2)
# >>>(1, 2, 3)
# >>>(1, 2, 3, 4) 

# def info(**kwargs):
#     print(kwargs)

# info(fn="Umesh", ln="Regmi", age=28)
# >>>{'fn': 'Umesh', 'ln': 'Regmi', 'age': 28}

# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
 
# add(2,3,4)
# >>>9 

# def sal(*args):
#     sum = 0
#     for salary in args:
#         sum = sum + salary
#     mean = sum/len(args)
#     print(f"Mean salary is {mean}")
#     if mean <= 10000:
#         print("You are poor")
#     else:
#         print("You are rich")

# sal(50000,40000,30000,60000,20000)
# >>>Mean salary is 40000.0
# >>>You are rich

#using function with return type, increases the reusability of code or functions

# def sal(*args):
#     sum = 0
#     for salary in args:
#         sum = sum + salary
#     mean = sum/len(args)
#     return mean

# total = sal(50000,40000,30000,60000,20000)
# print(f"Mean salary is {total}")
# if total <= 10000:
#      print("You are poor")
# else:
#     print("You are rich")

#if a function does not return anything, then it gives out None as ouptut.

#mean wala code remind

def sal(*args):
    sum = 0
    for salary in args:
        sum = sum + salary
    mean = sum/len(args)
    return mean

total = sal(50000,40000,30000,60000,20000)
print(f"Mean salary is {total}")
if total <= 10000:
    print("You are poor")
else:
    print("You are rich")