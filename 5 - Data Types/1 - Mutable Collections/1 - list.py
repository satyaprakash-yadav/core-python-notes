
# if 'a' in ('a', 'b' ,'aa'):
#     a = 4
#     print(a)
# else:
#     print(a)
# # print(a)

# import re

# x = '12341234             1234  1234'
# prn = '\d(3) \d(3) \d(3)'
# x1 = re.findall(prn, x)
# print(x1)


#                                                   LIST
'''
ls = []

print(type(ls))

print(len(ls))


# Add element into the list :-

# 1). append() :-
# append() used to add element into the list from the ending position.
# append() take one argument append(data).

# syntax :- list_obj.append(data)

ls = []

name = 'mahesh'
age = 22
city = 'thane'

ls.append(name)
print(ls)

ls.append(age)
print(ls)

ls.append(city)
print(ls)

# 2). insert() :-
# insert() used to add element into the list from a specific position
# insert() take two argument insert(position , data)

# syntax :- list_obj.insert(position, data)

ls = ['mahesh', 22, 'thane']
course = 'python'

ls.insert(0, course)
print(ls)

# 3). extend() :-
# extend() used to add multiple element into the from the ending position. 
# extend() take one argument as a extend(collection).

# syntax :- list_obj.extend(collection)

ls = ['mahesh', 22, 'thane']

lang = ['javascript', 'sql', 'html/css', 'reactjs']

ls.extend(lang)
print(ls)

# Delete element from the list :-
# 1). remove()
# remove() used to delete element from the list by using element name.
# remove() take one argument as a remove.(data)

# syntax :- list_obj.remove(data)
ls = ['html', 'python', 'sql', 'java']

ls.remove('java')
print(ls)

# 2). pop() 
# pop() used to delete element from the list by using data position
# pop() take one argument as pop(position).
# if pop() argument is empty then it will be remove from the ending position.

ls = ['mahesh', 'bscit', 'thane']

ls.pop(1)
print(ls)

ls.pop()
print(ls)

# 3). del keyword
# It is used to delete any object exists in python.

# Syntax :- del list_obj[optional]

ls = [2, 3, 4, 6]

del ls[0]

print(ls)

# List Method :-
# 1). copy() :-
# copy() used to copy the list obj.

ls = [2, 3, 4, 5, 6, 7]

ls1 = ls.copy()
print(ls1)

# 2). index()
#  index() used to return the index no. of list element.

ls = [2, 3, 4, 5, 6, 7]

ls1 = ls.index(7)
print(ls1)

# 3). count()
# count() used to count the duplicate element of the list. 

ls = ['a', 'n', 'e', 'a', 'z', 'e']

ls1 = ls.count('a')
print(ls1)

ls1 = ls.count('n')
print(ls1)

# 4). clear()
ls = [1, 2, 3, 4, 5, 6]

ls1 = ls.clear()
print(ls1)

# zip & unzip :-

s1 = ['Ashish', 22, 'thane']
s2 = ['rahul', 23, 'bhiwandi']
s3 = ['swapnil', 26, 'kalyan']

all_s = list(zip(s1, s2, s3))
print(all_s)

ls = [('Ashish', 'rahul', 'swapnil'), (22, 23, 26),
      ('thane', 'bhiwandi', 'kalyan')]

# cols :-
print(len(ls))

# row :-
print(len(ls[0]))

# a, b, c = zip(*ls)
# print(a)
# print(b)
# print(c)
'''

# list comprehsion :-
#  1 - way or normal way:-
'''
ls = [2, 3, 4, 5, 6]
ls1 = []

for i in ls:
    ls1.append(i ** 3) # exponential

print(ls1)

# list comprehsion :-
ls = [2, 3, 4, 5, 6]
ls1 = [i ** 3 for i in ls]

print(ls1)

# 1 - way :-
ls = [2, 3, 4, 5, 6]
even = []
odd = []

for i in ls:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

# List comprehsion :-

ls = [2, 3, 4, 5, 6]
even = [i for i in ls if i % 2 == 0]
odd = [i for i in ls if i % 2 != 0]

print(even)
print(odd)
'''
