# SET :-

# 1). set is a collection of well define object.
# 2). set is a unordered collection of data.
# 3). set is unchangeable, meaning you cannot change item of set once created.
# 4). set do not contain duplicate item.
# 5). set is mutable and iterable data type.
'''
s1 = {1, 2, 3, 4, 5, 6, 1}
#print(s1)

s2 = {"ashish", "mahesh", "satya", "rakesh"}
#print(s2)

s3 = {}      # invalid
#print(type(s3))

s4 = set()
print(type(s4))
'''

# add element into set :-
# 1). add() :-
# 2). update() :-

# 1). add() :-
# add() is used to add single element at a time.
'''
s = set()
course = "python"
loc = "bhiwandi"
duration = 6

s.add(course)
print(s)

s.add(loc)
print(s)

s.add(duration)
print(s)


# 2). update() :-
# update() is used to add multiple element using list or tuple.
# update() take 1 argument as a collection.

s = set()

col = ["Python", "Mysql", "Html/Css", "JavaScript"]
s.update(col)
print(s)

s.update("django", )
print(s)


# access element into set :-
s = {"mahesh", 22, "thane"}

# type casting :-
ls = list(s)
print(ls[1])

# iterable of set (for loop) :-
for i in s:
    print(i)


# Delete element into set :-
# 1). remove() :-
# 2). pop() :-

# 1). remove() :-
# syntax :- set_obj.remove(item)

s = {"mahesh", 22, "thane"}
s.remove("thane")
print(s)

# 2). pop() :-
# by default remove element from ending position
s.pop()
print(s)


# method in set :-
# 1). copy() :-
# 2). clear() :-

s = {1, 2, 3, 4}
c = s.copy()
print(c)

# 2). clear() :-
s.clear()
print(s)


# set comprehenson :-
# Table :-

s = {i*2 for i in range(1, 11)}
print(s)


# join set :-

# 1 - union() :- It return union of set as a new set.
set1 = {1, 2, 4, 6}
set2 = {8, 3, 1, 5}

set3 = set1.union(set2)
print(set3)

# 2 - intersection() :- It return intersection of two set as a new set.
set1 = {5, 2, 4, 6}
set2 = {8, 3, 1, 5}

set3 = set1.intersection(set2)
print(set3)


# 3 - symmetric_difference() :-

set1 = {5, 2, 4, 6}
set2 = {8, 3, 1, 5}

set3 = set1.symmetric_difference(set2)
print(set3)
'''









