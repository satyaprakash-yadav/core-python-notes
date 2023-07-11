#                   -------------------------- RECURSION FUNCTION -------------------------

'''
# Example 1 :-

def test():
    print("Hello World")
    test()

test()
'''

# Example 2 :-

def fact(n):
    if (n <= 1):
        return n

    else:
        return n*fact(n-1)

print(fact(5))



