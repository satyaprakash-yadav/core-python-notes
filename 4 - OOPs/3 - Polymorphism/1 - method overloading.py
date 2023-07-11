# Polymorphism :-
# Python doesn't support by default method overloading.

# Example :-
'''
ls = [1,2,3,4,5]
name = "Mahesh"

print(len(ls))          # len() is a function.
print(len(name))
'''

# 1 - Method overloading :-
# Example 1 :-
'''
class A:

    def show(self):
        print("This is method 1")

    def show(self, name):
        print("This is method 2", name)

    def show(self, name, age):      # Latest method inside a class which is call
        print("This is method 3\n", "Name is :"+str(name)+"\n", "Age is :"+str(age))

obj = A()   # object
obj.show("Mahesh", 22)
'''

# Example :-
'''
class A:

    def length_of_data(self, n):
        return len(n)

a = [1,2,3,5,6]
b = "Rakesh"

obj = A()

print(obj.length_of_data(a))
print(obj.length_of_data(b))
'''

'''
# decorator
# open cmd >>> pip install multipledispatch
from multipledispatch import dispatch

class A:

    @dispatch()
    def add(self):
        print("Addition is :", 10+20)

    @dispatch(int)
    def add(self, a):
        print("Addition is :", a+20)

    @dispatch(int, int)
    def add(self, a, b):
        print("Addition is :", a+b)


obj = A()
obj.add()

obj.add(40)

obj.add(60,70)    
'''


