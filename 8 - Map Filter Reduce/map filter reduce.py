#                           Map, Filter and Reduce

# Map() :-
# 1). Map function is a built in function.
# 2). It behaves like iterator which iterate each and every element of list a form operation as per given method or function.
# 3). It Takes 2 arguments 1st args function and 2nd args iterable data and return map object.
'''
ls = [2, 3, 4, 5, 6]

def test(n):
    return n ** 3

x = map(test, ls)
print(x)

for i in x:
    print(i)

# Example 2 :-
# Do with lambda function :-

ls = [2, 3, 4, 5, 6]

test = lambda n : n ** 3

x = map(test, ls)
print(list(x))
'''

# Filter() :-
# 1). Filter function is a built in function.
# 2). In Python it allow us to iterate a iterable data and also remove unsatisfied element from the iterable if it is supported.
# 3). It takes 2 arguments 1st args function and 2nd args iterable data and return filter object.
'''
# Remove odd number from the list
ls = [2, 3, 4, 5, 6, 7, 8]

def test(n):
    if n % 2 == 0:
        return n

x = filter(test, ls)
print(list(x))

# Remove negative number from the list using lambda function.

ls = [-1, -4, -5, 0, 1, 6, 8, 7]

test = lambda n : n if n > 0 else None

x = filter(test, ls)
print(list(x))
'''

# Reduce() :-
# 1). Reduce function used to impliment mathematical technique such as folding and reduction.
# 2). It is used to reduce whole data in a single value.
# 3). Python does not supperted reduce function that's why we use library or module functools.
# 4). It takes 2 arguments 1st function and 2nd iterable data and return value.

import functools
'''
# Example :-
ls = [2, 3, 4, 5, 6, 7, 8] 

def red(a, b):
    return a + b

x = functools.reduce(red, ls)
print(x)


# Example 2 :-
# Find the greater number in the list :-

ls = [2, 4, 9, 23, 54, 29]

def greater(a, b):          # impliment mathematical technique
    if a > b:
        return a

    else:
        return b

x = functools.reduce(greater, ls)
print(x)
'''


# Generator() :-
# 1). Generator is a function which is used to generate iterable object.
# 2). To make any generator function used yield keyword which is similar to return keyword
#     where return keyword return single data and here yield keyword return multiple values as a generator form.

# Return keyword :-
'''
def myFunc():
    for i in range(10):
        return i

x = myFunc()
print(x)
'''

# Generator or yield keyword :-
'''
def myFunc():
    for i in range(10):
        yield i

x = myFunc()
print(list(x))
'''


# Prime no. or not :-
'''
num = int(input("Enter Your Number :"))

for i in range(2, num):
    if num % i == 0:
        print(num, "is not prime number")
        break

else:
    print(num, "is prime number")

'''

# Python program to show the order
# in which methods are resolved

class A:
	def rk(self):
		print(" In class A")
class B:
	def rk(self):
		print(" In class B")

# classes ordering
class C(A, B):
	def __init__(self):
		print("Constructor C")

r = C()

# it prints the lookup order
print(C.__mro__)
print(C.mro())








































