# Decorator :- It is a very important tool in python which gives ability to modify any method without accessing it.
# There are 2 types of decorator :-
# 1). Built in     :-  @classmethod, @staticmethod,@abstractmethod , @dispatchmethod.  
# 2). User defined :- 

# 1). Function return whole function :-
'''
def decor_per(func):

    def inner_func(obt, tot):
        if obt > tot:
            obt , tot = tot, obt

        return func(obt, tot)
    return inner_func

@decor_per
def per(obt, tot):
    return obt / tot * 100


# p = per(450, 550)
# print(round(p, 2))

p = per(550, 450)
print(round(p, 2))
'''

# 2). Function take whole argument as function :-
'''
def add(a, b):
    return a + b

def mul(p, q):
    return p * q

def per(tot, add1, mul1, a, b, p, q):
    a1 = add(a, b)
    b1 = mul(p, q)

    return (a1 + b1) / tot * 100


p = per(500, add, mul, 20, 150, 10, 7)
print(p)
'''

# 3). Inner function :-
'''
def outer_func():
    msg1 = "Outer Function"

    def inner_func():
        msg = "Inner Function"
        return msg
    
    return inner_func()

print(outer_func())
'''
















