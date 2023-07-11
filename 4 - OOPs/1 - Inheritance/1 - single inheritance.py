# 1). Single Inheritance :-

# without constructor :-
# Example 1 :-
'''
class A:    # parent class
    def add(self):
        return 10 + 20

    def sub(self):
        return 20 - 30

class B(A): # child class
    def factorial(self,n):
        self.n = n
        fact = 1
        for i in range(self.n, 0, -1):
            fact *= i
        return fact

obj = B()   # object

add = obj.add()
sub = obj.sub()
fact = obj.factorial(5)

print("Addition is : "+str(add))
print("Substraction is : "+str(sub))
print("Factorial is : "+str(fact))
'''
# With constructor :-
# Example 2 :-
'''
class A:    # parent class
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.c - self.a

class B(A): # child class
    def __init__(self):
        self.tot = 500
        #super().__init__()
        #A.__init__(self)

    def percentage(self,obt):
        self.obt = obt
        if (self.obt > self.tot):
            self.obt , self.tot = self.tot , self.obt

        return (self.obt/self.tot) * 100

obj = B()   # object

add = obj.add()
sub = obj.sub()
per = obj.percentage(345)

print("Addition is : "+str(add))
print("Substraction is : "+str(sub))
print("Percentage is : "+str(per))
'''
'''
# constructor with parameter :-
# Example 3 :-

class A:    # parent class
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def set_data(self, a ,b):   # data redundancy
        self.a = a
        self.b = b

class B(A): # child class
    def __init__(self, c, a, b):
        self.c = c
        super().__init__(a, b)

    def fact(self):
        fact = 1
        for i in range(self.c, 0, -1):
            fact *= i
        return fact

obj = B(7, 20, 50)   # object

print(obj.add())
print(obj.fact())
obj.set_data(156, 200)
print(obj.add())
'''





































