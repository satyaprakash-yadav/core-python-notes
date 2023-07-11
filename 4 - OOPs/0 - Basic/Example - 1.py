#    ---------------------------------- OOPs ----------------------------------
'''
class test:
    a = 10              # a - Attribute
    def demo(self):     # def - Method & self - supported variable
        self.a = 10

    def demo1(self):
        self.demo()
        self.a = 20     # Data Redundancy
        print(self.a)

obj = test()            # obj - obj
obj.demo()              # obj - instance
obj.demo1()
# print(id(obj))          # To check the memory address of obj with the reference of self var  (obj == self)
'''
'''
# Example 1 :-

class A:
    def test(self):
        self.a = 10

    def test1(self):
        self.b = 20

    def addition(self):
        self.add = self.a + self.b
        return self.add

obj_A = A()
obj_A.test()
obj_A.test1()

print(obj_A.addition())

print(obj_A.a)
print(obj_A.b)

a = obj_A.a
b = obj_A.b
print(a + b)

obt = obj_A.addition()
res = obt / 100 * 100
print(res)
'''
'''
# Example 2 :-

class calc:
    def test(self, num1, num2):
        return num1 + num2

A = calc()

B = calc()

C = calc()

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

a = A.test(num1, num2)

b = B.test(num1, num2)

c = C.test(num1, num2)

print(a+b+c)

'''
'''
# Example 3 :-
class car:
    def collect_info(self, color, enginetype, seats):
        self.color = color
        self.enginetype = enginetype
        self.seats = seats

    def show_car_info(self):
        print("\n Show Car Info ")
        print("Car color : "+str(self.color))
        print("Car Engine Type : "+str(self.enginetype))
        print("Seater : "+str(self.seats))

audi = car()
audi.collect_info("red", "hybrid", 4)

bmw = car()
bmw.collect_info("black", "petrol", 4)

tesla = car()
tesla.collect_info("white", "electric", 4)

audi.show_car_info()
bmw.show_car_info()
tesla.show_car_info()

# Example 4 :-
# basic example with out constructor :-

class A:
    def define_values(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def add(self):
        return self.a + self.b + self.c

    def sub(self):
        return self.a - self.b - self.c

    def mul(self):
        return self.a * self.b * self.c

obj = A()
obj.define_values()
print(obj.add())
print(obj.sub())
print(obj.mul())
'''
'''
# Example 5 :-
# contructor without parameter

class A:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def add(self):
        return self.a + self.b + self.c

    def sub(self):
        return self.a - self.b - self.c

    def mul(self):
        return self.a * self.b * self.c

obj = A()
print(obj.add())
print(obj.sub())
print(obj.mul())
'''


























