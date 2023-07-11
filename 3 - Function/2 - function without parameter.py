#           ------------------------------------------- FUNCTION WITHOUT PARAMETER -------------------------------------------

'''
# percentage calculation :-

obt = int(input("Enter Your Obtain Marks : "))
tot = int(input("Enter Your Total Marks : "))

res = obt / tot * 100
print("Percentage is : ",res ,"%")


# Even or Odd Number :-

num = int(input("Enter Your Number : "))

if (num % 2 == 0):
    print(num , "is a Even Number")

else:
    print(num , "is a Odd Number")
'''


# Function Without Parameter(Call by reference Function) :-

# Percentage Calculator :-

def percentage():
    '''
    This function is used to calculate percentage   # Doc String
    its required 2 int values
    1 - obtain value
    2 - total value
    and return result value to the function
    '''
    obt = int(input("Enter Your Obtain Marks :"))
    tot = int(input("Enter Your Total Marks :"))

    res = obt / tot * 100
    print("Percentage is :",round(res,2),"%")


# Even or Odd Identify :-

def even_odd():
    '''
    This function is used to identify the
    even or odd number its required 1 int value
    1 - int number
    and return the value to the function
    '''
    n = int(input("Enter Your Number : "))

    if (n % 2 == 0):
        print(n , "is a Even Number")

    else:
        print(n, "is a Odd Number")


# Factorial calculation :-

def factorial():
    '''
    This is function is used to calculate factorial
    its required 1 int value
    1 - Int Value
    and return the result of fact to the function
    '''
    fact = 1
    n = int(input("Enter Your Number : "))
    for i in range(n , 0 , -1):
        fact = fact * i
    print("Factorial is :",fact)

# percentage() call the function
# help(percentage)


# even_odd()
# help(even_odd)

# help from builtin function
# help(print)


# factorial()
help(factorial)
