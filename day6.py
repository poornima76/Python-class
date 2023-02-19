#a = ('sun', 'mon', 'tues', 'thrus', 'fri', 'sat')
#print(a[0:8])
#print(id(a))
#b = (1)
#print(type(b))
# b = (1) uses the pemdas rule
#c = (1, ) #to signify a tuple with only one value


#Set:
#a = set()
#a = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 7 ,7 ,7 ,7}
#print(a)
#>>>{1, 2, 3, 4, 5, 6, 7}
a = {'hi', 'sam', 'how' ,'you'}
# a.add('poornima')
# print(a)
# >>>{'hi', 'poornima', 'how', 'you', 'sam'}

# a.remove('sam')
# print(a)
# >>>{'hi', 'you', 'how'}
# a.discard('alex')
# print(a)
# b = {1,2,3,4}
# c= {5,4,3,2,7}
# print(b.union(c))
# print(b.intersection(c))
# print(b.difference(c))

# type conversion between tuple list and set
li = list((1,2,3))
print(type(li))
print(li)

se = {1,2,3,4,5,5,6,4,4,3,3,6}
tup = tuple(se)
print(tup)

# if we use type conversion to convert list to set:
 
# listt = [1,2,3,4,5,5,5,6,7,7,7] #list
# bi = (1,2,3,4,5,6,6) #tuple
# print(set(listt))
# print(set(bi))
name = ('ram', 'shyam', 'gita','rita') 
li = list(name)
li.insert(1, 'sita')
print(tuple(li))