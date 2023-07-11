# control flow :-The order in which the program code execute and also control the flow of program.

#                                 Control Flow           
#      ________________________________↓_______________________________
#     ↓                                                                ↓
#    conditional statement/decision making stat                       loop
#                                                                _______↓___________  
#    if                                                         ↓                   ↓      
#    if else                                                  for loop         while loop          
#                                                            simple for       
#    if elif else                                            loop with cond..   same like
#    nested if                                               nested loop        for loop 
#                                                            nested with cond..
#                                                            continue break pass

'''                                                            
n1 = int(input("Enter Your Number : "))

if n1 > 0:
    print("Number is positive ")

if n1 < 0:
    print("Number is Negative")

if n1 == 0:
    print("Number is equals to zero")

ch = int(input("Enter Your Age : "))

if ch >= 18:
    print("You Are Adult")

if ch < 18:
    print("You Are Not Adult")


# if condition with membership opr:-

name = ["ravi" , "venu" , "mahi" , "rahul"]

new_name = input("Enter Your Name: ")

if (new_name in name):
    print("New Name is Exist" , new_name)

if (new_name not in name):
    print("New Name is Not Exist" , new_name)


# 2). if else:-

name = ["ravi" , "venu" , "mahi" , "rahul"]

new_name = input("Enter Your Name: ")

if (new_name in name):
    print("New Name is Exist" , new_name)

else:           # handle the error
    print("New Name is Not Exist" , new_name)
    

n1 = int(input("Enter Your Number: "))
n2 =int(input("Enter Your Number: "))

if n1 >= n2:
    print("Number is positive",n1)

else:
    print("Invalid Input")


n1 = int(input("Enter Your Number: "))
if n1 >= 0:
    print("Number is positive",n1)

else:
    print("Number is Negative",n1)
    
# 3). if - elif - else
n1 = int(input("Enter Your Number: "))
if n1 > 0:
    print("Number is positive",n1)

elif n1 < 0:
    print("Number is Negative" , n1)
    
else:
    print("Number is Zero",n1)

print("\n ------------ Calculator Application ------------- \n")
print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication")
print("4 - Division")
print()

ch = input("Enter Your Choice: ")

if ch == "1" or ch == "add":
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = a + b
    print("Addition is : " , c)

elif ch == "2":
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = a - b
    print("Addition is : " , c)

elif ch == "3":
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = a * b
    print("Addition is : " , c)

elif ch == "4":
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = a / b
    print("Addition is : " , round(c,2))
    
else:
    print("Invalid Input")

# Nested if :-
n = int(input("Enter Your Number: "))

if n >= 0:
    if n == 0:
        print("Number is Zero:",n)

    else:
        print("Number is Positive:",n)

else:
    print("Number is Negative:" , n)
    

n = int(input("Enter Your Number: "))

if n > 0:
    print("Number is Positive:",n)

else:
    if n == 0:
        print("Number is Zero:",n)

    else:
        print("Number is Negative:",n)

# write a program to get discount_price and after discount what is the actual_price?
#product_price = 14324
#dicount = 15
print("\n--------------- Discount Application ----------------\n")

product = int(input("Enter Your Product Price: "))
discount = int(input("Enter Your Discount %: "))

#formula = current * total / 100
dis_price = discount * product / 100

# actual_price = product - dis_price
actual_price = product - dis_price

print("\nAmount of Discount:" , dis_price)
print("After Discount Payable:" , actual_price)


# Triangle reflection :-

for row in range(6):
    for col in range(row):
        print(" ",end=" ")
    
    for col1 in range(5 , row , -1):
        print("*" , end= " ")
    
    for col2 in range(6 , row , -1):
        print("*" , end= " ")

    for col3 in range(row):
        print(" " , end= " ")
    
    print()
'''
