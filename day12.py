
# def sum(*args):
#     add = 0
#     for i in args:
#         add = add + i
#     return add

# def salary(*args):
#     total_sum =sum(*args)
#     mean = total_sum/len(args)
#     return mean

# print(salary(10000,50000,60000,40000))

# def identify(*args):
#     even_no = []
#     odd_no = []
#     for i in args:
#         if i%2 == 0:
#             return even_no
#         else:
#             return odd_no 

# def sum(*args):
#     add = 0
#     for item in args:
#         sum = sum + item
#     return sum

# def mean_salary(*args):
#     even_no = 
#     addition = sum(*args)



# def identify(num):
#     # if num % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return num % 2 == 0

# while True:
#     number = int(input("Enter the number: "))
#     print(identify(number))


# def ph_no(name):
#     n = input("Enter name: ")
#     if n in name:
#         return name[n]
#     else:
#         return 'not found'

# man = {'ram':9865426284,'shyam':9865420984, 'sita':9806426264, 'gita':9862026284, 'ramesh':9865426200}
# print(ph_no(man))


# def reverse(sentence):
#     return sentence[::-1] 
    
# sentence = input("Enter a string: ")
# print(reverse(sentence))


def palindrome(s):
    return s[::-1] == s
s = input("Enter a string: ")
print(palindrome(s))


# return as a stop or break
# local and global variable
# tuple unpacking