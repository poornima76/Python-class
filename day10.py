grade = {'umesh': 50, 'ram': 25, 'shyam': 99, 'rita':66}
while True:
    name = input("Enter your name: ")
    if name.lower() in grade:
        if grade[name]>= 80:
            print(f"Hi {name.title()} your grade is {grade[name.lower()]} and have passed with distinction.")
        elif grade[name] >=60:
            print(f"Congratulations! {name.title()} have passed with first divison.") 
        elif grade[name] >= 50:
            print(f"Congratulations! {name.title()} have passed with second divison.") 
    else:
        print(f"{name.title()} not found")


