#Dictionary
# a = {} 
# print(type(a)) type is dict because dictionaries are used very frequently and set are rarely used.
# marks = {'kitty':0, 'doggy':12}
# print(len(marks))
# print(marks.keys())
# marks['boi'] = 18 # if there is no key then creates a new key, if present overwrites the value of key. 

# keys should always be unique
# if key is duplicate then the duplicate replaces the key with the duplicate one:

# marks = {'kitty':0, 'doggy':12, 'kitty':5}
# print(marks)
# >>>{'kitty': 5, 'doggy': 12}
# for i in enumerate(marks):
#     print(marks.items())
#     print(marks.values()) 

# b = {'whale':9, 'mantaray':4}
# marks.update(b)
# print(marks)

# Nested dictionary:
info = {'name': 'umesh', 'age':28, 'address':{'city':'balaju', 'dis': 'ktm'}}
# print(info['address'])
# >>>{'city': 'balaju', 'dis': 'ktm'}

# print(info['address']['city'])
# >>>balaju
info.clear()
print(info)


#range 
# a = range(10)
# print(a)
# >>>range(0, 10)
# a = list(range(10))
# print(a)
# >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = list(range(2,10,2))
# print(a)
# >>>[2, 4, 6, 8]

# a = list(range(1,22,2))
# print(a)
# marks = {'u':50, 'r':52, 's':65, 'h':72}
# name = input("Enter the name: ")
# print(f"Hi {name}, your marks is: {marks[name]} ")
# Enter the name: h
# Hi h, your marks is: 72 

# data = {'pooh':21,'tigger':20,'piglet':27,'winslow':24 }
# name = input("Enter the name: ")
# print(f"Hi {name}, you will be {data[name]+5}")
# Enter the name: pooh
# Hi pooh, you will be 26

num = int(input("Enter the ending number: "))
print(list(range(0,num+1,2)))


