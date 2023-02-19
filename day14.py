# while True:
#     try:
#         a = int(input('Enter the first number: '))
#         b = int(input('Enter the second number: '))
#         if a > 100:
#             raise Exception('number must be less than 100!')
#         print(f'{a}/{b} is {a/b}')
#     except ZeroDivisionError:
#         print('division by zero')
#     except ValueError:
#         print('enter the number again in the right data type')
#     except Exception as e:
#         print(e)
#     else:
#         pass
#     finally:
#         print('Thanks for using this code.')

# try:
#     #risky code
# except:
#     #alternative code
# else:
#     #code to run when there is no error
# finally:
#     #code to run at last

# if database cannot be opened then we dont need to close it so,
# we need to put the closing of database code in else where code is kept that runs when 
# there is no error

    