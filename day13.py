# def take_input():
#     num = int(input("Enter a number: "))
#     return num

# def is_greatest():
#     a= take_input()
#     b= take_input()
#     c= take_input()
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# greatest = is_greatest()
# print(f"The greatest number among three number is {greatest} ")


# def multiply(*args):
#     m = 1
#     for item in args:
#         m = m * item
#     return m

# mul = multiply(4,5,6,7,8)
# print(f"Multiplication of given numbers is {mul}")

# def find_vowel(vow):
#     for letter in vow:
#         if letter in list('aeiou'):
#             return letter
 
# var = find_vowel('poornima')
# print(f"the first vowel is {var}")


# def find(name):
#     count_vowels = 0
#     count_consonant = 0 
#     for i in name:
#         if i in list('aeiou'):
#             count_vowels = count_vowels + 1 
#         else:
#             count_consonant = count_consonant + 1 
#     return count_vowels, count_consonant  

# print(find('umesh'))

# def greatest(*args):
#     max = 0
#     for item in args:
#         if item > max:
#             max = item
#     return max

# max = greatest(3,4,5,6)
# print(f'Greatest is {max}')

# def greatest(*args):
#     return max(args)
# max = greatest(3,4,5,6)
# print(f'Greatest is {max}')

#local variables: inside the function
salary = 50000
def inr_salary():
    global salary
    salary = salary + 5*salary/100 
    print(salary)
inr_salary()
print(salary)
