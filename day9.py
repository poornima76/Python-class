# loop
# grade = {'ram':92, 'shyam':80, 'hari':62, 'sita':42}
# while True:
#     name = input("Enter the name: ")
#     if grade[name] >=80:
#        print(f"Congratulations! {name.title()} have passed with distinction.") 
#     elif grade[name] >=60:
#         print(f"Congratulations! {name.title()} have passed with first divison.") 
#     elif grade[name] >= 50:
#         print(f"Congratulations! {name.title()} have passed with second divison.")  
#     else:
#         print("Mom's flying chappal recieved.")

#for loop

# num = (1,2,3,4,5,6,7,8)
# for item in num:
#     print(item)
# grade = {'ram':92, 'shyam':80, 'hari':62, 'sita':42}
# for item in grade:
#     print(item)
#>>> 
# ram
# shyam
# hari
# sita


# for item in grade:
#     print(grade[item])
# 92
# 80
# 62
# 42
#break 
# for item in [1,2,3,4,5,6,7,8,9,10]:
#     if
#  item == 5:
#         print('item found')
#         break
# print('Done')

#continue
# for item in [1,2,3,4,5,6,7,8]:
#     if item == 5:
#         continue
#         print('if condition')
#     else:
#         print(item)

# for item in range(10):
#     print(item, end='  ')
# >>>0  1  2  3  4  5  6  7  8  9 


# even = []
# odd = []
# for item in range(1,21):
#     if item%2 == 0:
#         even.append(item)  
#     else:
#         odd.append(item)
# print(even)
# print(odd)

while True:
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    if a > b:
        print(f'{a} is greater than {b}')
    else:
       print(f'{b} is greater than {a}') 
