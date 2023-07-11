#                                                   EXCEPTION HANDLING

# NameError :-
# e.g.
# print(name)

# syntax error :-
# e.g. 
# n = int(input('enter num))

# types of except handle :-

# 1). single except :- 
# 2). multiple except :- 
# 3). exception with else & finally block :-
# 4). user define except :-
# 5). raise keyword :-


# 1). single except :- 
'''
try:
    a = int(input('Enter Your Number :'))
    b = int(input('Enter Your Number :'))
    print(f'Addition is :{a+b}')
    print(f'Division is :{a/b}')


except:
    print('Enter only integer number not str or float.')

'''

# 2). multiple except :- 
'''
try:
    a = int(input('Enter Your Number :'))
    b = int(input('Enter Your Number :'))
    print(f'Addition is :{a+b}')
    print(f'Division is :{a/b}')

except ValueError as e:
    print(f'NumberError : {e}')

except ZeroDivisionError as z:
    print(f'ZeroError : {z}')
'''

# 3). exception with else & finally block :-
'''
try:
    a = int(input('Enter Your Number :'))
    b = int(input('Enter Your Number :'))
    print(f'Addition is :{a+b}')
    print(f'Division is :{a/b}')

except ValueError as e:
    print(f'NumberError : {e}')

else:
    print('No Error') # if no error this part executed

finally:
    print('Program Finish')
'''

# 5). raise keyword :-
'''
n = int(input('Enter Your Number :'))

if n > 0:
    raise ValueError('Greater than 0')

else:
    raise TypeError('Lesser than 0.')

'''


