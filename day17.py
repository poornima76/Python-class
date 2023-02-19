# Advanced concepts:
# def is_even(p):
#     # even = []
#     even = [x for x in p if x%2 == 0]
#     # for i in p:
#     #     if i%2==0:
#     #         even.append(i)
#     return even

# li = [1,2,3,4,5,6]
# print(is_even(li))
# a = ['umesh', 'ram', 'shyam', 'rita', 'sita', 'alex', 'elisa']
# vowel = [x.title() for x in a if x[0].lower() in ['a','e','i','o','u']]
# print(vowel)
# names = ['Umesh', 'Alex', "Elisa"]

# a = [True if x%2 == 0 else False for x in range(10)]
# print(a)

# li = [1,2,3,4,5,6,7,8,9,10]
# squared = [x*x for x in li]
# print(squared)

#lambda function:
#functions with no names are called lambda function. 
#lambda input : output
# def squared(x):
#     return x**2

# lambda x : x**2
# lambda function is used to filter, map and reduce
# lambda x, y : x*y

# def is_even(n):
#     return n % 2 == 0
#filter(function, iterables)
#a = filter(is_even, [1,2,3,4,5,6])
# a = filter(lambda x : x%2 == 0, [1,2,3,4,5,6]) returns True or False and it stores in the variable a
# print(list(a))
# output is less than the input in filter
# map

#maps the number of vaules, output is equal to input
# a = map(lambda x : x**2, [1,2,3,4,5,6])
# print(list(a))
# b = map(lambda x : x%2==0, [1,2,3,4,5,6])
# print(list(b))

# c = filter(lambda x : x%2 == 0, [1,2,3,4,5,6])
# print(list(c))

# reduce
# reduces all the values to a single value
# from functools import reduce
# a = reduce(lambda x,y : x+y, [1,2,3,4,5,6])
# print(a)