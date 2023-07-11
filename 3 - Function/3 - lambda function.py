#                                        ----------------------- LAMBDA FUNCTION ---------------------------

# Example 1 :
'''
num = lambda : 10 + 20

print(num())
'''

# Eaxmple 2 :-
'''
num = lambda a , b , c : a + b + c 

a = int(input('Enter Your Number : '))
b = int(input('Enter Your Number : '))
c = int(input('Enter Your Number : '))

print(num(a , b , c))
'''

# Example 3 :-
'''
ptr = lambda n : n * " *"

for i in range(10):
    print(ptr(i))
'''
'''
# Example 5 :-

table = lambda x , y : x * y

n = int(input("Enter Your Number : "))
for i in range(1,11):
    print(table(n,i))

'''
# Example 5 :-
'''                                        
data = lambda i : 'Even' if i % 2 == 0 else 'Odd'
n = int(input('Enter Your Number : '))
print(data(n))
'''


