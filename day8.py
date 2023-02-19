# if condition:
#     statements

# if condition:
#     pass #this allows to pass the handler to next line and prevent error
# a = 1
# b = 0 if a == 1 else 10 if a == 0 else 15 if a > 1 else 10

# num = int(input("Enter the number: "))
# if (num%2) == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")

grade = {'ram':92, 'shyam':80, 'hari':62, 'sita':42}
name = input("Enter the name: ")
if name in grade and grade[name] >= 80:
    print(f"Congratulations! {name.title()} have passed with distinction.")
elif name in grade and grade[name] >= 60: 
    print(f"Congratulations! {name.title()} have passed with first divison.") 
elif name in grade and grade[name] >= 50:
    print(f"Congratulations! {name.title()} have passed with second divison.")  
else:
    print("Mom's flying chappal recieved.")
