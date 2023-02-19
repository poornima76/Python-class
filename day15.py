# file handling:
# to read and write files

# f = open('abc.txt', 'r')
# print(f.read(3))
# print(f.read(5))
# >>>Hel, the pointer is now at the 4th word
# lo Po , so the next read starts from the 4th word
# print(f.readlines())
# >>>['Hello Pooh\n', '\n', 'HunterXHunter']

# for line in f.readlines():
#     print(line)

# >>> Hello Pooh

#     HunterXHunter

# write to a file:
# f = open('abc.txt', 'w')
# f.write('Killua')

# append to a file:
# f = open('abc.txt', 'a')
# f.write('\n Gon')

# f = open('abc.txt', 'a')
# f.write("\nWe're bestfriends")
# f.close()
# f.read()
# >>>     f.read()
# >>>     ValueError: I/O operation on closed file.

#closing file automatically after the file is opened is context manager
# with open('abc.txt', 'r') as f:
#     print(f.read())

# f.read()
# output:
# Killua
# Gon
# We're bestfriends
# We're bestfriends
# Traceback (most recent call last):
#   File "/Users/poornimamarasini/Python/day15.py", line 38, in <module>
#     f.read()
# ValueError: I/O operation on closed 