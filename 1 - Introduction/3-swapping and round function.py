'''
# concatenation :- To add two or more str value is called concatenate.

# Syntax :- Rule and regulation you have must follow.

#    128  64  32  16  8  4  2  1

# 1 - way :-
a = 17
b = 5

print(a & b)

# 2 - way ;-

a = 17/2   #1
print(a)

b = 8/2    #0
print(b)

c = 4/2    #0
print(c)

d = 2/2    #0
print(d)

e = 1/2    #1
print(e)

# swapping :- To exchange the value or data.

name = "Mahesh"
course = "Python"

#print("Normal :",name , course)

name , course = course , name
#print("Swapping :",name , course)

# Round Function :- Its round the whole value.


obt = 3482
tot = 500
#print(round(obt/tot*100,2))

print("\n---------------> PERCENTAGE APPLICATION <------------------\n")
print("1 - Percentage\nper - Percentage\n")

user = input("Enter Your Choice : ")

if user == "1" or user == "per":
    obt = int(input("Enter Your Obtain :"))
    tot = int(input("Enter Your Total :"))

if (obt > tot):
    obt , tot = tot , obt

print("Percentage : ",round(obt/tot*100,2))

# BMI = Body Mass Index
# BMI = weight / height ** 2

name = input("Enter  Your Nmae : ")
weight = int(input("Enter Your Weight : "))
height = float(input("Enter Your Height : "))
BMI = weight / height ** 2
print(name , "Your BMI is " , BMI)

# Typecasting :- It is converting one type of data into another type of data.
a = 10
print(str(a))
'
a1 =  float(a)
#print(a1)

a2 = complex(a1)
#print(a2)

a3 = hex(a)
#print(a3)

a4 = oct(a)
#print(a4)

a5 = bin(10)
#print(a5)

'''




















