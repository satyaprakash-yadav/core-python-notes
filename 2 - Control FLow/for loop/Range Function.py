# ---------------------------------- LOOP ------------------------------------

# Loop :- It is instruction in which repeat until condition is reached or at the end of condition.

# --------------------------------- Range Function ---------------------------

# For loop works on range basis.
# Range Function is genrate sequence of integer number.
#                   range = P1 , P2  , p3
#                   P1 = starting position
#                   P2 = ending position
#                   P3 = step
# Range Function used index positioning system to generate integer number.
# Range Function have a starting and ending position but minus(-) one from ending position.

# ------------------------------ Iteration ----------------------------------
# Iteration :- Take value one by one if value exist in loop then the value is empty iteration will be stop.

#for i in range(0 , 11 , +1):
#    print(i)

#for -- loop
#i   -- iterate
#range -- provide value.

# Formula :-
# No. of iteration = starting - ending
'''
# Example :-
for i in range(357 , 398 , +1):
    print(i)

# Negative decrement :-
for i in range(-10,1,+1):
    print(i)

for i in range(1 , 10 , +1):
    print(i)

# For Table:-
n = int(input("Enter Your Number: "))
for i in range(1 , 11 , +1):
    print(i*n)

# Nested for :-
for i in range(5):
    print("Number is :" , i)
    for j in range(5):  # Data Redundancy
        print("For Loop :" , j)
    print()

# Table 2 to 10 :-
for i in range(1 , 11):
    for j in range(2 , 11):
        print(i*j , end="\t")
    print()

# Square Pattern :-

for row in range(5):
    for col in range(5):
        print("*" , end = " ")
    print()

# Right Angle Triangle:-
for row in range(7):
    for col in range(row+1):
        print("*" , end = " ")
    print()

# opposite right angle Triangle :-

for row in range(7):
    for col in range(row):
        print(" " , end=" ")

    for col in range(7,row , -1):
        print("*" , end = " ")
    print()

# square with condition :-
for row in range(7):
    for col in range(7):
        if (row == 0) or (row == 6) or (col == 0) or (col == 6):
            print("*" , end = " ")

        elif (row == 3) and (col >= 2 and col <= 4):
            print("*",end= " ")

        elif (col == 3) and (row >= 2 and row <= 4):
            print("*" , end = " ")
            
        else:
            print(" ",end = " ")
    print()


# Triangle with condition :-
for row in range(6):
    for col in range(6):
        if (row == 5) or (col == 0) or (row == col):
            print("*" , end = " ")

        else:
            print(" " , end = " ")

    print()

for row in range(6):
    for col in range(6):
        if (row == 0) or (col == 5) or (row == col):
            print("*",end = " ")

        else:
            print(" ", end = " ")

    print()

# Pyramid

for row in range(4):
    for col in range(7):
        if (row == 3) or (row + col == 3) or (col - row == 3):
            print("*" ,end = " ")

        else:
            print(" " , end = " ")

    print()

for row in range(4):
    for col in range(7):
        if (row == 0) or (row == col) or (col + row == 6):
            print("*" ,end = " ")

        else:
            print(" " ,end = " ")

    print()

for row in range(7):
    for col in range(7):
        if (row + col == 3) or (col - row == 3) or (row - col == 3) or (col + row == 9):
            print("*" ,end = " ")

        else:
            print(" " , end = " ")

    print()

# User define Pattern :-
n = int(input("Enter Your Value For Pattern : "))
for row in range(n):
    for col in range(n):
        if (row == 0) or (row == n-1) or (col == 0) or (col == n-1):
            print("*" , end = " ")

        elif (row == n - 4) and (col >= n - 5 and col <= n - 3):
            print("*",end= " ")

        elif (col == n - 4) and (row >= n - 5 and row <= n - 3):
            print("*" , end = " ")
            
        else:
            print(" ",end = " ")
    print()

# Triangle User define
n = int(input("Enter Your Value For Pattern : "))
for row in range(n):
    for col in range(n):
        if (row == n-1) or (col == 0) or (row == col):
            print("*" , end = " ")

        else:
            print(" " , end = " ")

    print()

n = int(input("Enter Your Value For Pattern : "))
for row in range(n):
    for col in range(n):
        if (row == 0) or (col == n-1) or (row == col):
            print("*",end = " ")

        else:
            print(" ", end = " ")

    print()

# Daout :- 
n = int(input("Enter Your Value For Pattern : "))
for row in range(n-3):
    for col in range(n):
        if (row == n - 4) or (row + col == n - 4) or (col - row == n - 4):
            print("*" ,end = " ")

        else:
            print(" " , end = " ")

    print()

for row in range(6):
    for col in range(5):
        if (col == 0) or (col == 4):
            print("*" , end = " ")

        elif (row == col) and (row < 2):
            print("*" , end = " ")

        elif (col + row == 4) and (row < 3):
            print("*" , end = " ")

        else:
            print(" " ,end = " ")

    print()

for row in range(7):
    for col in range(5):
        if (row == 0) and (col == 2):
            print("*" , end = " ")

        elif (row + col == 2) or (col - row ==2):
            print("*" , end=" ")

        elif (row > 2) and (col == 0 or col == 4) or (row == 4):
            print("*" , end=" ")

        else:
            print(" " ,end = " ")

    print()
'''

# 26/11/2022

# Difference Between DATA and INFORMATION :-

# DATA :- Incomplete information or raw data.
# INFORMATION :- Full information or complete information.
'''
for row in range(11):
    for col in range(11):
        if(row + col == 5) or (col - row == 5) or (row - col == 5) or (col + row == 15):
            print("*" , end = " ")

        else:
            print(" " , end = " ")
    print()

n = int(input("Enter Your Number : "))
for row in range(n*2-1):
    for col in range(n*2-1):
        if(row + col == n-1) or (col - row == n-1) or (row - col == n-1) or (col + row == n*3-3):
            print("*" , end = " ")

        else:
            print(" " , end = " ")
    print()
'''
# for loop keyword :-

#1). break :- It is used to terminate the loop.
#2). continue :- It is used to continue the loop.
#3). pass :- It cannot give anything or errors.
'''

#1). break :-
for i in range(1,11):
    if (i == 5):
        break
    print(i)

#2). continue :-
for i in range(1,11):
    if (i == 5):
        continue
    print(i)

for i in range(1,11):
    pass 

print("\n ------------------- Application For Percentage -------------------\n")
subject = ["Maths","Telugu","Hindi","Marathi"]
sum_l = 0
for marks in subject:
    print("Enter Your Marks For: ",marks)
    a = int(input("Enter Marks : "))
    sum_l = sum_l + a

    if sum_l > 500:
        print("Invalid Marks")
        break
    else:
        print("Your Total sum is : ", sum_l)
        print("Your Total Percentage is : ", round(sum_l/500*100,2),"%")

'''
    
    




    


























































