#                               Dictionary

# Dictionaries are order collection of data or item.
# They are store multiple item in a single variable.
# Dictionary items are key-value pairs that are seperated by commas and enclosed within curly brackets {}.


#  syntax :- {key : value}
# e.g {1: "one", 2: "two"}

# Add element in Dictionary :-
# 1). process
# 2). update


# 1). process :-
'''
d = {}
name = "mahesh"
age = 22
loc = "thane"

d["Name"] = name
print(d)

d["Age"] = age
print(d)

d["Loc"] = loc
print(d)

# 2). update

d = {}
d.update({"name": "mahesh", "age": 22})
print(d)

# Access variable :-

d = {"name": ["mahesh", "rakesh"], "age": 22, "loc": "India"}

# get() :-
dt = d.get("loc")
print(dt)

# 2 - way :-

dt = d["name"]
print(dt)

# Example 2:-
dt = d["name"][1]
print(dt)

dt = d["loc"][3]
print(dt)


# Delete method in Dict :-
# 1). pop() :-
# 2). popitem() :-
# 3). del (keyword) :-

# 1). pop() :-
# syntax :- dict_obj[key]
d = {"name": ["mahesh", "rakesh"], "age": 22, "loc": "India"}

d.pop("loc")
print(d)

# 2). popitem() :-
d.popitem()
print(d)

# 3). del (keyword) :-
del d["name"][1]
print(d)


# Method in Dictionary :-
# 1). keys() :-
# 2). values() :-
# 3). copy() :-
# 4). clear() :-

d = {"name": ["mahesh", "rakesh"], "age": 22, "loc": "India"}

# 1). keys() :- It return all keys of dict object.
k = d.keys()
print(k)
print(type(k))

# 2). values() :-
v = d.values()
print(v)

# 3). copy() :-
c = d.copy()
print(c)

# 4). clear() :-
c1 = d.clear()
print(c1)
'''

# Method 1 :-
'''
key = [1, 2, 3, 4, 5, 6, 7]
value = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
d = {}

for k in range(len(key)):
    d[key[k]] = value[k]  # process

print(d)

# list comprehension :-
key = [1, 2, 3, 4, 5, 6, 7]
value = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
d = {key[k]: value[k] for k in range(len(key))}

print(d)

# Method 2 :-
key = [1, 2, 3, 4, 5, 6, 7]
value = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
d = {}

data = list(zip(key, value))
# print(data)
for k, v in data:
    d[k] = v

print(d)

# 2 - way :-
key = [1, 2, 3, 4, 5, 6, 7]
value = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
d = {k: v for k, v in list(zip(key, value))}

print(d)
'''
